#!/usr/bin/env python3
"""Application web du QCM — Streamlit."""
import random
import streamlit as st

from generators import (
    t01_polynome, t02_puissance, t03_fraction, t04_systeme, t05_inegalite,
    t06_droite, t07_mediatrice, t08_cercle, t09_points_cercle, t10_limite,
)

GENERATORS = [
    t01_polynome, t02_puissance, t03_fraction, t04_systeme, t05_inegalite,
    t06_droite, t07_mediatrice, t08_cercle, t09_points_cercle, t10_limite,
]

MULTI_TYPES = {"T05_inegalite", "T09_points_cercle"}
LETTRES = "ABCDEFGH"


# ---------- Utilitaires ----------

def has_duplicate_options(q):
    opts = [str(o).strip() for o in q["options"]]
    return len(opts) != len(set(opts))


def generate_questions(n, seed=None):
    from generators.utils import postprocess_unique
    rng = random.Random(seed)
    questions = []
    for _ in range(n):
        g = rng.choice(GENERATORS)
        for _ in range(10):
            q = g.generate(rng)
            if not has_duplicate_options(q):
                q = postprocess_unique(q, rng)
                questions.append(q)
                break
        else:
            questions.append(q)
    return questions


def correct_letters(q):
    """Retourne les lettres (A, B, ...) qui correspondent aux bonnes réponses."""
    rep = q["reponse"] if isinstance(q["reponse"], list) else [q["reponse"]]
    correct = set()
    for r in rep:
        for i, opt in enumerate(q["options"]):
            if str(opt).strip() == str(r).strip():
                correct.add(LETTRES[i])
    return sorted(correct)


# ---------- Configuration de la page ----------

st.set_page_config(
    page_title="QCM Mathématiques",
    page_icon="📐",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.title("📐 QCM de Mathématiques")
st.caption("Générateur aléatoire — 10 types de questions, difficulté progressive")


# ---------- Barre latérale ----------

with st.sidebar:
    st.header("⚙️ Paramètres")
    n_questions = st.slider("Nombre de questions", 1, 30, 10)
    mode = st.radio(
        "Mode de correction",
        ["Immédiate", "À la fin"],
        index=0,
    )
    seed_input = st.text_input("Seed (optionnel)", value="",
                              help="Laissez vide pour un tirage aléatoire")
    shuffle = st.checkbox("Mélanger l'ordre", value=True)

    if st.button("🔄 Nouveau QCM", use_container_width=True):
        st.session_state.clear()
        st.rerun()


# ---------- Initialisation de la session ----------

if "questions" not in st.session_state:
    seed = int(seed_input) if seed_input.strip().isdigit() else None
    questions = generate_questions(n_questions, seed)
    if shuffle:
        random.Random(seed).shuffle(questions)
    st.session_state.questions = questions
    st.session_state.answers = {}      # {idx: [lettres]}
    st.session_state.submitted = {}    # {idx: bool}
    st.session_state.finished = False

qs = st.session_state.questions


# ---------- Affichage d'une question ----------

def render_question(q, idx):
    multi = q["type"] in MULTI_TYPES
    st.markdown(f"### Question {idx + 1} / {len(qs)}  ·  `{q['type']}`")
    st.markdown(q["enonce"])

    if multi:
        st.caption("Plusieurs réponses possibles.")

    options_labels = [f"{LETTRES[i]}. {opt}" for i, opt in enumerate(q["options"])]
    previous = st.session_state.answers.get(idx, [])

    if multi:
        chosen = st.multiselect(
            "Votre réponse :",
            options=options_labels,
            default=[l for l in options_labels if l[0] in previous],
            key=f"multi_{idx}",
        )
        letters = [l[0] for l in chosen]
    else:
        default_idx = 0
        for i, l in enumerate(options_labels):
            if l[0] in previous:
                default_idx = i + 1
                break
        chosen = st.radio(
            "Votre réponse :",
            options=["—"] + options_labels,
            index=default_idx,
            key=f"single_{idx}",
        )
        letters = [chosen[0]] if chosen != "—" else []

    st.session_state.answers[idx] = letters

    # Correction immédiate
    if mode == "Immédiate":
        if st.button("Valider", key=f"validate_{idx}"):
            st.session_state.submitted[idx] = True

        if st.session_state.submitted.get(idx):
            cl = correct_letters(q)
            user_set = set(letters)
            correct_set = set(cl)
            if user_set == correct_set:
                st.success(f"✅ Correct ! Réponse : {', '.join(cl)}")
            else:
                rep_detail = ", ".join(
                    f"{l} ({q['options'][LETTRES.index(l)]})" for l in cl
                )
                st.error(
                    f"❌ Incorrect. Votre réponse : {', '.join(letters) or '—'}\n\n"
                    f"Bonne réponse : {rep_detail}"
                )
    st.divider()


# ---------- Affichage du QCM ----------

if not st.session_state.finished:
    for i, q in enumerate(qs):
        render_question(q, i)

    if mode == "À la fin":
        if st.button("📝 Valider le QCM", type="primary", use_container_width=True):
            st.session_state.finished = True
            st.rerun()


# ---------- Bilan final ----------

def show_results():
    score = 0
    detail = []
    for i, q in enumerate(qs):
        cl = correct_letters(q)
        user = st.session_state.answers.get(i, [])
        ok = set(user) == set(cl)
        score += int(ok)
        detail.append((i, q, user, cl, ok))

    total = len(qs)
    pct = round(100 * score / total)

    st.header("📊 Résultat")
    col1, col2 = st.columns(2)
    col1.metric("Score", f"{score} / {total}")
    col2.metric("Pourcentage", f"{pct} %")
    st.progress(score / total)

    # Détail par type
    st.subheader("Détail par type")
    by_type = {}
    for i, q, user, cl, ok in detail:
        t = q["type"]
        n, c = by_type.get(t, (0, 0))
        by_type[t] = (n + 1, c + int(ok))
    for t, (n, c) in sorted(by_type.items()):
        st.text(f"{t:22s} {c}/{n}")

    # Correction détaillée
    st.subheader("Correction détaillée")
    for i, q, user, cl, ok in detail:
        icon = "✅" if ok else "❌"
        with st.expander(f"{icon} Q{i+1} — {q['type']}"):
            st.markdown(q["enonce"])
            for j, opt in enumerate(q["options"]):
                lettre = LETTRES[j]
                marker = ""
                if lettre in cl:
                    marker = " ✅"
                if lettre in user:
                    marker += " (votre choix)"
                st.markdown(f"- **{lettre}.** {opt}{marker}")
            rep_detail = ", ".join(
                f"{l} ({q['options'][LETTRES.index(l)]})" for l in cl
            )
            st.info(f"Bonne réponse : {rep_detail}")

    if st.button("🔄 Recommencer", use_container_width=True):
        st.session_state.clear()
        st.rerun()


if st.session_state.finished:
    show_results()