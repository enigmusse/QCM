#!/usr/bin/env python3
"""Application web du QCM — Streamlit."""
import random
import streamlit as st

from registry import (
    list_matieres, list_types, list_numeros,
    get_config, get_generators,
)
from generators.utils import postprocess_unique, smart_render

MULTI_TYPES = {"T05_inegalite", "T09_points_cercle", "T32_integrales_conv", "T33_series_conv"}
LETTRES = "ABCDEFGH"


def has_duplicate_options(q):
    opts = [str(o).strip() for o in q["options"]]
    return len(opts) != len(set(opts))


def generate_questions(generators, n, seed=None):
    """Génère n questions dans l'ordre des générateurs (cycle si besoin)."""
    rng = random.Random(seed)
    questions = []
    for i in range(n):
        g = generators[i % len(generators)]
        for _ in range(10):
            q = g.generate(rng)
            if not has_duplicate_options(q):
                questions.append(postprocess_unique(q, rng))
                break
        else:
            questions.append(postprocess_unique(q, rng))
    return questions


def correct_letters(q):
    rep = q["reponse"] if isinstance(q["reponse"], list) else [q["reponse"]]
    correct = set()
    for r in rep:
        for i, opt in enumerate(q["options"]):
            if str(opt).strip() == str(r).strip():
                correct.add(LETTRES[i])
    return sorted(correct)


def correct_answer_display(q):
    cl = correct_letters(q)
    parts = [f"{l} ({q['options'][LETTRES.index(l)]})" for l in cl]
    rep_str = ", ".join(parts)
    math_rep = q.get("reponse_math")
    if math_rep and math_rep != q["reponse"]:
        rep_str += f"  →  valeur exacte : **{math_rep}**"
    return rep_str


# ---------- Barre latérale ----------

with st.sidebar:
    st.header("📚 Choix du QCM")
    matiere = st.selectbox("Matière", list_matieres())
    type_qcm = st.selectbox("Type", list_types(matiere))
    numeros = list_numeros(matiere, type_qcm)
    numero = st.selectbox(
        "Numéro",
        numeros,
        format_func=lambda n: f"QCM {n} — {get_config(matiere, type_qcm, n)['label']}",
    )

    st.divider()
    st.subheader("⚙️ Paramètres")
    n_questions = st.slider("Nombre de questions", 1, 50, 10)
    mode = st.radio("Mode de correction", ["Immédiate", "À la fin"])

    random_mode = st.checkbox(
        "🎲 Mode aléatoire",
        value=False,
        help="Si coché : questions différentes à chaque génération. "
             "Si décoché : mêmes questions (reproductible).",
    )
    shuffle = st.checkbox(
        "🔀 Mélanger l'ordre",
        value=False,
        help="Par défaut, les questions suivent l'ordre du QCM original.",
    )

    if st.button("🔄 Nouveau QCM", use_container_width=True):
        st.session_state.clear()
        st.rerun()


# ---------- Initialisation de la session ----------

if "questions" not in st.session_state:
    seed = None if random_mode else 0
    generators = get_generators(matiere, type_qcm, numero)
    questions = generate_questions(generators, n_questions, seed)
    if shuffle:
        random.Random(seed).shuffle(questions)
    st.session_state.questions = questions
    st.session_state.answers = {}
    st.session_state.submitted = {}
    st.session_state.finished = False
qs = st.session_state.questions


# ---------- Affichage d'une question ----------

def render_question(q, idx):
    multi = q["type"] in MULTI_TYPES
    st.markdown(f"### Question {idx + 1} / {len(qs)}  ·  `{q['type']}`")
    st.markdown(smart_render(q["enonce"]))

    if multi:
        st.caption("Plusieurs réponses possibles.")

    options_labels = [f"{LETTRES[i]}. {smart_render(str(opt))}" for i, opt in enumerate(q["options"])]
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

    if mode == "Immédiate":
        if st.button("Valider", key=f"validate_{idx}"):
            st.session_state.submitted[idx] = True

        if st.session_state.submitted.get(idx):
            cl = correct_letters(q)
            if set(letters) == set(cl):
                st.success(f"✅ Correct ! Réponse : {correct_answer_display(q)}")
            else:
                st.error(
                    f"❌ Incorrect. Votre réponse : {', '.join(letters) or '—'}\n\n"
                    f"Bonne réponse : {correct_answer_display(q)}"
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

    st.subheader("Détail par type")
    by_type = {}
    for i, q, user, cl, ok in detail:
        t = q["type"]
        n, c = by_type.get(t, (0, 0))
        by_type[t] = (n + 1, c + int(ok))
    for t, (n, c) in sorted(by_type.items()):
        st.text(f"{t:22s} {c}/{n}")

    st.subheader("Correction détaillée")
    for i, q, user, cl, ok in detail:
        icon = "✅" if ok else "❌"
        with st.expander(f"{icon} Q{i+1} — {q['type']}"):
            st.markdown(smart_render(q["enonce"]))
            for j, opt in enumerate(q["options"]):
                lettre = LETTRES[j]
                marker = ""
                if lettre in cl:
                    marker = " ✅"
                if lettre in user:
                    marker += " (votre choix)"
                st.markdown(f"- **{lettre}.** {smart_render(str(opt))}{marker}")
            st.info(f"Bonne réponse : {correct_answer_display(q)}")

    if st.button("🔄 Recommencer", use_container_width=True):
        st.session_state.clear()
        st.rerun()


if st.session_state.finished:
    show_results()