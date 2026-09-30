"""Registre des QCM disponibles : matière → type → numéro."""

# --- Types communs (QCM 0 et 1) — dans generators/common/ ---
from generators.common import (
    polynome,
    puissance,
    fraction,
    systeme,
    inegalite,
    droite,
    mediatrice,
    cercle,
    points_cercle,
    limite,
)

# --- Types spécifiques QCM 0 — dans generators/qcm_0/ ---
from generators.qcm_0 import (
    radicaux,
    log,
    expo,
    eq_expo,
    fractions_imbriquees,
    poly_developpe,
    equation,
    domaine,
    derivee,
    integrale,
    vecteurs,
    eq_diff,
    intersection,
    continuite,
    suites,
    integrales_conv,
    series_conv,
    serie_valeur,
)

# --- Types Thermo (QCM Sophie) ---
from generators.termo import (
    systems, variables, constants, gas, transformations,
    laplace, first_principle, heat_capacity, enthalpy, entropy,
    conventions, gibbs, energetic_balance,
)

TERMO_GENERATORS = [
    systems, variables, constants, gas, transformations,
    laplace, first_principle, heat_capacity, enthalpy, entropy,
    conventions, gibbs, energetic_balance,
]

# --- Liste des générateurs communs ---
COMMON_GENERATORS = [
    polynome,
    puissance,
    fraction,
    systeme,
    inegalite,
    droite,
    mediatrice,
    cercle,
    points_cercle,
    limite,
]

# --- Liste des générateurs spécifiques QCM 0 ---
QCM_0_SPECIFIC = [
    radicaux,
    log,
    expo,
    eq_expo,
    fractions_imbriquees,
    poly_developpe,
    equation,
    domaine,
    derivee,
    integrale,
    vecteurs,
    eq_diff,
    intersection,
    continuite,
    suites,
    integrales_conv,
    series_conv,
    serie_valeur,
]

REGISTRY = {
    "maths": {
        "rannou": {
            1: {
                "label": "QCM 1 (Rannou)",
                "data_file": "data/qcm_1.json",
                "generators": COMMON_GENERATORS,
                "n_default": 10,
            },
            0: {
                "label": "QCM 0 (Rannou)",
                "data_file": "data/qcm_0.json",
                "generators": COMMON_GENERATORS + QCM_0_SPECIFIC,
                "n_default": 34,
            },
        },
    },
    "termo": {
        "sophie": {
            1: {
                "label": "QCM 1 (Sophie Carles)",
                "data_file": "data/termo_qcm1.json",
                "generators": TERMO_GENERATORS,
                "n_default": 20,
            },
        },
    },
}


def list_matieres():
    return sorted(REGISTRY.keys())


def list_types(matiere):
    return sorted(REGISTRY[matiere].keys())


def list_numeros(matiere, type_qcm):
    return sorted(REGISTRY[matiere][type_qcm].keys())


def get_config(matiere, type_qcm, numero):
    return REGISTRY[matiere][type_qcm][numero]


def get_generators(matiere, type_qcm, numero):
    return get_config(matiere, type_qcm, numero)["generators"]


def get_data_file(matiere, type_qcm, numero):
    return get_config(matiere, type_qcm, numero)["data_file"]


if __name__ == "__main__":
    for mat, types in REGISTRY.items():
        for t, nums in types.items():
            for n, cfg in nums.items():
                print(f"{mat}/{t}/QCM {n} : {len(cfg['generators'])} générateurs")