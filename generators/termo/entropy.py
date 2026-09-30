"""T10 — Entropie et 2e principe."""
import random

QUESTIONS = [
    {"q": "L'entropie S est une grandeur :",
     "options": ["extensive", "intensive", "sans unité", "toujours nulle"],
     "ans": "extensive",
     "expl": "S est extensive (proportionnelle à la quantité de matière)."},

    {"q": "L'unité de l'entropie est :",
     "options": ["J·K⁻¹", "J·K", "J/K²", "J"],
     "ans": "J·K⁻¹",
     "expl": "ΔS s'exprime en J·K⁻¹."},

    {"q": "L'entropie échangée S^e s'écrit :",
     "options": ["S^e = ∫ δQ/T", "S^e = ∫ T δQ", "S^e = Q·T", "S^e = δQ·dT"],
     "ans": "S^e = ∫ δQ/T",
     "expl": "S^e = ∫ δQ/T, avec T la température de la frontière."},

    {"q": "Pour une transformation adiabatique, l'entropie échangée vaut :",
     "options": ["S^e = 0", "S^e > 0", "S^e < 0", "S^e = ΔS"],
     "ans": "S^e = 0",
     "expl": "Adiabatique : δQ = 0 ⟹ S^e = 0."},

    {"q": "Pour une transformation réversible, l'entropie produite vaut :",
     "options": ["S^p = 0", "S^p > 0", "S^p < 0", "S^p = ΔS"],
     "ans": "S^p = 0",
     "expl": "Réversible ⟹ Sp = 0 (cas limite)."},

    {"q": "Pour une transformation irréversible, l'entropie produite est :",
     "options": ["S^p > 0", "S^p = 0", "S^p < 0", "S^p = ΔS"],
     "ans": "S^p > 0",
     "expl": "2e principe : Sp ≥ 0, et > 0 si irréversible."},

    {"q": "Le 2e principe pour un système isolé s'écrit :",
     "options": ["ΔS ≥ 0", "ΔS = 0", "ΔS ≤ 0", "ΔS = cste"],
     "ans": "ΔS ≥ 0",
     "expl": "Pour un système isolé, l'entropie ne peut qu'augmenter (ou rester constante si réversible)."},

    {"q": "La relation de Boltzmann donne :",
     "options": ["S = kB ln(Ω)", "S = kB Ω", "S = -kB ln(Ω)", "S = Ω/kB"],
     "ans": "S = kB ln(Ω)",
     "expl": "S = kB ln(Ω), avec Ω le nombre de micro-états."},

    {"q": "Le 3e principe de la thermodynamique (Nernst) énonce :",
     "options": ["S = 0 pour un cristal parfait à T = 0 K",
                 "S = 0 pour tout corps à T = 0 K",
                 "S = ∞ à T = 0 K",
                 "S augmente avec T à volume constant"],
     "ans": "S = 0 pour un cristal parfait à T = 0 K",
     "expl": "3e principe : S(0 K) = 0 pour un cristal parfait."},

    {"q": "L'identité fondamentale de la thermodynamique s'écrit :",
     "options": ["dU = TdS - PdV", "dU = TdS + PdV",
                 "dU = SdT - VdP", "dU = -TdS + PdV"],
     "ans": "dU = TdS - PdV",
     "expl": "dU = TdS - PdV pour un système fermé de composition fixe."},

    {"q": "Pour une transformation adiabatique réversible :",
     "options": ["ΔS = 0", "ΔS > 0", "ΔS < 0", "ΔS = Se"],
     "ans": "ΔS = 0",
     "expl": "Adiabatique : Se = 0. Réversible : Sp = 0. Donc ΔS = 0."},

    {"q": "Pour une transformation adiabatique irréversible :",
     "options": ["ΔS > 0", "ΔS = 0", "ΔS < 0", "ΔS = 0 et Sp = 0"],
     "ans": "ΔS > 0",
     "expl": "Adiabatique : Se = 0. Irréversible : Sp > 0. Donc ΔS = Sp > 0."},

    {"q": "L'entropie de l'Univers lors d'une transformation réelle :",
     "options": ["augmente", "diminue", "reste constante", "peut diminuer"],
     "ans": "augmente",
     "expl": "ΔS_Univers = ΔS_système + ΔS_extérieur ≥ 0 (2e principe)."},

    {"q": "Un processus est impossible si :",
     "options": ["ΔS_Univers < 0", "ΔS_Univers > 0",
                 "ΔS_Univers = 0", "ΔS_système > 0"],
     "ans": "ΔS_Univers < 0",
     "expl": "Le 2e principe interdit toute transformation qui diminuerait l'entropie de l'Univers."},

    {"q": "L'entropie d'un corps pur lors d'un changement d'état (fusion, vaporisation) :",
     "options": ["augmente", "diminue", "reste constante", "est nulle"],
     "ans": "augmente",
     "expl": "S_gaz > S_liquide > S_solide : le désordre augmente."},

    {"q": "L'entropie augmente de façon discontinue à chaque :",
     "options": ["changement d'état physique",
                 "changement de pression",
                 "compression isotherme",
                 "détente adiabatique"],
     "ans": "changement d'état physique",
     "expl": "À chaque changement d'état (fusion, vaporisation), ΔS subit un saut."},

    {"q": "La flèche du temps en thermodynamique est portée par :",
     "options": ["l'augmentation de l'entropie",
                 "la conservation de l'énergie",
                 "la conservation de la masse",
                 "l'équilibre thermique"],
     "ans": "l'augmentation de l'entropie",
     "expl": "Le 2e principe définit un sens d'évolution : l'entropie croît."},
]


def generate(rng: random.Random, avoid=None):
    q = rng.choice(QUESTIONS)
    opts = q["options"][:]
    rng.shuffle(opts)
    return {
        "type": "T10_entropie",
        "enonce": q["q"], "options": opts,
        "reponse": q["ans"],
        "explanation": q.get("expl", ""),
        "params": {},
    }