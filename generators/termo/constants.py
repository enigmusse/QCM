"""T03 — Constantes R, kB, NA."""
import random

QUESTIONS = [
    {"q": "La constante des gaz parfaits R vaut :",
     "options": ["8,314 J·K⁻¹·mol⁻¹", "6,023 J·K⁻¹·mol⁻¹", "8,314 J·K⁻¹", "6,023 J·K⁻¹"],
     "ans": "8,314 J·K⁻¹·mol⁻¹",
     "expl": "R = 8,314 J·K⁻¹·mol⁻¹ (par mole)."},

    {"q": "La constante de Boltzmann kB vaut environ :",
     "options": ["1,38 × 10⁻²³ J·K⁻¹", "6,02 × 10⁻²³ J·K⁻¹",
                 "8,31 × 10⁻²³ J·K⁻¹", "1,60 × 10⁻¹⁹ J·K⁻¹"],
     "ans": "1,38 × 10⁻²³ J·K⁻¹",
     "expl": "kB = 1,38 × 10⁻²³ J·K⁻¹."},

    {"q": "Le nombre d'Avogadro N_A vaut environ :",
     "options": ["6,02 × 10²³ mol⁻¹", "1,38 × 10²³ mol⁻¹",
                 "8,31 × 10²³ mol⁻¹", "3,00 × 10⁸ mol⁻¹"],
     "ans": "6,02 × 10²³ mol⁻¹",
     "expl": "N_A = 6,02 × 10²³ mol⁻¹."},

    {"q": "Quelle relation lie R, kB et N_A ?",
     "options": ["R = N_A × kB", "R = N_A / kB", "R = kB / N_A", "R = N_A + kB"],
     "ans": "R = N_A × kB",
     "expl": "PV = nRT = NkB T et n = N/N_A ⟹ R = N_A · kB."},

    {"q": "L'équation d'état du gaz parfait s'écrit :",
     "options": ["PV = nRT", "PV = nRT²", "P/V = nRT", "P + V = nRT"],
     "ans": "PV = nRT",
     "expl": "PV = nRT = NkB T, valable pour un gaz parfait."},

    {"q": "Le nombre d'Avogadro N_A représente :",
     "options": ["le nombre de particules dans une mole",
                 "le nombre de molécules dans 1 L",
                 "le nombre de moles dans 1 kg",
                 "la constante des gaz parfaits"],
     "ans": "le nombre de particules dans une mole",
     "expl": "N_A = nombre de particules par mole : 6,02 × 10²³ mol⁻¹."},

    {"q": "Une pression de 1 atm équivaut à :",
     "options": ["1,013 × 10⁵ Pa", "1,000 × 10⁵ Pa", "1,013 × 10³ Pa", "760 Pa"],
     "ans": "1,013 × 10⁵ Pa",
     "expl": "1 atm = 1,01325 bar = 101 325 Pa = 760 Torr."},

    {"q": "La température 0 °C correspond à :",
     "options": ["273,15 K", "0 K", "100 K", "373,15 K"],
     "ans": "273,15 K",
     "expl": "T(K) = T(°C) + 273,15."},

    {"q": "La température 25 °C correspond environ à :",
     "options": ["298 K", "250 K", "273 K", "325 K"],
     "ans": "298 K",
     "expl": "25 + 273,15 = 298,15 K."},

    {"q": "Dans la loi de Dalton, la pression totale d'un mélange de gaz parfaits est :",
     "options": ["la somme des pressions partielles",
                 "le produit des pressions partielles",
                 "la moyenne des pressions partielles",
                 "égale à la plus grande pression partielle"],
     "ans": "la somme des pressions partielles",
     "expl": "P = Σ P_i où P_i = n_i RT/V est la pression partielle du gaz i."},
]


def generate(rng: random.Random, avoid=None):
    q = rng.choice(QUESTIONS)
    opts = q["options"][:]
    rng.shuffle(opts)
    return {
        "type": "T03_constantes",
        "enonce": q["q"], "options": opts,
        "reponse": q["ans"],
        "explanation": q.get("expl", ""),
        "params": {},
    }