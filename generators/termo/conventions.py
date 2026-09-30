"""T11 — Conventions de signe."""
import random

QUESTIONS = [
    {"q": "Un gaz qui se détend échange un travail W :",
     "options": ["W < 0 (le gaz fournit du travail)",
                 "W > 0 (le gaz reçoit du travail)",
                 "W = 0",
                 "W dépend du chemin uniquement"],
     "ans": "W < 0 (le gaz fournit du travail)",
     "expl": "Détente : le système fournit du travail à l'extérieur, W < 0 (convention récepteur)."},

    {"q": "Un gaz qui est comprimé échange un travail W :",
     "options": ["W > 0 (le gaz reçoit du travail)",
                 "W < 0 (le gaz fournit du travail)",
                 "W = 0",
                 "W < 0 car la pression augmente"],
     "ans": "W > 0 (le gaz reçoit du travail)",
     "expl": "Compression : le système reçoit du travail de l'extérieur, W > 0."},

    {"q": "Un système qui reçoit de la chaleur a :",
     "options": ["Q > 0", "Q < 0", "Q = 0", "Q indéterminé"],
     "ans": "Q > 0",
     "expl": "Convention : Q > 0 si la chaleur entre dans le système."},

    {"q": "Un système qui cède de la chaleur a :",
     "options": ["Q < 0", "Q > 0", "Q = 0", "Q indéterminé"],
     "ans": "Q < 0",
     "expl": "Convention : Q < 0 si la chaleur sort du système."},

    {"q": "Un système au repos (ΔE_c = 0) sans variation d'énergie potentielle extérieure vérifie :",
     "options": ["ΔU = W + Q", "ΔU = 0", "ΔU = W", "ΔU = Q"],
     "ans": "ΔU = W + Q",
     "expl": "Bilan énergétique : ΔE = ΔU = W + Q."},

    {"q": "Dans la convention « récepteur », un travail reçu par le système est :",
     "options": ["positif", "négatif", "nul", "égal à Q"],
     "ans": "positif",
     "expl": "Convention récepteur : ce que reçoit le système est positif."},

    {"q": "L'énergie interne U est :",
     "options": ["une quantité macroscopique indépendante du référentiel",
                 "une quantité dépendant du référentiel",
                 "observable directement",
                 "toujours nulle pour un gaz parfait"],
     "ans": "une quantité macroscopique indépendante du référentiel",
     "expl": "U est macroscopique, indépendante du référentiel, non observable directement."},

    {"q": "Un système isolé :",
     "options": ["n'échange ni matière ni énergie",
                 "échange seulement de l'énergie",
                 "échange seulement de la matière",
                 "échange matière et énergie"],
     "ans": "n'échange ni matière ni énergie",
     "expl": "Isolé = pas d'échange de matière ni d'énergie avec l'extérieur."},

    {"q": "Un système fermé :",
     "options": ["échange de l'énergie mais pas de matière",
                 "n'échange rien",
                 "échange de la matière mais pas d'énergie",
                 "échange matière et énergie"],
     "ans": "échange de l'énergie mais pas de matière",
     "expl": "Fermé = imperméable à la matière mais perméable à l'énergie."},
]


def generate(rng: random.Random, avoid=None):
    q = rng.choice(QUESTIONS)
    opts = q["options"][:]
    rng.shuffle(opts)
    return {
        "type": "T11_conventions",
        "enonce": q["q"], "options": opts,
        "reponse": q["ans"],
        "explanation": q.get("expl", ""),
        "params": {},
    }