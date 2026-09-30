"""T13 — Bilans énergétiques par type de transformation."""
import random

QUESTIONS = [
    {"q": "Pour une transformation isotherme réversible d'un GP, le travail vaut :",
     "options": ["W = -nRT·ln(V_f/V_i)", "W = -P·ΔV",
                 "W = 0", "W = -nCv·ΔT"],
     "ans": "W = -nRT·ln(V_f/V_i)",
     "expl": "Isotherme réversible : W = -nRT ln(V_f/V_i)."},

    {"q": "Pour une transformation isotherme réversible d'un GP, la chaleur vaut :",
     "options": ["Q = nRT·ln(V_f/V_i)", "Q = 0",
                 "Q = nCv·ΔT", "Q = -W"],
     "ans": "Q = nRT·ln(V_f/V_i)",
     "expl": "ΔU = 0 ⟹ Q = -W = nRT ln(V_f/V_i)."},

    {"q": "Pour une transformation isotherme d'un gaz parfait :",
     "options": ["ΔU = 0 et ΔH = 0", "ΔU > 0", "Q = 0", "W = 0"],
     "ans": "ΔU = 0 et ΔH = 0",
     "expl": "Lois de Joule : U = f(T), H = f(T) ⟹ ΔT = 0 ⟹ ΔU = ΔH = 0."},

    {"q": "Pour une transformation isochore d'un GP, le travail vaut :",
     "options": ["W = 0", "W = -P·ΔV", "W = -nRT·ln(...)", "W = nCv·ΔT"],
     "ans": "W = 0",
     "expl": "Isochore : dV = 0 ⟹ δW = -P dV = 0."},

    {"q": "Pour une transformation isochore d'un GP, ΔU vaut :",
     "options": ["ΔU = Q = nCv·ΔT", "ΔU = 0", "ΔU = W", "ΔU = nCp·ΔT"],
     "ans": "ΔU = Q = nCv·ΔT",
     "expl": "Isochore : dU = δQ = Cv dT."},

    {"q": "Pour une transformation isobare d'un GP, le travail vaut :",
     "options": ["W = -P0·(V_f - V_i)", "W = 0",
                 "W = -nRT·ln(...)", "W = nR·ΔT"],
     "ans": "W = -P0·(V_f - V_i)",
     "expl": "Isobare : W = -∫P0 dV = -P0(V_f - V_i)."},

    {"q": "Pour une transformation isobare d'un GP, Q vaut :",
     "options": ["Q = nCp·ΔT", "Q = nCv·ΔT", "Q = 0", "Q = nR·ΔT"],
     "ans": "Q = nCp·ΔT",
     "expl": "Isobare : Q = ΔH = nCp·ΔT."},

    {"q": "Pour une transformation adiabatique d'un GP, Q vaut :",
     "options": ["Q = 0", "Q = nCp·ΔT", "Q = nCv·ΔT", "Q = W"],
     "ans": "Q = 0",
     "expl": "Adiabatique : pas d'échange de chaleur, Q = 0."},

    {"q": "Pour une transformation adiabatique d'un GP, ΔU vaut :",
     "options": ["ΔU = W = nCv·ΔT", "ΔU = 0", "ΔU = Q", "ΔU = nCp·ΔT"],
     "ans": "ΔU = W = nCv·ΔT",
     "expl": "1er principe : ΔU = W + Q = W (car Q = 0). Et dU = Cv dT."},

    {"q": "Pour une transformation adiabatique réversible d'un GP :",
     "options": ["PV^γ = cste", "PV = cste", "P/T = cste", "V/T = cste"],
     "ans": "PV^γ = cste",
     "expl": "Loi de Laplace : PV^γ = cste pour une adiabatique réversible."},

    {"q": "Lors d'une détente isotherme d'un GP, le gaz :",
     "options": ["reçoit de la chaleur et fournit du travail",
                 "fournit de la chaleur et reçoit du travail",
                 "n'échange rien",
                 "ne fournit ni ne reçoit de travail"],
     "ans": "reçoit de la chaleur et fournit du travail",
     "expl": "Détente : W < 0. Isotherme : ΔU = 0 ⟹ Q = -W > 0."},

    {"q": "Lors d'une compression adiabatique d'un GP, la température :",
     "options": ["augmente", "diminue", "reste constante", "dépend de la nature du gaz"],
     "ans": "augmente",
     "expl": "Compression adiabatique : W > 0 et Q = 0 ⟹ ΔU = W > 0 ⟹ ΔT > 0."},

    {"q": "Dans un cycle thermodynamique, ΔU et ΔH valent :",
     "options": ["0 et 0", "W et Q", "Q et W", "non définis"],
     "ans": "0 et 0",
     "expl": "Cycle : état initial = état final ⟹ ΔU = ΔH = 0 (fonctions d'état)."},

    {"q": "Pour un cycle, le travail total W_cycle est égal à :",
     "options": ["-Q_cycle", "Q_cycle", "0", "ΔU"],
     "ans": "-Q_cycle",
     "expl": "Cycle : ΔU = 0 ⟹ W + Q = 0 ⟹ W = -Q."},
]


def generate(rng: random.Random, avoid=None):
    q = rng.choice(QUESTIONS)
    opts = q["options"][:]
    rng.shuffle(opts)
    return {
        "type": "T13_bilan_energ",
        "enonce": q["q"], "options": opts,
        "reponse": q["ans"],
        "explanation": q.get("expl", ""),
        "params": {},
    }