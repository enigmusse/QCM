import random


def _lin(a, var):
    """Retourne 'var', '2var', ... proprement."""
    if a == 1:
        return var
    if a == -1:
        return f"-{var}"
    return f"{a}{var}"


def generate(rng: random.Random, avoid=None):
    a = rng.choice([1, 2, 3, 4])
    r1 = rng.choice([2, 3, 4, 5, 6])
    r2 = rng.choice([-1, -2, -3, -4, -5])
    b = -(r1 + r2)
    c = r1 * r2

    n_solutions = 1  # r1 > 0 toujours, r2 < 0 toujours → 1 solution

    parts = [f"{_lin(a, 'e^(2x)')}"]
    if a * b != 0:
        parts.append(("+ " if a * b > 0 else "- ") + _lin(abs(a * b), "e^x"))
    if a * c != 0:
        parts.append(("+ " if a * c > 0 else "- ") + str(abs(a * c)))
    eq_str = " ".join(parts)

    enonce = f"Combien de solutions réelles possède l'équation {eq_str} = 0 ?"

    options = [str(n_solutions), str(max(0, n_solutions - 1)), str(n_solutions + 1), "Autre chose"]
    rng.shuffle(options)

    return {
        "type": "T06_eq_expo",
        "enonce": enonce,
        "options": options,
        "reponse": str(n_solutions),
        "params": {"a": a, "r1": r1, "r2": r2},
    }