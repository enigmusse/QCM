import random

AVOID = [
    (0, 1, -1, 3),
    (4, 1, 0, 2),
    (-2, 1, 2, 3),
    (3, -1, -1, 0),
    (3, 4, -1, 2),
    (2, -3, -4, -1),    
    (1, 2, 4, 1),         
]


def _on_circle(px, py, xA, yA, xB, yB):
    """Vérifie si (px,py) est sur le cercle de diamètre [AB], en arithmétique entière."""
    r2_int = (xA - xB) ** 2 + (yA - yB) ** 2
    lhs = (2 * px - xA - xB) ** 2 + (2 * py - yA - yB) ** 2
    return lhs == r2_int


def generate(rng: random.Random, avoid=None):
    avoid = avoid or AVOID
    for _ in range(200):
        xA = rng.randint(-4, 4)
        yA = rng.randint(-4, 4)
        xB = rng.randint(-4, 4)
        yB = rng.randint(-4, 4)
        if (xA, yA) == (xB, yB):
            continue
        if (xA, yA, xB, yB) in avoid or (xB, yB, xA, yA) in avoid:
            continue
        break

    # A et B sont TOUJOURS sur le cercle (ce sont les extrémités du diamètre)
    corrects = [[xA, yA], [xB, yB]]

    # Deux points qui ne sont PAS sur le cercle
    wrongs = []
    tries = 0
    while len(wrongs) < 2 and tries < 500:
        tries += 1
        px = rng.randint(-6, 6)
        py = rng.randint(-6, 6)
        if [px, py] in corrects or [px, py] in wrongs:
            continue
        if not _on_circle(px, py, xA, yA, xB, yB):
            wrongs.append([px, py])

    if len(wrongs) < 2:
        wrongs = [[xA + 1, yA], [xB, yB + 1]]

    candidats = corrects + wrongs
    rng.shuffle(candidats)

    enonce = (
        f"Dans un repère orthonormé, on considère A({xA},{yA}) et B({xB},{yB}). "
        f"Parmi les points suivants, lesquels appartiennent au cercle de diamètre [AB] ?"
    )

    return {
        "type": "T09_points_cercle",
        "enonce": enonce,
        "options": [f"({p[0]}, {p[1]})" for p in candidats],
        "reponse": [f"({p[0]}, {p[1]})" for p in corrects],
        "params": {"xA": xA, "yA": yA, "xB": xB, "yB": yB, "candidats": candidats},
    }