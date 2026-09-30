"""T05 — Types de transformations."""
import random

QUESTIONS = [
    {"q": "Une transformation isotherme vérifie :",
     "options": ["T = constante", "P = constante", "V = constante", "Q = 0"],
     "ans": "T = constante",
     "expl": "Isotherme : T reste constante."},

    {"q": "Une transformation isobare vérifie :",
     "options": ["P = constante", "T = constante", "V = constante", "Q = 0"],
     "ans": "P = constante",
     "expl": "Isobare : P reste constante."},

    {"q": "Une transformation isochore vérifie :",
     "options": ["V = constante", "T = constante", "P = constante", "W = 0 uniquement pour un GP"],
     "ans": "V = constante",
     "expl": "Isochore : V reste constant. Comme dV = 0, W = 0."},

    {"q": "Une transformation adiabatique vérifie :",
     "options": ["Q = 0", "W = 0", "T = 0", "ΔU = 0"],
     "ans": "Q = 0",
     "expl": "Adiabatique : pas d'échange de chaleur."},

    {"q": "Une transformation réversible est :",
     "options": ["une succession d'états d'équilibre infiniment voisins",
                 "une transformation brutale",
                 "toujours adiabatique",
                 "toujours isotherme"],
     "ans": "une succession d'états d'équilibre infiniment voisins",
     "expl": "Réversible = quasi-statique et sans dissipation : on peut revenir en arrière."},

    {"q": "Une transformation cyclique :",
     "options": ["retourne à l'état initial", "est toujours réversible",
                 "est toujours isotherme", "a un ΔU ≠ 0"],
     "ans": "retourne à l'état initial",
     "expl": "Un cycle : état initial = état final, donc ΔU = 0 et ΔH = 0."},

    {"q": "Pour une transformation cyclique, la variation d'énergie interne vaut :",
     "options": ["ΔU = 0", "ΔU = W", "ΔU = Q", "ΔU > 0"],
     "ans": "ΔU = 0",
     "expl": "Fonction d'état : ΔU = U_f - U_i = 0 si i = f."},

    {"q": "Pour une transformation isochore, le travail échangé vaut :",
     "options": ["W = 0", "W = -P·ΔV", "W = P·ΔV", "W = Q"],
     "ans": "W = 0",
     "expl": "dV = 0 ⟹ W = -∫P dV = 0."},

    {"q": "Pour une transformation adiabatique, dU = ",
     "options": ["δW", "δQ", "0", "δW + δQ"],
     "ans": "δW",
     "expl": "1er principe : dU = δW + δQ, avec δQ = 0 ⟹ dU = δW."},

    {"q": "Pour une transformation isochore, dU = ",
     "options": ["δQ", "δW", "0", "δW + δQ"],
     "ans": "δQ",
     "expl": "dV = 0 ⟹ δW = 0 ⟹ dU = δQ."},

    {"q": "Une transformation quasi-statique :",
     "options": ["est toujours lente et proche de l'équilibre",
                 "est toujours brutale",
                 "est toujours irréversible",
                 "est toujours isotherme"],
     "ans": "est toujours lente et proche de l'équilibre",
     "expl": "Quasi-statique = modification progressive, système toujours proche de l'équilibre."},

    {"q": "En plongée, les bulles d'air qui remontent lentement subissent approximativement une transformation :",
     "options": ["isotherme", "isochore", "adiabatique", "aucune"],
     "ans": "isotherme",
     "expl": "La température de l'eau est quasi constante à faible profondeur : T ≈ cste."},

    {"q": "Le gonflage rapide d'un pneu à vélo est approximativement :",
     "options": ["adiabatique", "isotherme", "isochore", "cyclique"],
     "ans": "adiabatique",
     "expl": "Trop rapide pour évacuer la chaleur ⟹ Q ≈ 0."},

    {"q": "La détente de Joule-Gay-Lussac est :",
     "options": ["adiabatique irréversible", "isotherme réversible",
                 "isochore", "isobare"],
     "ans": "adiabatique irréversible",
     "expl": "Détente dans le vide : Q = 0, W = 0, mais P change brutalement."},
]


def generate(rng: random.Random, avoid=None):
    q = rng.choice(QUESTIONS)
    opts = q["options"][:]
    rng.shuffle(opts)
    return {
        "type": "T05_transform",
        "enonce": q["q"], "options": opts,
        "reponse": q["ans"],
        "explanation": q.get("expl", ""),
        "params": {},
    }