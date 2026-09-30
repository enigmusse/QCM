import random

SERIES = [
    ("sum_{n=0}^{+∞} (-1)^n / (√(n+1) ln(n+2))", True),
    ("sum_{n=1}^{+∞} 1 / (n√n)", True),
    ("sum_{n=0}^{+∞} e^n / (2^n + n²)", False),
    ("sum_{n=0}^{+∞} (n² + 1) / (n³ + 3n)", False),
]


def generate(rng: random.Random, avoid=None):
    # Pioche 4 séries et mélange
    s = SERIES[:]
    rng.shuffle(s)
    options = [x[0] for x in s]
    reponse = [x[0] for x in s if x[1]]

    enonce = "Parmi les séries suivantes, lesquelles convergent ?"

    return {
        "type": "T33_series_conv",
        "enonce": enonce,
        "options": options,
        "reponse": reponse,
        "params": {},
    }