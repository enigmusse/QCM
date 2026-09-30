import random
from fractions import Fraction
from generators.utils import fmt_term


def _fmt_fraction(frac):
    if frac.denominator == 1:
        return str(frac.numerator)
    return f"{frac.numerator}/{frac.denominator}"


def _fmt_mixed(a, b, c):
    """Formate 'a + b/c' proprement."""
    if a == 0:
        return _fmt_fraction(Fraction(b, c))
    tail = fmt_term(b, f"/{c}", first=False) if b != 0 else ""
    return f"{a} {tail}" if tail else str(a)


def generate(rng: random.Random, avoid=None):
    for _ in range(50):
        a = rng.randint(-3, 5); b = rng.randint(-5, 5); c = rng.randint(2, 6)
        d = rng.randint(-3, 5); e = rng.randint(-5, 5); f = rng.randint(2, 6)

        num = Fraction(a) + Fraction(b, c)
        den = Fraction(d) + Fraction(e, f)
        if den == 0:
            continue
        val = num / den

        enonce = (
            f"Que vaut l'expression : "
            f"({_fmt_mixed(a, b, c)}) / ({_fmt_mixed(d, e, f)}) ?"
        )

        correct = _fmt_fraction(val)
        candidates = [
            _fmt_fraction(val + 1),
            _fmt_fraction(val - 1),
            _fmt_fraction(-val),
            _fmt_fraction(val * 2),
        ]
        seen = {correct}
        distractors = []
        for c_ in candidates:
            if c_ not in seen:
                distractors.append(c_)
                seen.add(c_)
            if len(distractors) >= 3:
                break
        while len(distractors) < 3:
            distractors.append("Autre chose")
        options = [correct] + distractors[:3]
        rng.shuffle(options)

        return {
            "type": "T07_fractions_imbriquees",
            "enonce": enonce, "options": options,
            "reponse": correct,
            "params": {"a": a, "b": b, "c": c, "d": d, "e": e, "f": f},
        }