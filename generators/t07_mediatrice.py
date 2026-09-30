import random
import sympy as sp
from .utils import fmt_line

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
        if (xA, yA) == (xB, yB) or xA == xB or yA == yB:
            continue
        if (xA, yA, xB, yB) not in avoid and (xB, yB, xA, yA) not in avoid:
            break

    xI = sp.Rational(xA + xB, 2)
    yI = sp.Rational(yA + yB, 2)
    m = sp.Rational(yB - yA, xB - xA)
    m_perp = -1 / m
    p = yI - m_perp * xI
    correct = fmt_line(m_perp, p)

    enonce = (
        f"Dans un repère orthonormé, on considère A({xA},{yA}) et B({xB},{yB}). "
        f"Une équation de la médiatrice de [AB] est :"
    )

    distractors = [
        fmt_line(m, p),
        fmt_line(m_perp, p + 1),
        fmt_line(-m_perp, p),
    ]
    options = [correct] + distractors
    rng.shuffle(options)

    return {
        "type": "T07_mediatrice",
        "enonce": enonce,
        "options": options,
        "reponse": correct,
        "params": {"xA": xA, "yA": yA, "xB": xB, "yB": yB},
    }