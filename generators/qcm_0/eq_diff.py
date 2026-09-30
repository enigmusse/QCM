import random
import sympy as sp


def generate(rng: random.Random, avoid=None):
    a = rng.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    b = rng.choice([-5, -3, -2, 1, 2, 3, 5])
    # Éq : a·y + y' + b = 0 → y = A·e^(-a x) + b/a

    # Forme correcte : solution particulière
    c0 = sp.Rational(b, a)
    sign_c = "+" if c0 >= 0 else "-"
    correct = f"{'exp(%dx)' % (-a)} {'+' if c0 >= 0 else '-'} {abs(c0)}"

    eq_str = f"{a}y + y' {'+' if b>=0 else '-'} {abs(b)} = 0" if a else None
    enonce = f"Une solution de l'équation différentielle : {eq_str} est :"

    distractors = [
        f"{'exp(%dx)' % a} + {abs(c0)}",
        f"-{abs(c0)} + exp({-a}x)",
        "Autre chose",
    ]
    options = [correct] + distractors
    rng.shuffle(options)

    return {
        "type": "T19_eq_diff",
        "enonce": enonce,
        "options": options,
        "reponse": correct,
        "params": {"a": a, "b": b},
    }