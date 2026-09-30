#!/usr/bin/env python3
"""QCM interactif : répondre aux questions et avoir la correction."""
import argparse
import random
import sys

from registry import get_generators
from generators.utils import postprocess_unique

MULTI_TYPES = {"T05_inegalite", "T09_points_cercle", "T32_integrales_conv", "T33_series_conv"}


def _has_duplicate_options(q):
    opts = [str(o).strip() for o in q["options"]]
    return len(opts) != len(set(opts))


def _generate_all(generators, n, seed):
    """Génère n questions dans l'ordre des générateurs (cycle si besoin)."""
    rng = random.Random(seed)
    questions = []
    for i in range(n):
        g = generators[i % len(generators)]
        for _ in range(10):
            q = g.generate(rng)
            if not _has_duplicate_options(q):
                questions.append(postprocess_unique(q, rng))
                break
        else:
            questions.append(postprocess_unique(q, rng))
    return questions


def bar(title=""):
    print("\n" + "=" * 70)
    if title:
        print(title)
        print("=" * 70)


def show_question(q, idx, total):
    bar(f"Question {idx}/{total}  [{q['type']}]")
    print(q["enonce"])
    print()
    lettres = "ABCDEFGH"
    for i, opt in enumerate(q["options"]):
        print(f"  {lettres[i]}. {opt}")
    if q["type"] in MULTI_TYPES:
        print("\n(plusieurs réponses possibles — séparer par des espaces, ex: 'A C')")


def ask_answer(q):
    lettres_valides = "ABCDEFGH"[: len(q["options"])].lower()
    while True:
        try:
            raw = input("\nVotre réponse : ").strip().upper()
        except (EOFError, KeyboardInterrupt):
            print("\n(interrompu)")
            sys.exit(0)

        if raw in ("Q", "QUIT", "EXIT"):
            print("Au revoir.")
            sys.exit(0)

        lettres = [l for l in raw.replace(",", " ").replace(";", " ").split() if l]
        if not lettres:
            print("Saisissez au moins une lettre (ou 'q' pour quitter).")
            continue
        invalid = [l for l in lettres if l.lower() not in lettres_valides]
        if invalid:
            print(f"Lettre(s) invalide(s) : {', '.join(invalid)}")
            continue
        if q["type"] not in MULTI_TYPES and len(lettres) > 1:
            print("Cette question attend UNE seule réponse.")
            continue
        return sorted(set(lettres))


def correct(q, user_letters):
    lettres = "ABCDEFGH"
    rep = q["reponse"] if isinstance(q["reponse"], list) else [q["reponse"]]
    correct_set = set()
    for r in rep:
        for i, opt in enumerate(q["options"]):
            if str(opt).strip() == str(r).strip():
                correct_set.add(lettres[i])

    is_ok = (set(user_letters) == correct_set)

    parts = [f"{l} ({q['options'][lettres.index(l)]})" for l in sorted(correct_set)]
    rep_str = ", ".join(parts)
    math_rep = q.get("reponse_math")
    if math_rep and math_rep != q["reponse"]:
        rep_str += f"  →  valeur exacte : {math_rep}"

    return is_ok, sorted(correct_set), rep_str


def _print_explanation(q, prefix="   "):
    """Affiche l'explication d'une question si elle existe."""
    expl = q.get("explanation", "")
    if expl:
        print(f"{prefix}💡 {expl}")


def run(questions, immediate=True, show_expl=True):
    bar("QCM interactif — tapez 'q' pour quitter à tout moment")
    print(f"{len(questions)} questions, correction {'immédiate' if immediate else 'à la fin'}")

    score = 0
    results = []
    for i, q in enumerate(questions, 1):
        show_question(q, i, len(questions))
        user = ask_answer(q)
        ok, cl, rep_str = correct(q, user)
        results.append((i, q, user, ok, cl))
        if ok:
            score += 1

        if immediate:
            print()
            if ok:
                print(f"✅ Correct ! Réponse : {rep_str}")
            else:
                print(f"❌ Incorrect. Votre réponse : {' '.join(user) or '—'}")
                print(f"   Bonne réponse : {rep_str}")
            if show_expl:
                _print_explanation(q)

    bar("RÉSULTAT")
    print(f"Score : {score}/{len(questions)}  ({100*score/len(questions):.0f}%)")
    print()

    if not immediate:
        for i, q, user, ok, cl in results:
            status = "✅" if ok else "❌"
            lettres = "ABCDEFGH"
            rep_str = ", ".join(f"{l} ({q['options'][lettres.index(l)]})" for l in cl)
            print(f"{status} Q{i} [{q['type']}] — Votre réponse : {' '.join(user) or '—'}")
            print(f"     Bonne réponse : {rep_str}")
            if show_expl:
                _print_explanation(q)
            print()

    print("Détail par type :")
    by_type = {}
    for i, q, user, ok, _ in results:
        t = q["type"]
        n, c = by_type.get(t, (0, 0))
        by_type[t] = (n + 1, c + int(ok))
    for t, (n, c) in sorted(by_type.items()):
        barre = "█" * c + "░" * (n - c)
        print(f"  {t:22s} {c}/{n}  {barre}")


def main():
    p = argparse.ArgumentParser(description="QCM interactif")
    p.add_argument("--no-expl", action="store_true",
                   help="Ne pas afficher les explications")
    p.add_argument("--matiere", default="maths")
    p.add_argument("--type", dest="type_qcm", default="rannou")
    p.add_argument("--numero", type=int, default=1)
    p.add_argument("-n", "--number", type=int, default=10)
    p.add_argument("--no-random", action="store_true",help="Mode reproductible : seed fixe (0 par défaut). ""Sans ce flag, les questions sont aléatoires.")
    p.add_argument("--seed", type=int, default=0,
                   help="Seed fixe utilisée avec --no-random.")
    p.add_argument("--shuffle", action="store_true",
                   help="Mélanger l'ordre (désactivé par défaut)")
    p.add_argument("--final", action="store_true", help="Correction à la fin")
    args = p.parse_args()

    seed = args.seed if args.no_random else None
    generators = get_generators(args.matiere, args.type_qcm, args.numero)
    questions = _generate_all(generators, args.number, seed)
    if args.shuffle:
        random.Random(seed).shuffle(questions)

    run(questions, immediate=not args.final, show_expl=not args.no_expl)


if __name__ == "__main__":
    main()