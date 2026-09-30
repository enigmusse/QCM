import random
import sympy as sp
from generators.utils import fmt_expr

X, Y = sp.symbols("x y")

AVOID = [
    (0, 1, -1, 3),
    (4, 1, 0, 2),
    (-2, 1, 2, 3),
    (3, -1, -1, 0),
    (3, 4, -1, 2),
    (2, -3, -4, -1),  
    (1, 2, 4, 1),        
]


def generate(rng: random.Random, avoid=None):
    avoid = avoid or AVOID
    for _ in range(200):
        xA = rng.randint(-4, 4)
        yA = rng.randint(-4, 4)
        xB = rng.randint(-4, 4)
        yB = rng.randint(-4, 4)
        if (xA, yA) == (xB, yB):
            continue
        if (xA, yA, xB, yB) not in avoid and (xB, yB, xA, yA) not in avoid:
            break

    xI = sp.Rational(xA + xB, 2)
    yI = sp.Rational(yA + yB, 2)
    r2 = (xA - xI) ** 2 + (yA - yI) ** 2

    eq = sp.expand((X - xI) ** 2 + (Y - yI) ** 2 - r2)
    correct = fmt_expr(eq) + " = 0"

    enonce = (
        f"Dans un repère orthonormé, on considère A({xA},{yA}) et B({xB},{yB}). "
        f"Une équation du cercle de diamètre [AB] est :"
    )

    eq2 = sp.expand((X - xI - 1) ** 2 + (Y - yI) ** 2 - r2)
    eq3 = sp.expand((X - xI) ** 2 + (Y - yI - 1) ** 2 - r2)
    distractors = [fmt_expr(eq2) + " = 0", fmt_expr(eq3) + " = 0", "Autre chose"]
    options = [correct] + distractors
    rng.shuffle(options)

    return {
        "type": "T08_cercle",
        "enonce": enonce,
        "options": options,
        "reponse": correct,
        "params": {"xA": xA, "yA": yA, "xB": xB, "yB": yB},
    }