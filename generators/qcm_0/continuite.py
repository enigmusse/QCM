import random
import sympy as sp
from generators.utils import fmt_poly_terms, fmt_term


def _fmt_poly(coeffs):
    """coeffs = [a3, a2, a1, a0] → a3x³ + a2x² + a1x + a0 proprement."""
    a3, a2, a1, a0 = coeffs
    return fmt_poly_terms([
        (a3, "x³"), (a2, "x²"), (a1, "x"), (a0, ""),
    ])


def generate(rng: random.Random, avoid=None):
    sous_type = rng.choice(["simple", "derivee"])
    a, b = sp.symbols("a b")

    if sous_type == "simple":
        x0 = rng.randint(-2, 2)
        x1 = x0 + rng.randint(1, 3)
        A1, B1, C1 = rng.randint(1, 3), rng.randint(-3, 3), rng.randint(-5, 5)
        A2, B2, C2 = rng.randint(1, 3), rng.randint(-3, 3), rng.randint(-5, 5)
        v0 = A1 * x0**2 + B1 * x0 + C1
        v1 = A2 * x1**2 + B2 * x1 + C2
        sol = sp.solve([
            sp.Eq(a * x0 + b - 2 * x0**2, v0),
            sp.Eq(a * x1 + b - 2 * x1**2, v1),
        ], [a, b])
        if not sol:
            return generate(rng, avoid)
        val = sp.simplify(3 * sol[a] - 4 * sol[b])
        enonce = (
            f"Soit f définie par morceaux : "
            f"f(x) = {_fmt_poly([0, A1, B1, C1])} si x ≤ {x0}, "
            f"f(x) = ax + b - 2x² si {x0} < x < {x1}, "
            f"f(x) = {_fmt_poly([0, A2, B2, C2])} si x ≥ {x1}. "
            f"a₀, b₀ rendent f continue. Que vaut 3a₀ - 4b₀ ?"
        )
    else:
        x0 = rng.randint(-3, -1)
        A1, B1, C1, D1 = rng.randint(1, 3), rng.randint(-3, 3), rng.randint(-5, 5), rng.randint(-5, 5)
        v = A1 * x0**3 + B1 * x0**2 + C1 * x0 + D1
        dv = 3 * A1 * x0**2 + 2 * B1 * x0 + C1
        c = rng.randint(-5, 5)
        sol = sp.solve([
            sp.Eq(a * x0**2 + b * x0 + x0**3 + c, v),
            sp.Eq(2 * a * x0 + b + 3 * x0**2, dv),
        ], [a, b])
        if not sol:
            return generate(rng, avoid)
        val = sp.simplify(3 * sol[a] - 4 * sol[b])
        c_tail = fmt_term(c, "", first=False)
        sec_terme = f"x³ {c_tail}" if c_tail else "x³"
        enonce = (
            f"Soit f définie par "
            f"f(x) = {_fmt_poly([A1, B1, C1, D1])} si x ≤ {x0}, "
            f"f(x) = ax² + bx + {sec_terme} si x > {x0}. "
            f"a₀, b₀ rendent f et f' continues en {x0}. "
            f"Que vaut 3a₀ - 4b₀ ?"
        )

    correct = sp.sstr(val)
    candidates = [
        sp.sstr(sp.sympify(correct) + 1),
        sp.sstr(sp.sympify(correct) - 1),
        sp.sstr(sp.sympify(correct) + 2),
    ]
    seen = {correct}
    distractors = []
    for c_ in candidates:
        if c_ not in seen:
            distractors.append(c_)
            seen.add(c_)
        if len(distractors) >= 3:
            break
    while len(distractors) < 3:
        distractors.append("Autre chose")
    options = [correct] + distractors[:3]
    rng.shuffle(options)

    return {
        "type": "T22_continuite",
        "enonce": enonce, "options": options,
        "reponse": correct,
        "params": {},
    }