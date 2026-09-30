"""T12 — Règle des phases, coefficients thermoélastiques."""
import random

QUESTIONS = [
    {"q": "La règle des phases de Gibbs s'écrit :",
     "options": ["v = c + 2 - φ", "v = c - 2 + φ", "v = c + φ", "v = c·φ"],
     "ans": "v = c + 2 - φ",
     "expl": "v = c + 2 - φ où c = nombre de constituants, φ = nombre de phases."},

    {"q": "Pour un gaz parfait (c = 1, φ = 1), la variance est :",
     "options": ["v = 2", "v = 1", "v = 0", "v = 3"],
     "ans": "v = 2",
     "expl": "v = 1 + 2 - 1 = 2 : système divariant (P et T varient librement)."},

    {"q": "Pour un corps pur sous deux phases en équilibre (c = 1, φ = 2), la variance est :",
     "options": ["v = 1", "v = 2", "v = 0", "v = 3"],
     "ans": "v = 1",
     "expl": "v = 1 + 2 - 2 = 1 : système univariant (fixer P fixe T et inversement)."},

    {"q": "Pour un corps pur au point triple (c = 1, φ = 3), la variance est :",
     "options": ["v = 0", "v = 1", "v = 2", "v = 3"],
     "ans": "v = 0",
     "expl": "v = 1 + 2 - 3 = 0 : point invariant, P et T sont fixés."},

    {"q": "Le coefficient de dilatation isobare α est défini par :",
     "options": ["α = (1/V)(∂V/∂T)_P", "α = (1/P)(∂P/∂T)_V",
                 "α = -(1/V)(∂V/∂P)_T", "α = (∂V/∂T)_P"],
     "ans": "α = (1/V)(∂V/∂T)_P",
     "expl": "α = (1/V)(∂V/∂T)_P : dilatation relative à P constante."},

    {"q": "Le coefficient de compressibilité isotherme χ_T est défini par :",
     "options": ["χ_T = -(1/V)(∂V/∂P)_T", "χ_T = (1/V)(∂V/∂P)_T",
                 "χ_T = (1/P)(∂P/∂V)_T", "χ_T = (1/V)(∂V/∂T)_P"],
     "ans": "χ_T = -(1/V)(∂V/∂P)_T",
     "expl": "χ_T = -(1/V)(∂V/∂P)_T > 0."},

    {"q": "Pour un gaz parfait, α vaut :",
     "options": ["1/T", "T", "1/P", "P"],
     "ans": "1/T",
     "expl": "PV = nRT ⟹ α = (1/V)(∂V/∂T)_P = 1/T."},

    {"q": "La relation entre α, β et χ_T pour un système est :",
     "options": ["α = β·χ_T·P", "α = β/(χ_T·P)", "α = β + χ_T", "α = χ_T/β"],
     "ans": "α = β·χ_T·P",
     "expl": "Relation entre les trois coefficients thermoélastiques."},

    {"q": "Le coefficient de dilatation isobare α est :",
     "options": ["positif pour presque tous les corps, sauf l'eau entre 0 et 4 °C",
                 "toujours positif",
                 "toujours négatif",
                 "toujours nul"],
     "ans": "positif pour presque tous les corps, sauf l'eau entre 0 et 4 °C",
     "expl": "Cas particulier : l'eau se contracte entre 0 et 4 °C (α < 0)."},

    {"q": "L'eau a une masse volumique maximale à :",
     "options": ["4 °C", "0 °C", "10 °C", "100 °C"],
     "ans": "4 °C",
     "expl": "ρ_max à 4 °C : la glace flotte car sa masse volumique est plus faible."},

    {"q": "L'équation de Van der Waals pour un gaz réel s'écrit :",
     "options": ["(P + a(n/V)²)(V - nb) = nRT", "PV = nRT",
                 "(P - a)(V + b) = nRT", "PV² = nRT"],
     "ans": "(P + a(n/V)²)(V - nb) = nRT",
     "expl": "Le terme a(n/V)² corrige les attractions, nb corrige le covolume (volume propre des molécules)."},

    {"q": "Le terme « nb » dans l'équation de Van der Waals représente :",
     "options": ["le covolume (volume propre des molécules)",
                 "les interactions attractives",
                 "la constante des gaz parfaits",
                 "la masse molaire"],
     "ans": "le covolume (volume propre des molécules)",
     "expl": "nb = covolume des molécules, exclu du volume accessible."},
]


def generate(rng: random.Random, avoid=None):
    q = rng.choice(QUESTIONS)
    opts = q["options"][:]
    rng.shuffle(opts)
    return {
        "type": "T12_gibbs",
        "enonce": q["q"], "options": opts,
        "reponse": q["ans"],
        "explanation": q.get("expl", ""),
        "params": {},
    }