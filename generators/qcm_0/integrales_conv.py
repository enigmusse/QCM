import random

INTEGRALES = [
    ("∫₀¹ (eˣ - 1)/x dx",              True),
    ("∫₀¹ 1/x² dx",                    False),
    ("∫₁^∞ (x² + √x)/(x⁴ + sin(x)) dx", True),
    ("∫₁^∞ (x + 1)/(x² + 3) dx",       False),
]


def generate(rng: random.Random, avoid=None):
    s = INTEGRALES[:]
    rng.shuffle(s)
    options = [x[0] for x in s]
    reponse = [x[0] for x in s if x[1]]
    enonce = "Parmi les intégrales suivantes, lesquelles convergent ?"

    return {
        "type": "T32_integrales_conv",
        "enonce": enonce,
        "options": options,
        "reponse": reponse,
        "params": {},
    }