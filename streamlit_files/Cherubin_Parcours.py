import streamlit as st
import streamlit as st
import os
import time
from pathlib import Path


# --------------------------------------------------
# Global page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Cherubin Makembele | Academic Profile",
    layout="wide"
)
# --------------------------------------------------
# Global CSS (icon cards + hover + mobile)
# --------------------------------------------------
st.markdown("""
<style>
/* Card grid */
.icon-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 1rem;
    margin-top: 1rem;
}

/* Card style */
.icon-card {
    background-color: var(--secondary-background-color);
    border-radius: 16px;
    padding: 1.2rem 1rem;
    text-align: center;
    text-decoration: none;
    color: inherit;
    transition: all 0.25s ease;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
}

/* Hover effect */
.icon-card:hover {
    transform: translateY(-6px) scale(1.02);
    box-shadow: 0 12px 30px rgba(0,0,0,0.15);
}

/* Icon */
.icon {
    font-size: 2.2rem;
    margin-bottom: 0.5rem;
}

/* Label */
.icon-label {
    font-weight: 600;
    font-size: 1rem;
}

/* Mobile polish */
@media (max-width: 600px) {
    .icon {
        font-size: 2rem;
    }
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Sidebar navigation menu
# --------------------------------------------------
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Home", "Profile", "Academic History", "Projects", "Interactive Code", "Contact"],
    key="menu"
)

# --------------------------------------------------
# Pages logic
# --------------------------------------------------
if menu == "Home":
    st.title("Academic Profile App")
    st.write(
        """
        Welcome to my academic portfolio.  
        Use the **sidebar menu** to explore my profile, academic background,
        research projects, interactive python scripts, and more!
        """
    )
    st.info("Select a page from the sidebar to get started.")


# ----------------------ACADEMIC HISTORY----------------------------
from pathlib import Path

if menu == "Academic History":
    st.title("Academic History")

    st.markdown(
        """
        - **Diploma in Mathematical Sciences** — CPUT  
        - **Advanced Diploma in Mathematical Sciences** — CPUT  
        - **BSc Honours in Mathematics** — UWC  
        - **MSc in Mathematics** *(in progress)* — UWC  
        """,     unsafe_allow_html=True

    )

    st.markdown(
    """
    I come from a city named Kinshasa where I spent 19 years, and underwent my primary (École Ku-Ntwala) and high-school (Complexe-Scolaire Les Loupiots). Additionnally, I have a Diploma of french as a study language (DELF B2), from Lycée-Français Réné DesCartes.
    """,     unsafe_allow_html=True)
    
    st.markdown(
    """
    In South Africa, I am an alumnus of the Cape Peninsula University of Technology (CPUT) and the
    University of the Western Cape (UWC). My Diploma and Advanced Diploma in
    Mathematical Sciences at CPUT emphasized mathematical and statistical modelling,
    numerical methods, matrix theory, and introductory machine learning, alongside
    coursework in logic, biomathematics, and biostatistics. This training was
    complemented by applied data analysis using SQL, R (RStudio), Python, and SAS.
    I later completed a BSc Honours degree in Mathematics at UWC and am currently
    pursuing an MSc in Mathematics, specializing in pure mathematics.
    """,     unsafe_allow_html=True)


   

# ---------------------PROFILE-----------------------------

from pathlib import Path
import os
import streamlit as st

# ================= MENU LOGIC =================

from pathlib import Path
import streamlit as st

if menu == "Profile":
    st.title("Profile")
    st.subheader("Cherubin Makembele")

    st.write("**Field:** Mathematics")
    st.write("**Research interests:** Graph theory, ring theory, and algebraic structures, machine learning, matrices, etc.")
    st.write("**Current research:** Annihilating ideal graphs of commutative unitary rings.")


    st.write(
    "**About Me:** I am fluent in French and English, I enjoy science in all its forms, from random fun facts to the "
    "algorithm-ish patterns you see in nature, languages, sports, etc. ")
    
    st.write(
    "I’m naturally curious and like exploring ideas across different fields, "
    "especially when they connect abstract thinking with the real world."
    " More importantly ust learn fun facts backed by sciences for when I am a cool dad and a gramps 😎")

    st.write(
    "On the side, I am a Jiu-Jitsu hobbyist who competes from times to times "
    "and I like football so naturally I play regularly")


    BASE_DIR = Path(__file__).parent
    PHOTO_DIR = BASE_DIR / "photos"
    photos = list(PHOTO_DIR.glob("*"))

    if not photos:
        st.error("No photos found.")
    else:
        # st.subheader("Gallery")

        n_cols = 3

        for i in range(0, len(photos), n_cols):
            cols = st.columns(n_cols)
            for col, photo in zip(cols, photos[i:i+n_cols]):
                with col:
                    st.image(
                        photo,
                        use_container_width=True,
                        caption=None
                    )






# ----------------- PROJECTS ---------------------------------
elif menu == "Projects":
    st.title("Projects")

    st.subheader("Academic Projects")

    st.write(
    "My academic training spans pure and applied mathematics, with strong foundations "
    "in algebra, analysis, and mathematical modelling. Over the course of my studies, "
    "I have completed coursework and projects in graph theory, ring theory, linear algebra, "
    "numerical methods, probability and statistics, biomathematics, biostatistics, and "
    "introductory machine learning. These projects often involved both theoretical reasoning "
    "and computational implementation using tools such as Python, R (RStudio and R Markdown), "
    "Jupyter Notebook, SQL, and SAS, providing outlets toward roles in pure math associated positions, data analysis, data science, "
    "and software development."
)

    st.write(
        "Below are **selected highlights of documents and projects** I have produced so far. "
        "This is **not an exhaustive list**, but a representative sample of my academic work "
        "across different stages of my studies."
    )

    projects = {
        "📄 Honours Project": "files/honours_project.pdf",
        "📄 Survival Analysis Project": "files/Survival_Analysis_project.pdf",
        "📄 Advanced Diploma Machine Learning Project": "files/advanced_diploma_ml_project.pdf",
        "📄 Biomathematics Bifurcation Analysis": "files/Biomathematics_bifurcation_analysis.pdf"
    }

    for label, path in projects.items():
        file_path = Path(path)
        if file_path.exists():
            st.download_button(
                label=label,
                data=file_path.read_bytes(),
                file_name=file_path.name,
                mime="application/pdf"
            )
        else:
            st.warning(f"{label} not available.")


# ------------------------Interactive codes--------------------------
elif menu == "Interactive Code":
    st.title("Interactive Code")

    # ---- Sub-menu ----
    code_menu = st.radio(
    "Choose a mini program:",
    [
        "Ordered Integers (Ascending)",
        "Ordered Integers (Reverse)",
        "Quadratic Equation Solver",
        "Proper divisors of a Number",
        "Perfect Number Checker",
        "Numbers Above / Below Average"
    ]
)


    # ==================================================
    # Program 1 — Ascending order
    # ==================================================
    if code_menu == "Ordered Integers (Ascending)":
        st.subheader("Ordered Integers (Ascending)")
        st.write(
    "Enter integers one by one. Enter **0** to stop. "
    "The numbers are stored in a list and can be displayed "
    "in **ascending order**."
)


        if "integers_asc" not in st.session_state:
            st.session_state.integers_asc = []

        with st.form("asc_form", clear_on_submit=True):
            user_input = st.number_input(
                "Enter a number:",
                step=1,
                format="%d"
            )
            submitted = st.form_submit_button("Add number")

        if submitted:
            if user_input != 0:
                st.session_state.integers_asc.append(int(user_input))
            else:
                st.warning("0 entered. Input stopped.")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Show ordered list"):
                if st.session_state.integers_asc:
                    ordered = sorted(st.session_state.integers_asc)
                    st.success(f"Your numbers ordered asc are: {ordered}")
                else:
                    st.info("No numbers entered yet.")

        with col2:
            if st.button("Reset"):
                st.session_state.integers_asc = []
                st.info("List cleared.")

    # ==================================================
    # Program 2 — Reverse order (Problem 2)
    # ==================================================
    elif code_menu == "Ordered Integers (Reverse)":
        st.subheader("Ordered Integers (Reverse)")
        st.write(
    "Enter integers one by one. Enter **0** to stop. "
    "The numbers will be displayed in **reverse order**, "
    "with one value appearing on each line."
)


        if "integers_rev" not in st.session_state:
            st.session_state.integers_rev = []

        with st.form("rev_form", clear_on_submit=True):
            user_input = st.number_input(
                "Enter a number:",
                step=1,
                format="%d"
            )
            submitted = st.form_submit_button("Add number")

        if submitted:
            if user_input != 0:
                st.session_state.integers_rev.append(int(user_input))
                st.session_state.integers_rev.sort()
            else:
                st.warning("0 entered. Input stopped.")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Show reverse order"):
                if st.session_state.integers_rev:
                    st.success("Numbers in reverse order:")
                    for n in reversed(st.session_state.integers_rev):
                        st.write(n)
                else:
                    st.info("No numbers entered yet.")

        with col2:
            if st.button("Reset"):
                st.session_state.integers_rev = []
                st.info("List cleared.")

   
    # ==================================================
    # Program 3 — Quadratic Equation Solver & Graph
    # ==================================================
    elif code_menu == "Quadratic Equation Solver":
        st.subheader("Quadratic Equation Solver & Graph")
    
        st.write(
            "Enter the coefficients a, b, and c of the quadratic equation "
            "ax² + bx + c = 0. "
            "You may enter integers or fractions (e.g. 1/2, -3/4)."
        )
    
        from fractions import Fraction
        import numpy as np
        import plotly.graph_objects as go
        import cmath
    
        col1, col2, col3 = st.columns(3)
    
        with col1:
            a_str = st.text_input("Coefficient a", value="1")
        with col2:
            b_str = st.text_input("Coefficient b", value="0")
        with col3:
            c_str = st.text_input("Coefficient c", value="0")
    
        try:
            # Exact fractions
            a_frac = Fraction(a_str)
            b_frac = Fraction(b_str)
            c_frac = Fraction(c_str)
    
            if a_frac == 0:
                st.error("Coefficient a must be non-zero.")
                st.stop()
    
            # Display equation
            st.markdown(
                f"**Your equation is:**  \n"
                f"${a_frac}x^2 + {b_frac}x + {c_frac} = 0$"
            )
    
            # Float values for computation/plotting
            a = float(a_frac)
            b = float(b_frac)
            c = float(c_frac)
    
            # Discriminant
            delta = b**2 - 4*a*c
            st.write(f"**Discriminant:** Δ = {delta}")
    
            # Complex-aware solutions
            sqrt_delta = cmath.sqrt(delta)
            x1 = (-b + sqrt_delta) / (2*a)
            x2 = (-b - sqrt_delta) / (2*a)
    
            roots = []
    
            if delta > 0:
                st.success(
                    f"Two real solutions:\n"
                    f"- x₁ = {x1.real:.4f}\n"
                    f"- x₂ = {x2.real:.4f}"
                )
                roots = [x1.real, x2.real]
    
            elif delta == 0:
                st.success(f"One real solution:\n- x = {x1.real:.4f}")
                roots = [x1.real]
    
            else:
                st.info("No real solutions. Complex solutions are:")
                st.latex(rf"x_1 = {x1.real:.4f} + {x1.imag:.4f}i")
                st.latex(rf"x_2 = {x2.real:.4f} - {x2.imag:.4f}i")
    
            # ===============================
            # Smart auto-scaling
            # ===============================
            if roots:
                x_center = sum(roots) / len(roots)
                x_span = max(roots) - min(roots)
                margin = max(1.0, 0.8 * x_span)
                x_min = x_center - margin
                x_max = x_center + margin
            else:
                x_vertex = -b / (2 * a)
                x_min = x_vertex - 5
                x_max = x_vertex + 5
        
            x_vals = np.linspace(x_min, x_max, 400)
            y_vals = a * x_vals**2 + b * x_vals + c
        
            fig = go.Figure()
        
            fig.add_trace(
                go.Scatter(
                    x=x_vals,
                    y=y_vals,
                    mode="lines",
                    name="y = ax² + bx + c"
                )
            )
        
            if roots:
                fig.add_trace(
                    go.Scatter(
                        x=roots,
                        y=[0] * len(roots),
                        mode="markers",
                        name="Real roots",
                        marker=dict(size=10)
                    )
                )
        
            fig.update_layout(
                title="Quadratic Function (Orthonormal Auto-Scale)",
                xaxis=dict(
                    title="x",
                    range=[x_min, x_max],
                    showgrid=True,
                    zeroline=True,
                    zerolinewidth=3,      # bold x-axis
                    zerolinecolor="white",
                    showline=True,
                    linewidth=3,          # bold axis line
                    linecolor="white",
                    scaleanchor="y",
                    scaleratio=1
                ),
                yaxis=dict(
                    title="y",
                    showgrid=True,
                    zeroline=True,
                    zerolinewidth=3,      # bold y-axis
                    zerolinecolor="white",
                    showline=True,
                    linewidth=3,          # bold axis line
                    linecolor="white"
                ),
                showlegend=True
            )
        
            st.plotly_chart(fig, use_container_width=True)


        except Exception as e:
            st.error(f"Invalid input: {e}")

                 
    # ==================================================
    # Program 4 — Proper Divisors of a Number
    # ==================================================
    elif code_menu == "Proper divisors of a Number":
        st.subheader("Proper Divisors of a Number")
    
        st.write(
            "Proper divisors are all positive integer factors of a number, "
            "excluding the number itself.\n\n"
            "Example: for **6**, the proper divisors are **1, 2, 3**."
        )
    
        # Session state
        if "pd_result" not in st.session_state:
            st.session_state.pd_result = None
    
        with st.form("proper_divisors_form"):
            user_input = st.number_input(
                "Enter a positive integer:",
                min_value=1,
                step=1
            )
            submitted = st.form_submit_button("Compute proper divisors")
    
        if submitted:
            if user_input > 1:
                divisors = [i for i in range(1, user_input) if user_input % i == 0]
                if divisors:
                    st.session_state.pd_result = (
                        "success",
                        f"✅ **The proper divisors of {user_input} are:**  \n"
                        f"{', '.join(map(str, divisors))}"
                    )
                else:
                    st.session_state.pd_result = (
                        "info",
                        f"ℹ️ **{user_input} has no proper divisors (prime number).**"
                    )
    
        if st.button("Reset"):
            st.session_state.pd_result = None
    
        if st.session_state.pd_result:
            kind, message = st.session_state.pd_result
            getattr(st, kind)(message)

    # ==================================================
    # Program 5 — Perfect Number Checker
    # ==================================================
    elif code_menu == "Perfect Number Checker":
        st.subheader("Perfect Number Checker")
    
        st.write(
            "Perfect numbers are positive integers equal to the sum of their "
            "proper divisors (excluding the number itself).\n\n"
            "Example: **6 = 1 + 2 + 3**"
        )
    
        if "perfect_result" not in st.session_state:
            st.session_state.perfect_result = None
    
        with st.form("perfect_number_form"):
            user_input = st.number_input(
                "Enter a positive integer to test:",
                min_value=1,
                step=1
            )
            submitted = st.form_submit_button("Check if perfect")
    
        if submitted:
            divisors = [i for i in range(1, user_input) if user_input % i == 0]
            divisor_sum = sum(divisors)
    
            if divisor_sum == user_input:
                st.session_state.perfect_result = (
                    "success",
                    f"✅ **{user_input} is a perfect number**  \n"
                    f"because **{' + '.join(map(str, divisors))} = {user_input}**"
                )
            else:
                st.session_state.perfect_result = (
                    "info",
                    f"❌ **{user_input} is not a perfect number**  \n"
                    f"because **{' + '.join(map(str, divisors))} = {divisor_sum} ≠ {user_input}**"
                )
    
        if st.button("Reset"):
            st.session_state.perfect_result = None
    
        if st.session_state.perfect_result:
            kind, message = st.session_state.perfect_result
            getattr(st, kind)(message)

    # ==================================================
    # Program 6 — Numbers Above and Below the Average
    # ==================================================
    elif code_menu == "Numbers Above / Below Average":
        st.subheader("Numbers Above and Below the Average")
    
        st.write(
            "Enter integers one by one. "
            "Press **Add number** to store values. "
            "The average and classification update automatically."
        )
    
        if "numbers" not in st.session_state:
            st.session_state.numbers = []
    
        number = st.number_input(
            "Enter an integer:",
            step=1
        )
    
        col1, col2 = st.columns(2)
    
        with col1:
            if st.button("Add number"):
                st.session_state.numbers.append(int(number))
    
        with col2:
            if st.button("Reset"):
                st.session_state.numbers = []
    
        if st.session_state.numbers:
            numbers = st.session_state.numbers
            avg = sum(numbers) / len(numbers)
    
            below_avg = sorted([n for n in numbers if n < avg])
            above_avg = sorted([n for n in numbers if n > avg])
    
            st.write(f"**Numbers entered:** {numbers}")
            st.write(f"**Average:** {avg:.2f}")
            st.write(f"**Below average:** {below_avg}")
            st.write(f"**Above average:** {above_avg}")



# -------------- CONTACTS ------------------------------------
elif menu == "Contact":
    st.title("Contact")
    st.divider()

    st.subheader("Get in touch")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.link_button(
            "📧 Email",
            "mailto:cherubinmakembele@gmail.com"
        )

    with col2:
        st.link_button(
            "🔗 GitHub",
            "https://github.com/cherubinmakembele-dotcom"
        )

    with col3:
        st.link_button(
            "💼 LinkedIn",
            "https://www.linkedin.com/in/chérubin-makembele-521143211"
        )

    st.info("Use the sidebar to navigate to other pages.")

