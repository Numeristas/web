import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Coding Tutorials", layout="wide")
# --- UI SANCTUARY: HIDE STREAMLIT BRANDING & FIX SIDEBAR ---
# --- UI SANCTUARY: HIDE STREAMLIT BRANDING & LOCK SIDEBAR ---


# --- INITIALIZE MEMORY ---
if 'lang' not in st.session_state:
    st.session_state.lang = "EN"
if 'selected_view' not in st.session_state:
    st.session_state.selected_view = "Home"

# --- TRANSLATIONS DICTIONARY ---
ui_text = {
    "EN": {
        "home_btn": "🏠 Home", "tut_header": "### TUTORIALS",
        "ex_add": "Addition"
    },
    "ES": {
        "home_btn": "🏠 Inicio", "tut_header": "### TUTORIALES",
        "ex_add": "Suma"
    },
    "ZH": {
        "home_btn": "🏠 首页", "tut_header": "### 教程",
        "ex_add": "加法"
    }
}
t = ui_text[st.session_state.lang]

# 2. Top Center Menu
col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 2])
with col2: st.button("⭐ Rate App", use_container_width=True)
with col3: st.button("💬 Feedback", use_container_width=True)
with col4: st.button("💸 Contribute", use_container_width=True)
st.divider()

# 3. Left Sidebar (Navigation & Language)

lang1, lang2, lang3 = st.sidebar.columns(3)

# The type="primary" turns the active button blue!
if lang1.button("EN", use_container_width=True, type="primary" if st.session_state.lang == "EN" else "secondary"):
    st.session_state.lang = "EN"
    st.rerun()  # Forces instant visual update
if lang2.button("ES", use_container_width=True, type="primary" if st.session_state.lang == "ES" else "secondary"):
    st.session_state.lang = "ES"
    st.rerun()
if lang3.button("ZH", use_container_width=True, type="primary" if st.session_state.lang == "ZH" else "secondary"):
    st.session_state.lang = "ZH"
    st.rerun()

st.sidebar.divider()

# Home Button
if st.sidebar.button(t["home_btn"], use_container_width=True,
                     type="primary" if st.session_state.selected_view == "Home" else "secondary"):
    st.session_state.selected_view = "Home"
    st.rerun()

st.sidebar.markdown(t["tut_header"])

# Exercise Buttons
# We map the visual translated name to an internal "fixed" ID so routing doesn't break when switching languages
exercises = [
    {"id": "Addition", "label": t["ex_add"]},

]

for ex in exercises:
    if st.sidebar.button(ex["label"], use_container_width=True,
                         type="primary" if st.session_state.selected_view == ex["id"] else "secondary"):
        st.session_state.selected_view = ex["id"]
        st.rerun()

# 4. Central Section (Dynamic Content)
selected_view = st.session_state.selected_view

if selected_view == "Home":
    if st.session_state.lang == "EN":
        st.title("Numeristas: High-Performance Brain Training")

        st.write(
            "Numeristas is a high-performance brain training platform designed to push your computational limits through deep focus and minimal prerequisites.")

        st.header("The Philosophy")
        st.markdown("""
            * **The Instant-Answer Trap:** If you know the answer in a tenth of a second, you aren't training; you're reciting. You can increase and adjust difficulty in all exercises.
            * **Embrace the Friction:** Real growth happens in the "struggle zone." Whether it takes 30 seconds or 30 minutes, the goal is to find the boundary of your mental capacity.
            * **Adult-Grade Computation:** While 2 + 2 serves its purpose for children, Numeristas is built for adults who want to maintain and expand their cognitive agility.
            * **Minimal Prerequisites:** You don't need a PhD in Mathematics. We’ve stripped away the fluff, requiring only a grasp of fundamental arithmetic and foundational logic to get started.
            * **Built-in Feedback:** For specialized fields outside the standard curriculum, we provide real-time feedback and guidance—with a few intentional exceptions designed to keep you challenged without feeling overwhelmed.
            """)

        st.header("The Training Landscape")
        st.write(
            "Numeristas covers a vast landscape of mental disciplines. Whether you are looking to master hardcore arithmetic, recursive thinking, algorithmic logic, or spatial reasoning, we have a field for you.")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🔢 Arithmetic & Algebra")
            st.write("*Master the fundamental language of numbers, then push into the complex.*")
            st.markdown("""
                        * **The Essentials:** Precision training in Addition, Subtraction, Multiplication, Division, and Fractions.
                        * **Time Zones:** Calculate global hour conversions.
                        * **Advanced Powers:** Tackle Powers, Nth Roots, and Logarithms to build exponential intuition.              
                        * **Alternative Systems:** Master Base Conversions to break free from decimal-only thinking.                       
                        * **Systems & Matrices:** Solve Systems of Equations, perform Matrix Multiplication, and calculate Determinants.
                        * **Algebra through Geometry:** Derive and evaluate spatial constraints using second and third-degree polynomial relationships.
                        * **Symbolic Chains:** Execute Substitution Chains.
                        """)

            st.subheader("🎲 Number Theory & Probability")
            st.write("*Explore the fundamental properties of integers and the mathematics of chance.*")
            st.markdown("""
                        * **Prime Numbers:** Master prime identification and prime factorization.
                        * **Greatest Common Divisor:** Calculate the largest shared factors between numbers.
                        * **Least Common Multiple:** Find the smallest common multiples across sets.                       
                        * **Calendrical Logic:** Apply modular arithmetic to mentally calculate the exact day of the week for historical or future dates.
                        * **Probability:** Internalize risk with Dice Probability and Coin Combinations.
                        """)

            st.subheader("🧠 Memory & Focus")
            st.write("*Specialized exercises designed to increase your 'Mental RAM' and focus.*")
            st.markdown("""
                        * **Memory Loads:** High-digit Memory retention.
                        * **Piano:** Compute using sound instead of visual inputs in the Piano exercise.                        
                        * **Dynamic Attention:** Master Mental Gravity and Dynamic Counting.
                        """)

        with col2:
            st.subheader("🧭 Spatial Reasoning")
            st.write("*Develop a 'mental GPS' by performing complex transformations in 2D and 3D space.*")
            st.markdown("""
                        * **Movement:** Calculate movement on a virtual 3D coordinate system through Orthogonal and Diagonal Translations, Rotations, and Symmetry.
                        * **Projection:** Master Adjacent and Opposite Projections on cubes of different sizes.
                        * **Pathfinding:** Solve the Shortest Path and evaluate Eulerian circuits in Königsberg Bridge problems.                       
                        """)

            st.subheader("🌀 Recurrences")
            st.write("*Train your brain to handle multiple variables and recursive patterns simultaneously.*")
            st.markdown("""
                        * **Pattern Recognition:** Master Recurrence Relations, find Recurrence Coefficients, and identify Missing Terms in complex sequences.
                        * **Continued Fractions:** Break down rational values into continued fractions, and reverse-engineer standard fractions from their coefficients.                      
                        * **Algorithmic Sequences:** Solve the recursive logic of the Josephus Problem.
                        * **Numeric Progressions:** Master the numerical expansions of Generalised Pascal Patterns.                       
                        """)

            st.subheader("🧩 Computer Science & Logic")
            st.write("*Bridge the gap between mathematics and computer science.*")
            st.markdown("""
                        * **Code Execution:** Run Pseudocode in your head and manage Parallel Computing scheduling.
                        * **Algorithmic Puzzles:** Solve the Towers of Hanoi, Safe Cracker modulo-logic, and Water Jug puzzles.
                        * **Logic Grids:** Complex spatial logic with Sudoku (2D & 3D), Bridges, and Sliding Puzzles.
                        * **Map Coloring:** Calculate the maximum number of cells that can be grouped under strict adjacency constraints.
                        * **Cellular Automata:** Compute subsequent generations of Cellular Growth patterns based on strict algorithmic rules.                    
                        """)

        st.divider()

        st.header("Tune the Engine")
        st.write("Customize the platform to your specific level:")
        st.markdown("""
            * **Flexible Exercise Selection:**  Tailor every session to your immediate objectives. Whether you want to master a single exercise or tackle the full 50-exercise circuit, the platform adapts to your pace. The cycle continues seamlessly. 
            * **Difficulty Scaling:** Granular controls to move past the "instant answer" phase and back into the productive struggle.
            * **Order Logic:** Choose Sequential to build momentum or Random to test your adaptability.
            * **Advanced Complexity (Base/Remap):** For those who have mastered standard computation, switch to Base 2–9 to force your brain out of its decimal comfort zone, or activate Remapping to completely overwrite how you process standard digits. Remapping severs the tie between symbol and value—forcing your brain to compute when the symbol "1" actually means 3, "2" means 7...
            * **Precision Timing:** Control the momentum of your training session. Adjust the exact delay before the engine automatically loads the next exercise. Set a 0-second jump for correct answers to maintain a rapid-fire flow state, or program a 2-minute delay for incorrect answers, giving yourself time to reverse-engineer complex solutions before moving on. You can always click on "Skip" to move on.
            * **Memory Mode:** Toggle this constraint to force immediate retention. You set the exact exposure time; once the clock hits zero, the exercise vanishes, forcing you to hold the variables and compute entirely in your working memory.
            """)

        st.divider()


    elif st.session_state.lang == "ES":
        st.title("¡Bienvenido a la aplicación de tutoriales! 🚀")
        st.write(
            "Navega usando los botones azules a la izquierda para explorar nuestros ejercicios interactivos de lógica 3D y 2D.")
    elif st.session_state.lang == "ZH":
        st.title("欢迎来到编程教程应用！🚀")
        st.write("使用左侧的蓝色按钮导航，探索我们的交互式3D和2D逻辑练习。")


elif selected_view == "Addition":
    # 1. Language routing nested INSIDE the Addition view
    if st.session_state.lang == "EN":
        st.title("Tutorial: Addition")

        st.markdown("""
**Engine Specifications:**
* **Operands:** 2 to 6 simultaneous variables.
* **Magnitude:** 1 to 6 digits per operand.
* **Allow negative values:** Optional .
* **Advanced Complexity (Base/Remap):** Optional
* **Pacing:** Global Timer

### The Objective
Compute the exact sum of the presented numerical values as quickly and accurately as possible.

### Constraint Logic: Alternative Bases
If the Base modifier is active, an indicator circle at the top center of the screen will display the current numerical base (e.g., **3**). Both the presented variables and your final submitted answer must be processed in this base.

**Example (Base 3):**
* **Displayed:** 101 + 102
* **Decimal Translation:** 10 + 11 = 21
* **Required Input:** 210 (which is 21 converted back into Base 3)

### Constraint Logic: Remapping
If the Remap modifier is active, the indicator circle will display **R**. This signifies that the visual symbols have been hijacked and no longer represent their standard values. However, your final input will always be entered using standard, unmapped digits.

**Example Mapping:** 1=3, 2=1, 3=2, 4=5, 5=4, 6=7, 7=8, 8=9, 9=6

* **Displayed:** 12 + 34
* **Mental Translation:** The symbol '1' means 3, and '2' means 1 (True Value: 31). The symbol '3' means 2, and '4' means 5 (True Value: 25).
* **True Computation:** 31 + 25 = 56
* **Required Input:** 56
""")

    elif st.session_state.lang == "ES":
        st.title("Tutorial: Suma")
        st.write("**Objetivo:** Aprender a sumar dos números.")

    elif st.session_state.lang == "ZH":
        st.title("教程：加法")
        st.write("**目标：** 学习如何将两个数字相加。")

# 3. The outer chain remains unbroken
else:
    st.title(t["home_btn"])

st.sidebar.divider()

with st.sidebar.expander("Legal & Privacy", expanded=False):
    st.markdown("""
    **Contact:** Any feedback or requests are welcome: info@numeristas.com

    **Privacy Policy:** We don't collect any personal data or tracking cookies.

    **Disclaimer & Liability:** This platform was engineered with extensive use of Artificial Intelligence. As a result, the engine or the generated logic may contain errors or inaccuracies. The developer assumes no responsibility or liability for any issues, crashes, or incorrect computations arising from its use. Furthermore, we make no medical or cognitive claims regarding this software.

    **Hardware Warning:** Please be advised that the final exercise utilizes an exact C++ solver that exhaustively computes every possible branch of a decision tree. This algorithmic execution is hardware and power intensive, and may cause rapid battery drain or thermal throttling on mobile devices.
    """)