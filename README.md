### Lineamientos básicos
- El trabajo se realizará en forma individual.

- Se debe entregar el informe en formato pdf en el aula virtual de la materia.

- El informe debe presentar carátula con datos del autor y fecha de entrega. Debe incluir número de hoja en cada página.

- Debe presentar codigo fuente e instrucciones de compilación y ejecución

- En caso de re-entrega, entregar un apartado con las correcciones mencionadas

## Parte 1: La señal para la ruta

Para una ruta recién inaugurada de “k” kilómetros de longitud se debe construir un conjunto de antenas celulares para cubrir su recorrido. Se recibieron un conjunto de “n” propuestas. Cada propuesta corresponde a la instalación de una antena en una ubicación determinada. Las características de las antenas pueden variar. Sabemos por la información de cada contrato dónde se ubicará la antena y la cantidad de kilómetros que cubrirá de la ruta expresado en un radio de una cantidad de kilómetros desde donde está ubicada.

Nos solicitan seleccionar el menor subconjunto de contratos de forma que toda la ruta quede totalmente cubierta o que informe que esto no es posible.

Resuelva:

1. Proponga al menos 2 estrategias greedy que no sean óptimas para resolver el problema. Ejemplifique. ¿Por qué considera que son del tipo greedy?

2. Proponga una estrategia greedy que sea óptima. Justifique su optimalidad.

3. Explique cómo implementar algorítmicamente esa estrategia. Brinde pseudocódigo y estructuras de datos a utilizar.

4. Analice complejidad temporal y espacial de su propuesta

5. Programe su algoritmo.

6. Analice el resultado que obtiene mediante su algoritmo. ¿Puede encontrar alguna característica que beneficie algunos contratos frente a otros? ¿Existe alguna otra solución óptima alternativa?

7. Su programa mantiene la complejidad espacial y temporal de su algoritmo?

Nota: El informe presentado NO debe superar las 7 páginas. Recuerde utilizar pseudocódigos para acompañar los ejemplos.

### Formato de los archivos:

El algoritmo debe recibir por parámetro el valor k y luego el nombre del archivo que contiene los contratos.

El archivo de los contratos corresponde a un archivo de texto que tiene una línea por contrato con el siguiente formato: nro, posición, radio

Ejemplo “contratos.txt”:
```text
1,44,50
2,402,150
3,219,35
4,100,80
5,80,80
6,300,160
7,150,30
```
El programa debe mostrar en pantalla en una misma línea los números de contrato seleccionados