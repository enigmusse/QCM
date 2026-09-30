import random
from fractions import Fraction
from sympy import factorint


def _exposants(k1, p1, e1, p2, e2, p3, e3, p4, e4, k2, p5, e5):
    """Calcule les exposants de chaque premier dans l'expression."""
    exp = {}

    def add(n, mult):
        for prime, e in factorint(n).items():
            exp[prime] = exp.get(prime, Fraction(0)) + mult * e

    add(k1, e1)
    exp[p1] = exp.get(p1, Fraction(0)) + Fraction(e1, 2)
    add(p2, e2)
    add(p3, e3)
    add(p4, -e4)
    add(k2, -e5)
    exp[p5] = exp.get(p5, Fraction(0)) - Fraction(e5, 2)
    return exp


def generate(rng: random.Random, avoid=None):
    for _ in range(300):
        p1 = rng.choice([2, 3, 5, 7])
        p2 = rng.choice([2, 3, 5])
        p3 = rng.choice([10, 12, 15, 20])
        p4 = rng.choice([2, 3, 5])
        p5 = rng.choice([2, 3, 5])
        k1, k2 = rng.choice([2, 3]), rng.choice([2, 3])
        e1, e2 = rng.choice([2, 4]), rng.choice([2, 4])
        e3, e5 = rng.choice([1, 2]), rng.choice([2, 4])
        e4 = rng.choice([-3, -2, -1])

        exp = _exposants(k1, p1, e1, p2, e2, p3, e3, p4, e4, k2, p5, e5)

        # Résultat entier seulement si tous les exposants sont entiers positifs
        if all(v.denominator == 1 and v >= 0 for v in exp.values()):
            result = 1
            for prime, e in exp.items():
                result *= prime ** int(e)
            if result > 1:
                break
    else:
        # fallback garanti
        k1, p1, e1 = 2, 5, 2
        p2, e2 = 5, 4
        p3, e3 = 20, 2
        p4, e4 = 5, -3
        k2, p5, e5 = 2, 20, 2
        result = 2**2 * 5**9

    enonce = (
        f"En quelle expression peut se simplifier : "
        f"({k1}√{p1})^{e1} × {p2}^{e2} × {p3}^{e3} / "
        f"({p4}^{e4} × ({k2}√{p5})^{e5}) ?"
    )

    # Format du résultat : "2^a * 5^b"
    parts = []
    for prime, e in sorted(exp.items()):
        if e != 0:
            if e == 1:
                parts.append(f"{prime}")
            else:
                parts.append(f"{prime}^{int(e)}")
    correct = " * ".join(parts) if parts else str(result)

    options = [correct, correct + " * 2", correct + " * 5", "Autre chose"]
    rng.shuffle(options)

    return {
        "type": "T02_puissance",
        "enonce": enonce,
        "options": options,
        "reponse": correct,
        "params": {"k1": k1, "p1": p1, "e1": e1, "p2": p2, "e2": e2,
                   "p3": p3, "e3": e3, "p4": p4, "e4": e4,
                   "k2": k2, "p5": p5, "e5": e5},
    }