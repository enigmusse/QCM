import random
from generators.utils import fmt_poly

AVOID = [
    (2, (-5, 1, 1)),
    (3, (-3, 1, 2)),
    (4, (-2, 1, 3)),
    (3, (-1, 1, 7)),
    (-4, (-2, 1, 3)),
    (3, (-8, -1, -1)),    
    (2, (1, 4, 5)),      
]


def generate(rng: random.Random, avoid=None):
    avoid = avoid or AVOID
    for _ in range(200):
        a = rng.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        roots = tuple(sorted(rng.choices(range(-5, 6), k=3)))
        if (a, roots) not in avoid:
            break

    r1, r2, r3 = roots
    b = -a * (r1 + r2 + r3)
    c = a * (r1 * r2 + r1 * r3 + r2 * r3)
    d = -a * r1 * r2 * r3
    result = r1 + 2 * r2 - r3

    poly_str = fmt_poly([a, b, c, d])
    enonce = (
        f"On considère P(X) = {poly_str}. "
        f"Déterminer les racines x1≤x2≤x3. Que vaut x1 + 2x2 − x3 ?"
    )

    options = [result, result + 1, result - 1, result + 3]
    rng.shuffle(options)

    return {
        "type": "T01_polynome",
        "enonce": enonce,
        "options": options,
        "reponse": result,
        "params": {"a": a, "roots": list(roots)},
    }