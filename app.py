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
        st.title("Numeristas: Entrenamiento cerebral a través de las matemáticas")

        st.write(
            "Numeristas es una plataforma de entrenamiento cerebral que incluye 50 ejercicios matemáticos variados, pensados para ejercitar el cálculo mental con unos requisitos mínimos.")

        st.header("La Filosofía")
        st.markdown("""
                * **La Trampa de la Respuesta Inmediata:** Si sabes la respuesta en una décima de segundo, no estás entrenando; estás recitando. En tal caso hay que aumentar la dificultad. Todos los ejercicios tienen varios niveles.
                * **Abraza la Fricción:** El verdadero crecimiento ocurre en la "zona de esfuerzo". Bien sea que cueste 30 segundos o 30 minutos, el objetivo es encontrar el límite de tu capacidad mental.
                * **Computación para Adultos:** Mientras que 2 + 2 cumple su propósito para los niños, Numeristas está diseñado para adultos que desean mantener y expandir su agilidad cognitiva.
                * **Requisitos Mínimos:** No necesitas un doctorado en Matemáticas. Hemos eliminado el relleno, intentando que los conocimientos para poder disfrutar de todos los ejercicios sean mínimos. 
                * **Feedback integrado:** En ejercicios especializados fuera del plan de estudios estándar proporcionamos simulaciones completas con todos los pasos hasta la respuesta final. Tan solo hay 2 excepciones a esta regla.
                """)

        st.header("El Panorama de Entrenamiento")
        st.write(
            "En Numeristas abarcamos un amplio espectro de disciplinas. Tanto si te apasiona la aritmética, el pensamiento recursivo, la lógica algorítmica o el razonamiento espacial, aquí encontrarás el espacio ideal para desarrollar tu potencial.")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🔢 Aritmética y Álgebra")
            st.write("*Domina el lenguaje fundamental de los números y luego adéntrate en el álgebra.*")
            st.markdown("""
                            * **Lo Esencial:** Entrenamiento de precisión en Suma, Resta, Multiplicación, División y Fracciones.
                            * **Zonas Horarias:** Calcula conversiones de horas globales.
                            * **Potencias Avanzadas:** Aborda Potencias, Raíces y Logaritmos para construir intuición.              
                            * **Sistemas Alternativos:** Domina las Conversiones de Base para liberarte del pensamiento exclusivamente decimal.                       
                            * **Sistemas y Matrices:** Resuelve Sistemas de Ecuaciones, realiza Multiplicación de Matrices y calcula Determinantes.
                            * **Álgebra a través de la Geometría:** Resuelve problemas geométricos con polinomios de segundo y tercer grado.
                            * **Cadenas Simbólicas:** Ejecuta Cadenas de Sustitución.
                            """)

            st.subheader("🎲 Teoría de Números y Probabilidad")
            st.write("*Explora las propiedades fundamentales de los enteros y las matemáticas del azar.*")
            st.markdown("""
                            * **Números Primos:** Domina la identificación y la factorización de números primos.
                            * **Máximo Común Divisor:** Calcula los factores compartidos más grandes entre números.
                            * **Mínimo Común Múltiplo:** Encuentra los múltiplos comunes más pequeños entre números.                       
                            * **Día de la semana:** Aplica la aritmética modular para calcular mentalmente el día exacto de la semana para fechas históricas o futuras.
                            * **Probabilidad:** Internaliza el riesgo con Probabilidad de Dados y Combinaciones de Monedas.
                            """)

            st.subheader("🧠 Memoria y Concentración")
            st.write("*Ejercicios especializados diseñados para aumentar tu 'RAM Mental' y concentración.*")
            st.markdown("""
                            * **Memoria:** Recuerda números cada vez con una mayor cantidad de dígitos.
                            * **Piano:** Calcula usando sonido en lugar de entradas visuales en el ejercicio del Piano.                        
                            * **Atención Dinámica:** Realiza sumas de números que cambian dinámicamente (Mental Gravity) o cuenta el total de cuadrados que aparecen dinámicamente (Dynamic Count).
                            """)

        with col2:
            st.subheader("🧭 Razonamiento Espacial")
            st.write("*Desarrolla un 'GPS mental' realizando transformaciones complejas en el espacio 2D y 3D.*")
            st.markdown("""
                            * **Movimiento:** Calcula el movimiento en un sistema de coordenadas 3D virtual a través de Traslaciones Ortogonales y Diagonales, Rotaciones y Simetría.
                            * **Proyección:** Domina las Proyecciones Adyacentes y Opuestas en cubos de diferentes tamaños.
                            * **Búsqueda de Caminos:** Resuelve el Camino Más Corto y evalúa circuitos Eulerianos en problemas de los Puentes de Königsberg.                       
                            """)

            st.subheader("🌀 Recurrencias")
            st.write("*Entrena tu cerebro para manejar múltiples variables y patrones recursivos simultáneamente.*")
            st.markdown("""
                            * **Reconocimiento de Patrones:** Domina las Relaciones de Recurrencia, encuentra Coeficientes de Recurrencia e identifica Términos Faltantes en secuencias complejas.
                            * **Fracciones Continuas:** Descompón valores racionales en fracciones continuas o sigue el camino inverso, encuentra la fracción que corresponde a unos coeficientes dados.                
                            * **Secuencias Algorítmicas:** Resuelve la lógica recursiva del Problema de Flavio Josefo.
                            * **Progresiones Numéricas:** Domina las expansiones numéricas de los Patrones de Pascal Generalizados.                       
                            """)

            st.subheader("🧩 Informática y Lógica")
            st.write("*Cierra la brecha entre las matemáticas y la informática.*")
            st.markdown("""
                            * **Ejecución de Código y computación paralela:** Ejecuta Pseudocódigo en tu cabeza y averigua cuál es la forma más eficiente de gestionar recursos disponibles en paralelo.
                            * **Acertijos Algorítmicos:** Resuelve las Torres de Hanói, la lógica modular del Rompecajas y los acertijos de Jarras de Agua.
                            * **Cuadrículas Lógicas:** Lógica espacial compleja con Sudoku (2D y 3D), Puentes y Rompecabezas Deslizantes.
                            * **Coloración de Mapas:** Calcula el número máximo de celdas que pueden agruparse bajo estrictas restricciones de adyacencia.
                            * **Autómatas Celulares:** Calcula las generaciones posteriores de patrones de Crecimiento Celular basados en reglas algorítmicas estrictas.                    
                            """)

        st.divider()

        st.header("Afina el Motor")
        st.write("Personaliza la plataforma a tu nivel específico, tan solo tienes que pulsar en el botón de ajustes y modificar los parámetros:")
        st.markdown("""
                * **Selección Flexible de Ejercicios:** Adapta cada sesión a tus objetivos inmediatos. Ya sea que quieras dominar un solo ejercicio o abordar el circuito completo de 50 ejercicios, la plataforma se adapta a tu ritmo. El ciclo continúa sin interrupciones. 
                * **Ajustes de dificultad de cada ejercicio individual:** Controles granulares para superar la fase de "respuesta inmediata" y volver al esfuerzo productivo.
                * **Lógica de Orden:** Elige Secuencial para ganar impulso o Aleatorio para poner a prueba tu adaptabilidad.
                * **Complejidad Avanzada (Base/Remapeo):** Aquellos que hayan dominado la computación estándar pueden cambiar la base numérica a 2–9 en algunos ejercicios específicos para forzar a su cerebro a salir de su zona de confort decimal. También pueden activar el Remapeo para sobrescribir por completo cómo procesan los dígitos estándar. El remapeo rompe el vínculo entre símbolo y valor—obligando a tu cerebro a calcular cuando el símbolo "1" en realidad significa 3, el "2" significa 7...
                * **Tiempo entre ejercicios:** Controla el ritmo de tu sesión de entrenamiento. Ajusta el retraso exacto que el motor tarda en cargar el siguiente ejercicio. Si no quieres perder el tiempo leyendo "correcto" puedes fijar un salto de 0 segundos en respuestas correctas. Para respuestas incorectas puedes programar un retraso más largo, de 5, 10, 60... segundos, para que te de tiempo a averiguar qué falló en el razonamiento. En ejercicios que tengan simulaciones como feedback el contador global está deshabilitado, simplemente cuando termina la simulación el motor salta al siguiente ejercicio en pocos segundos. Siempre puedes hacer click en "Skip" para continuar.
                * **Modo Memoria:** Activar esta opción hará que algunos ejercicios básicos se compliquen, puesto que al terminar el tiempo establecido desaparecerán de la pantalla. En tal caso, hay que retener el ejercicio y luego calcular mentalmente todos los pasos, por lo que la carga cognitiva es superior.
                """)

        st.divider()
    elif st.session_state.lang == "ZH":
        st.title("Numeristas: 高性能大脑训练")

        st.write(
            "Numeristas 是一个高性能大脑训练平台，旨在通过深度专注和极低的前提要求来突破您的计算极限。")

        st.header("理念")
        st.markdown("""
                * **瞬答陷阱：** 如果你能在一十分之一秒内得出答案，那你不是在训练，而是在背诵。你可以在所有练习中增加并调整难度。
                * **拥抱摩擦：** 真正的成长发生在“挣扎区”。无论需要30秒还是30分钟，目标是找到你心智能力的边界。
                * **成人级计算：** 虽然 2 + 2 对儿童有其意义，但 Numeristas 是为那些希望保持和扩展认知敏捷性的成年人量身定制的。
                * **极低门槛：** 你不需要数学博士学位。我们去除了所有繁文缛节，只需掌握基础算术和基本逻辑即可开始。
                * **内置反馈：** 对于标准课程之外的专业领域，我们提供实时反馈和指导——当然也有几个有意为之的例外，旨在让你保持挑战感而不至于感到不知所措。
                """)

        st.header("训练领域")
        st.write(
            "Numeristas 涵盖了广阔的思维训练领域。无论你是想精通硬核算术、递归思维、算法逻辑，还是空间推理，我们都有适合你的领域。")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🔢 算术与代数")
            st.write("*掌握数字的基础语言，然后向复杂领域推进。*")
            st.markdown("""
                            * **基础要素：** 加、减、乘、除和分数的精准训练。
                            * **时区：** 计算全球时间转换。
                            * **高阶乘方：** 应对乘方、n次方根和对数，以建立指数直觉。              
                            * **替代系统：** 精通进制转换，打破纯十进制思维的束缚。                       
                            * **系统与矩阵：** 求解方程组、执行矩阵乘法并计算行列式。
                            * **几何代数：** 利用二次和三次多项式关系推导和评估空间约束。
                            * **符号链：** 执行替换链计算。
                            """)

            st.subheader("🎲 数论与概率")
            st.write("*探索整数的基本性质和随机性的数学。*")
            st.markdown("""
                            * **素数：** 精通素数识别和素数分解。
                            * **最大公约数：** 计算数字之间的最大公因数。
                            * **最小公倍数：** 寻找多个集合中的最小公倍数。                       
                            * **历法逻辑：** 应用模算术在脑海中准确计算出历史或未来日期的星期。
                            * **概率：** 通过骰子概率和硬币组合将风险内化。
                            """)

            st.subheader("🧠 记忆与专注")
            st.write("*专门设计的练习，旨在增加你的'心智内存'和专注力。*")
            st.markdown("""
                            * **记忆负荷：** 高位数记忆保持。
                            * **钢琴：** 在“钢琴”练习中，使用声音而非视觉输入进行计算。                        
                            * **动态注意力：** 掌握心理重力和动态计数。
                            """)

        with col2:
            st.subheader("🧭 空间推理")
            st.write("*通过在2D和3D空间中进行复杂的变换来开发'心理GPS'。*")
            st.markdown("""
                            * **运动：** 通过正交和对角平移、旋转及对称，计算虚拟3D坐标系上的运动。
                            * **投影：** 掌握不同尺寸立方体上的相邻和相对投影。
                            * **寻路：** 解决最短路径问题，并在哥尼斯堡桥梁问题中评估欧拉回路。                       
                            """)

            st.subheader("🌀 递推")
            st.write("*训练你的大脑同时处理多个变量和递归模式。*")
            st.markdown("""
                            * **模式识别：** 掌握递推关系，寻找递推系数，并识别复杂序列中的缺失项。
                            * **连分数：** 将有理数值分解为连分数，并从其系数反推标准分数。                      
                            * **算法序列：** 解决约瑟夫斯问题的递归逻辑。
                            * **数字数列：** 精通广义帕斯卡模式的数值展开。                       
                            """)

            st.subheader("🧩 计算机科学与逻辑")
            st.write("*弥合数学与计算机科学之间的差距。*")
            st.markdown("""
                            * **代码执行：** 在脑海中运行伪代码并管理并行计算调度。
                            * **算法谜题：** 解决汉诺塔、保险箱破解（模逻辑）和水壶谜题。
                            * **逻辑网格：** 涉及数独（2D和3D）、桥梁和滑块谜题的复杂空间逻辑。
                            * **地图着色：** 计算在严格相邻约束下可以分组的最大单元格数量。
                            * **元胞自动机：** 基于严格的算法规则计算细胞生长的后续演化。                    
                            """)

        st.divider()

        st.header("调优引擎")
        st.write("根据你的具体水平定制平台：")
        st.markdown("""
                * **灵活选择练习：** 根据你的当前目标量身定制每次训练。无论你是想精通单一练习还是挑战完整的50项回路，平台都能适应你的节奏。循环无缝进行。 
                * **难度缩放：** 精细的控制，让你超越“瞬答”阶段，重新回到富有成效的“挣扎”中。
                * **排序逻辑：** 选择“顺序”以建立动力，或选择“随机”来测试你的适应性。
                * **高级复杂性 (进制/重映射)：** 对于那些已经掌握标准计算的人，可以切换到 2–9 进制，迫使大脑走出十进制的舒适区；或者激活“重映射”功能，完全覆盖你处理标准数字的方式。重映射切断了符号与数值之间的联系——当符号“1”实际上代表3，“2”代表7时，迫使你的大脑重新进行计算……
                * **精准计时：** 控制训练过程的节奏。调整引擎自动加载下一个练习前的精确延迟时间。将正确答案的跳转时间设置为0秒以保持快节奏的心流状态；或者为错误答案设置2分钟的延迟，给自己留出时间在继续之前反推复杂的解决方案。你随时可以点击“跳过”继续。
                * **记忆模式：** 启用此约束以强制进行即时记忆。你设定准确的暴露时间；一旦倒计时归零，练习就会消失，迫使你将变量保留在工作记忆中并完全在脑海中完成计算。
                """)

        st.divider()


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

        st.markdown("""
    **Especificaciones del Motor:**
    * **Operandos:** De 2 a 6 variables simultáneas.
    * **Magnitud:** De 1 a 6 dígitos por operando.
    * **Permitir valores negativos:** Opcional.
    * **Complejidad Avanzada (Base/Remapeo):** Opcional.
    * **Ritmo:** Temporizador Global.

    ### El Objetivo
    Calcula la suma exacta de los valores numéricos presentados con la mayor rapidez y precisión posible.

    ### Lógica de Restricción: Bases Alternativas
    Si el modificador de Base está activo, un círculo indicador en la parte superior central de la pantalla mostrará la base numérica actual (ej. **3**). Tanto las variables presentadas como tu respuesta final enviada deben ser procesadas en esta base.

    **Ejemplo (Base 3):**
    * **Mostrado:** 101 + 102
    * **Traducción a Decimal:** 10 + 11 = 21
    * **Entrada Requerida:** 210 (que es 21 convertido de nuevo a Base 3)

    ### Lógica de Restricción: Remapeo
    Si el modificador de Remapeo está activo, el círculo indicador mostrará una **R**. Esto significa que los símbolos visuales han sido secuestrados y ya no representan sus valores estándar. Sin embargo, tu respuesta final siempre deberá ingresarse utilizando dígitos estándar y no remapeados.

    **Ejemplo de Mapeo:** 1=3, 2=1, 3=2, 4=5, 5=4, 6=7, 7=8, 8=9, 9=6

    * **Mostrado:** 12 + 34
    * **Traducción Mental:** El símbolo '1' significa 3, y el '2' significa 1 (Valor Real: 31). El símbolo '3' significa 2, y el '4' significa 5 (Valor Real: 25).
    * **Computación Real:** 31 + 25 = 56
    * **Entrada Requerida:** 56
    """)

    elif st.session_state.lang == "ZH":
        st.title("教程：加法")

        st.markdown("""
    **引擎规格：**
    * **操作数：** 2至6个并发变量。
    * **量级：** 每个操作数1至6位数字。
    * **允许负值：** 可选。
    * **高级复杂性（进制/重映射）：** 可选。
    * **节奏：** 全局计时器。

    ### 目标
    尽可能快速、准确地计算出所提供数值的精确总和。

    ### 约束逻辑：替代进制
    如果激活了“进制”修饰符，屏幕顶部中央的指示圆圈将显示当前的数字进制（例如，**3**）。无论是呈现的变量还是你最终提交的答案，都必须在该进制下进行处理。

    **示例（三进制）：**
    * **显示内容：** 101 + 102
    * **十进制转换：** 10 + 11 = 21
    * **需要输入的答案：** 210（即将21重新转换回三进制）

    ### 约束逻辑：重映射
    如果激活了“重映射”修饰符，指示圆圈将显示 **R**。这意味着视觉符号已被劫持，不再代表其标准值。但是，你最终的输入将始终使用标准的、未映射的数字来键入。

    **映射示例：** 1=3, 2=1, 3=2, 4=5, 5=4, 6=7, 7=8, 8=9, 9=6

    * **显示内容：** 12 + 34
    * **心理转换：** 符号'1'代表3，'2'代表1（真实值：31）。符号'3'代表2，'4'代表5（真实值：25）。
    * **真实计算：** 31 + 25 = 56
    * **需要输入的答案：** 56
    """)

# 3. The outer chain remains unbroken
else:
    st.title(t["home_btn"])

st.sidebar.divider()

# --- LEGAL & PRIVACY EXPANDER ---
if st.session_state.lang == "EN":
    expander_title = "Legal & Privacy"
    legal_text = """
    **Contact:** Any feedback or requests are welcome: info@numeristas.com

    **Privacy Policy:** We don't collect any personal data or tracking cookies.

    **Disclaimer & Liability:** This platform was engineered with extensive use of Artificial Intelligence. As a result, the engine or the generated logic may contain errors or inaccuracies. The developer assumes no responsibility or liability for any issues, crashes, or incorrect computations arising from its use. Furthermore, we make no medical or cognitive claims regarding this software.

    **Hardware Warning:** Please be advised that the final exercise utilizes an exact C++ solver that exhaustively computes every possible branch of a decision tree. This algorithmic execution is hardware and power intensive, and may cause rapid battery drain or thermal throttling on mobile devices.
    """
elif st.session_state.lang == "ES":
    expander_title = "Legal y Privacidad"
    legal_text = """
    **Contacto:** Cualquier comentario o solicitud es bienvenido: info@numeristas.com

    **Política de Privacidad:** No recopilamos datos personales ni cookies de seguimiento.

    **Descargo de Responsabilidad:** Esta plataforma fue desarrollada con un uso extensivo de Inteligencia Artificial. Como resultado, el motor o la lógica generada pueden contener errores o inexactitudes. El desarrollador no asume ninguna responsabilidad legal por problemas, fallos o cálculos incorrectos derivados de su uso. Además, no afirmamos que el uso de este software aporte ningún beneficio médico o cognitivo.

    **Advertencia de Hardware:** Tenga en cuenta que el último ejercicio utiliza un solucionador exacto en C++ que calcula exhaustivamente cada rama posible de un árbol de decisiones. Esta ejecución algorítmica requiere un uso intensivo de hardware y energía, y puede causar un rápido consumo de batería o estrangulamiento térmico (thermal throttling) en dispositivos móviles.
    """
elif st.session_state.lang == "ZH":
    expander_title = "法律与隐私"
    legal_text = """
    **联系方式：** 欢迎提供任何反馈或要求：info@numeristas.com

    **隐私政策：** 我们不收集任何个人数据或跟踪 cookie。

    **免责声明：** 本平台在开发过程中广泛使用了人工智能。因此，引擎或生成的逻辑可能包含错误或不准确之处。开发者对因使用本软件而引起的任何问题、崩溃或计算错误不承担任何责任或法律责任。此外，我们不对本软件提出任何医疗或认知方面的声明。

    **硬件警告：** 请注意，最终练习使用了一个精确的 C++ 求解器，它会穷举计算决策树的每个可能分支。这种算法执行会大量消耗硬件资源和电量，可能会导致移动设备电池快速耗尽或触发过热降频。
    """

with st.sidebar.expander(expander_title, expanded=False):
    st.markdown(legal_text)