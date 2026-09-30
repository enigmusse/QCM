import random
import sympy as sp

X = sp.Symbol("x", real=True)


def _unique_options(correct, candidates, rng):
    seen = {str(correct)}
    distractors = []
    for c in candidates:
        s = str(c)
        if s not in seen:
            distractors.append(s)
            seen.add(s)
        if len(distractors) >= 3:
            break
    while len(distractors) < 3:
        distractors.append("Autre chose")
    options = [str(correct)] + distractors[:3]
    rng.shuffle(options)
    return options


def generate(rng: random.Random, avoid=None):
    sous_type = rng.choice(["lineaire", "second_degre"])

    if sous_type == "lineaire":
        a = rng.randint(1, 5); b = rng.randint(1, 5)
        c = rng.randint(1, 8); d = rng.randint(1, 5)
        e = rng.randint(1, 6)
        sol = sp.Rational(a * e - c * d, b * d + e)
        correct = sp.sstr(sol)
        candidates = [
            sp.sstr(sol + 1), sp.sstr(sol - 1), sp.sstr(-sol), sp.sstr(sol * 2),
        ]
        enonce = (
            f"L'équation ({a} - x)/({b}x + {c}) = {d}/{e} a comme solution :"
        )
    else:
        a = rng.randint(1, 5); b = rng.randint(1, 6)
        c = rng.randint(1, 5); d = rng.randint(1, 5)
        eq = sp.Eq((a - X) / (b * X + c), X / d)
        sols = sp.solve(eq, X)
        if len(sols) != 2:
            return generate(rng, avoid)
        s1, s2 = sols
        correct = f"{sp.sstr(s1)} et {sp.sstr(s2)}"
        candidates = [
            f"{sp.sstr(s1 + 1)} et {sp.sstr(s2)}",
            f"{sp.sstr(s1)} et {sp.sstr(s2 - 1)}",
            f"{sp.sstr(s1 - 1)} et {sp.sstr(s2 + 1)}",
        ]
        enonce = (
            f"L'équation ({a} - x)/({b}x + {c}) = x/{d} a comme solutions :"
        )

    options = _unique_options(correct, candidates, rng)

    return {
        "type": "T10_equation",
        "enonce": enonce, "options": options,
        "reponse": correct,
        "params": {},
    }