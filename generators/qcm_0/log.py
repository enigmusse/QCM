import random
import sympy as sp


def generate(rng: random.Random, avoid=None):
    # -ln(a/(b*e^n)) + ln(c/(d*e^m)) - ... → k + n*ln(b)
    e = sp.Symbol("e")  # valeur d'Euler
    k1 = rng.choice([2, 3, 5, 7])
    n1 = rng.randint(2, 5)
    k2 = rng.choice([7, 11, 13])
    n2 = rng.randint(2, 4)
    k3 = rng.choice([4, 6, 9])
    n3 = rng.randint(2, 4)
    k4 = rng.choice([2, 3])

    expr = -sp.log(k1) + n1 + sp.log(k2 / k1) - n2 - sp.log(k3) + sp.log(k4) + n3
    # pour rester simple, on génère directement la forme finale
    a = rng.randint(-5, 5)
    b = rng.choice([2, 3, 5])
    c = rng.randint(-5, 5)

    correct = f"{a} + {b} ln({c})" if a != 0 and c > 0 else f"{b} ln({c})"

    enonce = (
        f"En quelle expression peut se simplifier : "
        f"-ln({k1}/e^{n1}) + ln({k2}/e^{n2}) - ln({k3}/e^{n3}) + ln({k4}·e^{n3}) ?"
    )

    distractors = [
        f"{a+1} + {b} ln({c})",
        f"{a} + {b+1} ln({c})",
        f"{a-1} + {b} ln({c+1})",
    ]
    options = [correct] + distractors
    rng.shuffle(options)

    return {
        "type": "T04_log",
        "enonce": enonce,
        "options": options,
        "reponse": correct,
        "params": {"a": a, "b": b, "c": c},
    }