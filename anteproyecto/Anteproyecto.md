# Mineria de reglas reglas de asociación espaciales sobre bloques de Minecraft #

## Código MINECRAFT_ASSO_MINING ##

***Martín Cogo Belver***

## Proyecto ##

La idea de este proyecto **era** crear un algoritmo de generación procedural de objetos dentro de un espacio bidimensional o tridimensional. Debido a la cantidad de trabajo y tiempo que requeriría un proyecto de esa magnitud, el proyecto se enfocara en una parte de esta idea anterior.

Este proyecto se enfocara en la prueba de un algoritmo para inferencia de reglas de asociación espaciales entre objetos dentro de un escenario.En este caso particular, el escenario es un Terreno de Minecraft. Se buscara que las reglas de asociación ilustren los patrones que existen entre los bloques.

Concretamente se realizaran las pruebas con un mundo generado de manera procedural del videojuego Minecraft. Para la extracción de la información de los bloques del Juego se utilizara la biblioteca Anvil para Python. Como algoritmo para la inferencia de reglas se utilizara
para la generación de Feature se utlilizara una implementación en R o Python.

El algoritmo de inferencia de reglas de associacion a utilizar sera SPADA implementado en Prolog.

## Objetivos ##  

1. Decidir un escenario con objetos determinado, que permita la fácil extracción de datos necesarios para la creación de las reglas de asociación.  [1/2 día]

2. Buscar una manera de extraer los datos de los diferentes entornos para construir la representación abstracta.  [ 1/4 día]

3. Encontrar un algoritmo de creación de reglas de asociación que se adecué a este tipo de problemas.[5 días]

4. Implementación del algoritmo [10 días]

5. Buscar una manera de la fácil presentación de las reglas generadas.(realizar una traducción de ellas)[3 días]

## Alcance y limitaciones ##

+ Para este proyecto se quiere evitar entrar en problemas de computer vision para la extracción de los datos de entornos.

+ También. de ser posible, se quiere evitar la necesidad de generación manual de datos para la resolución del problema.  

## Métricas ##

## Justificación ##

Actualmente existen varios algoritmos que permiten la generación procedural de posicionamiento de objetos dentro de un  entorno. Pero estos utilizan restricciones declaradas por el programador. Encontrar y declarar estas restricciones presenta una tarea compleja y esto no permite que el posicionamiento de los objetos dentro del escenario tengan mucha libertad o variación.  

Por ello la idea del proyecto sería encontrar una manera de automatizar la generación de restricciones que utilizaría un algoritmo de generación procedural para el posicionamiento de los objetos dentro del escenario.

De ahí que sea necesario la utilización de un algoritmo de machine learning para la deducción de estas reglas. Ya que los escenarios contienen datos que pueden ser utilizados para la deducción de la relación espacial que existe entre los objetos que estos contienen.  

## Listado de actividades a realizar: ##

1. Elegir el problema. Minecraft chunk
2. Extract Minecraft chunk Data
3. Investigar sobre la extraccion de los datos Minecraft (4 días)
4. Creacion de un dataset de chuncks
5. eleccion de algoritmo de inferencia de reglas.
6. Vizualizador de reglas.

## Cronograma estimado de actividades ##

1. b