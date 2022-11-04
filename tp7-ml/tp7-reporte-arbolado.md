
# Estrategia para desafió kaggle #

## Preprocesamiento ## 

Se elimino la columna de fecha de modificación, se transformaron todas las columnas restantes con factor y se dejo como double la columna de latitud y longitud.

No se crearon nuevas columnas
No se normalizaron valores

Los Resultados obtenidos en kaggle se encuentran entre 0.43 y 0.68

El algoritmo utlizado primero importa los dataset de entrenamiento y de prueba.
Realiza las modificaciones en ambos dataset tranformado las columnas con factor.
Separa una parte del dataset de entrenamiento para utilizar como validacion.
Se crea utiliza una funcion para calcular pesos de las clases en funcion de una diferencia porcentual dada como parametro.

La diferencia porcentual entre el peso total de la clase de arboles peligrosos con respecto a la de arboles no peligrosos es del 50%.

Se utliza la funcion train de caret para entrenar el modelo utilizando el algoritmo de random forest.
Ademas se realiza con k-crossvalidation utilizando 3 folds y realizando para cada seleccion de fold de validacion 3 repeticiones.

Luego se valida el modelo resultante con el conjunto de validacion

si el porcentaje de eficiencia es mayor a 0.68 entonces se evalua el conjunto de test brindado por kaggle y se genera el resultado en csv para enviar.