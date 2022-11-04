# Generación de reglas de asociación espaciales con bloques de Minecraft #

## Código RANDOBJGEN ##

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

## Bibliografía ##

[Clasificación de objetos mediante momentos de
Hahn 3D y aprendizaje profundo](https://rcs.cic.ipn.mx/2020_149_8/Clasificacion%20de%20objetos%20mediante%20momentos%20de%20Hahn%203D%20y%20aprendizaje%20profundo.pdf)

[DISEÑO DE ALGORITMO DE GENERACIÓN
PROCEDURAL ENFOCADO A VIDEOJUEGOS](https://repositorio.usm.cl/bitstream/handle/11673/49444/3560902038911UTFSM.pdf?sequence=1&isAllowed=y)
(https://www.alanzucconi.com/2022/06/05/minecraft-world-generation/)
(https://www.youtube.com/watch?v=fpGsOdxcU2M&ab_channel=ParametricCamp)
(https://unmined.net)
(https://www.reddit.com/r/VoxelGameDev/comments/8c4a67/a_better_way_to_extract_minecraft_data/)
(https://pessimistress.github.io/minecraft/)
(https://github.com/Pessimistress/minecraft-chunk-viewer)
(https://minecraft.fandom.com/wiki/Region_file_format)
(https://wiki.vg/Region_Files)
(https://minecraft.fandom.com/es/wiki/Formato_NBT)
(https://github.com/mstefarov/fNbt)
[Spacial association rules](https://link.springer.com/chapter/10.1007/3-540-60159-7_4)
[Presentaicon Spacial associatuib ryeks](https://www.ismll.uni-hildesheim.de/lehre/spatial-09w/script/association_web.pdf)
["Algoritmo ESPADA implementado en Prolog para inferencia de spatial association rules"](https://edz.bib.uni-mannheim.de/www-edz/pdf/eurostat/02/KS-CS-02-001-EN-N-EN.pdf#page=26)
["Metricas para reglas de associacion"](https://towardsdatascience.com/association-rules-2-aa9a77241654)
["Apriori en R"](https://www.geeksforgeeks.org/association-rule-mining-in-r-programming/#:~:text=Association%20Rule%20Mining%20in%20R%20Language%20is%20an%20Unsupervised%20Non,in%20a%20transaction%20or%20relation.)