#!/usr/bin/env python3
"""Génère un QCM TOTALEMENT aléatoire contenant les 10 types de questions."""
import argparse
import json
import random
from pathlib import Path
from generators.utils import postprocess_unique

from generators import (
    t01_polynome, t02_puissance, t03_fraction, t04_systeme, t05_inegalite,
    t06_droite, t07_mediatrice, t08_cercle, t09_points_cercle, t10_limite,
)

GENERATORS = [
    t01_polynome, t02_puissance, t03_fraction, t04_systeme, t05_inegalite,
    t06_droite, t07_mediatrice, t08_cercle, t09_points_cercle, t10_limite,
]


def generate_qcm(seed: int | None = None, shuffle: bool = True) -> list[dict]:
    rng = random.Random(seed)
    questions = [postprocess_unique(g.generate(rng), rng) for g in GENERATORS]
    if shuffle:
        rng.shuffle(questions)
    for i, q in enumerate(questions, 1):
        q["numero"] = i
    return questions


def pretty_print(qcm: list[dict]):
    print("=" * 70)
    print("QCM — 10 questions, types variés, généré aléatoirement")
    print("=" * 70)
    for q in qcm:
        print(f"\nQuestion {q['numero']} [{q['type']}]")
        print(q["enonce"])
        for opt in q["options"]:
            print(f"   ☐ {opt}")
        rep = q["reponse"]
        if isinstance(rep, list):
            rep = ", ".join(rep)
        print(f"   → Réponse : {rep}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--seed", type=int, default=None)
    p.add_argument("--no-shuffle", action="store_true")
    p.add_argument("-o", "--output", type=str, default=None)
    args = p.parse_args()

    qcm = generate_qcm(seed=args.seed, shuffle=not args.no_shuffle)
    pretty_print(qcm)

    if args.output:
        Path(args.output).write_text(
            json.dumps(qcm, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"\n→ Exporté vers {args.output}")


if __name__ == "__main__":
    main()