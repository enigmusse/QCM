import random


def generate(rng: random.Random, avoid=None):
    correct = "-e"
    enonce = "Calculer la valeur de la série : sum_{n=0}^{+∞} (2n - 3)/n!"
    options = [correct, "e^-1", "e^2 + e^-3", "Autre chose"]
    rng.shuffle(options)

    return {
        "type": "T34_serie_valeur",
        "enonce": enonce,
        "options": options,
        "reponse": correct,
        "params": {},
    }