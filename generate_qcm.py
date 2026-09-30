#!/usr/bin/env python3
"""Génère un QCM : choisir matière → type → numéro."""
import argparse
import json
import random
from pathlib import Path

from registry import list_matieres, list_types, list_numeros, get_config, get_generators
from generators.utils import postprocess_unique


def has_duplicate_options(q):
    opts = [str(o).strip() for o in q["options"]]
    return len(opts) != len(set(opts))


def generate_questions(generators, n, seed=None):
    """Génère n questions en respectant l'ordre des générateurs (cycle si n > len)."""
    rng = random.Random(seed)
    questions = []
    for i in range(n):
        g = generators[i % len(generators)]
        for _ in range(10):
            q = g.generate(rng)
            if not has_duplicate_options(q):
                q = postprocess_unique(q, rng)
                questions.append(q)
                break
        else:
            questions.append(postprocess_unique(q, rng))
    return questions


def ask_menu():
    print("\n" + "=" * 60)
    print("QCM — Sélection du sujet")
    print("=" * 60)

    matieres = list_matieres()
    print("\nMatière disponible :")
    for i, m in enumerate(matieres, 1):
        print(f"  {i}. {m}")
    choix = input("\nVotre choix (défaut: 1) : ").strip()
    matiere = matieres[int(choix) - 1] if choix.isdigit() and 1 <= int(choix) <= len(matieres) else matieres[0]

    types = list_types(matiere)
    print(f"\nType de QCM ({matiere}) :")
    for i, t in enumerate(types, 1):
        print(f"  {i}. {t}")
    choix = input("\nVotre choix (défaut: 1) : ").strip()
    type_qcm = types[int(choix) - 1] if choix.isdigit() and 1 <= int(choix) <= len(types) else types[0]

    numeros = list_numeros(matiere, type_qcm)
    print(f"\nNuméro du QCM ({matiere} / {type_qcm}) :")
    for i, n in enumerate(numeros, 1):
        cfg = get_config(matiere, type_qcm, n)
        print(f"  {i}. QCM {n} — {cfg['label']}")
    choix = input("\nVotre choix (défaut: 1) : ").strip()
    numero = numeros[int(choix) - 1] if choix.isdigit() and 1 <= int(choix) <= len(numeros) else numeros[0]

    return matiere, type_qcm, numero


def pretty_print(qcm):
    print("\n" + "=" * 70)
    print(f"QCM — {len(qcm)} questions")
    print("=" * 70)
    for q in qcm:
        print(f"\nQuestion {q.get('numero', '?')} [{q['type']}]")
        print(q["enonce"])
        for opt in q["options"]:
            print(f"   ☐ {opt}")
        rep = q["reponse"]
        if isinstance(rep, list):
            rep = ", ".join(str(r) for r in rep)
        suffix = ""
        mr = q.get("reponse_math")
        if mr and mr != q["reponse"]:
            suffix = f"  →  valeur exacte : {mr}"
        print(f"   → Réponse : {rep}{suffix}")


def main():
    p = argparse.ArgumentParser(description="Générateur de QCM")
    p.add_argument("--matiere", default=None)
    p.add_argument("--type", dest="type_qcm", default=None)
    p.add_argument("--numero", type=int, default=None)
    p.add_argument("-n", type=int, default=None)
    p.add_argument("--random", action="store_true",
                   help="Mode aléatoire : seed tirée au hasard (questions différentes à chaque run)")
    p.add_argument("--seed", type=int, default=0,
                   help="Seed fixe (0 par défaut). Ignoré si --random.")
    p.add_argument("--shuffle", action="store_true",
                   help="Mélanger l'ordre des questions (désactivé par défaut)")
    p.add_argument("-o", "--output", default=None)
    p.add_argument("--menu", action="store_true")
    args = p.parse_args()

    if args.menu or (args.matiere is None and args.type_qcm is None and args.numero is None):
        matiere, type_qcm, numero = ask_menu()
    else:
        matiere = args.matiere or "maths"
        type_qcm = args.type_qcm or "rannou"
        numero = args.numero if args.numero is not None else 1

    # Choix de la seed
    seed = None if args.random else args.seed
    mode_label = "aléatoire (seed random)" if args.random else f"reproductible (seed={seed})"

    cfg = get_config(matiere, type_qcm, numero)
    generators = get_generators(matiere, type_qcm, numero)
    n = args.n or cfg.get("n_default", 10)

    print(f"\n>>> {matiere} / {type_qcm} / QCM {numero} — {cfg['label']}")
    print(f">>> {n} questions parmi {len(generators)} types")
    print(f">>> Mode : {mode_label}, ordre : {'mélangé' if args.shuffle else 'QCM original'}")

    qcm = generate_questions(generators, n, seed)
    if args.shuffle:
        random.Random(seed).shuffle(qcm)
    for i, q in enumerate(qcm, 1):
        q["numero"] = i

    pretty_print(qcm)

    if args.output:
        Path(args.output).write_text(
            json.dumps(qcm, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"\n→ Exporté vers {args.output}")


if __name__ == "__main__":
    main()