import random


def generate(rng: random.Random, avoid=None):
    for _ in range(50):
        a = rng.choice([1, 2, 3])
        b = rng.choice([2, 3, 5])
        c = rng.choice([2, 3, 5])
        d = rng.choice([2, 3, 4])
        e = rng.choice([2, 3, 5])
        f = rng.choice([2, 3, 5])

        val = a * b**c - d * e**f
        correct = str(val)

        candidates = [str(val + 1), str(val - 1), str(val * 2), str(val + 5)]
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

        enonce = (
            f"En quelle expression peut se simplifier : "
            f"{a}·e^{c}ln({b}) - {d}·e^{f}ln({e}) ?"
        )
        options = [correct] + distractors[:3]
        rng.shuffle(options)

        return {
            "type": "T05_expo",
            "enonce": enonce, "options": options,
            "reponse": correct,
            "params": {"a": a, "b": b, "c": c, "d": d, "e": e, "f": f},
        }