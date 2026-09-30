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
        if (xA, yA) == (xB, yB):
            continue
        if xA == xB:                  # droite verticale : pas d'équation y = ...
            continue
        if yA == yB:                  # droite horizontale : m = 0, distracteurs ambigus
            continue
        if (xA, yA, xB, yB) not in avoid and (xB, yB, xA, yA) not in avoid:
            break

    m = sp.Rational(yB - yA, xB - xA)
    p = sp.Rational(yA) - m * xA
    correct = fmt_line(m, p)

    enonce = (
        f"Dans un repère orthonormé, on considère A({xA},{yA}) et B({xB},{yB}). "
        f"Une équation de la droite (AB) est :"
    )

    # Distracteurs garantis uniques
    distractors = []
    candidates = [fmt_line(m, p + 1), fmt_line(-m, p), fmt_line(m + 1, p)]
    for c in candidates:
        if c != correct and c not in distractors:
            distractors.append(c)
    while len(distractors) < 3:
        distractors.append("Autre chose")

    options = [correct] + distractors[:3]
    rng.shuffle(options)

    return {
        "type": "T06_droite",
        "enonce": enonce,
        "options": options,
        "reponse": correct,
        "params": {"xA": xA, "yA": yA, "xB": xB, "yB": yB},
    }