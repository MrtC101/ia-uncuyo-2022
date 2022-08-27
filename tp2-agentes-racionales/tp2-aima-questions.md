## **Martín Cogo Belver**

# Preguntas del AIMA

## 2.10 Considere una version modificada del entorno de la aspiradora , en el cual el agente es penalizado un punto por cada movimiento.

1. ¿Puede un agente reflexivo simple ser perfectamente rational para este entorno?

>En este caso no, puede ser racional debido a que no maximiza la función de rendimiento. La aspiradora nesesita moverse y no para poder detectar la tierra y limpiarla.

2. ¿Que tal un agente reflexivo con estados? Diseñe el agente.
> En el caso de un Agente basado en modelos con estados internos, podría maximizar los movimientos fuera de los lugares por los que ya ha pasado. Por lo tanto podría ser racional.

3. ¿Como contestaria la pregunta 1 y 2 si la persepción del agente devolviera limpio/sucio en cada cuadro del entorno? 
> En el caso de que todo el entorno sea observable, el agente reflexivo simple podría dirigirse a la tierra directamente, minimizando los cuadros hasta llegar a la suciedad.
> El gente basado en modelos tendría un rendimiento similar al simplemente reflexivo.

## 2.11 Considere una version midificada el entrono de la aspiradora, en el cual tanto la extension, los limites y los obstaculos fueran desconocidos como la localización de la tierra.(El agente tiene las mismos movimientos).
1. ¿Puede un agente reflexivo simple prefectamente ser racional en este entorno?
> En este caso el Agente reflexivo simple podría tener una logíca que detecte colisiones, de tal manera que cambie la dirección de los desplazamientos.Aún así podrían haber varias colisiones.
2. ¿Puede un agente reflexivo simple con un comportamiento aleatorio superar a un agente reflexivo simple?
> En este caso Tendría un rendimiento peor que el agente reflexivo simple.Tendría muchas probabilidades de chocar con obstaculos o limites del entorno más de una vez. Esto generaria un desperdicio de movimientos y evitaría maximizar la funcion de rendimiento por lo que no sería un agente racional.
3. ¿Puede diseñar un entorno donde un agente de comportamiento aleatorio rinda apropiadamente?  

> El agente reflexivo simple con comportamiento aleatorio podría rendir más apropiadamente si el entrono tiene los obstaculos, y limites definidos y son conocidos por el agente.
4. ¿Puede un agente reflexivo con estados superar a un agente reflexivo simple?(diseñe tal agente y mida su rendimiento en varios entornos. ¿Puede diseñar un agente racional de este tipo?

> El agente reflexivo basado en modelos puede superar al agente reflexivo simple, debido a que puede guardar estados que permitan detectar obstaculos y limites del entorno minimizando las colisiones y permitiendo un mejor desempeño.
