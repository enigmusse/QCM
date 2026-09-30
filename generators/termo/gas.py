"""T04 — Gaz parfait, équation d'état."""
import random

QUESTIONS = [
    {"q": "Un gaz parfait est un gaz :",
     "options": ["à faible pression, sans interaction entre particules",
                 "à haute pression",
                 "dont les particules interagissent fortement",
                 "toujours monoatomique"],
     "ans": "à faible pression, sans interaction entre particules",
     "expl": "Hypothèses : particules ponctuelles, sans interaction, agitées de mouvement brownien."},

    {"q": "La loi de Boyle-Mariotte concerne une transformation :",
     "options": ["isotherme", "isobare", "isochore", "adiabatique"],
     "ans": "isotherme",
     "expl": "À T constante : PV = cste."},

    {"q": "La loi de Charles concerne une transformation :",
     "options": ["isobare", "isotherme", "isochore", "adiabatique"],
     "ans": "isobare",
     "expl": "À P constante : V/T = cste."},

    {"q": "La loi de Gay-Lussac concerne une transformation :",
     "options": ["isochore", "isotherme", "isobare", "adiabatique"],
     "ans": "isochore",
     "expl": "À V constant : P/T = cste."},

    {"q": "D'après l'équation d'état des gaz parfaits, à V fixé :",
     "options": ["P augmente avec T",
                 "P diminue quand T augmente",
                 "P ne varie pas avec T",
                 "P dépend du nombre de moles seulement"],
     "ans": "P augmente avec T",
     "expl": "PV = nRT ⟹ P = nRT/V : à V fixé, P ∝ T."},

    {"q": "D'après l'équation d'état des gaz parfaits, à T fixée :",
     "options": ["V diminue si P augmente",
                 "V augmente si P augmente",
                 "V ne dépend pas de P",
                 "V est constant"],
     "ans": "V diminue si P augmente",
     "expl": "PV = nRT ⟹ V = nRT/P : à T fixé, V ∝ 1/P."},

    {"q": "Un gaz parfait enfermé dans un volume constant, on augmente la température. La pression :",
     "options": ["augmente", "diminue", "ne change pas", "peut augmenter ou diminuer"],
     "ans": "augmente",
     "expl": "P = nRT/V, à V fixé : P ∝ T."},

    {"q": "Un gaz parfait est comprimé à température constante. Son volume :",
     "options": ["diminue", "augmente", "ne change pas", "dépend de la nature du gaz"],
     "ans": "diminue",
     "expl": "PV = cste (Boyle-Mariotte) : V ∝ 1/P."},

    {"q": "Loi d'Avogadro-Ampère : à T et P données, des volumes égaux de gaz parfaits contiennent :",
     "options": ["le même nombre de particules",
                 "la même masse",
                 "le même nombre de moles mais pas de particules",
                 "des nombres différents de particules"],
     "ans": "le même nombre de particules",
     "expl": "V égaux, P et T égales ⟹ N égal (loi d'Avogadro)."},

    {"q": "À 0 °C et 1 atm, le volume molaire d'un gaz parfait vaut :",
     "options": ["22,4 L", "24,0 L", "11,2 L", "1 L"],
     "ans": "22,4 L",
     "expl": "Conditions normales (CNTP) : Vm = 22,4 L·mol⁻¹."},
]


def generate(rng: random.Random, avoid=None):
    q = rng.choice(QUESTIONS)
    opts = q["options"][:]
    rng.shuffle(opts)
    return {
        "type": "T04_gaz_parfait",
        "enonce": q["q"], "options": opts,
        "reponse": q["ans"],
        "explanation": q.get("expl", ""),
        "params": {},
    }