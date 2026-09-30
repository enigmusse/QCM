"""T01 — Types de systèmes thermodynamiques."""
import random

QUESTIONS = [
    {"q": "La planète Terre est un système :",
     "options": ["isolé", "adiabatique", "ouvert", "fermé"],
     "ans": "fermé",
     "expl": "La Terre échange de l'énergie (rayonnement) mais très peu de matière avec l'espace : elle est fermée."},

    {"q": "L'Univers est un système :",
     "options": ["isolé", "adiabatique", "ouvert", "fermé"],
     "ans": "isolé",
     "expl": "Par définition, l'Univers n'échange rien avec l'extérieur : il est isolé."},

    {"q": "L'atmosphère terrestre est un système :",
     "options": ["isolé", "adiabatique", "ouvert", "fermé"],
     "ans": "ouvert",
     "expl": "L'atmosphère échange matière (évaporation, gaz) et énergie avec le reste : système ouvert."},

    {"q": "Un thermos fermé contenant du café est un système :",
     "options": ["isolé (approximativement)", "ouvert", "diatherme", "perméable"],
     "ans": "isolé (approximativement)",
     "expl": "Le thermos est rigide, adiabatique et imperméable : c'est une bonne approximation d'un système isolé."},

    {"q": "Une casserole d'eau bouillante sans couvercle est un système :",
     "options": ["ouvert", "fermé", "isolé", "adiabatique"],
     "ans": "ouvert",
     "expl": "Elle échange matière (vapeur d'eau) et énergie avec l'extérieur."},

    {"q": "Un ballon de baudruche gonflé à l'hélium est un système :",
     "options": ["fermé", "isolé", "ouvert", "adiabatique"],
     "ans": "fermé",
     "expl": "Le ballon est déformable, diatherme mais imperméable : système fermé."},

    {"q": "Une paroi est dite adiabatique si :",
     "options": ["elle bloque tout transfert de chaleur",
                 "elle laisse passer la chaleur",
                 "elle bloque tout transfert de matière",
                 "elle est rigide"],
     "ans": "elle bloque tout transfert de chaleur",
     "expl": "Adiabatique = pas d'échange thermique (Q = 0)."},

    {"q": "Une paroi est dite diatherme si :",
     "options": ["elle laisse passer la chaleur",
                 "elle bloque la chaleur",
                 "elle bloque la matière",
                 "elle est déformable"],
     "ans": "elle laisse passer la chaleur",
     "expl": "Diatherme = perméable aux échanges thermiques."},

    {"q": "Le concept d'Univers en thermodynamique désigne :",
     "options": ["système + milieu extérieur",
                 "le système uniquement",
                 "le milieu extérieur uniquement",
                 "l'ensemble des galaxies"],
     "ans": "système + milieu extérieur",
     "expl": "Univers = système thermodynamique + environnement."},
]


def generate(rng: random.Random, avoid=None):
    q = rng.choice(QUESTIONS)
    opts = q["options"][:]
    rng.shuffle(opts)
    return {
        "type": "T01_systemes",
        "enonce": q["q"], "options": opts,
        "reponse": q["ans"],
        "explanation": q.get("expl", ""),
        "params": {},
    }