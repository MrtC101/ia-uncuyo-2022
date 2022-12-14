
# Inteligencia Artificial 1

## Martín Cogo Belver

## Trabajo Practico 6 : CSP

## 1. Describir en detalle una formulación CSP para el SUDOKU

### Planteamiento

+ Estado inicial : $\{\}$  
+ Función Sucesor: Se asigna a un valor a la proxima variable con menor cantidad de variables legales y mayor grado de restricciones (si se detecta inconsistencia se utiliza backtracking).  
+ Estado objetivo: La asignación de todas las casillas de manera consistente.
+ Costo de camino: consto constante para cada elección.
+ Para representar el tablero de Sudoku se puede utilizar una matriz de 9 por 9.  

En este caso entonces se puede interpretar como un problema que se resuelve como un CSP donde:  
Las variables son cada casilla del tablero:  
$$\{X_{00},X_{01},X_{02},X_{03},X_{04},...,X_{10},X_{11},...,X_{88}\}$$ 
Para cada variable el dominio es de los números naturales del 1 al 9 por Ej:
$$D_{00}=\{1,2,3,4,5,6,7,8,9\}$$
Existen un conjunto finito de restricciones:
$$\{C_1,C_2,C_3\}$$

### Las restricciones son  

+ $C_1$: Las variables en cada columna de la tabla no deben repetir ningún valor.
+ $C2$: Las variables en cada fila de la tabla no deben repetir ningún valor.
+ $C3$: Las variables en las 9 tablas cuadradas de 3 por 3 interiores no deben repetir ningún valor.

El tablero comienza con variables ya inicializadas que no violan ninguna restricción y estas no son modificables. Por lo que el dominio de la mayoría de las variables se ve restringido al comienzo del problema.

Cada asignación en la matriz nos genera un grafo de restricciones.

### Por ejemplo la asignación de la variable $X_{42}$ nos genera el siguiente grafo de restricciones

![Grafo](./images/Grafo.png)
![Referencias](./images/ReferenciasGrafo.png)

### En la tabla se estarían influenciadas las siguientes variables

!["cuadriculaSudoku"][cuadricula]

Para solucionar este problema CSP se utilizara un algoritmo basado en **Backtracking** y **heurísticas** como:

+ La heurística de **Minimum Remaining Values (MRV)** para elegir variables con menor cantidad de valores legales restantes primero.
+ También se utiliza la **Heurística de Grado** para poder determinar las casillas con mayor grado de restricción y de esta manera se rellenarían las casillas más restringidas primero.

## 2. Utilizar el algoritmo AC-3 para demostrar que la arco consistencia puede detectar la inconsistencia de la asignación parcial {WA=red, V=blue} para el problema del colorar el mapa de Australia  

### Demostración

Hipótesis:  
$P :=$ La arco consistencia puede detectar Inconsistencias de Arco.  
Tesis:  
$Q :=$ La asignación $X=\{WA=Rojo, V=Azul\}$ para el problema del coloreado de mapa de Australia con tres colores no es arco consistente.

Se busca demostrar que $P\implies Q$.

El problema de coloreado del mapa de Australia se puede interpretar como un CSP. Entonces, para la demostración, utilizaremos el algoritmo **AC-3** que utiliza la heurística inconsistencia de arco para detectar asignaciones incorrectas en las variables de un problema CSP.

!["AC-3 Code"][AC-3]

El Algoritmo AC-3 recibe como entrada una tupla de tres conjuntos $(X,D,C)$. $X$ es el conjunto de Variables, $D$ es el conjunto de dominios de Cada Variable, y $C$ es el conjunto de restricciones del problema.

En el caso particular del problema de Pintar el Mapa de Australia con tres colores, estas variables se pueden definir los conjuntos como:  

!["Mapa de Australia y Grafo"](./images/MapaAustralia.png)  

El Conjunto de variables:
$$X = \{WA,NT,SA,Q,NSW,V,T\}$$
El Dominio de cada variable es igual para todas:
$$D_n = \{Rojo,Azul,Amarillo\}$$
El Conjunto de Restricciones:
$$C=\{C_1\}$$
Donde la restricción es:

+ $C_1$: No pueden pintarse dos nodos adyacentes del mismo color.

Para la demostración *AC-3* recibirá en la tupla de entrada el conjunto $X=\{WA=Rojo, V=Azul\}$ donde las demás variables se encuentran no inicializadas (sin color).
Para representar el Dominio utilizaremos un arreglo donde se ven los colores de cada Dominio.

### Prueba de escritorio  (Se realizan 30 iteraciones)

1. Se inicializa la cola con los arcos  
$[(WA,NT),(NT,WA),(WA,SA),(SA,WA),(NT,SA),(SA,NT),(NT,Q),$
$(Q,NT),(SA,Q),(Q,SA),(SA,NSW),(NSW,SA),(SA,V),(V,SA),$
$(Q,NSW),(NSW,Q),(NSW,V),(V,NSW)]$  
2. Como la cola no esta Vacía itera  

Tabla de Dominios:

![Dom_it0](./images/Dominio_it0.png)  

3. iteración #1:  
3.1- La cola devuelve $(WA,NT)$ y la cola queda:  
$[(NT,WA),(WA,SA),(SA,WA),(NT,SA),(SA,NT),(NT,Q),$
$(Q,NT),(SA,Q),(Q,SA),(SA,NSW),(NSW,SA),(SA,V),(V,SA),$
$(Q,NSW),(NSW,Q),(NSW,V),(V,NSW)]$  
3.2- Se ingresa al método **Revise()**  
3.3- Por cada color $x$ en $D_{WA}$ comprueba que para todo color $y$ en $D_{NT}$ permita la asignación $(x,y)$.(Como $WA=Rojo$ se revisará solo $x=Rojo$ con los tres colores de y)  
3.4- La salida de **Revise()** retorna Falso  

4. iteración #2:  
4.1- La cola devuelve $(NT,WA)$ y la cola queda:  
$[(WA,SA),(SA,WA),(NT,SA),(SA,NT),(NT,Q),(Q,NT),(SA,Q),$
$(Q,SA),(SA,NSW),(NSW,SA),(SA,V),(V,SA),(Q,NSW),$
$(NSW,Q),(NSW,V),(V,NSW)]$  
4.2- Se ingresa al método **Revise()**  
4.3- Por cada color $x$ en $D_{NT}$ comprueba que para todo color $y$ en $D_{WA}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
4.4- La salida de **Revise()** retorna Verdadero y se elimina $\textcolor{red}{Rojo}$ del dominio $D_{NT}$.  
6.5- Verifica que tamaño de $D_{NT}\neq0$  
6.6- Por cada Variable $X_k$ en $X_{NT}.NEIGHBORS-\{X_{WA}\}$ se añade $(X_k,X_{NT})$ a la cola. Se añade  
$[(WA,SA),(SA,WA),(NT,SA),(SA,NT),(NT,Q),(Q,NT),(SA,Q),$
$(Q,SA),(SA,NSW),(NSW,SA),(SA,V),(V,SA),(Q,NSW),$
$(NSW,Q),(NSW,V),(V,NSW),\textcolor{LimeGreen}{(SA,NT),(Q,NT)}]$  

![Dom_2](./images/Dominio_it2.png)

5. iteración #3:  
5.1- La cola devuelve $(WA,SA)$ y la cola queda:  
$[(SA,WA),(NT,SA),(SA,NT),(NT,Q),(Q,NT),(SA,Q),$
$(Q,SA),(SA,NSW),(NSW,SA),(SA,V),(V,SA),(Q,NSW),$
$(NSW,Q),(NSW,V),(V,NSW),(SA,NT),(Q,NT)]$  
5.2- Se ingresa al método **Revise()**  
5.3- Por cada color $x$ en $D_{WA}$ comprueba que para todo color $y$ en $D_{SA}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
5.4- La salida de **Revise()** retorna Falso


6. iteración #4:  
6.1- La cola devuelve $(SA,WA)$ y la cola queda:  
$[(NT,SA),(SA,NT),(NT,Q),(Q,NT),(SA,Q),(Q,SA),$
$(SA,NSW),(NSW,SA),(SA,V),(V,SA),(Q,NSW),$
$(NSW,Q),(NSW,V),(V,NSW),(SA,NT),(Q,NT)]$  
6.2- Se ingresa al método **Revise()**  
6.3- Por cada color $x$ en $D_{SA}$ comprueba que para todo color $y$ en $D_{WA}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
6.4- La salida de **Revise()** retorna Verdadero y se elimina $\textcolor{red}{Rojo}$ del dominio $D_{SA}$.  
6.5- Verifica que tamaño de $D_{SA}\neq0$  
6.6- Por cada Variable $X_k$ en $X_{SA}.NEIGHBORS-\{X_{WA}\}$ se añade $(X_k,X_{SA})$ a la cola. Se añade  
$[(NT,SA),(SA,NT),(NT,Q),(Q,NT),(SA,Q),(Q,SA),(SA,NSW),$
$(NSW,SA),(SA,V),(V,SA),(Q,NSW),(NSW,Q),(NSW,V),$
$(V,NSW),(SA,NT),(Q,NT),\textcolor{LimeGreen}{(NT,SA),(Q,SA),(NSW,SA),(V,SA)}]$  

Tabla de Dominio:

![Dom_4](./images/Dominio_it4.png)

7. iteración #4:  
7.1- La cola devuelve $(NT,SA)$ y la cola queda:  
$[(SA,NT),(NT,Q),(Q,NT),(SA,Q),(Q,SA),(SA,NSW),$
$(NSW,SA),(SA,V),(V,SA),(Q,NSW),(NSW,Q),(NSW,V),$
$(V,NSW),(SA,NT),(Q,NT),(NT,SA),(Q,SA),(NSW,SA),(V,SA)]$  
7.2- Se ingresa al método **Revise()**  
7.3- Por cada color $x$ en $D_{NT}$ comprueba que para todo color $y$ en $D_{SA}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
7.4- La salida de **Revise()** retorna Falso.

8. iteración #5:  
8.1- La cola devuelve $(SA,NT)$ y la cola queda:  
$[(NT,Q),(Q,NT),(SA,Q),(Q,SA),(SA,NSW),(NSW,SA),$
$(SA,V),(V,SA),(Q,NSW),(NSW,Q),(NSW,V),(V,NSW),(SA,NT),$
$(Q,NT),(NT,SA),(Q,SA),(NSW,SA),(V,SA)]$  
8.2- Se ingresa al método **Revise()**  
8.3- Por cada color $x$ en $D_{SA}$ comprueba que para todo color $y$ en $D_{NT}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
8.4- La salida de **Revise()** retorna Falso.

9. iteración #6:  
9.1- La cola devuelve $(NT,Q)$ y la cola queda:  
$[(Q,NT),(SA,Q),(Q,SA),(SA,NSW),(NSW,SA),(SA,V),$
$(V,SA),(Q,NSW),(NSW,Q),(NSW,V),(V,NSW),(NT,SA),$
$(Q,SA),(NSW,SA),(V,SA),(WA,NT),(NT,Q)]$  
9.2- Se ingresa al método **Revise()**  
9.3- Por cada color $x$ en $D_{NT}$ comprueba que para todo color $y$ en $D_{Q}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
9.4- La salida de **Revise()** retorna Falso.  

10. iteración #7:  
10.1- La cola devuelve $(Q,NT)$ y la cola queda:  
$[(SA,Q),(Q,SA),(SA,NSW),(NSW,SA),(SA,V),$
$(V,SA),(Q,NSW),(NSW,Q),(NSW,V),(V,NSW),(NT,SA),$
$(Q,SA),(NSW,SA),(V,SA),(WA,NT),(NT,Q)]$  
10.2- Se ingresa al método **Revise()**  
10.3- Por cada color $x$ en $D_{Q}$ comprueba que para todo color $y$ en $D_{NT}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
10.4- La salida de **Revise()** retorna Falso.

11. iteración #8:  
11.1- La cola devuelve $(SA,Q)$ y la cola queda:  
$[(Q,SA),(SA,NSW),(NSW,SA),(SA,V),(V,SA),(Q,NSW),$
$(NSW,Q),(NSW,V),(V,NSW),(NT,SA),(Q,SA),(NSW,SA),$
$(V,SA),(WA,NT),(NT,Q)]$  
11.2- Se ingresa al método **Revise()**  
11.3- Por cada color $x$ en $D_{SA}$ comprueba que para todo color $y$ en $D_{Q}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
11.4- La salida de **Revise()** retorna Falso.

12. iteración #9:  
12.1- La cola devuelve $(Q,SA)$ y la cola queda:  
$[(SA,NSW),(NSW,SA),(SA,V),(V,SA),(Q,NSW),(NSW,Q),$
$(NSW,V),(V,NSW),(NT,SA),(Q,SA),(NSW,SA),(V,SA),$
$(WA,NT),(NT,Q)]$  
12.2- Se ingresa al método **Revise()**  
12.3- Por cada color $x$ en $D_{Q}$ comprueba que para todo color $y$ en $D_{SA}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
12.4- La salida de **Revise()** retorna Falso.

13. iteración #10:  
13.1- La cola devuelve $(SA,NSW)$ y la cola queda:  
$[(NSW,SA),(SA,V),(V,SA),(Q,NSW),(NSW,Q),(NSW,V),(V,NSW),$
$(NT,SA),(Q,SA),(NSW,SA),(V,SA),(WA,NT),(NT,Q)]$  
13.2- Se ingresa al método **Revise()**  
13.3- Por cada color $x$ en $D_{Q}$ comprueba que para todo color $y$ en $D_{SA}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
13.4- La salida de **Revise()** retorna Falso.

14. iteración #11:  
14.1- La cola devuelve $(SA,NSW)$ y la cola queda:  
$[(SA,V),(V,SA),(Q,NSW),(NSW,Q),(NSW,V),(V,NSW),$
$(NT,SA),(Q,SA),(NSW,SA),(V,SA),(WA,NT),(NT,Q)]$ 
14.2- Se ingresa al método **Revise()**  
14.3- Por cada color $x$ en $D_{SA}$ comprueba que para todo color $y$ en $D_{NSW}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
14.4- La salida de **Revise()** retorna Falso.

15. iteración #12:  
15.1- La cola devuelve $(SA,V)$ y la cola queda:  
$[(V,SA),(Q,NSW),(NSW,Q),(NSW,V),(V,NSW),(NT,SA),$
$(Q,SA),(NSW,SA),(V,SA),(WA,NT),(NT,Q)]$  
15.2- Se ingresa al método **Revise()**  
15.3- Por cada color $x$ en $D_{SA}$ comprueba que para todo color $y$ en $D_{V}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
15.4- La salida de **Revise()** retorna Verdadero y se elimina $\textcolor{blue}{Azul}$ del dominio $D_{SA}$.  
15.5- Verifica que tamaño de $D_{SA}\neq0$  
15.6- Por cada Variable $X_k$ en $X_{SA}.NEIGHBORS-\{X_{V}\}$ se añade $(X_k,X_{SA})$ a la cola. Se añade  
$[(V,SA),(Q,NSW),(NSW,Q),(NSW,V),(V,NSW),(NT,SA),(Q,SA),$
$(NSW,SA),(V,SA),(WA,NT),(NT,Q),\textcolor{LimeGreen}{(WA,SA),(NT,SA),(Q,SA)}]$  

Tabla de Dominio:

![Dom_12](./images/Dominio_it12.png)

16. iteración #13:  
16.1- La cola devuelve $(V,SA)$ y la cola queda:  
$[(Q,NSW),(NSW,Q),(NSW,V),(V,NSW),(NT,SA),(Q,SA),(NSW,SA),$
$(V,SA),(WA,NT),(NT,Q),(WA,SA),(NT,SA),(Q,SA)]$  
16.2- Se ingresa al método **Revise()**  
16.3- Por cada color $x$ en $D_{V}$ comprueba que para todo color $y$ en $D_{SA}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
16.4- La salida de **Revise()** retorna Falso.

17. iteración #14:  
17.1- La cola devuelve $(V,SA)$ y la cola queda:  
$[(Q,NSW),(NSW,Q),(NSW,V),(V,NSW),(NT,SA),(Q,SA),$
$(NSW,SA),(V,SA),(WA,NT),(NT,Q),\textcolor{LimeGreen}{(WA,SA),(NT,SA),(Q,SA)}]$  
17.2- Se ingresa al método **Revise()**  
17.3- Por cada color $x$ en $D_{V}$ comprueba que para todo color $y$ en $D_{SA}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
17.4- La salida de **Revise()** retorna Falso.

18. iteración #15:  
18.1- La cola devuelve $(Q,NSW)$ y la cola queda:  
$[(NSW,Q),(NSW,V),(V,NSW),(NT,SA),(Q,SA),(NSW,SA),$
$(V,SA),(WA,NT),(NT,Q),(WA,SA),(NT,SA),(Q,SA)]$  
18.2- Se ingresa al método **Revise()**  
18.3- Por cada color $x$ en $D_{V}$ comprueba que para todo color $y$ en $D_{SA}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
18.4- La salida de **Revise()** retorna Falso.

19. iteración #16:  
19.1- La cola devuelve $(NSW,Q)$ y la cola queda:  
$[(NSW,V),(V,NSW),(NT,SA),(Q,SA),(NSW,SA),$
$(V,SA),(WA,NT),(NT,Q),(WA,SA),(NT,SA),(Q,SA)]$  
19.2- Se ingresa al método **Revise()**  
19.3- Por cada color $x$ en $D_{V}$ comprueba que para todo color $y$ en $D_{SA}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
19.4- La salida de **Revise()** retorna Falso.

20. iteración #17:  
20.1- La cola devuelve $(NSW,V)$ y la cola queda:  
$[(V,NSW),(NT,SA),(Q,SA),(NSW,SA),(V,SA),$
$(WA,NT),(NT,Q),(WA,SA),(NT,SA),(Q,SA)]$  
20.2- Se ingresa al método **Revise()**  
20.3- Por cada color $x$ en $D_{NSW}$ comprueba que para todo color $y$ en $D_{V}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
20.4- La salida de **Revise()** retorna Verdadero y se elimina $\textcolor{blue}{Azul}$ del dominio $D_{NSW}$.  
20.5- Verifica que tamaño de $D_{NSW}\neq0$  
20.6- Por cada Variable $X_k$ en $X_{NSW}.NEIGHBORS-\{X_{V}\}$ se añade $(X_k,X_{NSW})$ a la cola. Se añade  
$[(V,SA),(Q,NSW),(NSW,Q),(NSW,V),(V,NSW),(NT,SA),(Q,SA),$
$(NSW,SA),(V,SA),(WA,NT),(NT,Q),\textcolor{LimeGreen}{(SA,NSW),(Q,NSW)}]$  

Tabla de Dominio:

![Dom_17](./images/Dominio_it17.png)

21. iteración #18:  
21.1- La cola devuelve $(V,NSW)$ y la cola queda:  
$[(NT,SA),(Q,SA),(NSW,SA),(V,SA),(WA,NT),(NT,Q),$
$(WA,SA),(NT,SA),(Q,SA),(SA,NSW),(Q,NSW)]$  
21.2- Se ingresa al método **Revise()**  
21.3- Por cada color $x$ en $D_{V}$ comprueba que para todo color $y$ en $D_{NSW}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
21.4- La salida de **Revise()** retorna Falso.

22. iteración #19:  
22.1- La cola devuelve $(NT,SA)$ y la cola queda:  
$[(Q,SA),(NSW,SA),(V,SA),(WA,NT),(NT,Q),$
$(WA,SA),(NT,SA),(Q,SA),(SA,NSW),(Q,NSW)]$  
22.2- Se ingresa al método **Revise()**  
22.3- Por cada color $x$ en $D_{NT}$ comprueba que para todo color $y$ en $D_{SA}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
22.4- La salida de **Revise()** retorna Verdadero y se elimina $\textcolor{yellow}{Amarillo}$ del dominio $D_{NT}$.  
22.5- Verifica que tamaño de $D_{NT}\neq0$  
22.6- Por cada Variable $X_k$ en $X_{NT}.NEIGHBORS-\{X_{SA}\}$ se añade $(X_k,X_{NT})$ a la cola. Se añade  
$[(Q,SA),(NSW,SA),(V,SA),(WA,NT),(NT,Q),$
$(WA,SA),(NT,SA),(Q,SA),(SA,NSW),(Q,NSW), \textcolor{LimeGreen}{(WA,NT),(Q,NT)}]$  

Tabla de Dominio:

![Dom_19](./images/Dominio_it19.png)

23. iteración #20:  
23.1- La cola devuelve $(Q,SA)$ y la cola queda:  
$[(NSW,SA),(V,SA),(WA,NT),(NT,Q),(WA,SA),(NT,SA),$
$(Q,SA),(SA,NSW),(Q,NSW),(WA,NT),(Q,NT)]$  
23.2- Se ingresa al método **Revise()**  
23.3- Por cada color $x$ en $D_{Q}$ comprueba que para todo color $y$ en $D_{SA}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
23.4- La salida de **Revise()** retorna Verdadero y se elimina $\textcolor{yellow}{Amarillo}$ del dominio $D_{Q}$.  
23.5- Verifica que tamaño de $D_{Q}\neq0$  
23.6- Por cada Variable $X_k$ en $X_{Q}.NEIGHBORS-\{X_{SA}\}$ se añade $(X_k,X_{Q})$ a la cola. Se añade  
$[(NSW,SA),(V,SA),(WA,NT),(NT,Q),(WA,SA),(NT,SA),$
$(Q,SA),(SA,NSW),(Q,NSW), \textcolor{LimeGreen}{(NT,Q),(NSW,Q)}]$  

Tabla de Dominio:

![Dom_20](./images/Dominio_it20.png)

24. iteración #21:  
24.1- La cola devuelve $(NSW,SA)$ y la cola queda:  
$[(V,SA),(WA,NT),(NT,Q),(WA,SA),(NT,SA),(Q,SA),$
$(SA,NSW),(Q,NSW),(WA,NT),(Q,NT),(NT,Q),(NSW,Q)]$  
24.2- Se ingresa al método **Revise()**  
24.3- Por cada color $x$ en $D_{NSW}$ comprueba que para todo color $y$ en $D_{SA}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
24.4- La salida de **Revise()** retorna Verdadero y se elimina $\textcolor{yellow}{Amarillo}$ del dominio $D_{NSW}$.  
24.5- Verifica que tamaño de $D_{NSW}\neq0$  
24.6- Por cada Variable $X_k$ en $X_{NSW}.NEIGHBORS-\{X_{SA}\}$ se añade $(X_k,X_{NSW})$ a la cola. Se añade  
$[[(V,SA),(WA,NT),(NT,Q),(WA,SA),(NT,SA),(Q,SA),(SA,NSW),$
$(Q,NSW),(WA,NT),(Q,NT),(NT,Q),(NSW,Q), \textcolor{LimeGreen}{(Q,NSW),(V,NSW)}]$  

Tabla de Dominio:

![Dom_21](./images/Dominio_it21.png)

24. iteración #22:  
24.1- La cola devuelve $(V,SA)$ y la cola queda:  
$[(WA,NT),(NT,Q),(WA,SA),(NT,SA),(Q,SA),(SA,NSW),(Q,NSW),$
$(WA,NT),(Q,NT),(NT,Q),(NSW,Q),(Q,NSW),(V,NSW)]$  
24.2- Se ingresa al método **Revise()**  
24.3- Por cada color $x$ en $D_{NSW}$ comprueba que para todo color $y$ en $D_{SA}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
24.4- La salida de **Revise()** retorna False.

25. iteración #23:  
25.1- La cola devuelve $(WA,NT)$ y la cola queda:  
$[(NT,Q),(WA,SA),(NT,SA),(Q,SA),(SA,NSW),(Q,NSW),$
$(WA,NT),(Q,NT),(NT,Q),(NSW,Q),(Q,NSW),(V,NSW)]$  
25.2- Se ingresa al método **Revise()**  
25.3- Por cada color $x$ en $D_{NSW}$ comprueba que para todo color $y$ en $D_{SA}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
25.4- La salida de **Revise()** retorna False.

26. iteración #24:  
26.1- La cola devuelve $(NT,Q)$ y la cola queda:  
$[(WA,SA),(NT,SA),(Q,SA),(SA,NSW),(Q,NSW),(WA,NT),$
$(Q,NT),(NT,Q),(NSW,Q),(Q,NSW),(V,NSW)]$  
26.2- Se ingresa al método **Revise()**  
26.3- Por cada color $x$ en $D_{NSW}$ comprueba que para todo color $y$ en $D_{SA}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
26.4- La salida de **Revise()** retorna False.

27. iteración #25:  
27.1- La cola devuelve $(NT,SA)$ y la cola queda:  
$[(Q,SA),(SA,NSW),(Q,NSW),(WA,NT),(Q,NT),(NT,Q),$
$(NSW,Q),(Q,NSW),(V,NSW)]$  
27.2- Se ingresa al método **Revise()**  
27.3- Por cada color $x$ en $D_{NT}$ comprueba que para todo color $y$ en $D_{SA}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
27.4- La salida de **Revise()** retorna False.

28. iteración #26:  
28.1- La cola devuelve $(Q,SA)$ y la cola queda:  
$[(SA,NSW),(Q,NSW),(WA,NT),(Q,NT),
$(NT,Q),(NSW,Q),(Q,NSW),(V,NSW)]$  
28.2- Se ingresa al método **Revise()**  
28.3- Por cada color $x$ en $D_{Q}$ comprueba que para todo color $y$ en $D_{SA}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
28.4- La salida de **Revise()** retorna False.

29. iteración #27:  
29.1- La cola devuelve $(SA,NSW)$ y la cola queda:  
$[(Q,NSW),(WA,NT),(Q,NT),(NT,Q),(NSW,Q),$
$(Q,NSW),(V,NSW)]$  
29.2- Se ingresa al método **Revise()**  
29.3- Por cada color $x$ en $D_{SA}$ comprueba que para todo color $y$ en $D_{NSW}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
29.4- La salida de **Revise()** retorna False.

30. iteración #28:  
30.1- La cola devuelve $(Q,NSW)$ y la cola queda:  
$[(WA,NT),(Q,NT),(NT,Q),(NSW,Q),(Q,NSW),(V,NSW)]$  
30.2- Se ingresa al método **Revise()**  
30.3- Por cada color $x$ en $D_{Q}$ comprueba que para todo color $y$ en $D_{NSW}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
30.4- La salida de **Revise()** retorna Verdadero y se elimina $\textcolor{red}{Rojo}$ del dominio $D_{Q}$.  
30.5- Verifica que tamaño de $D_{Q}\neq0$  
30.6- Por cada Variable $X_k$ en $X_{Q}.NEIGHBORS-\{X_{NSW}\}$ se añade $(X_k,X_{Q})$ a la cola. Se añade  
$[[(WA,NT),(Q,NT),(NT,Q),(NSW,Q),(Q,NSW),$
$(V,NSW),\textcolor{LimeGreen}{(NT,Q),(SA,Q)}]$  

Tabla de Dominio:

![Dom_28](./images/Dominio_it28.png)

31. iteración #29:  
31.1- La cola devuelve $(WA,NT)$ y la cola queda:  
$[(Q,NT),(NT,Q),(NSW,Q),(Q,NSW),$
$(V,NSW),(NT,Q),(SA,Q)]$  
31.2- Se ingresa al método **Revise()**  
31.3- Por cada color $x$ en $D_{WA}$ comprueba que para todo color $y$ en $D_{NT}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
31.4- La salida de **Revise()** retorna False.

32. iteración #30:  
32.1- La cola devuelve $(Q,NT)$ y la cola queda:  
$[(NT,Q),(NSW,Q),(Q,NSW),(V,NSW),$
$(NT,Q),(SA,Q)]$  
32.2- Se ingresa al método **Revise()**  
32.3- Por cada color $x$ en $D_{WA}$ comprueba que para todo color $y$ en $D_{NT}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
32.4- La salida de **Revise()** retorna Verdadero y se elimina $\textcolor{blue}{Azul}$ del dominio $D_{Q}$.  
32.5- Verifica que tamaño de $D_{Q}=0$  
32.6- Retorna Falso.

Tabla de Dominio:

![Dom_30](./images/Dominio_it30.png)

### Conclusión

***De esta manera el algoritmo AC-3 retorna Falso indicando que la asignación $X=\{WA=Rojo, V=Azul\}$ para el CSP de colorar el mapa de Australia no es arco consistente. Por lo que queda demostrado que $P\implies Q$ es verdadero.***

## 3. ¿Cuál es la complejidad en el peor caso cuando se ejecuta AC-3 en un árbol estructurado CSP?

![AC-3]

La complejidad del algoritmo *AC-3* en un grafo es $O(cd^3)$.

Al tratarse de un árbol sabemos que la cola del algoritmo se inicia con una cantidad de arcos $(n-1)$ siendo $n$ la cantidad de variables o nodos en el árbol, los arcos deben estar ordenados de manera que el padre de un nodo siempre aparezca antes que el nodo.

El método $REVISE()$ en el peor caso tienen una complejidad de $d^2$ siendo $d$ la cardinalidad del dominio $D_i$ de la variable $X_i$.  

De esta manera no es necesario revisar los arcos en ambos sentidos ya que si el padre es arco consistente con su hijo entonces cualquier asignación al padre nos asegurará existen valores para sus hijos.

Nos devuelve una complejidad temporal $O(nd^2)$

## 4. Demostrar que la arco consistencia puede lograrse en un tiempo total $O(n^2d^2)$

Si cada nodo $X_i$ del grafo, representando una variable del CSP, tiene un contador por cada variable adyacente $X_k$, donde se lleva cuenta de la cantidad de valores del dominio $D_i$ que son consistentes con **todos** los valores del dominio $D_k$. Entonces, puede lograrse una complejidad de $O(n^2d^2)$.

El algoritmo iniciará con todos los contadores en $0$, luego estos se actualizarán en cada iteración con la función $REVISE(X_i,X_j)$.  

La función $REVISE$ suma una unidad a una variable local $count$ por cada valor de $x$ de $D_i$ que no presente inconsistencia con **ninguna** variable $y$ de $D_j$. Y antes de retornar el valor de $revised$, Se actualiza el contador de $X_i$ respecto a $X_j$ asignándole el valor de $count$ y el de $X_j$ respecto a $X_i$ asignándole el resultado de  $ \#(D_j) - \#(D_i) + count $ .

Finalmente cuando el bucle for quiera agregar un arco $(X_k,X_i)$ deberá revisar si el contador de $X_i$ respecto a $X_k$ tiene es igual a $0$. Si se cumple entonces agrega el arco a la cola.

PSEUDOCÓDIGO

    function AC-3(csp) returns false if an inconsistency is found and true otherwise  
        local variables: queue, a queue of arcs, initially all the arcs in csp  
        while queue is not empty do    
            (X_i, X_j) = REMOVE-FIRST(queue)   
            if REVISE(csp, X_i, X_j) then  
                if size of D_i = 0 then return false   
                for each X_k in X_i.NEIGHBORS - {X_j} do  
                    if X_i.Counters[k] = 0 then add (X_k, X_i) to queue   
            return true  

    function REVISE( csp, X_i, X_j) returns true iff we revise the domain of X_i  
        revised = false  
        count = 0
        for each x in D_i do   
            if value y in D_j allows (x,y) to satisfy the constraint between X_i and X_j then  
                delete x from D_i  
                revised = true  
            else count = count + 1  
        X_i.Counters[j] = count  
        X_j.Counters[i] = #(D_j)-#(D_i) + count   
        return revised

La complejidad de REVISE siguie siendo $O(d^2)$ pero la cantidad de arcos que se revisaran son solo $c$ esto nos deja una complejidad de $O(cd^2)$ pero como la cantidad maxima cantidad de arcos del grafo es $c = n*(n-1) = n^2-n$, entonces podemos escribir la complejidad como $O(n^2d^2)$.

## 5. Demostrar que para un CSP cuyo grafo de restricciones es un árbol estructurado con 2-consistencia implica que tiene n-consistencia (siendo n número total de variables)

$Q(N):=$ un árbol estructurado CSP $T$ es $N$-consistente  

Se debe demostrar:  
$$Q(2) \implies Q(n)$$  

### Demostración por inducción

#### Paso base

$Q(2) \implies Q(3)$

Para verificar 3-consistencia o consistencia de camino en un grafo se puede tomar todo camino $(X_i,X_m,X_j)$ y verificar que exista al menos 1 valor en el dominio de cada variable que permita una asignación consistente.  

Si queremos comprobar si hay consistencia de camino en la terna, y teniendo en cuenta de que se trata de un árbol (no hay ciclos), simplemente podemos verificar que los arcos $(X_i,X_m)$ y $(X_m,X_j)$ son arco consistentes.

Por hipótesis sabemos que el árbol es 2-consistente, es decir, todo arco $(X_i,X_j)$ es arco consistente. Esto quiere decir que tanto $(X_i,X_j)$ y $(X_m,X_j)$ son arco consistentes y por lo tanto cualquier terna $(X_i,X_m,X_j)$ es camino consistente.

Si cada terna es camino consistente entonces el árbol es 3-consistente.

#### Paso Inductivo  

$Q(k) \implies Q(k+1)$

Para verificar si un grafo es (k+1)-consistente debemos verificar que para toda (k+1)-upla $(X_i,X_j,...,X_k,X_{k+1})$ existe almenos un valor en el dominio de cada variable que permita consistencia.  

Teniendo en cuenta que se trata de un árbol (no tiene ciclos). Podemos verificar que cada (k+1)-upla es consistente verificando que cada k-upla, que sea subdupla, es k-consistente.  

Es decir, debemos verificar que $(X_i,X_j,...,X_k)$,...,$(X_j,...,X_k,X_{k+1})$ son k-consistentes. Esto es verdadero por hipótesis. Por lo tanto, toda (k+1)-upla del árbol es (k+1)-consistente, entonces el árbol es (k+1)-consistente. 

Queda demostrado que $Q(2) \implies Q(n)$

[AC-3]:./images/AlgoritmoAC-3.png

[Cuadricula]:./images/Cuadicula.png

## Results

### Conclusión

Como el problema de las n reinas es un csp y por lo tanto no importa el orden de asignación de las variables he decidido colocar las reinas de izquierda a derecha, por esta razón todas las soluciones son la misma en cada iteración y la cantidad de estados explorados también. Por esto es que no existen gran cantidad de variaciones

### Cantidad de estados explorados

!["Cantidad de estados explorados"](./ResultSet/BoxPlot-ExploredStates.png)

### Tiempo transcurrido de cada algoritmo

![""](./ResultSet/BoxPlot-Time.png)