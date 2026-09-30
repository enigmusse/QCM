import random
import sympy as sp
from generators.utils import fmt_term


def _lin(a, var):
    if a == 0:
        return ""
    if a == 1:
        return var
    if a == -1:
        return f"-{var}"
    return f"{a}{var}"


def generate(rng: random.Random, avoid=None):
    sous_type = rng.choice(["droites", "parabole"])

    if sous_type == "droites":
        for _ in range(50):
            Ax, Ay = rng.randint(-4, 4), rng.randint(-4, 4)
            Bx, By = rng.randint(-4, 4), rng.randint(-4, 4)
            Cx, Cy = rng.randint(-4, 4), rng.randint(-4, 4)
            Dx, Dy = rng.randint(-4, 4), rng.randint(-4, 4)
            det = (Bx - Ax) * (Dy - Cy) - (By - Ay) * (Dx - Cx)
            if det == 0:
                continue
            x, y = sp.symbols("x y")
            eq1 = sp.Eq((x - Ax) * (By - Ay) - (y - Ay) * (Bx - Ax), 0)
            eq2 = sp.Eq((x - Cx) * (Dy - Cy) - (y - Cy) * (Dx - Cx), 0)
            sol = sp.solve([eq1, eq2], [x, y])
            if not sol or not sol[x].is_rational:
                continue
            val = 3 * sol[x] - 4 * sol[y]
            correct = sp.sstr(sp.simplify(val))
            enonce = (
                f"Dans un repère orthonormé, A({Ax},{Ay}), B({Bx},{By}), "
                f"C({Cx},{Cy}), D({Dx},{Dy}). I est l'intersection de (AB) et (CD). "
                f"Que vaut 3x_I - 4y_I ?"
            )
            break
    else:
        Ax, Ay = rng.randint(-3, 3), rng.randint(-3, 3)
        Bx, By = rng.randint(-3, 3), rng.randint(-3, 3)
        p = rng.randint(-3, 3)
        q = rng.randint(-3, 3)
        x = sp.Symbol("x")
        if Bx == Ax:
            return generate(rng, avoid)
        m = sp.Rational(By - Ay, Bx - Ax)
        c = Ay - m * Ax
        eq = sp.Eq(m * x + c, x**2 + p * x + q)
        sols = sp.solve(eq, x)
        if len(sols) != 2:
            return generate(rng, avoid)
        x0, x1 = sols
        y0, y1 = m * x0 + c, m * x1 + c
        val = sp.simplify(3 * (x0 + x1) - 4 * (y0 + y1))
        correct = sp.sstr(val)

        # Formate proprement y = x² + px + q
        poly_str = "x²"
        if p != 0:
            poly_str += " " + fmt_term(p, "x", first=False)
        if q != 0:
            poly_str += " " + fmt_term(q, "", first=False)

        enonce = (
            f"Dans un repère orthonormé, A({Ax},{Ay}), B({Bx},{By}). "
            f"I et J sont les intersections de (AB) avec y = {poly_str}. "
            f"Que vaut 3(x_I + x_J) - 4(y_I + y_J) ?"
        )

    distractors = [sp.sstr(sp.sympify(correct) + 1),
                   sp.sstr(sp.sympify(correct) - 1),
                   "Autre chose"]
    options = [correct] + distractors
    rng.shuffle(options)

    return {
        "type": "T20_intersection",
        "enonce": enonce,
        "options": options,
        "reponse": correct,
        "params": {},
    }