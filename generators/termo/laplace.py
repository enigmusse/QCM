"""T06 — Loi de Laplace."""
import random

QUESTIONS = [
    {"q": "La loi de Laplace pour une adiabatique réversible d'un gaz parfait s'écrit :",
     "options": ["PV^γ = cste", "PV = cste", "P/T = cste", "V/T = cste"],
     "ans": "PV^γ = cste",
     "expl": "Adiabatique réversible ⟹ PV^γ = cste."},

    {"q": "Autre forme de la loi de Laplace :",
     "options": ["TV^(γ-1) = cste", "TV^γ = cste", "PV = cste", "T^γ V = cste"],
     "ans": "TV^(γ-1) = cste",
     "expl": "Loi de Laplace : PV^γ = TV^(γ-1) = T^γ P^(1-γ) = cste."},

    {"q": "Pour un gaz parfait MONOATOMIQUE, γ vaut :",
     "options": ["5/3 ≈ 1,67", "7/5 = 1,40", "4/3 ≈ 1,33", "1"],
     "ans": "5/3 ≈ 1,67",
     "expl": "Monoatomique : Cv = 3R/2, Cp = 5R/2, γ = 5/3."},

    {"q": "Pour un gaz parfait DIATOMIQUE (rigide) à température ambiante, γ vaut :",
     "options": ["7/5 = 1,40", "5/3 ≈ 1,67", "1", "3/2"],
     "ans": "7/5 = 1,40",
     "expl": "Diatomique rigide : Cv = 5R/2, Cp = 7R/2, γ = 7/5."},

    {"q": "Dans un diagramme de Clapeyron (P, V), une adiabatique réversible est :",
     "options": ["plus pentue qu'une isotherme",
                 "moins pentue qu'une isotherme",
                 "parallèle à l'axe des V",
                 "identique à une isotherme"],
     "ans": "plus pentue qu'une isotherme",
     "expl": "La pente d'une adiabatique est -γP/V, plus raide que celle d'une isotherme (-P/V)."},

    {"q": "Dans un diagramme (P, V), une transformation adiabatique irréversible est représentée :",
     "options": ["en pointillés", "en trait plein", "par un point", "par une horizontale"],
     "ans": "en pointillés",
     "expl": "L'irréversibilité se représente en pointillés : les états intermédiaires ne sont pas définis."},

    {"q": "Une transformation adiabatique réversible est aussi appelée :",
     "options": ["isentropique", "isotherme", "isochore", "isobare"],
     "ans": "isentropique",
     "expl": "Adiabatique (Q = 0) + réversible (Sp = 0) ⟹ ΔS = 0."},

    {"q": "La relation de Mayer pour un gaz parfait s'écrit :",
     "options": ["Cp - Cv = nR", "Cp + Cv = nR", "Cp·Cv = nR", "Cp/Cv = nR"],
     "ans": "Cp - Cv = nR",
     "expl": "Relation de Mayer : Cp - Cv = nR pour un gaz parfait."},

    {"q": "γ est défini par :",
     "options": ["γ = Cp/Cv", "γ = Cv/Cp", "γ = Cp - Cv", "γ = Cp·Cv"],
     "ans": "γ = Cp/Cv",
     "expl": "γ = Cp/Cv > 1 (car Cp > Cv)."},

    {"q": "Une transformation adiabatique irréversible d'un gaz parfait :",
     "options": ["a une entropie qui augmente",
                 "a une entropie constante",
                 "est isentropique",
                 "est impossible"],
     "ans": "a une entropie qui augmente",
     "expl": "Irréversible ⟹ Sp > 0. Adiabatique ⟹ Se = 0. Donc ΔS = Sp > 0."},
]


def generate(rng: random.Random, avoid=None):
    q = rng.choice(QUESTIONS)
    opts = q["options"][:]
    rng.shuffle(opts)
    return {
        "type": "T06_laplace",
        "enonce": q["q"], "options": opts,
        "reponse": q["ans"],
        "explanation": q.get("expl", ""),
        "params": {},
    }