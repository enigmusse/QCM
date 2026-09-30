"""Utilitaires partagés par tous les générateurs."""
import re


def to_latex(s):
    """Convertit une expression plain-text en LaTeX."""
    if not isinstance(s, str):
        s = str(s)

    # Exposants : x^2 → x^{2}, e^-x → e^{-x}
    s = re.sub(r"\^([A-Za-z0-9]+)", r"^{\1}", s)
    s = re.sub(r"\^([+\-]?[A-Za-z0-9]+)", r"^{\1}", s)

    # Indices : x1 → x_{1}, x_1 → x_{1}
    s = re.sub(r"\b([a-zA-Z])_?(\d)\b", r"\1_{\2}", s)

    # Racines : √x → \sqrt{x}, √(x+1) → \sqrt{x+1}
    s = re.sub(r"√\s*\(([^)]+)\)", r"\\sqrt{\1}", s)
    s = re.sub(r"√\s*([A-Za-z0-9]+)", r"\\sqrt{\1}", s)

    # Exposants unicode
    for sup, num in [("²", "^2"), ("³", "^3"), ("⁴", "^4"), ("⁵", "^5")]:
        s = s.replace(sup, num)
    # Repasse les exposants unicode convertis
    s = re.sub(r"\^([+\-]?[A-Za-z0-9]+)", r"^{\1}", s)

    # Symboles
    s = s.replace("×", r"\times ")
    s = s.replace("·", r"\cdot ")
    s = s.replace("≤", r"\leq ")
    s = s.replace("≥", r"\geq ")
    s = s.replace("≠", r"\neq ")
    s = s.replace("∞", r"\infty ")
    s = s.replace("π", r"\pi ")
    s = s.replace("Σ", r"\sum ")
    s = s.replace("∑", r"\sum ")
    s = s.replace("∫", r"\int ")
    s = s.replace("→", r"\to ")
    s = s.replace("−", "-")

    # Fractions numériques simples : 1/12 → \frac{1}{12}
    s = re.sub(
        r"(?<![\w/])(-?\d+)\s*/\s*(\d+)(?![\w/])",
        r"\\frac{\1}{\2}",
        s,
    )

    return s


def smart_render(text):
    """Rend un texte mixte (français + maths) prêt pour st.markdown.
    Entoure les segments mathématiques de $...$."""
    if not isinstance(text, str):
        text = str(text)

    pattern = re.compile(
        r"""
        (?P<eq>[A-Za-z]\([^)]*\)\s*=\s*[-−]?[^.,;!?\n]+)
        |(?P<ineq>x[_ ]?\d+(?:\s*[≤≥<>=]\s*x[_ ]?\d+)+)
        |(?P<sum>x[_ ]?\d+(?:\s*[+\-−]\s*\d*x[_ ]?\d+)+)
        |(?P<frac>(?<![\w/])-?\d+\s*/\s*\d+(?![\w/]))
        |(?P<sqrt>√\s*\(?[A-Za-z0-9+\-]+\)?)
        |(?P<pow>(?<!\w)[A-Za-z0-9]\^[A-Za-z0-9]+(?!\w))
        """,
        re.VERBOSE,
    )

    def _wrap(m):
        s = m.group(0)
        return f"${to_latex(s)}$"

    return pattern.sub(_wrap, text)



def fmt_signed(value, var="x"):
    """Formate '+ ax' ou '- ax' proprement, gère 0, 1, -1."""
    if value == 0:
        return ""
    if value == 1:
        return f"+ {var}"
    if value == -1:
        return f"- {var}"
    if value > 0:
        return f"+ {value}{var}"
    return f"- {abs(value)}{var}"


def fmt_line(m, p):
    """Formate 'y = mx + p' proprement. Gère le cas m=0, p=0."""
    parts = ["y ="]

    if m == 1:
        parts.append("x")
    elif m == -1:
        parts.append("-x")
    elif m != 0:
        parts.append(f"{m}x")

    if p != 0:
        if len(parts) == 1:
            parts.append(str(p))
        else:
            parts.append(f"+ {p}" if p > 0 else f"- {abs(p)}")

    if len(parts) == 1:
        parts.append("0")

    return " ".join(parts)


def fmt_poly(coeffs):
    """coeffs = [a,b,c,d] pour aX^3 + bX^2 + cX + d."""
    a, b, c, d = coeffs
    terms = []

    if a != 0:
        if a == 1:
            terms.append("X^3")
        elif a == -1:
            terms.append("-X^3")
        else:
            terms.append(f"{a}X^3")

    if b != 0:
        if b == 1:
            terms.append("+ X^2")
        elif b == -1:
            terms.append("- X^2")
        else:
            terms.append(f"+ {b}X^2" if b > 0 else f"- {abs(b)}X^2")

    if c != 0:
        if c == 1:
            terms.append("+ X")
        elif c == -1:
            terms.append("- X")
        else:
            terms.append(f"+ {c}X" if c > 0 else f"- {abs(c)}X")

    if d != 0:
        terms.append(f"+ {d}" if d > 0 else f"- {abs(d)}")

    return " ".join(terms) if terms else "0"


def fmt_expr(expr):
    """Convertit une expression sympy en texte lisible."""
    s = str(expr)
    s = s.replace("**", "^")
    s = re.sub(r"(\d)\*([a-zA-Z])", r"\1\2", s)
    s = re.sub(r"([a-zA-Z])\*([a-zA-Z])", r"\1\2", s)
    return s


# ---------- Nouveaux helpers pour les générateurs QCM 0 ----------

def fmt_term(coef, var="", first=False):
    """Formate un terme '+ ax' ou '- ax' proprement. Gère 0, ±1."""
    if coef == 0:
        return ""
    if first:
        sign = "" if coef > 0 else "-"
    else:
        sign = "+ " if coef > 0 else "- "
    abs_c = abs(coef)
    if abs_c == 1 and var:
        coef_str = ""
    else:
        coef_str = str(abs_c)
    return f"{sign}{coef_str}{var}".strip()


def fmt_poly_terms(terms):
    """terms = [(coef, 'x^2'), (coef, 'x'), (coef, '')]. Retourne une string propre."""
    parts = []
    for coef, var in terms:
        if coef == 0:
            continue
        parts.append(fmt_term(coef, var, first=(len(parts) == 0)))
    return " ".join(parts) if parts else "0"


def fmt_lin(a, b, var="x"):
    """Formate une expression linéaire a·var + b proprement."""
    parts = []
    if a != 0:
        if a == 1:
            parts.append(var)
        elif a == -1:
            parts.append(f"-{var}")
        else:
            parts.append(f"{a}{var}")
    if b != 0:
        if not parts:
            parts.append(str(b))
        else:
            parts.append(f"+ {b}" if b > 0 else f"- {abs(b)}")
    return " ".join(parts) if parts else "0"


# Types à réponses multiples (non concernés par le post-traitement)
MULTI_TYPES = {
    "T05_inegalite",
    "T09_points_cercle",
    "T32_integrales_conv",
    "T33_series_conv",
}


def postprocess_unique(q, rng, p_autre=0.20):
    """'Autre chose' toujours en D, avec 20% de chance d'être la bonne réponse.
    Conserve la vraie réponse mathématique dans q['reponse_math']."""
    if q["type"] in MULTI_TYPES:
        return q

    rep = q["reponse"]
    if isinstance(rep, list):
        return q

    rep_s = str(rep).strip()
    options = q["options"]

    distractors = []
    seen = {rep_s, "Autre chose"}
    for o in options:
        os_ = str(o).strip()
        if os_ not in seen:
            distractors.append(os_)
            seen.add(os_)

    while len(distractors) < 3:
        distractors.append(f"Option {len(distractors) + 1}")
    distractors = distractors[:3]

    if rng.random() < p_autre:
        abc = distractors[:]
        rng.shuffle(abc)
        options_new = abc + ["Autre chose"]
        rep_new = "Autre chose"
    else:
        abc = [rep_s] + distractors[:2]
        rng.shuffle(abc)
        options_new = abc + ["Autre chose"]
        rep_new = rep_s

    q = dict(q)
    q["options"] = options_new
    q["reponse"] = rep_new
    q["reponse_math"] = rep_s    # ← vrai contenu mathématique, toujours préservé
    return q