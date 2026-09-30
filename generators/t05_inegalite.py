import random

CONDITIONS = [
    ("0 < x ≤ 2y",
     ["y/x ≤ 1", "0 > 1/y − 1/x", "√x ≤ √(2y)", "0 ≤ 4y² − x²"],
     ["√x ≤ √(2y)", "0 ≤ 4y² − x²"]),
    ("x > 1 et y < 1",
     ["1/x + 1/y > 1", "2x − y > 1", "x² + y² > 1", "x/y > 1"],
     ["2x − y > 1", "x² + y² > 1"]),
    ("x ≤ 2y",
     ["2x ≤ 4y", "x² ≤ 2xy", "x² < 4y²", "2x ≤ x + 2y"],
     ["2x ≤ 4y", "2x ≤ x + 2y"]),
    ("x > 2 et y > 1",
     ["x + y > 3", "xy > 2", "x² + y² > 5", "x − y > 0"],
     ["x + y > 3", "xy > 2", "x² + y² > 5"]),
    ("x > 1 et y < 0",
     ["x + y > 1", "x − y > 0", "x² + y² > 1", "xy < 0"],
     ["x − y > 0", "x² + y² > 1", "xy < 0"]),
]


def generate(rng: random.Random, avoid=None):
    cond, options, reponse = rng.choice(CONDITIONS)
    enonce = f"Soient x et y deux réels non nuls. Si {cond} alors :"
    shuffled = options[:]
    rng.shuffle(shuffled)
    return {
        "type": "T05_inegalite",
        "enonce": enonce,
        "options": shuffled,
        "reponse": reponse,
        "params": {"cond": cond},
    }