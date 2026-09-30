import random
import sympy as sp
from generators.utils import fmt_expr

X = sp.Symbol("x", real=True)


def generate(rng: random.Random, avoid=None):
    a = rng.randint(2, 9)
    b = rng.randint(1, 5)
    f = sp.cos(sp.sqrt(a * X + b))
    df = sp.diff(f, X)
    correct = fmt_expr(df)

    enonce = f"Une expression de f'(x) sur R+ de f(x) = cos(√({a}x+{b})) est :"
    distractors = [
        fmt_expr(-sp.sin(sp.sqrt(a * X + b))),
        fmt_expr(sp.sin(sp.sqrt(a * X + b))),
        fmt_expr(sp.cos(sp.sqrt(a * X + b))),
    ]
    options = [correct] + distractors
    rng.shuffle(options)

    return {
        "type": "T14_derivee",
        "enonce": enonce,
        "options": options,
        "reponse": correct,
        "params": {"a": a, "b": b},
    }