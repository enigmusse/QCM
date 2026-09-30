"""T09 — Enthalpie H."""
import random

QUESTIONS = [
    {"q": "L'enthalpie H est définie par :",
     "options": ["H = U + PV", "H = U - PV", "H = U/PV", "H = U·PV"],
     "ans": "H = U + PV",
     "expl": "H = U + PV est la définition de l'enthalpie."},

    {"q": "Pour une transformation isobare (P = cste), dH = ",
     "options": ["δQ", "δW", "0", "dU"],
     "ans": "δQ",
     "expl": "dH = dU + PdV + VdP, à P constant : dH = δQ."},

    {"q": "Pour une transformation isobare d'un gaz parfait, la chaleur échangée vaut :",
     "options": ["Q = nCp·ΔT", "Q = nCv·ΔT", "Q = 0", "Q = nR·ΔT"],
     "ans": "Q = nCp·ΔT",
     "expl": "Isobare + loi de Joule : Q = ΔH = nCp·ΔT."},

    {"q": "Pour une transformation isochore d'un gaz parfait, la chaleur échangée vaut :",
     "options": ["Q = nCv·ΔT", "Q = nCp·ΔT", "Q = 0", "Q = nR·ΔT"],
     "ans": "Q = nCv·ΔT",
     "expl": "Isochore + 1er principe : Q = ΔU = nCv·ΔT."},

    {"q": "L'enthalpie H est :",
     "options": ["une fonction d'état extensive",
                 "une fonction d'état intensive",
                 "une grandeur qui dépend du chemin",
                 "toujours nulle"],
     "ans": "une fonction d'état extensive",
     "expl": "H = U + PV est une fonction d'état (combinaison de fonctions d'état)."},

    {"q": "Pour une transformation isotherme d'un gaz parfait, ΔH vaut :",
     "options": ["0", "nCp·ΔT", "W", "Q"],
     "ans": "0",
     "expl": "Loi de Joule : H = f(T), donc si ΔT = 0, ΔH = 0."},

    {"q": "Pour une transformation adiabatique d'un gaz parfait, ΔH vaut :",
     "options": ["nCp·ΔT", "0", "nCv·ΔT", "Q"],
     "ans": "nCp·ΔT",
     "expl": "Loi de Joule : dH = Cp·dT, valable pour toute transformation d'un GP."},

    {"q": "Pour un gaz parfait, dH s'écrit :",
     "options": ["dH = Cp·dT", "dH = Cv·dT", "dH = 0", "dH = R·dT"],
     "ans": "dH = Cp·dT",
     "expl": "2e loi de Joule : H = f(T) ⟹ dH = Cp·dT."},

    {"q": "Pour un gaz parfait, dU s'écrit :",
     "options": ["dU = Cv·dT", "dU = Cp·dT", "dU = 0", "dU = R·dT"],
     "ans": "dU = Cv·dT",
     "expl": "1ère loi de Joule : U = f(T) ⟹ dU = Cv·dT."},

    {"q": "Si un système reçoit de la chaleur (Q > 0), son enthalpie :",
     "options": ["augmente à P constante",
                 "diminue à P constante",
                 "ne varie pas",
                 "dépend de la nature du gaz"],
     "ans": "augmente à P constante",
     "expl": "Isobare : ΔH = Q, donc si Q > 0 alors ΔH > 0."},
]


def generate(rng: random.Random, avoid=None):
    q = rng.choice(QUESTIONS)
    opts = q["options"][:]
    rng.shuffle(opts)
    return {
        "type": "T09_enthalpie",
        "enonce": q["q"], "options": opts,
        "reponse": q["ans"],
        "explanation": q.get("expl", ""),
        "params": {},
    }