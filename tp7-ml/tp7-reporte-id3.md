
# Implementación de árbol de deserción en python # # # #

## Conjunto de Entrenamiento ##

```
     outlook  temp humidity  windy play
3      rainy  mild     high  False  yes
7      sunny  mild     high  False   no
6   overcast  cool   normal   True  yes
2   overcast   hot     high  False  yes
10     sunny  mild   normal   True  yes
4      rainy  cool   normal  False  yes
1      sunny   hot     high   True   no
12  overcast   hot   normal  False  yes
0      sunny   hot     high  False   no
13     rainy  mild     high   True   no
9      rainy  mild   normal  False  yes

```

## arbol generado ##

```
humidity
├── ['high', 'outlook']
│   ├── ['overcast', 'yes']
│   ├── ['rainy', 'windy']
│   │   ├── [False, 'yes']
│   │   └── [True, 'no']
│   └── ['sunny', 'no']
└── ['normal', 'yes']
```

## conjunto de Prueba ##

```
     outlook  temp humidity  windy play_orig play
5      rainy  cool   normal   True        no  yes
8      sunny  cool   normal  False       yes  yes
11  overcast  mild     high   True       yes  yes
```

## Estrategia para datos de tipo real ##

Los arboles cuya variable de destino toma valores continuos se llama **Árbol de regresión**. 

Un árbol de regresión consiste en hacer preguntas de tipo $¿xk≤c?$ para cada una de las covariables, de esta forma el espacio de las covariables es divido en hiper-rectángulos y todas las observaciones que queden dentro de un hiper-rectángulo tendrán el mismo valor estimado. 

![](./Images/ilustracion_arb_regresion.png)