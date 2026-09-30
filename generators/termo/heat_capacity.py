"""T08 — Capacités thermiques Cp, Cv, γ."""
import random

QUESTIONS = [
    {"q": "Pour un gaz parfait, la 1ère loi de Joule s'écrit :",
     "options": ["U ne dépend que de T", "U ne dépend que de V",
                 "U ne dépend que de P", "U = cste"],
     "ans": "U ne dépend que de T",
     "expl": "U_gp = f(T) : l'énergie interne d'un GP ne dépend que de sa température."},

    {"q": "Pour un gaz parfait, la 2ème loi de Joule s'écrit :",
     "options": ["H ne dépend que de T", "H ne dépend que de P",
                 "H = cste", "H = U"],
     "ans": "H ne dépend que de T",
     "expl": "H_gp = f(T) : l'enthalpie d'un GP ne dépend que de sa température."},

    {"q": "Pour une transformation isotherme d'un gaz parfait, ΔU vaut :",
     "options": ["0", "nCv·ΔT", "nR·ΔT", "nCp·ΔT"],
     "ans": "0",
     "expl": "Loi de Joule : U = f(T), ΔT = 0 ⟹ ΔU = 0."},

    {"q": "Pour une transformation isotherme d'un gaz parfait, ΔH vaut :",
     "options": ["0", "nCp·ΔT", "nR·ΔT", "W"],
     "ans": "0",
     "expl": "Loi de Joule : H = f(T), ΔT = 0 ⟹ ΔH = 0."},

    {"q": "Pour une transformation isochore d'un gaz parfait :",
     "options": ["ΔU = nCv·ΔT", "ΔU = nCp·ΔT", "ΔU = 0", "ΔU = W"],
     "ans": "ΔU = nCv·ΔT",
     "expl": "dU = Cv·dT pour toute transformation d'un GP (loi de Joule)."},

    {"q": "Pour une transformation isobare d'un gaz parfait :",
     "options": ["ΔH = nCp·ΔT", "ΔH = nCv·ΔT", "ΔH = 0", "ΔH = W"],
     "ans": "ΔH = nCp·ΔT",
     "expl": "dH = Cp·dT pour toute transformation d'un GP (loi de Joule)."},

    {"q": "Pour un gaz parfait monoatomique, Cv molaire vaut :",
     "options": ["3R/2", "5R/2", "R", "7R/2"],
     "ans": "3R/2",
     "expl": "Monoatomique : 3 degrés de translation ⟹ Cv,m = 3R/2."},

    {"q": "Pour un gaz parfait diatomique rigide, Cv molaire vaut :",
     "options": ["5R/2", "3R/2", "7R/2", "R"],
     "ans": "5R/2",
     "expl": "Diatomique rigide : 3 translations + 2 rotations ⟹ Cv,m = 5R/2."},

    {"q": "Pour un gaz parfait monoatomique, Cp molaire vaut :",
     "options": ["5R/2", "3R/2", "7R/2", "4R"],
     "ans": "5R/2",
     "expl": "Cp,m = Cv,m + R = 3R/2 + R = 5R/2."},

    {"q": "Pour un gaz parfait diatomique rigide, Cp molaire vaut :",
     "options": ["7R/2", "5R/2", "3R/2", "5R"],
     "ans": "7R/2",
     "expl": "Cp,m = Cv,m + R = 5R/2 + R = 7R/2."},

    {"q": "La capacité thermique massique cp de l'eau liquide vaut environ :",
     "options": ["4185 J·K⁻¹·kg⁻¹", "1000 J·K⁻¹·kg⁻¹",
                 "444 J·K⁻¹·kg⁻¹", "2000 J·K⁻¹·kg⁻¹"],
     "ans": "4185 J·K⁻¹·kg⁻¹",
     "expl": "cp(eau liquide) ≈ 4185 J·K⁻¹·kg⁻¹ (l'une des plus élevées)."},

    {"q": "La capacité thermique est une grandeur qui mesure :",
     "options": ["la capacité du système à accumuler de l'énergie thermique",
                 "la capacité du système à produire du travail",
                 "la vitesse de réaction",
                 "la conductivité thermique"],
     "ans": "la capacité du système à accumuler de l'énergie thermique",
     "expl": "C = δQ/dT : énergie nécessaire pour élever la température de 1 K."},

    {"q": "Pour un solide ou un liquide, on peut écrire approximativement :",
     "options": ["Cp ≈ Cv", "Cp >> Cv", "Cp << Cv", "Cp = 0"],
     "ans": "Cp ≈ Cv",
     "expl": "Solides/liquides : dilatation très faible ⟹ Cp ≈ Cv."},
]


def generate(rng: random.Random, avoid=None):
    q = rng.choice(QUESTIONS)
    opts = q["options"][:]
    rng.shuffle(opts)
    return {
        "type": "T08_capacites",
        "enonce": q["q"], "options": opts,
        "reponse": q["ans"],
        "explanation": q.get("expl", ""),
        "params": {},
    }