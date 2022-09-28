## Martín Cogo Belver
# Inteligencia Artificial 1
## Trabajo Practico 6

## CSP

### Respuestas:

## 1. SUDOKU
Para representar el tablero de Sudoku se puede utilizar una matriz de 9 por 9.  
En este caso entonces se puede interpretar como un problema que se resuelve como un CSP donde:  
Las variables son cada casilla del tablero:  
$$\{X_{00},X_{01},X_{02},X_{03},X_{04},...,X_{10},X_{11},...,X_{88}\}$$ 
Para cada variable el dominio es de los números naturales del 1 al 9 por Ej: 
$$D_{00}=\{1,2,3,4,5,6,7,8,9\}$$
Existen un conjunto finito de restricciones: 
$$\{C_1,C_2,C_3\}$$
### Las restricciones son :

+ $C_1$: Las variables en cada columna de la tabla no deben repetir ningún valor.
+ $C2$: Las variables en cada fila de la tabla no deben repetir ningún valor.
+ $C3$: Las variables en las 9 tablas cuadradas de 3 por 3 interiores no deben repetir ningún valor.

El tablero comienza con variables ya inicializadas que no violan ninguna restricción y estas no son modificables. Por lo que el dominio de la mayoría de las variables se ve restringido al comienzo del problema.

Cada asignación en la matriz nos genera un grafo de restricciones. 
### Por ejemplo la asignación de la variable $X_{42}$ nos genera el siguiente grafo de restricciones 
### Grafo
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
#### Referencia:
+ El Color <input type="color" value="#e0589f"> indica que la variable es afectada por la restriccion $C_1$.
+ El Color <input type="color" value="#e38e35"> indica que la variable es afectada por la restriccion $C_2$.
+ El Color <input type="color" value="#93c47d"> indica que la variable es afectada por la restriccion $C_3$.

### En la tabla se estarían influenciadas las siguientes variables.
!["cuadriculaSudoku"][cuadricula]

Para solucionar este problema CSP se utilizaría un algoritmo basado en **Backtraking** y **heurísticas** como:

+ La heurística de **Minimum Remaining Values (MRV)** para elegír variables con menor cantidad de valores legales restantes primero.
+ También se utiliza la **Heurística de Grado** para poder determinar las casillas con mayor grado de restricción y de esta manera se rellenarían las casillas más restringidas primero.

## 2. Utilizar AC-3 para demostrar que la arco consistencia puede detectar la inconsistencia de la asignación parcial {WA=red, V=blue}  para el problema del colorar el mapa de Australia.

## Demostracion
Hipotesis:  
$P :=$ La arco consitencia puede detectar Inconcistencias de Arco.  
Tesis:  
$Q :=$ La asignación $X=\{WA=Rojo, V=Azul\}$ para el problema del coloreado de mapa de Australia con tres colores es arco inconcistente.

Se busca demostrar que $P\implies Q$.

El problema de coloreado del mapa de Australia se puede interpretar como un CSP. Entonces, para la demostracion, utilizaremos el algoritmo **AC-3** que utiliza la heurística inconcistencia de arco para detectar asignaciones incorrectas en las variables de un problema CSP.

![][AC-3]

El Algoritmo AC-3 resive como entrada una tupla de tres conjuntos $(X,D,C)$. $X$ es el conjunto de Variables, $D$ es el conjunto de dominios de Cada Variable, y $C$ es el conjunto de restricciones del problema.

En el caso particular del problema de Pintar el Mapa de Australia con tres colores, estas variables se pueden definir los conjuntos como:  
!["Mapa de Australia y Grafo"][MapaAutralia]  
El Conjunto de variables:
$$X = \{WA,NT,SA,Q,NSW,V,T\}$$
El Dominio de cada variable es igual para todas:
$$D_n = \{Rojo,Azul,Amarillo\}$$
El Conjunto de Restricciones:
$$C=\{C_1\}$$
Donde la restriccion es:

+ $C_1$: No pueden pintarse dos nodos adyacentes del mismo color.

Para la demostración *AC-3* resivira en la tupla de entrada el conjunto $X=\{WA=Rojo, V=Azul\}$ donde las demas variables se encuentran no inicializadas (sin color).
Para represenar el Dominio Utilizaremos un arreglo donde se ven los colores de cada Dominio.
Entonces el Algoritmo seguira los siguientes pasos:
1. Se inicializa la cola con los arcos 
$$[(WA,NT),(NT,WA),(WA,SA),(SA,WA),(NT,SA),(SA,NT),(NT,Q),(Q,NT),(SA,Q),(Q,SA),(SA,NSW),(NSW,SA),(SA,V),(V,SA),(Q,NSW),(NSW,Q),(NSW,V),(V,NSW)]$$
2. Como la cola no esta Vacia itera
3. iteracion #1:  
    1. La cola devuelve $(WA,NT)$
    2. Se ingresa al metodo **Revise()**
    3. Por cada color $x$ en $D_{WA}$ comprueba que para todo color $y$ en %D_{NT}% permita la asignacion $(x,y)$.(Como $WA=Rojo$ se revisara solo $x=Rojo$ con los tres colores de y)
    4.Como resultado $D_{WA} = {}$


<table border="1" cellpadding="0" cellspacing="0">
    <tr>
        <td width="8%">
            <table border="1" cellpadding="" cellspacing="0" width="2%">
            <caption>WA</caption>
                <tr>
                    <td width="100%" bgcolor="red"></td>
                </tr>
            </table>
        </td>
        <td width="8%">
            <table border="1" cellpadding="" cellspacing="0" width="2%"><caption>NT</caption>
                <tr>
                    <td width="100%" bgcolor="red"></td>
                    <td width="100%" bgcolor="blue"></td>
                    <td width="100%" bgcolor="yellow"></td>
                </tr>
            </table>
        </td>
        <<td width="8%">
            <table border="1" cellpadding="" cellspacing="0" width="2%"><caption>SA</caption>
                <tr>
                    <td width="100%" bgcolor="red"></td>
                </tr>
            </table>
        </td>
        <td width="8%">
            <table border="1" cellpadding="" cellspacing="0" width="2%"><caption>Q</caption>
                <tr>
                    <td width="100%" bgcolor="red"></td>
                </tr>
            </table>
        </td>
        <td width="8%">
            <table border="1" cellpadding="" cellspacing="0" width="2%"><caption>NSW</caption>
                <tr>
                    <td width="100%" bgcolor="red"></td>
                </tr>
            </table>
        </td>
        <td width="8%">
            <table border="1" cellpadding="" cellspacing="0" width="2%"><caption>V</caption>
                <tr>
                    <td width="100%" bgcolor="red"></td>
                </tr>
            </table>
        </td>
        <td width="8%">
            <table border="1" cellpadding="" cellspacing="0" width="2%"><caption>T</caption>
                <tr>
                    <td width="100%" bgcolor="red"></td>
                </tr>
            </table>
        </td>
    </tr>
</table>

3. E.

4. E.

5. E.


Imagenes:  

[MapaAutralia]:MapaAustralia.png
[AC-3]:AlgoritmoAC-3.png
[Cuadricula]:Cuadicula.png