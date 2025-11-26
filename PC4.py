

# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.

# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.

# Luego activamos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# deactivate
# En MacOS/Linux:
# source .venv/bin/activate

import streamlit as st

# Lista de páginas
paginas = ['Inicio', 'Experiencia', 'Gráficos']

# Sidebar con solo UNA cajita
st.sidebar.title("Navegación")
pagina_seleccionada = st.sidebar.selectbox(
    'Selecciona la sección que deseas ver',
    paginas
)

# Condicionales para cada página
if pagina_seleccionada == 'Inicio':
    st.title("Página de inicio")
    st.write("Bienvenidos a mi PC4 con Streamlit.")

elif pagina_seleccionada == 'Experiencia':
    st.title("Mi experiencia")
    st.write("Aquí escribo mi experiencia aprendiendo a programar.")

elif pagina_seleccionada == 'Gráficos':
    st.title("Gráficos")
    st.write("Aquí irán mis gráficos.")


if pagina_seleccionada == 'Inicio':

    st.markdown("<h1 style='text-align: center;'>Corazón Delator</h1>", unsafe_allow_html=True)

    # columnas para imagen + texto
    col1, col2 = st.columns(2)

    # IMAGEN DE PERFIL
    col1.image("yo.jpeg", caption='Alejandra Hernández Rossi', width=300)

    # TEXTO PERSONAL
    texto = """
¡Hola! Soy Alejandra Hernández Rossi, limeña y estudiante de periodismo de cuarto ciclo en la PUCP. 
El periodismo es una carrera que me gustó desde que estaba en tercero de secundaria porque creo que le brinda 
a la sociedad la proximidad a la verdad. Además, siempre me ha gustado mucho hablar, hacer crítica literaria 
y escribir. Así, participo en espacios de feminismo y literatura donde he encontrado a mis autores favoritos 
como Isabel Allende o Benito Taibo. Por ello, en el futuro quisiera dedicarme al periodismo literario o de 
crítica literaria, que también podría encaminarme a realizar análisis de series o películas que me gusta mucho 
ver en mi tiempo libre como Gilmore Girls.
"""

    # Mostrar texto
    col2.markdown(
        f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>",
        unsafe_allow_html=True
    )

    # CADENA DE 3 FOTOS
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("ISABEL.jpg", caption="Isabel Allende", width=200)

    with col2:
        st.image("BENITO.jpg", caption="Benito Taibo", width=200)

    with col3:
        st.image("GILMORE GIRLS.jpg", caption="Gilmore Girls", width=200)
elif pagina_seleccionada == 'Experiencia':
    st.markdown("<h1 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h1>", unsafe_allow_html=True)

    texto_2 = """
Al principio sentí mucho miedo porque nunca había experimentado con Python ni con nada parecido. 
Siempre me había parecido complicado y estuve a punto de no llevar el curso. 
Con el pasar de los meses, cada PC me ha aterraba un poco, pero también siento que he puesto muchísimo 
esfuerzo y compromiso. Esto me ha enseñado a ser dedicada, constante y muy paciente conmigo misma.
Lo más bonito ha sido descubrir que estos conocimientos pueden acompañarme en otras áreas de mi vida, 
por ejemplo para crear una página web sobre mi red feminista o un espacio literario donde pueda escribir, 
recomendar libros o hablar de mis autoras favoritas.
Además, me he sorprendido encontrando temas que realmente me gustan, como los bucles o el uso de funciones. 
Nunca imaginé que algo de programación pudiera parecerme tan interesante. Me he divertido aprendiendo 
lo que puedo construir con unas cuantas líneas de código, y eso me motiva a seguir explorando más.
"""
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2}</div>", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center;'>Datos booleanos en Python: Guía básica de una principiante</h2>", unsafe_allow_html=True)

    # Video de YouTube
    st.video("https://www.youtube.com/watch?v=NSCt81lq2es")

elif pagina_seleccionada == 'Gráficos':
    st.markdown("<h1 style='text-align: center;'>Mis primeros gráficos</h1>", unsafe_allow_html=True)

    # Lista de gráficos
    graficos = [
        'Histogramas de goles anotados y recibidos por el Bayern Munich en GE1 2023-2024',
        'Gráfico de barras de tarjetas rojas recibidas por los equipos en el GE1 2023-2024',
        'Pie Chart resultados del Dortmund como visitante en la GE1 2023-2024',
        'Mapa mis películas'
    ]

    # Selección de gráfico
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    # Mostrar gráfico según selección
    if grafico_seleccionado == 'Histogramas de goles anotados y recibidos por el Bayern Munich en GE1 2023-2024':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>Aquí debe ir una breve interpretación de tu gráfico</div>", unsafe_allow_html=True)
        st.image("HISTOGRAMASBAYERN.png", caption='Histogramas de goles anotados y recibidos por el Bayern Munich en GE1 2023-2024', width=500)

    elif grafico_seleccionado == 'Gráfico de barras de tarjetas rojas recibidas por los equipos en el GE1 2023-2024':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>Aquí debe ir una breve interpretación de tu gráfico</div>", unsafe_allow_html=True)
        st.image("tarjetas rojas.png", caption='Gráfico de barras de tarjetas rojas recibidas por los equipos en el GE1 2023-2024', width=500)

    elif grafico_seleccionado == 'Pie Chart resultados del Dortmund como visitante en la GE1 2023-2024':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>Aquí debe ir una breve interpretación de tu gráfico</div>", unsafe_allow_html=True)
        st.image("resultados visitantes.png", caption='Pie Chart resultados del Dortmund como visitante en la GE1 2023-2024', width=500)

    elif grafico_seleccionado == 'Mapa mis películas':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>Aquí debe ir una breve interpretación de tu mapa</div>", unsafe_allow_html=True)
        # Mostrar HTML con components
        import streamlit.components.v1 as components
        with open("mapa_peliculas.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=500)
