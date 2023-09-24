# Manual Técnico - Aplicación Numérica con Análisis Léxico 

El Programa de Análisis de JSON es una aplicación que permite cargar, analizar y generar informes gráficos basados en archivos JSON que contienen operaciones aritméticas y trigonométricas.


## Arquitectura del Sistema

El sistema se basa en una arquitectura cliente-servidor donde el cliente es la interfaz de usuario (UI) creada con tkinter y el servidor es el módulo analizador (Analizador.py). La interfaz de usuario interactúa con el módulo analizador para cargar archivos JSON, iniciar análisis y generar informes gráficos.

## Componentes del Programa
El programa se compone de varios módulos que trabajan juntos para realizar sus funciones principales.

### Interfaz de Usuario (UI)

-   Desarrollada utilizando la biblioteca tkinter de Python.
-   Proporciona una ventana de aplicación con un área de texto y un menú.
-   Permite abrir, guardar y analizar archivos JSON, así como generar informes gráficos.

### Módulo Analizador (Analizador.py)

-   Encargado de analizar el contenido JSON y generar resultados.
-   Convierte el contenido JSON en una estructura de datos interpretable.
-   Detecta errores y los informa a través de ventanas emergentes.
-   Proporciona funciones para el análisis de expresiones aritméticas y trigonométricas.
### Módulo de Expresiones Aritméticas (Expresiones.aritmeticas)

-   Define una clase para representar y evaluar expresiones aritméticas.
-   Admite operadores como suma, resta, multiplicación y división.
-   Realiza cálculos aritméticos con valores numéricos.

### Módulo de Expresiones Trigonométricas (Expresiones.trigonometricas)

-   Define una clase para representar y evaluar expresiones trigonométricas.
-   Admite funciones trigonométricas como seno, coseno, tangente e inverso.
-   Realiza cálculos trigonométricos con valores numéricos.
### Módulo de Gráficas (Graficas.Arbol)

-   Proporciona funcionalidad para generar informes gráficos basados en datos.
-   Utiliza Graphviz para crear visualizaciones de árboles.
-   Personaliza la apariencia de las gráficas según las configuraciones proporcionadas.

## Requisitos del Sistema
-   Python 3.x instalado en el sistema.
-   Bibliotecas de Python requeridas como tkinter, Graphviz, etc.
-   Archivos JSON que contienen las operaciones a analizar.

## Instalación y Ejecución

1.  Asegúrate de tener Python 3.x instalado en tu sistema.
2.  Instala las bibliotecas requeridas si aún no están instaladas (puedes usar `pip`).
3.  Ejecuta el script `Proyecto1.py` para iniciar la aplicación.


## Información para futuros Desarrolladores

Si se desea modificar o extender el programa, aquí hay algunas pautas generales:

-   Puedes agregar nuevas funcionalidades a través de la expansión de los módulos existentes o creando nuevos módulos.
-   Asegúrate de seguir las convenciones de estilo de Python y mantener un código limpio y legible.
-   Documenta tu código adecuadamente para facilitar su comprensión y mantenimiento.
-   Puedes personalizar la interfaz de usuario y las opciones de configuración según tus necesidades.