"""Utilitaires partagés par tous les générateurs."""
import re


def fmt_signed(value, var="x"):
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
    """Formate 'y = mx + p'. Gère m=0 et p=0."""
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

    if len(parts) == 1:        # m=0 et p=0 → 'y = 0'
        parts.append("0")

    return " ".join(parts)


def fmt_poly(coeffs):
    a, b, c, d = coeffs
    terms = []
    if a != 0:
        terms.append("X^3" if a == 1 else "-X^3" if a == -1 else f"{a}X^3")
    if b != 0:
        terms.append("+ X^2" if b == 1 else "- X^2" if b == -1
                     else (f"+ {b}X^2" if b > 0 else f"- {abs(b)}X^2"))
    if c != 0:
        terms.append("+ X" if c == 1 else "- X" if c == -1
                     else (f"+ {c}X" if c > 0 else f"- {abs(c)}X"))
    if d != 0:
        terms.append(f"+ {d}" if d > 0 else f"- {abs(d)}")
    return " ".join(terms) if terms else "0"


def fmt_expr(expr):
    s = str(expr).replace("**", "^")
    s = re.sub(r"(\d)\*([a-zA-Z])", r"\1\2", s)
    s = re.sub(r"([a-zA-Z])\*([a-zA-Z])", r"\1\2", s)
    return s


# Types à réponses multiples (pas concernés par le post-traitement)
MULTI_TYPES = {"T05_inegalite", "T09_points_cercle"}


def postprocess_unique(q, rng, p_autre=0.20):
    """
    Réorganise les options d'une question à réponse UNIQUE :
    - 'Autre chose' est TOUJOURS en position D
    - Avec probabilité p_autre (20%), 'Autre chose' est la bonne réponse
    - Sinon, la bonne réponse est en A, B ou C
    """
    if q["type"] in MULTI_TYPES:
        return q

    rep = q["reponse"]
    if isinstance(rep, list):
        return q  # sécurité : devrait être multiple

    rep_s = str(rep).strip()
    options = q["options"]

    # Récupère les distracteurs (en excluant la bonne réponse et 'Autre chose')
    distractors = []
    seen = {rep_s, "Autre chose"}
    for o in options:
        os_ = str(o).strip()
        if os_ not in seen:
            distractors.append(os_)
            seen.add(os_)

    # Garantit 3 distracteurs
    while len(distractors) < 3:
        distractors.append(f"Option {len(distractors) + 1}")
    distractors = distractors[:3]

    # Décide qui est la bonne réponse
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
    return q