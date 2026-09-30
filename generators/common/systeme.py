import random
import sympy as sp

AVOID = [
    (3, 5, 1, 2, 5, 4),
    (2, 3, 2, 1, 5, 8),
    (4, 6, 2, 1, 4, -2),
    (2, 2, 1, -1, -3, 1),
    (-3, 2, 1, -1, 1, -9),  
    (4, 1, 5, 2, 2, 3),   
]


def _fmt_eq(a, b, c, var1="x", var2="y"):
    """Formate 'ax + by = c' proprement."""
    parts = []

    if a == 1:
        parts.append(var1)
    elif a == -1:
        parts.append(f"-{var1}")
    else:
        parts.append(f"{a}{var1}")

    if b > 0:
        parts.append(f"+ {b}{var2}" if b != 1 else f"+ {var2}")
    elif b < 0:
        parts.append(f"- {abs(b)}{var2}" if b != -1 else f"- {var2}")

    parts.append(f"= {c}")
    return " ".join(parts)


def generate(rng: random.Random, avoid=None):
    avoid = avoid or AVOID
    for _ in range(300):
        x0 = sp.Rational(rng.choice([-10, -5, -3, -2, -1, 0, 1, 2, 3, 5, 10]))
        y0 = sp.Rational(rng.choice([-10, -5, -3, -2, -1, 0, 1, 2, 3, 5, 10]))
        a1 = rng.choice([-4, -3, -2, 2, 3, 4])
        b1 = rng.choice([-6, -5, -4, -3, -2, 2, 3, 4, 5, 6])
        a2 = rng.choice([-4, -3, -2, 2, 3, 4])
        b2 = rng.choice([-6, -5, -4, -3, -2, 2, 3, 4, 5, 6])
        if a1 * b2 - a2 * b1 == 0:
            continue
        c1 = a1 * x0 + b1 * y0
        c2 = a2 * x0 + b2 * y0
        key = (a1, b1, a2, b2, int(c1), int(c2))
        if key not in avoid:
            break

    result = 3 * x0 - 4 * y0

    eq1 = _fmt_eq(a1, b1, c1)
    eq2 = _fmt_eq(a2, b2, c2)

    enonce = (
        f"On pose (x0, y0) la solution du système : "
        f"{eq1} ; {eq2}. Que vaut 3x0 − 4y0 ?"
    )

    correct = sp.sstr(result)
    distractors = [sp.sstr(result + 1), sp.sstr(result - 1), sp.sstr(result + 2)]
    options = [correct] + distractors
    # dédoublonnage au cas où
    seen = set()
    unique = []
    for o in options:
        if o not in seen:
            unique.append(o)
            seen.add(o)
    while len(unique) < 4:
        unique.append("Autre chose")
    options = unique[:4]
    rng.shuffle(options)

    return {
        "type": "T04_systeme",
        "enonce": enonce,
        "options": options,
        "reponse": correct,
        "params": {"a1": a1, "b1": b1, "a2": a2, "b2": b2,
                   "c1": int(c1), "c2": int(c2),
                   "x0": int(x0), "y0": int(y0)},
    }