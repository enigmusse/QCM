import random
import sympy as sp

X = sp.Symbol("x", real=True)

FONCTIONS = [
    ("sin(x)/x^2 * ln(1+x)", 1),
    ("(exp(-x/2) - cos(sqrt(x)))/x^2", sp.Rational(1, 12)),
    ("(1 - cos(x))/x^2", sp.Rational(1, 2)),
    ("ln(1+x)/x", 1),
    ("(exp(x) - 1 - x)/x^2", sp.Rational(1, 2)),
    ("(sin(x) - x)/x^3", sp.Rational(-1, 6)),
    ("(sqrt(1+x) - 1 - x/2)/x^2", sp.Rational(-1, 8)),
    ("(exp(x**2) - cos(x))/x^2", sp.Rational(3, 2)),
]


def generate(rng: random.Random, avoid=None):
    f, expected = rng.choice(FONCTIONS)
    correct = sp.sstr(expected)

    enonce = f"Déterminer la limite suivante (vous pouvez utiliser des DL) : lim_{{x→0}} {f}"

    options = [correct, sp.sstr(-expected), "0", "+∞"]
    rng.shuffle(options)

    return {
        "type": "T10_limite",
        "enonce": enonce,
        "options": options,
        "reponse": correct,
        "params": {"f": f},
    }