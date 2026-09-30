import random


def generate(rng: random.Random, avoid=None):
    k = rng.choice([2, 3, 4, 5])
    correct = f"[{k} ; +∞["
    enonce = f"Le domaine de définition de f(x) = √(x - {k}) · ln(x + 2) est :"

    distractors = [
        f"] -2 ; +∞[",
        f"] -2 ; {k}]",
        f"]{k} ; +∞[",
    ]
    options = [correct] + distractors
    rng.shuffle(options)

    return {
        "type": "T13_domaine",
        "enonce": enonce,
        "options": options,
        "reponse": correct,
        "params": {"k": k},
    }