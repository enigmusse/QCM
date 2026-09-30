import random
import sympy as sp
from generators.utils import fmt_expr, fmt_term

X = sp.Symbol("x", real=True)


def _poly_factor(a, b):
    """Formate ax + b proprement."""
    if a == 1:
        base = "x"
    elif a == -1:
        base = "-x"
    else:
        base = f"{a}x"
    tail = fmt_term(b, "", first=False)
    return f"{base} {tail}" if tail else base


def _quad(c, d):
    """Formate x² + cx + d proprement."""
    base = "x²"
    if c != 0:
        base += " " + fmt_term(c, "x", first=False)
    if d != 0:
        base += " " + fmt_term(d, "", first=False)
    return base


def generate(rng: random.Random, avoid=None):
    for _ in range(50):
        if rng.random() < 0.5:
            a = rng.randint(1, 3); b = rng.randint(-3, 3)
            c = rng.randint(-3, 3); d = rng.randint(-3, 3)
            prim = (sp.Rational(a, 2)) * sp.exp(X**2 + c * X + d)
            f_str = f"({_poly_factor(a, b)})e^({_quad(c, d)})"
            x1, x2 = sorted(rng.sample(range(-3, 4), 2))
        else:
            a = rng.randint(1, 4); b = rng.randint(-3, 3)
            c = rng.randint(-3, 3); d = rng.randint(-3, 3)
            prim = (sp.Rational(a, 2)) * sp.sin(X**2 + c * X + d)
            f_str = f"({_poly_factor(a, b)})cos({_quad(c, d)})"
            x1, x2 = sorted(rng.sample(range(0, 4), 2))

        val = sp.simplify(prim.subs(X, x2) - prim.subs(X, x1))
        correct = fmt_expr(val)

        candidates = [
            fmt_expr(sp.simplify(val + 1)),
            fmt_expr(sp.simplify(val - 1)),
            fmt_expr(sp.simplify(val * 2)),
            fmt_expr(sp.simplify(-val)),
        ]
        seen = {correct}
        distractors = []
        for c_ in candidates:
            if c_ not in seen:
                distractors.append(c_)
                seen.add(c_)
            if len(distractors) >= 3:
                break
        if len(distractors) < 3:
            continue

        enonce = f"La valeur de ∫_{x1}^{x2} {f_str} dx est :"
        options = [correct] + distractors[:3]
        rng.shuffle(options)

        return {
            "type": "T15_integrale",
            "enonce": enonce, "options": options,
            "reponse": correct,
            "params": {},
        }