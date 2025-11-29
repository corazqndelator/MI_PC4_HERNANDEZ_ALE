

# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.

# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.

# Luego activamos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# deactivate
# En MacOS/Linux:
# source .venv/bin/activate

import streamlit as st #Abrimos la biblioteca streamlit y le colocamos asst para no tener que poner el nombre completo al usar las funciones

# hacemos una lista de las tres páginas que debemos utilizar: inicio, gráficos y experiencia
paginas = ['Inicio', 'Experiencia', 'Visualizaciones']

#añadimos un side bar para que el usuario pueda abrir la pagina que desee
st.sidebar.title("Navegación")
pagina_seleccionada = st.sidebar.selectbox( #esta página va a ser un select box, es ecir, habrá una caja con las opciones y uno debe clickear para desplegar y poder entrar a otra sección
    'Selecciona la sección que deseas ver', #añadimos este texto para que el usuario sepa que debe abrir alguna sección
    paginas
) #solo va a poder las páginas de la lista y una de ellas a la vez, esta abierta será pagina seleccionada

# hacemos las condicionales para cada página que se elija
if pagina_seleccionada == 'Inicio': #empezamos con inicio. cuando se abra esta página se mostrará:
    #st.title("Página de inicio")
    #st.write("Bienvenidos a mi PC4 con Streamlit.")

    st.markdown("<h1 style='text-align: center;'>Corazón Delator ♡</h1>", unsafe_allow_html=True) #ahora lo que hacemos es añadir el nombre del blog que es corazón delator pq es el user de mi ig 

        # ahora creamos columnas para imagen + texto
    col1, col2 = st.columns(2)

        # lo primero que hago esponer mi foto DE PERFIL añadiendola como aparece guardada en mi carpeta y con una descripción abajo de lo que refleja la foto
    col1.image("yo.jpeg", caption='Alejandra Hernández Rossi', width=300)

        # ahora entre tres comillas añado mi texto de presentación
    texto = """
    ¡Hola! Soy Alejandra Hernández Rossi, limeña y estudiante de periodismo de cuarto ciclo en la PUCP. 
    El periodismo es una carrera que me gustó desde que estaba en tercero de secundaria porque creo que le brinda 
    a la sociedad la proximidad a la verdad. Además, siempre me ha gustado mucho hablar, hacer crítica literaria 
    y escribir. Así, participo en espacios de feminismo y literatura donde he encontrado a mis autores favoritos 
    como Isabel Allende o Benito Taibo. Por ello, en el futuro quisiera dedicarme al periodismo literario o de 
    crítica literaria, que también podría encaminarme a realizar análisis de series o películas que me gusta mucho 
    ver en mi tiempo libre como Gilmore Girls.
    """

        #luego voy a mostrar el texto
    col2.markdown(
            f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>",
            unsafe_allow_html=True
        )

        #ahora hago una cadena de tres fotos con columnas para mostrar las fotos de mis escritores favoritos y mi serie favorita
    col3, col4, col5 = st.columns(3)
    #uso with porque me dijo google que debía ponerlo así para separar las columnas y que cada foto esté en su respectiva parte
    with col3:
            st.image("ISABEL.jpg", caption="Isabel Allende", width=200)

    with col4:
            st.image("BENITO.jpg", caption="Benito Taibo", width=200)
    #repito el proceso con col1, 2 y 3 añadiendo las fotos como aparecen en mi carpeta y una descripción debajp
    with col5:
            st.image("GILMORE GIRLS.jpg", caption="Gilmore Girls", width=200)
    

elif pagina_seleccionada == 'Experiencia': #si se abre mi experiencia se mostrará:
    #st.title("Mi experiencia")
    #st.write("Aquí escribo mi experiencia aprendiendo a programar.")
    st.markdown("<h1 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h1>", unsafe_allow_html=True)

    #añado un segundo texto donde cuento mi experiencia programando
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
#lo justifico y alineo
    st.markdown("<h2 style='text-align: center;'>Datos booleanos en Python: Guía básica de una principiante</h2>", unsafe_allow_html=True)

    # ahora agrego el video de YouTube que hice para la pc1 de datos booleanos, como está puúblico en youtube nada más copio el link
    st.video("https://www.youtube.com/watch?v=NSCt81lq2es")

elif pagina_seleccionada == 'Visualizaciones': # y si se quiere abrir gráficos se va a mostrar el output de ese texto
    #st.title("Visualizaciones")
    #st.write("Aquí irán mis gráficos.")
    st.markdown("<h1 style='text-align: center;'>Mis primeros gráficos</h1>", unsafe_allow_html=True)

    # hago una lista de gráficos con sus nombres respectivos
    graficos = [
        'Histogramas de goles anotados y recibidos por el Bayern Munich en GE1 2023-2024',
        'Gráfico de barras de tarjetas rojas recibidas por los equipos en el GE1 2023-2024',
        'Pie Chart resultados del Dortmund como visitante en la GE1 2023-2024',
        'Mapa mis películas'
    ]

    # ahora hago otra barra de selectbox donde se puede elegir que gráfico se quiere ver de la lista
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    # y ahora con condicionales muestro gráfico según selección, si se escoge el histograma, se ve la imagen del histograma con su descripción y análisis
    if grafico_seleccionado == 'Histogramas de goles anotados y recibidos por el Bayern Munich en GE1 2023-2024':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>Este gráfico fue realizado para la primera parte de la PC3. En esta tuve que analizar los datos obtenidos a partir de la primera división alemana, es decir, la Bundesliga 2023-2024. En los gráficos se analiza los goles que recibió el Bayern Munich en esta temporada como local y visitante, mostrando que como visitante recibió más goles (hasta 6). Por otro lado, en cuanto a los goles anotados, también se analiza cuantos realizaron en cada categoría, resultando que como locales anotaron muchos más (hasta 8).</div>", unsafe_allow_html=True)
        st.image("HISTOGRAMASBAYERN.png", caption='Histogramas de goles anotados y recibidos por el Bayern Munich en GE1 2023-2024', width=500)
#si se escoge el gráfico de barras, entonces se muestran las barras y su análisis
    elif grafico_seleccionado == 'Gráfico de barras de tarjetas rojas recibidas por los equipos en el GE1 2023-2024':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>Este gráfico también pertenece al análisisde datos dela Bundesliga 2023-2024. En las barras, podemos observar cuantas tarjetas rojas recibieron en promedio los equipos jugando como local. En el gráfico, vemos que el equipo que recibió más fue Freiburg con un promedio de 0.25. Por su parte, Leverkusen, M´gladbach, RB Leizpig y Stuttgart no recibieron tarjetas rojas en toda la temporada.</div>", unsafe_allow_html=True)
        st.image("tarjetas rojas.png", caption='Gráfico de barras de tarjetas rojas recibidas por los equipos en el GE1 2023-2024', width=500)
#exactamente lo mismo si se elige el pie chart ya que las tres son imagenes en png
    elif grafico_seleccionado == 'Pie Chart resultados del Dortmund como visitante en la GE1 2023-2024':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>Este gráfico analiza los partidos ganados, perdidos y empatados por el Dortmund como equipo visitante en la Bundesliga 2023-2024. En este pie chart, se puede observar que como visitante, el Dortmund ganó muchos más partidos (47.1% ganados) de los que perdió (17.6% perdidos) o empató (35.3% empatados). Ello, muestra que la temporada para el Dortmund jugando como visitante fue bastante exitosa.</div>", unsafe_allow_html=True)
        st.image("resultados visitantes.png", caption='Pie Chart resultados del Dortmund como visitante en la GE1 2023-2024', width=500)
#ahora con el mapa si es distinto porque está en un html y por eso debemos importar de streamlit los componentes de html y así poder agregar el mapa. hago una descripción y análisis que queda como texto
    elif grafico_seleccionado == 'Mapa mis películas':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>Este mapa refleja donde fueron grabadas mis 5 películas favoritas: Don´t Worry Darling, Cruella de Vil Live Action, Tick Tick Boom, Madeinusa y The Intern. El mapa, muestra que la mayoría de mis favoritas fueron grabadas en Estados Unidos (Tick Tick Boom y The Intern en New York, Don´t Worry Darling en los Ángeles). Por su parte, Cruella de Vil fue grabada en Londres, por eso la estética de la película es mucho más clásica. Por último, Madeinusa es una película nacional grabada en Áncash.</div>", unsafe_allow_html=True)
        # Mostrar HTML con components
        import streamlit.components.v1 as components
        with open("mapa_peliculas.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=500)
#fin