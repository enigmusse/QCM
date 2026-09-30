import random
import sympy as sp


def generate(rng: random.Random, avoid=None):
    for _ in range(100):
        Ax, Ay = rng.randint(-4, 4), rng.randint(-4, 4)
        Bx, By = rng.randint(-4, 4), rng.randint(-4, 4)
        Cx, Cy = rng.randint(-4, 4), rng.randint(-4, 4)
        if (Ax, Ay) == (Bx, By) or (Ax, Ay) == (Cx, Cy):
            continue
        # AB = (Bx-Ax, By-Ay)
        abx, aby = Bx - Ax, By - Ay
        if abx == 0 and aby == 0:
            continue

        # CD colinéaire à AB : (Dx-Cx)*aby - (Dy-Cy)*abx = 0
        # AB orthogonale à DB : abx*(Dx-Bx) + aby*(Dy-By) = 0
        Dx, Dy = sp.symbols("Dx Dy")
        eq1 = sp.Eq((Dx - Cx) * aby - (Dy - Cy) * abx, 0)
        eq2 = sp.Eq(abx * (Dx - Bx) + aby * (Dy - By), 0)
        sol = sp.solve([eq1, eq2], [Dx, Dy])
        if not sol or not sol[Dx].is_rational or not sol[Dy].is_rational:
            continue
        break

    val = 3 * sol[Dx] - 4 * sol[Dy]
    correct = sp.sstr(sp.simplify(val))

    enonce = (
        f"Dans un repère orthonormé, A({Ax},{Ay}), B({Bx},{By}), C({Cx},{Cy}). "
        f"D(xD,yD) tel que AB et CD soient colinéaires, et AB et DB orthogonaux. "
        f"Que vaut 3x_D - 4y_D ?"
    )

    distractors = [sp.sstr(sp.simplify(val + 1)),
                   sp.sstr(sp.simplify(val - 1)),
                   "Autre chose"]
    options = [correct] + distractors
    rng.shuffle(options)

    return {
        "type": "T17_vecteurs",
        "enonce": enonce,
        "options": options,
        "reponse": correct,
        "params": {"A": [Ax, Ay], "B": [Bx, By], "C": [Cx, Cy]},
    }