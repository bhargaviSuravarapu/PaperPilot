
from time import perf_counter
import sys
from pathlib import Path

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from generator import (
    BacktrackingStrategy,
    BranchBoundStrategy,
    DPStrategy,
    ExamPaperGenerator,
    GreedyStrategy,
)
from models import PaperSpecification
from question_bank import QuestionBank
from validator import PaperValidator


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="PaperPilot",
    page_icon="📄",
    layout="wide",
)

# --------------------------------------------------
# CUSTOM PURPLE THEME
# --------------------------------------------------

st.markdown(
    """
    <style>
    .stApp {
        background-color: #F7F3FF;
        color: #29213D;
    }

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    [data-testid="stSidebar"] {
        background-color: #24113F;
    }

    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #FFFFFF !important;
    }

    [data-testid="stSidebar"] input {
        background-color: #FFFFFF !important;
        color: #24113F !important;
        -webkit-text-fill-color: #24113F !important;
    }

    [data-testid="stSidebar"] [data-baseweb="select"] {
        background-color: #FFFFFF;
    }

    [data-testid="stSidebar"] [data-baseweb="select"] * {
        color: #24113F !important;
    }

    [data-testid="stSidebar"] [data-testid="stNumberInput"] button {
        background-color: #E9DDFC !important;
        color: #54278F !important;
        border: 1px solid #D8C7F5 !important;
    }

    [data-testid="stSidebar"] [data-testid="stNumberInput"] button svg {
        color: #54278F !important;
        fill: #54278F !important;
        stroke: #54278F !important;
    }

    [data-testid="stSidebar"] [data-testid="stNumberInput"] button:hover {
        background-color: #D8C2FA !important;
    }

    h1 {
        color: #54278F;
        font-weight: 800;
    }

    h2, h3 {
        color: #6D3DB8;
    }

    .stMarkdown p,
    .stMarkdown li {
        color: #29213D;
    }

    [data-testid="stMetric"] {
        background-color: #FFFFFF;
        border: 1px solid #E3D5FA;
        padding: 18px;
        border-radius: 14px;
        box-shadow: 0 4px 14px rgba(84, 39, 143, 0.07);
    }

    [data-testid="stMetricValue"],
    [data-testid="stMetricLabel"] {
        color: #54278F !important;
    }

    .stButton > button,
    .stDownloadButton > button {
        background-color: #7C3AED;
        color: #FFFFFF !important;
        border: none;
        border-radius: 10px;
        padding: 0.65rem 1rem;
        font-weight: 600;
    }

    .stButton > button:hover,
    .stDownloadButton > button:hover {
        background-color: #5B21B6;
        color: #FFFFFF !important;
        border: none;
    }

    [data-testid="stAlert"] {
        border-radius: 12px;
    }

    hr {
        border-color: #E3D5FA;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# LOAD QUESTION BANK
# --------------------------------------------------

data_path = PROJECT_ROOT / "data" / "questions.json"

try:
    bank = QuestionBank(str(data_path))
    questions = bank.get_all()
except Exception as exc:
    st.error(f"Could not load the question bank: {exc}")
    st.stop()

# Count the available questions in each difficulty.
available_counts = {
    "easy": sum(
        q.difficulty.lower() == "easy" for q in questions
    ),
    "medium": sum(
        q.difficulty.lower() == "medium" for q in questions
    ),
    "hard": sum(
        q.difficulty.lower() == "hard" for q in questions
    ),
}

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.caption("INTELLIGENT ASSESSMENT PLATFORM")
st.title("✈️ PaperPilot")
st.subheader(
    "Intelligent Question Paper Generation System"
)
st.write(
    "Configure difficulty levels, choose an algorithm, "
    "and generate a validated question paper."
)
st.divider()

# --------------------------------------------------
# SIDEBAR SETTINGS
# --------------------------------------------------

st.sidebar.header("⚙️ Paper Settings")

st.sidebar.caption(
    "Choose how many questions to include."
)

easy_count = st.sidebar.number_input(
    "Easy Questions",
    min_value=0,
    max_value=available_counts["easy"],
    value=min(3, available_counts["easy"]),
    step=1,
)

medium_count = st.sidebar.number_input(
    "Medium Questions",
    min_value=0,
    max_value=available_counts["medium"],
    value=min(4, available_counts["medium"]),
    step=1,
)

hard_count = st.sidebar.number_input(
    "Hard Questions",
    min_value=0,
    max_value=available_counts["hard"],
    value=min(1, available_counts["hard"]),
    step=1,
)

total_marks = (
    easy_count * 2
    + medium_count * 5
    + hard_count * 10
)

st.sidebar.number_input(
    "Total Marks",
    min_value=0,
    value=int(total_marks),
    disabled=True,
)

algorithm = st.sidebar.selectbox(
    "Selection Algorithm",
    [
        "Branch & Bound",
        "Dynamic Programming",
        "Greedy",
        "Backtracking",
    ],
)

st.sidebar.divider()

st.sidebar.caption(
    f"Available questions: {len(questions)}"
)

# --------------------------------------------------
# GENERATE QUESTION PAPER
# --------------------------------------------------

if st.button(
    "🚀 Generate Paper",
    type="primary",
    use_container_width=False,
):

    if easy_count + medium_count + hard_count == 0:
        st.warning(
            "Please select at least one question."
        )

    else:
        specification = PaperSpecification(
            total_marks=total_marks,
            easy_count=easy_count,
            medium_count=medium_count,
            hard_count=hard_count,
        )

        if algorithm == "Branch & Bound":
            strategy = BranchBoundStrategy()
        elif algorithm == "Dynamic Programming":
            strategy = DPStrategy()
        elif algorithm == "Greedy":
            strategy = GreedyStrategy()
        else:
            strategy = BacktrackingStrategy()

        generator = ExamPaperGenerator(strategy)

        try:
            start_time = perf_counter()

            paper = generator.generate(
                questions,
                specification,
            )
            if algorithm == "Greedy":
                paper = sorted(
                    paper,
                    key=lambda q: q.marks,
                    reverse=True,
          )

            execution_time = (
                perf_counter() - start_time
            )

            is_valid = PaperValidator.validate(
                paper,
                specification,
            )

        except Exception as exc:
            st.error(
                f"Paper generation failed: {exc}"
            )
            st.stop()

        st.info(
            f"Algorithm Used: **{algorithm}**  |  "
            f"Execution Time: **{execution_time:.6f} seconds**"
        )

        if not paper:
            st.error(
                "No question paper was generated. "
                "Try a different algorithm or selection."
            )

        else:
            generated_marks = sum(
                q.marks for q in paper
            )

            # --------------------------------------
            # GENERATED PAPER
            # --------------------------------------

            st.divider()
            st.subheader("📄 Generated Question Paper")

            st.caption(
                f"{len(paper)} questions · "
                f"{generated_marks} total marks"
            )

            with st.container(border=True):
                st.markdown("### Examination Questions")
                st.divider()

                for number, question in enumerate(
                    paper, start=1
                ):
                    left, right = st.columns([8, 1])

                    with left:
                        st.markdown(
                            f"**Q{number}.** "
                            f"{question.question}"
                        )

                    with right:
                        st.markdown(
                            f"**{question.marks} marks**"
                        )

                    st.divider()

            # --------------------------------------
            # DOWNLOAD PAPER
            # --------------------------------------

            st.subheader("📥 Export Question Paper")

            paper_text = [
                "PAPERPILOT - QUESTION PAPER",
                "=" * 40,
                f"Total Questions: {len(paper)}",
                f"Total Marks: {generated_marks}",
                f"Algorithm: {algorithm}",
                "",
                "QUESTIONS",
                "-" * 40,
                "",
            ]

            for number, question in enumerate(
                paper, start=1
            ):
                paper_text.append(
                    f"Q{number}. {question.question}"
                )
                paper_text.append(
                    f"Marks: {question.marks}"
                )
                paper_text.append("")

            st.download_button(
                label="📄 Download Question Paper (.txt)",
                data="\n".join(paper_text),
                file_name="PaperPilot_Question_Paper.txt",
                mime="text/plain",
                type="primary",
                use_container_width=True,
            )

            # --------------------------------------
            # METRICS
            # --------------------------------------

            st.divider()
            st.subheader("📌 Paper Overview")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "📝 Total Marks",
                    generated_marks,
                )

            with col2:
                st.metric(
                    "📚 Total Questions",
                    len(paper),
                )

            with col3:
                st.metric(
                    "🛡️ Validation",
                    "Valid" if is_valid else "Invalid",
                )

            # --------------------------------------
            # DIFFICULTY DISTRIBUTION
            # --------------------------------------

            st.divider()
            st.subheader("📊 Difficulty Distribution")

            st.caption(
                "Number of selected questions by difficulty."
            )

            difficulty_data = {
                "Easy": sum(
                    q.difficulty.lower() == "easy"
                    for q in paper
                ),
                "Medium": sum(
                    q.difficulty.lower() == "medium"
                    for q in paper
                ),
                "Hard": sum(
                    q.difficulty.lower() == "hard"
                    for q in paper
                ),
            }

            chart_col, summary_col = st.columns(
                [3, 2],
                gap="large",
            )

            with chart_col:
                st.bar_chart(
                    difficulty_data,
                    color="#7C3AED",
                )

            with summary_col:
                with st.container(border=True):
                    st.markdown("#### Question Breakdown")
                    st.write(
                        f"Easy: **{difficulty_data['Easy']}**"
                    )
                    st.write(
                        f"Medium: **{difficulty_data['Medium']}**"
                    )
                    st.write(
                        f"Hard: **{difficulty_data['Hard']}**"
                    )
                    st.divider()
                    st.write(
                        f"**Total:** {len(paper)} questions"
                    )

            # --------------------------------------
            # PAPER SUMMARY
            # --------------------------------------

            st.divider()
            st.subheader("📋 Paper Summary")

            summary_col1, summary_col2 = st.columns(2)

            with summary_col1:
                st.write(
                    f"**Easy:** {difficulty_data['Easy']}"
                )
                st.write(
                    f"**Medium:** {difficulty_data['Medium']}"
                )
                st.write(
                    f"**Hard:** {difficulty_data['Hard']}"
                )

            with summary_col2:
                st.write(
                    f"**Required Marks:** "
                    f"{specification.total_marks}"
                )
                st.write(
                    f"**Generated Marks:** {generated_marks}"
                )

            # --------------------------------------
            # VALIDATION REPORT
            # --------------------------------------

            st.divider()
            st.subheader("🛡️ Validation Report")

            if is_valid:
                st.success(
                    "PaperPilot verified the generated paper."
                )

                check_col1, check_col2, check_col3 = (
                    st.columns(3)
                )

                with check_col1:
                    st.markdown("**Marks Check**")
                    st.write(
                        "Review required and generated marks."
                    )

                with check_col2:
                    st.markdown("**Paper Validation**")
                    st.write(
                        "The paper passed the existing validator."
                    )

                with check_col3:
                    st.markdown("**Final Status**")
                    st.write("✅ VALID")

            else:
                st.error(
                    "The generated paper failed validation. "
                    "Review the selected counts, marks, and "
                    "available questions."
                )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()
st.caption(
    "PaperPilot · Intelligent Question Paper Generation "
    "using Python and algorithmic selection"
)
