"""T02 — Variables extensives / intensives."""
import random

QUESTIONS = [
    {"q": "Parmi les variables suivantes, lesquelles sont INTENSIVES ?",
     "options": ["La masse", "La température", "La masse volumique", "Le volume massique"],
     "ans": ["La température", "La masse volumique", "Le volume massique"],
     "expl": "Intensive = indépendante de la quantité de matière : T, ρ, v (volume massique). Extensives : masse, volume, n."},

    {"q": "Parmi les variables suivantes, lesquelles sont EXTENSIVES ?",
     "options": ["Le volume", "La masse", "La pression", "Le nombre de moles"],
     "ans": ["Le volume", "La masse", "Le nombre de moles"],
     "expl": "Extensive = proportionnelle à la quantité de matière : V, m, n. La pression est intensive."},

    {"q": "Si on réunit deux ballons identiques (même P, T, V, n) en un seul, la pression finale P_f est :",
     "options": ["P_f = P_i", "P_f = 2 P_i", "P_f = P_i / 2", "P_f = 4 P_i"],
     "ans": "P_f = P_i",
     "expl": "La pression est intensive : elle reste identique quand on double la quantité de matière."},

    {"q": "Si on réunit deux ballons identiques en un seul, la température finale T_f est :",
     "options": ["T_f = T_i", "T_f = 2 T_i", "T_f = T_i / 2", "T_f = 0"],
     "ans": "T_f = T_i",
     "expl": "La température est intensive : elle ne dépend pas de la quantité de matière."},

    {"q": "Si on réunit deux ballons identiques en un seul, le volume final V_f est :",
     "options": ["V_f = 2 V_i", "V_f = V_i", "V_f = V_i / 2", "V_f = 4 V_i"],
     "ans": "V_f = 2 V_i",
     "expl": "Le volume est extensif : il double avec la quantité de matière."},

    {"q": "Laquelle de ces grandeurs n'est PAS une variable d'état ?",
     "options": ["Le travail W", "La pression P", "La température T", "Le volume V"],
     "ans": "Le travail W",
     "expl": "W et Q ne sont pas des fonctions d'état : ils dépendent du chemin suivi."},

    {"q": "Laquelle de ces grandeurs est une fonction d'état ?",
     "options": ["L'énergie interne U", "Le travail W", "La chaleur Q", "Aucune"],
     "ans": "L'énergie interne U",
     "expl": "U est une fonction d'état : sa variation ne dépend que de l'état initial et final."},

    {"q": "La masse volumique d'un corps pur est une grandeur :",
     "options": ["intensive", "extensive", "ni l'une ni l'autre", "les deux"],
     "ans": "intensive",
     "expl": "La masse volumique ρ = m/V ne dépend pas de la quantité de matière."},

    {"q": "Le volume massique d'un corps pur est une grandeur :",
     "options": ["intensive", "extensive", "ni l'une ni l'autre", "les deux"],
     "ans": "intensive",
     "expl": "v = V/m = 1/ρ : c'est l'inverse de la masse volumique, donc intensive."},
]


def generate(rng: random.Random, avoid=None):
    q = rng.choice(QUESTIONS)
    opts = q["options"][:]
    rng.shuffle(opts)
    return {
        "type": "T02_variables",
        "enonce": q["q"], "options": opts,
        "reponse": q["ans"],
        "explanation": q.get("expl", ""),
        "params": {},
    }