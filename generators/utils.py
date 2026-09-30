"""Utilitaires partagés par tous les générateurs."""
import re


def fmt_signed(value, var="x"):
    """Formate '+ ax' ou '- ax' proprement, gère 0, 1, -1."""
    if value == 0:
        return ""
    if value == 1:
        return f"+ {var}"
    if value == -1:
        return f"- {var}"
    if value > 0:
        return f"+ {value}{var}"
    return f"- {abs(value)}{var}"


def fmt_line(m, p):
    """Formate 'y = mx + p' proprement."""
    parts = ["y ="]

    if m == 1:
        parts.append("x")
    elif m == -1:
        parts.append("-x")
    elif m != 0:
        parts.append(f"{m}x")

    if p != 0:
        if len(parts) == 1:                # pas de terme en x
            parts.append(str(p))
        else:
            parts.append(f"+ {p}" if p > 0 else f"- {abs(p)}")

    return " ".join(parts)


def fmt_poly(coeffs):
    """coeffs = [a,b,c,d] pour aX^3 + bX^2 + cX + d."""
    a, b, c, d = coeffs
    terms = []

    if a != 0:
        if a == 1:
            terms.append("X^3")
        elif a == -1:
            terms.append("-X^3")
        else:
            terms.append(f"{a}X^3")

    if b != 0:
        if b == 1:
            terms.append("+ X^2")
        elif b == -1:
            terms.append("- X^2")
        else:
            terms.append(f"+ {b}X^2" if b > 0 else f"- {abs(b)}X^2")

    if c != 0:
        if c == 1:
            terms.append("+ X")
        elif c == -1:
            terms.append("- X")
        else:
            terms.append(f"+ {c}X" if c > 0 else f"- {abs(c)}X")

    if d != 0:
        terms.append(f"+ {d}" if d > 0 else f"- {abs(d)}")

    return " ".join(terms)


def fmt_expr(expr):
    """Convertit une expression sympy en texte lisible.
    - '**' → '^'
    - '3*x' → '3x'
    - '4*y' → '4y'
    """
    s = str(expr)
    s = s.replace("**", "^")
    s = re.sub(r"(\d)\*([a-zA-Z])", r"\1\2", s)
    s = re.sub(r"([a-zA-Z])\*([a-zA-Z])", r"\1\2", s)
    return s