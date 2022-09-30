
# Inteligencia Artificial 1

## Martín Cogo Belver

## Trabajo Practico 6 : CSP

## 1. Describir en detalle una formulación CSP para el SUDOKU

Para representar el tablero de Sudoku se puede utilizar una matriz de 9 por 9.  
En este caso entonces se puede interpretar como un problema que se resuelve como un CSP donde:  
Las variables son cada casilla del tablero:  
$$\{X_{00},X_{01},X_{02},X_{03},X_{04},...,X_{10},X_{11},...,X_{88}\}$$ 
Para cada variable el dominio es de los números naturales del 1 al 9 por Ej:
$$D_{00}=\{1,2,3,4,5,6,7,8,9\}$$
Existen un conjunto finito de restricciónes:
$$\{C_1,C_2,C_3\}$$

### Las restricciónes son  

+ $C_1$: Las variables en cada columna de la tabla no deben repetir ningún valor.
+ $C2$: Las variables en cada fila de la tabla no deben repetir ningún valor.
+ $C3$: Las variables en las 9 tablas cuadradas de 3 por 3 interiores no deben repetir ningún valor.

Estado inicial ? $\{\}$
Función Susesor: Se asigna a un valor a la proxima variable con menor cantidad de variables legales y mayor grado de restricciones(si se detecta inconcistencia se utiliza backtracking).
Estado objetivo: La asignacion de todas las casillas de manera concistente.
Costo de camino: consto constante para cada eleccion.

El tablero comienza con variables ya inicializadas que no violan ninguna restricción y estas no son modificables. Por lo que el dominio de la mayoría de las variables se ve restringido al comienzo del problema.

Cada asignación en la matriz nos genera un grafo de restricciónes.

### Por ejemplo la asignación de la variable $X_{42}$ nos genera el siguiente grafo de restricciónes

:::mermaid
    graph LR;
    id30((X<sub>30</sub>))
    ---id40((X<sub>40</sub>))
    ---id50((X<sub>50</sub>));
    id31((X<sub>31</sub>))
    ---id41((X<sub>41</sub>))
    ---id51((X<sub>51</sub>));
    id32((X<sub>32</sub>))
    ---id42((X<sub>42</sub>))
    ---id52((X<sub>52</sub>));
    id30((X<sub>30</sub>))---id31((X<sub>31</sub>))---id32((X<sub>32</sub>));
    id40((X<sub>40</sub>))
    ---id41((X<sub>41</sub>))
    ---id42((X<sub>42</sub>));
    id50---id51---id52;
    id42((X<sub>42</sub>))
    ---id43((X<sub>43</sub>))
    ---id44((X<sub>44</sub>))
    ---id45((X<sub>45</sub>))
    ---id46((X<sub>46</sub>))
    ---id47((X<sub>47</sub>))
    ---id48((X<sub>48</sub>));
    id02((X<sub>02</sub>))
    ---id12((X<sub>12</sub>))
    ---id22((X<sub>22</sub>))
    ---id32;
    id52---id62((X<sub>62</sub>))
    ---id72((X<sub>72</sub>))
    ---id82((X<sub>82</sub>));

    classDef selected fill:#e06666ff,stroke:#ffffffff,stroke-width:3px,color:#000000ff;
    id42:::selected;

    classDef restrictionC1 fill:#e0589fff,stroke:#ffffffff,stroke-width:3px,color:#000000ff;
    id02:::restrictionC1;
    id12:::restrictionC1;
    id22:::restrictionC1;
    id32:::restrictionC1;
    id52:::restrictionC1;
    id62:::restrictionC1;
    id72:::restrictionC1;
    id82:::restrictionC1;

    classDef restrictionC2 fill:#e38e35ff,stroke:#ffffffff,stroke-width:3px,color:#000000ff;
    id40:::restrictionC2;
    id41:::restrictionC2;
    id43:::restrictionC2;
    id44:::restrictionC2;
    id45:::restrictionC2;
    id46:::restrictionC2;
    id47:::restrictionC2;
    id48:::restrictionC2;

    classDef restrictionC3 fill:#93c47dff,stroke:#ffffffff,stroke-width:3px,color:#000000ff;
    id30:::restrictionC3;
    id31:::restrictionC3;
    id50:::restrictionC3;
    id51:::restrictionC3;
:::

### Referencia

+ El Color <input type="color" value="#e0589f"> indica que la variable es afectada por la restricción $C_1$.
+ El Color <input type="color" value="#e38e35"> indica que la variable es afectada por la restricción $C_2$.
+ El Color <input type="color" value="#93c47d"> indica que la variable es afectada por la restricción $C_3$.

### En la tabla se estarían influenciadas las siguientes variables

!["cuadriculaSudoku"][cuadricula]

Para solucionar este problema CSP se utilizara un algoritmo basado en **Backtracking** y **heurísticas** como:

+ La heurística de **Minimum Remaining Values (MRV)** para elegir variables con menor cantidad de valores legales restantes primero.
+ También se utiliza la **Heurística de Grado** para poder determinar las casillas con mayor grado de restricción y de esta manera se rellenarían las casillas más restringidas primero.

## 2. Utilizar el algoritmo AC-3 para demostrar que la arco consistencia puede detectar la inconsistencia de la asignación parcial {WA=red, V=blue} para el problema del colorar el mapa de Australia.  

### Demostración

Hipótesis:  
$P :=$ La arco consistencia puede detectar Inconsistencias de Arco.  
Tesis:  
$Q :=$ La asignación $X=\{WA=Rojo, V=Azul\}$ para el problema del coloreado de mapa de Australia con tres colores no es arco consistente.

Se busca demostrar que $P\implies Q$.

El problema de coloreado del mapa de Australia se puede interpretar como un CSP. Entonces, para la demostración, utilizaremos el algoritmo **AC-3** que utiliza la heurística inconsistencia de arco para detectar asignaciónes incorrectas en las variables de un problema CSP.

!["AC-3 Code"][AC-3]

El Algoritmo AC-3 resibe como entrada una tupla de tres conjuntos $(X,D,C)$. $X$ es el conjunto de Variables, $D$ es el conjunto de dominios de Cada Variable, y $C$ es el conjunto de restricciónes del problema.

En el caso particular del problema de Pintar el Mapa de Australia con tres colores, estas variables se pueden definir los conjuntos como:  
!["Mapa de Australia y Grafo"][MapaAutralia]  
El Conjunto de variables:
$$X = \{WA,NT,SA,Q,NSW,V,T\}$$
El Dominio de cada variable es igual para todas:
$$D_n = \{Rojo,Azul,Amarillo\}$$
El Conjunto de Restricciónes:
$$C=\{C_1\}$$
Donde la restricción es:

+ $C_1$: No pueden pintarse dos nodos adyacentes del mismo color.

Para la demostración *AC-3* resibirá en la tupla de entrada el conjunto $X=\{WA=Rojo, V=Azul\}$ donde las demás variables se encuentran no inicializadas (sin color).
Para representar el Dominio utilizaremos un arreglo donde se ven los colores de cada Dominio.

Entonces el Algoritmo seguirá los siguientes pasos:  

1. Se inicializa la cola con los arcos  
$[(WA,NT),(NT,WA),(WA,SA),(SA,WA),(NT,SA),(SA,NT),(NT,Q),$
$(Q,NT),(SA,Q),(Q,SA),(SA,NSW),(NSW,SA),(SA,V),(V,SA),$
$(Q,NSW),(NSW,Q),(NSW,V),(V,NSW)]$  
2. Como la cola no esta Vacia itera  

Tabla de Dominios:
<table aling="center" border="1">
    <tr>
        <td width="1%">
            <table border="1" width="100%"><caption>WA</caption>
                <tr>
                    <td bgcolor="red"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>NT</caption>
                <tr>
                    <td bgcolor="red"></td>
                    <td bgcolor="blue"></td>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>SA</caption>
                <tr>
                    <td bgcolor="red"></td>
                    <td bgcolor="blue"></td>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>Q</caption>
                <tr>
                    <td width="100%" bgcolor="red"></td>
                    <td width="100%" bgcolor="blue"></td>
                    <td width="100%" bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>NSW</caption>
                <tr>
                    <td bgcolor="red"></td>
                    <td bgcolor="blue"></td>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>V</caption>
                <tr>
                    <td bgcolor="blue"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>T</caption>
                <tr>
                    <td bgcolor="red"></td>
                    <td bgcolor="blue"></td>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
    </tr>
</table>  

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

<table aling="center" border="1">
    <tr>
        <td width="1%">
            <table border="1" width="100%"><caption>WA</caption>
                <tr>
                    <td bgcolor="red"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>NT</caption>
                <tr>
                    <td bgcolor="blue"></td>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>SA</caption>
                <tr>
                    <td bgcolor="red"></td>
                    <td bgcolor="blue"></td>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>Q</caption>
                <tr>
                    <td width="100%" bgcolor="red"></td>
                    <td width="100%" bgcolor="blue"></td>
                    <td width="100%" bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>NSW</caption>
                <tr>
                    <td bgcolor="red"></td>
                    <td bgcolor="blue"></td>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>V</caption>
                <tr>
                    <td bgcolor="blue"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>T</caption>
                <tr>
                    <td bgcolor="red"></td>
                    <td bgcolor="blue"></td>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
    </tr>
</table> 

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
<table aling="center" border="1">
    <tr>
        <td width="1%">
            <table border="1" width="100%"><caption>WA</caption>
                <tr>
                    <td bgcolor="red"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>NT</caption>
                <tr>
                    <td bgcolor="blue"></td>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>SA</caption>
                <tr>
                    <td bgcolor="blue"></td>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>Q</caption>
                <tr>
                    <td width="100%" bgcolor="red"></td>
                    <td width="100%" bgcolor="blue"></td>
                    <td width="100%" bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>NSW</caption>
                <tr>
                    <td bgcolor="red"></td>
                    <td bgcolor="blue"></td>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>V</caption>
                <tr>
                    <td bgcolor="blue"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>T</caption>
                <tr>
                    <td bgcolor="red"></td>
                    <td bgcolor="blue"></td>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
    </tr>
</table>

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
<table aling="center" border="1">
    <tr>
        <td width="1%">
            <table border="1" width="100%"><caption>WA</caption>
                <tr>
                    <td bgcolor="red"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>NT</caption>
                <tr>
                    <td bgcolor="blue"></td>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>SA</caption>
                <tr>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>Q</caption>
                <tr>
                    <td width="100%" bgcolor="red"></td>
                    <td width="100%" bgcolor="blue"></td>
                    <td width="100%" bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>NSW</caption>
                <tr>
                    <td bgcolor="red"></td>
                    <td bgcolor="blue"></td>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>V</caption>
                <tr>
                    <td bgcolor="blue"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>T</caption>
                <tr>
                    <td bgcolor="red"></td>
                    <td bgcolor="blue"></td>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
    </tr>
</table>
  
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
<table aling="center" border="1">
    <tr>
        <td width="1%">
            <table border="1" width="100%"><caption>WA</caption>
                <tr>
                    <td bgcolor="red"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>NT</caption>
                <tr>
                    <td bgcolor="blue"></td>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>SA</caption>
                <tr>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>Q</caption>
                <tr>
                    <td width="100%" bgcolor="red"></td>
                    <td width="100%" bgcolor="blue"></td>
                    <td width="100%" bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>NSW</caption>
                <tr>
                    <td bgcolor="red"></td>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>V</caption>
                <tr>
                    <td bgcolor="blue"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>T</caption>
                <tr>
                    <td bgcolor="red"></td>
                    <td bgcolor="blue"></td>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
    </tr>
</table> 

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
<table aling="center" border="1">
    <tr>
        <td width="1%">
            <table border="1" width="100%"><caption>WA</caption>
                <tr>
                    <td bgcolor="red"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>NT</caption>
                <tr>
                    <td bgcolor="blue"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>SA</caption>
                <tr>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>Q</caption>
                <tr>
                    <td width="100%" bgcolor="red"></td>
                    <td width="100%" bgcolor="blue"></td>
                    <td width="100%" bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>NSW</caption>
                <tr>
                    <td bgcolor="red"></td>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>V</caption>
                <tr>
                    <td bgcolor="blue"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>T</caption>
                <tr>
                    <td bgcolor="red"></td>
                    <td bgcolor="blue"></td>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
    </tr>
</table> 

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
<table aling="center" border="1">
    <tr>
        <td width="1%">
            <table border="1" width="100%"><caption>WA</caption>
                <tr>
                    <td bgcolor="red"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>NT</caption>
                <tr>
                    <td bgcolor="blue"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>SA</caption>
                <tr>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>Q</caption>
                <tr>
                    <td width="100%" bgcolor="red"></td>
                    <td width="100%" bgcolor="blue"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>NSW</caption>
                <tr>
                    <td bgcolor="red"></td>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>V</caption>
                <tr>
                    <td bgcolor="blue"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>T</caption>
                <tr>
                    <td bgcolor="red"></td>
                    <td bgcolor="blue"></td>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
    </tr>
</table> 

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
<table aling="center" border="1">
    <tr>
        <td width="1%">
            <table border="1" width="100%"><caption>WA</caption>
                <tr>
                    <td bgcolor="red"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>NT</caption>
                <tr>
                    <td bgcolor="blue"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>SA</caption>
                <tr>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>Q</caption>
                <tr>
                    <td width="100%" bgcolor="red"></td>
                    <td width="100%" bgcolor="blue"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>NSW</caption>
                <tr>
                    <td bgcolor="red"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>V</caption>
                <tr>
                    <td bgcolor="blue"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>T</caption>
                <tr>
                    <td bgcolor="red"></td>
                    <td bgcolor="blue"></td>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
    </tr>
</table> 

24. iteración #21:  
24.1- La cola devuelve $(V,SA)$ y la cola queda:  
$[(WA,NT),(NT,Q),(WA,SA),(NT,SA),(Q,SA),(SA,NSW),(Q,NSW),$
$(WA,NT),(Q,NT),(NT,Q),(NSW,Q),(Q,NSW),(V,NSW)]$  
24.2- Se ingresa al método **Revise()**  
24.3- Por cada color $x$ en $D_{NSW}$ comprueba que para todo color $y$ en $D_{SA}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
24.4- La salida de **Revise()** retorna False.

25. iteración #22:  
25.1- La cola devuelve $(WA,NT)$ y la cola queda:  
$[(NT,Q),(WA,SA),(NT,SA),(Q,SA),(SA,NSW),(Q,NSW),$
$(WA,NT),(Q,NT),(NT,Q),(NSW,Q),(Q,NSW),(V,NSW)]$  
25.2- Se ingresa al método **Revise()**  
25.3- Por cada color $x$ en $D_{NSW}$ comprueba que para todo color $y$ en $D_{SA}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
25.4- La salida de **Revise()** retorna False.

26. iteración #23:  
26.1- La cola devuelve $(NT,Q)$ y la cola queda:  
$[(WA,SA),(NT,SA),(Q,SA),(SA,NSW),(Q,NSW),(WA,NT),$
$(Q,NT),(NT,Q),(NSW,Q),(Q,NSW),(V,NSW)]$  
26.2- Se ingresa al método **Revise()**  
26.3- Por cada color $x$ en $D_{NSW}$ comprueba que para todo color $y$ en $D_{SA}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
26.4- La salida de **Revise()** retorna False.

27. iteración #24:  
27.1- La cola devuelve $(NT,SA)$ y la cola queda:  
$[(Q,SA),(SA,NSW),(Q,NSW),(WA,NT),(Q,NT),(NT,Q),$
$(NSW,Q),(Q,NSW),(V,NSW)]$  
27.2- Se ingresa al método **Revise()**  
27.3- Por cada color $x$ en $D_{NT}$ comprueba que para todo color $y$ en $D_{SA}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
27.4- La salida de **Revise()** retorna False.

28. iteración #25:  
28.1- La cola devuelve $(Q,SA)$ y la cola queda:  
$[(SA,NSW),(Q,NSW),(WA,NT),(Q,NT),
$(NT,Q),(NSW,Q),(Q,NSW),(V,NSW)]$  
28.2- Se ingresa al método **Revise()**  
28.3- Por cada color $x$ en $D_{Q}$ comprueba que para todo color $y$ en $D_{SA}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
28.4- La salida de **Revise()** retorna False.

29. iteración #26:  
29.1- La cola devuelve $(SA,NSW)$ y la cola queda:  
$[(Q,NSW),(WA,NT),(Q,NT),(NT,Q),(NSW,Q),$
$(Q,NSW),(V,NSW)]$  
29.2- Se ingresa al método **Revise()**  
29.3- Por cada color $x$ en $D_{SA}$ comprueba que para todo color $y$ en $D_{NSW}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
29.4- La salida de **Revise()** retorna False.

30. iteración #27:  
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
<table aling="center" border="1">
    <tr>
        <td width="1%">
            <table border="1" width="100%"><caption>WA</caption>
                <tr>
                    <td bgcolor="red"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>NT</caption>
                <tr>
                    <td bgcolor="blue"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>SA</caption>
                <tr>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>Q</caption>
                <tr>
                    <td width="100%" bgcolor="blue"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>NSW</caption>
                <tr>
                    <td bgcolor="red"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>V</caption>
                <tr>
                    <td bgcolor="blue"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>T</caption>
                <tr>
                    <td bgcolor="red"></td>
                    <td bgcolor="blue"></td>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
    </tr>
</table>

31. iteración #28:  
31.1- La cola devuelve $(WA,NT)$ y la cola queda:  
$[(Q,NT),(NT,Q),(NSW,Q),(Q,NSW),$
$(V,NSW),(NT,Q),(SA,Q)]$  
31.2- Se ingresa al método **Revise()**  
31.3- Por cada color $x$ en $D_{WA}$ comprueba que para todo color $y$ en $D_{NT}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
31.4- La salida de **Revise()** retorna False.

32. iteración #29:  
32.1- La cola devuelve $(Q,NT)$ y la cola queda:  
$[(NT,Q),(NSW,Q),(Q,NSW),(V,NSW),$
$(NT,Q),(SA,Q)]$  
32.2- Se ingresa al método **Revise()**  
32.3- Por cada color $x$ en $D_{WA}$ comprueba que para todo color $y$ en $D_{NT}$ permita la asignación $(x,y)$ sin satisfacer alguna restricción.  
32.4- La salida de **Revise()** retorna Verdadero y se elimina $\textcolor{blue}{Azul}$ del dominio $D_{Q}$.  
32.5- Verifica que tamaño de $D_{Q}=0$  
32.6- Retorna Falso.

Tabla de Dominio:
<table aling="center" border="1">
    <tr>
        <td width="1%">
            <table border="1" width="100%"><caption>WA</caption>
                <tr>
                    <td bgcolor="red"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>NT</caption>
                <tr>
                    <td bgcolor="blue"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>SA</caption>
                <tr>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>Q</caption>
                <tr>
                    <td bgcolor="black"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>NSW</caption>
                <tr>
                    <td bgcolor="red"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>V</caption>
                <tr>
                    <td bgcolor="blue"></td>
                </tr>
            </table>
        </td>
        <td width="1%">
            <table border="1"><caption>T</caption>
                <tr>
                    <td bgcolor="red"></td>
                    <td bgcolor="blue"></td>
                    <td bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
    </tr>
</table>

### Conclusión

***De esta manera el algoritmo AC-3 retorna Falso indicando que la asignación $X=\{WA=Rojo, V=Azul\}$ para el CSP de colorar el mapa de Australia no es arco consistente. Por lo que queda demostrado que $P\implies Q$ es verdadero.***

## 3. ¿Cuál es la complejidad en el peor caso cuando se ejecuta AC-3 en un árbol estructurado CSP?

![AC-3]

La complejidad del algoritmo AC-3 es de

La complejidad del algoritmo *AC-3* en un grafo es $O(cd^3)$.

Al tratarse de un arbol sabemos que la cola del algoritmo se inicia con una cantidad de arcos $(n-1)$ siendo n la cantidad de variables o nodos en el árbol, los arcos deben estar ordenados de manera que el padre de un nodo siempre aparezca antes que el nodo.

El metodo REVISE() en el peor caso tienen una complejidad de $d^2$ siendo $d$ la cardinalidad del dominio $D_i$ de la variable $X_i$. 

De esta manera no es nesesario revisar los arcos en ambos sentidos ya que si el padre es arco concistente con su hijo entonces cualquier asignacion al padre nos asegurara existiran valores para sus hijos.

Nos devuelve una complejidad temporal $O(nd^2)$

## 4. Demostrar que la arco consistencia puede lograrse en un tiempo total $O(n^2d^2)$

Si cada nodo del grafo representando una variable del CSP, tiene una lista de contadores con un contador por cada variable adyacente en el grafo, donde se lleva cuenta de la cantidad de valores del dominio de el nodo que son concistentes con todos los valores del dominio de cada nodo adyacentes puede lograrse una complejidad de O(n^2d^2).

El algoritmo iniciara con todos los contadores en $0$, luego estos se actualizaran en cada iteracion con la funcion REVISE($X_i,X_j$). La función revise suma una unidad a una variable local $count$ por cada valor de $x$ de $D_i$ que no presente inconcistencia con ninguna variable $y$ de %D_j%. Finalmente antes de retornar el valor $revised$. Se actualiza el contador de $X_i$ respecto a $X_j$ y el de $X_j$ respecto a $X_i$. Al contador de $X_i$ se le asignara el valor de $count$ y al contador de  $X_j$ el valor resultado de  $ \#(D_j) - \#(D_i) + count$

Finalmente cuando el bucle for quiera agregar un arco $(X_k,X_i)$ debera revisar si el contador de X_i respecto a la cantidad de variables que permiten consistencia con todos los valores de $X_k$ es igual a 0. Si se cumple entonces agrega el arco a la cola.

PSEUDOCODIGO

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

La complejidad de REVISE siguie siendo $O(d^2)$ pero ahora cada arco $(X_k,X_i)$ solo se revisara 

## 5. Demostrar que para un CSP cuyo grafo de restricciones es un árbol estructurado con 2-consistencia implica que tiene n-consistencia (siendo n número total de variables)




[MapaAutralia]:MapaAustralia.png
[AC-3]:AlgoritmoAC-3.png
[Cuadricula]:Cuadicula.png