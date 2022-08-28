## **Martín Cogo Belver**

# Preguntas del AIMA

## 2.10 Considere una version modificada del entorno de la aspiradora , en el cual el agente es penalizado un punto por cada movimiento.

1. ¿Puede un agente reflexivo simple ser perfectamente racional para este entorno?

>En este caso no puede ser racional debido a que no maximiza la función de rendimiento. La aspiradora necesita moverse y no para poder detectar la tierra y limpiarla.

2. ¿Qué tal un agente reflexivo con estados? Diseñe el agente.
> En el caso de un Agente basado en modelos con estados internos, podría maximizar los movimientos fuera de los lugares por los que ya ha pasado, y evitar transitar nuevamente por los mismos. Por lo tanto, podría ser racional.

El Agente comenzaría a construir un mapa por los lugares donde ha pasado y a la hora de tomar decisiones evitaría pasar por un lugar repetido a menos que sea necesario. 

3. ¿Cómo contestaría la pregunta 1 y 2 si la percepción del agente devolviera limpio/sucio en cada cuadro del entorno? 

> En el caso de que todo el entorno sea observable, el agente reflexivo simple podría dirigirse a la tierra directamente, minimizando los cuadros hasta llegar a la suciedad.

> El agente basado en modelos tendría un rendimiento similar al simplemente reflexivo.

## 2.11 Considere una versión modificada el entorno de la aspiradora, en el cual tanto la extensión, los limites y los obstáculos fueran desconocidos igual que la localización de la tierra. (El agente tiene los mismos movimientos).
1. ¿Puede un agente reflexivo simple perfectamente ser racional en este entorno?

> En este caso el Agente reflexivo simple puede ser racional ya que maximiza la función de rendimiento, pero el rendimiento sería menor que la que se tienen en el entorno con limites definidos y sin obstáculos.

2. ¿Puede un agente reflexivo simple con un comportamiento aleatorio superar a un agente reflexivo simple?

> No debido a que este no maximizaría la función de desempeño debido a que aspiraría en lugares donde no es necesario y esto desperdiciaría tiempo y movimientos. 

3. ¿Puede diseñar un entorno donde un agente de comportamiento aleatorio rinda apropiadamente?  

> No hay ningún entorno donde el Agente reflexivo simple con comportamiento aleatorio tenga un comportamiento racional.

4. ¿Puede un agente reflexivo con estados superar a un agente reflexivo simple? (Diseñe tal agente y mida su rendimiento en varios entornos. ¿Puede diseñar un agente racional de este tipo?

> El agente reflexivo con estados puede superar al agente reflexivo simple, debido a que puede guardar estados que permitan detectar obstáculos y límites del entorno minimizando las colisiones y permitiendo un mejor desempeño.
