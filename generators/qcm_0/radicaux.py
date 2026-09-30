import random
import sympy as sp
from generators.utils import fmt_term


def _fmt_rad(p, q, r):
    """Formate p ± q√r proprement."""
    if q == 0:
        return str(p)
    if p == 0:
        return f"{fmt_term(q, f'√{r}', first=True)}"
    return f"{p} {fmt_term(q, f'√{r}', first=False)}"


def generate(rng: random.Random, avoid=None):
    for _ in range(100):
        a = rng.randint(2, 6)
        b = rng.choice([8, 12, 18, 20, 24, 45, 48, 75])
        c = rng.randint(3, 9)
        d = rng.randint(2, 6)
        e = rng.randint(2, 4)
        f = rng.choice([3, 5, 6, 7])

        expr = (a * sp.sqrt(b) - c) ** 2 - (d - e * sp.sqrt(f)) ** 2
        simplified = sp.expand(expr)
        if simplified.is_number:
            break

    coeffs = sp.expand(simplified).as_coefficients_dict()
    sqrt_key = next((k for k in coeffs if k.is_Pow and k.exp == sp.Rational(1, 2)), None)
    p = int(coeffs.get(sp.Integer(1), 0))
    q = int(coeffs.get(sqrt_key, 0)) if sqrt_key else 0
    radicand = int(sqrt_key.base) if sqrt_key else 0

    correct = _fmt_rad(p, q, radicand) if radicand else str(p)

    enonce = f"En quelle expression peut se simplifier : ({a}√{b} - {c})² - ({d} - {e}√{f})² ?"

    distractors = [
        _fmt_rad(p + 1, q, radicand),
        _fmt_rad(p, q + 1, radicand),
        _fmt_rad(p - 1, -q, radicand),
    ]
    options = [correct] + distractors
    rng.shuffle(options)

    return {
        "type": "T03_radicaux",
        "enonce": enonce,
        "options": options,
        "reponse": correct,
        "params": {"a": a, "b": b, "c": c, "d": d, "e": e, "f": f},
    }