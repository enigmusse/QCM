import random
import sympy as sp
from generators.utils import fmt_term

X = sp.Symbol("x")


def _lin(a, b):
    """Formate (ax + b) proprement."""
    if a == 1:
        base = "x"
    elif a == -1:
        base = "-x"
    else:
        base = f"{a}x"
    tail = fmt_term(b, "", first=False)
    return f"({base} {tail})" if tail else f"({base})"


def generate(rng: random.Random, avoid=None):
    m = rng.randint(1, 5); n = rng.randint(1, 6)
    p = rng.randint(1, 6); q = rng.randint(1, 6)
    r = rng.randint(1, 6); s = rng.randint(-6, 6)

    expr = (m * X + n) ** 3 - (p * X + q) * (r * X + s)
    poly = sp.Poly(sp.expand(expr), X)
    e = int(poly.coeff_monomial(1))
    d = int(poly.coeff_monomial(X))
    c = int(poly.coeff_monomial(X**2))
    b = int(poly.coeff_monomial(X**3))
    a = int(poly.coeff_monomial(X**4)) if poly.degree() >= 4 else 0
    val = a + 2 * b - c - d + e

    enonce = (
        f"Simplifier {_lin(m, n)}³ - {_lin(p, q)}{_lin(r, s)} "
        f"sous la forme ax⁴ + bx³ + cx² + dx + e. "
        f"Que vaut a + 2b - c - d + e ?"
    )

    candidates = [str(val + 1), str(val - 1), str(val + 5), str(val - 5)]
    seen = {str(val)}
    distractors = []
    for c_ in candidates:
        if c_ not in seen:
            distractors.append(c_)
            seen.add(c_)
        if len(distractors) >= 3:
            break
    options = [str(val)] + distractors[:3]
    rng.shuffle(options)

    return {
        "type": "T09_poly_developpe",
        "enonce": enonce, "options": options,
        "reponse": str(val),
        "params": {"m": m, "n": n, "p": p, "q": q, "r": r, "s": s},
    }