#!/usr/bin/env python3
"""QCM interactif : répondre aux questions et avoir la correction."""
import random
import sys
from generators import (
    t01_polynome, t02_puissance, t03_fraction, t04_systeme, t05_inegalite,
    t06_droite, t07_mediatrice, t08_cercle, t09_points_cercle, t10_limite,
)

GENERATORS = [
    t01_polynome, t02_puissance, t03_fraction, t04_systeme, t05_inegalite,
    t06_droite, t07_mediatrice, t08_cercle, t09_points_cercle, t10_limite,
]

# Types à réponses multiples (l'utilisateur saisit plusieurs lettres)
MULTI_TYPES = {"T05_inegalite", "T09_points_cercle"}


# ---------- affichage ----------

def _has_duplicate_options(q):
    """Détecte si deux options sont identiques (bug de générateur)."""
    opts = [str(o).strip() for o in q["options"]]
    return len(opts) != len(set(opts))


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


# ---------- saisie ----------

def ask_answer(q):
    """Retourne la liste des lettres choisies (ex: ['A', 'C'])."""
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

        lettres = raw.replace(",", " ").replace(";", " ").split()
        lettres = [l for l in lettres if l]

        if not lettres:
            print("Veuillez saisir au moins une lettre (ou 'q' pour quitter).")
            continue

        invalid = [l for l in lettres if l.lower() not in lettres_valides]
        if invalid:
            print(f"Lettre(s) invalide(s) : {', '.join(invalid)}. "
                  f"Choix possibles : {' '.join(lettres_valides.upper())}")
            continue

        if q["type"] not in MULTI_TYPES and len(lettres) > 1:
            print("Cette question attend UNE seule réponse.")
            continue

        return sorted(set(lettres))


# ---------- correction ----------

def compute_correct_letters(q):
    """Retourne les lettres correspondant aux bonnes réponses."""
    lettres = "ABCDEFGH"
    rep = q["reponse"]
    if not isinstance(rep, list):
        rep = [rep]

    correct = set()
    for r in rep:
        for i, opt in enumerate(q["options"]):
            if str(opt).strip() == str(r).strip():
                correct.add(lettres[i])
    return sorted(correct)


def correct(q, user_letters):
    """Retourne (est_correct, correct_letters, message)."""
    lettres = "ABCDEFGH"
    rep = q["reponse"]
    if not isinstance(rep, list):
        rep = [rep]

    correct_set = set()
    for r in rep:
        for i, opt in enumerate(q["options"]):
            if str(opt).strip() == str(r).strip():
                correct_set.add(lettres[i])

    user_set = set(user_letters)
    is_ok = (user_set == correct_set)

    rep_str = ", ".join(f"{l} ({q['options'][lettres.index(l)]})"
                        for l in sorted(correct_set))
    return is_ok, sorted(correct_set), rep_str


# ---------- boucle principale ----------

def run(n_questions=10, seed=None, immediate=True, shuffle=True):
    rng = random.Random(seed)

    # Génère n_questions en tirant des types au hasard (avec remise possible)
    chosen = [rng.choice(GENERATORS) for _ in range(n_questions)]
    questions = []
    for g in chosen:
        for _ in range(10):          # max 10 essais
            q = g.generate(rng)
            if not _has_duplicate_options(q):
                questions.append(q)
                break
        else:
            # Si le générateur n'arrive pas à produire d'options uniques
            questions.append(q)
    if shuffle:
        rng.shuffle(questions)

    bar("QCM interactif — tapez 'q' pour quitter à tout moment")
    print(f"{n_questions} questions, correction {'immédiate' if immediate else 'à la fin'}")
    print("Entrée = valider votre réponse")

    score = 0
    results = []  # (idx, question, user_letters, is_correct, correct_letters)

    for i, q in enumerate(questions, 1):
        show_question(q, i, n_questions)
        user = ask_answer(q)
        ok, correct_letters, rep_str = correct(q, user)

        results.append((i, q, user, ok, correct_letters))
        if ok:
            score += 1

        if immediate:
            print()
            if ok:
                print(f"✅ Correct ! Réponse : {rep_str}")
            else:
                print(f"❌ Incorrect. Votre réponse : {' '.join(user)}")
                print(f"   Bonne réponse : {rep_str}")

    # Bilan final
    bar("RÉSULTAT")
    pct = 100 * score / n_questions
    print(f"Score : {score}/{n_questions}  ({pct:.0f}%)")
    print()

    # Correction détaillée
    if not immediate:
        for i, q, user, ok, correct_letters in results:
            status = "✅" if ok else "❌"
            lettres = "ABCDEFGH"
            rep_str = ", ".join(f"{l} ({q['options'][lettres.index(l)]})"
                                for l in correct_letters)
            print(f"{status} Q{i} [{q['type']}] — Votre réponse : {' '.join(user) or '—'}")
            print(f"     Bonne réponse : {rep_str}")
            print()

    # Statistiques par type
    print("Détail par type :")
    by_type = {}
    for i, q, user, ok, _ in results:
        t = q["type"]
        n, c = by_type.get(t, (0, 0))
        by_type[t] = (n + 1, c + (1 if ok else 0))
    for t, (n, c) in sorted(by_type.items()):
        barre = "█" * c + "░" * (n - c)
        print(f"  {t:22s} {c}/{n}  {barre}")


# ---------- CLI ----------

def main():
    import argparse
    p = argparse.ArgumentParser(description="QCM interactif")
    p.add_argument("-n", "--number", type=int, default=10, help="Nombre de questions")
    p.add_argument("--seed", type=int, default=None)
    p.add_argument("--final", action="store_true",
                   help="Correction à la fin (par défaut : immédiate)")
    p.add_argument("--no-shuffle", action="store_true",
                   help="Garde l'ordre des types")
    args = p.parse_args()

    run(
        n_questions=args.number,
        seed=args.seed,
        immediate=not args.final,
        shuffle=not args.no_shuffle,
    )


if __name__ == "__main__":
    main()