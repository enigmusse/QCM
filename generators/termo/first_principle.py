"""T07 — 1er principe de la thermodynamique."""
import random

QUESTIONS = [
    {"q": "Le 1er principe de la thermodynamique s'écrit :",
     "options": ["dU = δW + δQ", "dU = δW - δQ", "dU = δQ - δW", "dU = δW × δQ"],
     "ans": "dU = δW + δQ",
     "expl": "1er principe : dU = δW + δQ (convention récepteur)."},

    {"q": "Une transformation isochore est caractérisée par :",
     "options": ["dU = δQ", "dU = δW", "dU = 0", "dU = -P dV"],
     "ans": "dU = δQ",
     "expl": "Isochore : dV = 0 ⟹ δW = -P dV = 0 ⟹ dU = δQ."},

    {"q": "Une transformation adiabatique est caractérisée par :",
     "options": ["dU = δW", "dU = δQ", "dU = 0", "dU = δW + δQ"],
     "ans": "dU = δW",
     "expl": "Adiabatique : δQ = 0 ⟹ dU = δW."},

    {"q": "Une transformation cyclique est caractérisée par :",
     "options": ["dU = 0", "dU = δQ", "dU = δW", "dU = δW + δQ"],
     "ans": "dU = 0",
     "expl": "Fonction d'état : ΔU = U_f - U_i = 0 si le système revient à son état initial."},

    {"q": "Le travail élémentaire des forces de pression s'écrit :",
     "options": ["δW = -P_ext dV", "δW = +P_ext dV", "δW = P_ext/V", "δW = -P_ext/V"],
     "ans": "δW = -P_ext dV",
     "expl": "δW = -P_ext dV (convention récepteur)."},

    {"q": "Pour une détente (V augmente), le travail échangé par le gaz est :",
     "options": ["négatif (W < 0)", "positif (W > 0)", "nul", "indéterminé"],
     "ans": "négatif (W < 0)",
     "expl": "Détente : V_f > V_i ⟹ W_if = -∫P dV < 0. Le gaz fournit du travail."},

    {"q": "Pour une compression (V diminue), le travail échangé par le gaz est :",
     "options": ["positif (W > 0)", "négatif (W < 0)", "nul", "indéterminé"],
     "ans": "positif (W > 0)",
     "expl": "Compression : V_f < V_i ⟹ W_if > 0. Le gaz reçoit du travail."},

    {"q": "Dans un diagramme de Clapeyron (P, V), W_if représente :",
     "options": ["l'opposé de l'aire sous la courbe",
                 "l'aire sous la courbe",
                 "la pente de la courbe",
                 "l'ordonnée à l'origine"],
     "ans": "l'opposé de l'aire sous la courbe",
     "expl": "W_if = -∫P_ext dV : c'est l'opposé de l'aire (orientée) sous la courbe."},

    {"q": "Le travail W échangé par un gaz lors d'une transformation isobare (P = P0) vaut :",
     "options": ["W = -P0 (V_f - V_i)", "W = -P0 V_f",
                 "W = P0 (V_f - V_i)", "W = 0"],
     "ans": "W = -P0 (V_f - V_i)",
     "expl": "P constant : W_if = -P0 (V_f - V_i)."},

    {"q": "Le travail et la chaleur sont :",
     "options": ["des grandeurs qui dépendent du chemin suivi",
                 "des fonctions d'état",
                 "toujours positifs",
                 "égaux"],
     "ans": "des grandeurs qui dépendent du chemin suivi",
     "expl": "W et Q ne sont pas des fonctions d'état : ils dépendent du chemin suivi."},

    {"q": "La variation d'énergie interne ΔU entre deux états :",
     "options": ["ne dépend que des états initial et final",
                 "dépend du chemin suivi",
                 "est toujours nulle",
                 "est toujours positive"],
     "ans": "ne dépend que des états initial et final",
     "expl": "U est une fonction d'état : ΔU ne dépend que de i et f."},

    {"q": "L'énergie interne U est :",
     "options": ["une fonction d'état extensive",
                 "une fonction d'état intensive",
                 "une grandeur qui dépend du chemin",
                 "toujours nulle"],
     "ans": "une fonction d'état extensive",
     "expl": "U est une fonction d'état et extensive (proportionnelle à la quantité de matière)."},

    {"q": "Un système isolé évolue avec :",
     "options": ["U constante", "U croissante", "U décroissante", "U indéterminée"],
     "ans": "U constante",
     "expl": "Système isolé : W = 0 et Q = 0 ⟹ ΔU = 0."},
]


def generate(rng: random.Random, avoid=None):
    q = rng.choice(QUESTIONS)
    opts = q["options"][:]
    rng.shuffle(opts)
    return {
        "type": "T07_1er_principe",
        "enonce": q["q"], "options": opts,
        "reponse": q["ans"],
        "explanation": q.get("expl", ""),
        "params": {},
    }