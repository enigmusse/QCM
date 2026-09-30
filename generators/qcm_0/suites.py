import random
import sympy as sp


def generate(rng: random.Random, avoid=None):
    a = rng.choice([2, 3, 4, 5])
    b = rng.randint(1, 5)
    u0 = rng.randint(-3, 5)

    # Suite u_{n+1} = u_n/a + b, v_n = u_n - a*b/(a-1)
    # v_n géométrique de raison 1/a, u_n → a*b/(a-1)

    limite = sp.Rational(a * b, a - 1)
    correct = sp.sstr(limite)

    enonce = (
        f"Soit (u_n) définie par u_0 = {u0} et u_(n+1) = u_n/{a} + {b}. "
        f"On pose v_n = u_n - {sp.sstr(limite)}. La limite de (u_n) est :"
    )

    distractors = [sp.sstr(limite + 1), sp.sstr(limite - 1), "+∞", "Autre chose"]
    options = [correct] + distractors[:3]
    rng.shuffle(options)

    return {
        "type": "T24_suites",
        "enonce": enonce,
        "options": options,
        "reponse": correct,
        "params": {"a": a, "b": b, "u0": u0},
    }