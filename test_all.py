#!/usr/bin/env python3
"""Teste tous les générateurs des deux QCM."""
import random
import sys
import traceback

from registry import REGISTRY, get_generators, get_config


def has_duplicate_options(q):
    opts = [str(o).strip() for o in q["options"]]
    return len(opts) != len(set(opts))


def check_enonce(text):
    """Détecte les patterns cassés dans un énoncé."""
    problems = []
    if " + -" in text or " − -" in text or " - -" in text:
        problems.append("double signe (+ -)")
    if " 0x" in text or "+ 0 " in text or " + 0)" in text:
        problems.append("zéro superflu")
    if " 1x" in text and "1x" not in text.replace(" 1x", " 1x"):
        problems.append("coefficient 1 explicite")
    if " 1e^" in text:
        problems.append("coefficient 1 devant e^")
    return problems


def check_options(options):
    """Détecte les patterns cassés dans les options."""
    problems = []
    for opt in options:
        s = str(opt)
        if " + -" in s or " − -" in s or " - -" in s:
            problems.append(f"double signe dans option : {s}")
        if s.strip() in ("+", "-", ""):
            problems.append(f"option vide : {s!r}")
    return problems


def test_generator(module, rng, n=5):
    """Teste un générateur sur n tirages."""
    errors = []
    for i in range(n):
        try:
            q = module.generate(rng)
        except Exception as e:
            errors.append(f"CRASH : {type(e).__name__}: {e}")
            traceback.print_exc()
            break

        # Vérifications structurelles
        for key in ("type", "enonce", "options", "reponse"):
            if key not in q:
                errors.append(f"clé manquante : {key}")
                break

        if "options" in q and has_duplicate_options(q):
            errors.append(f"options en double : {q['options']}")

        if "enonce" in q:
            p = check_enonce(q["enonce"])
            if p:
                errors.append(f"énoncé cassé : {p} → {q['enonce'][:80]}")

        if "options" in q:
            p = check_options(q["options"])
            if p:
                errors.append(f"options cassées : {p}")

        # Vérifie que la réponse est bien dans les options
        rep = q.get("reponse")
        opts = [str(o).strip() for o in q["options"]]
        if isinstance(rep, list):
            for r in rep:
                if str(r).strip() not in opts:
                    errors.append(f"réponse {r!r} absente des options")
        else:
            if str(rep).strip() not in opts:
                errors.append(f"réponse {rep!r} absente des options")

    return errors


def main():
    n_tirages = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    rng = random.Random(42)
    total_ok = 0
    total_ko = 0

    print("=" * 70)
    print(f"Test de tous les générateurs — {n_tirages} tirages par générateur")
    print("=" * 70)

    for matiere, types in REGISTRY.items():
        for type_qcm, numeros in types.items():
            for numero, cfg in numeros.items():
                label = f"{matiere}/{type_qcm}/QCM {numero}"
                generators = cfg["generators"]
                print(f"\n▶ {label} — {len(generators)} générateurs")

                for module in generators:
                    modname = module.__name__.split(".")[-1]
                    errors = test_generator(module, rng, n_tirages)
                    if errors:
                        total_ko += 1
                        print(f"  ❌ {modname}")
                        for e in errors[:3]:
                            print(f"       {e}")
                    else:
                        total_ok += 1
                        print(f"  ✅ {modname}")

    print("\n" + "=" * 70)
    print(f"Résultat : {total_ok} OK / {total_ko} KO")
    print("=" * 70)

    sys.exit(1 if total_ko else 0)


if __name__ == "__main__":
    main()