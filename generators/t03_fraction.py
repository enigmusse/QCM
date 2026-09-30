import random
import sympy as sp
from .utils import fmt_expr

X = sp.Symbol("x")

AVOID = [
    (2, 3, 4, 12),
    (4, 1, 2, 8),
    (3, -1, 4, -6),
    (2, 1, -3, 4),
    (3, 3, 2, -12),
]


def generate(rng: random.Random, avoid=None):
    avoid = avoid or AVOID
    for _ in range(200):
        p = rng.choice([2, 3, 4, 5])
        A = rng.choice([-3, -2, -1, 1, 2, 3])
        B = rng.choice([-3, -2, -1, 1, 2, 3])
        C = rng.choice([-12, -8, -6, -4, 4, 6, 8, 12])
        if (p, A, B, C) not in avoid:
            break

    expr = A / (X + p) + B / (X - p) + C / (X**2 - p**2)
    simplified = sp.simplify(expr)
    correct = fmt_expr(simplified)

    def sign(v):
        return "+" if v >= 0 else "−"

    enonce = (
        f"En quelle expression peut se simplifier : "
        f"{A}/(x+{p}) {sign(B)} {abs(B)}/(x−{p}) "
        f"{sign(C)} {abs(C)}/(x^2−{p*p}) ?"
    )

    # Candidats distracteurs, filtrés pour unicité
    candidates = [
        fmt_expr(sp.simplify(expr * 2)),
        fmt_expr(sp.simplify(expr / 2)),
        fmt_expr(sp.simplify(expr + 1)),
        fmt_expr(sp.simplify(expr - 1)),
    ]
    seen = {correct}
    distractors = []
    for c in candidates:
        if c not in seen:
            distractors.append(c)
            seen.add(c)
    while len(distractors) < 3:
        distractors.append("Autre chose")

    options = [correct] + distractors[:3]
    rng.shuffle(options)

    return {
        "type": "T03_fraction",
        "enonce": enonce,
        "options": options,
        "reponse": correct,
        "params": {"p": p, "A": A, "B": B, "C": C},
    }