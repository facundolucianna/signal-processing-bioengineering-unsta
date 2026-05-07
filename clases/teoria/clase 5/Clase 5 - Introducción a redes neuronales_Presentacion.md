<!-- slide -->
## Diapositiva 1
### Introducción a Redes Neuronales
#### Análisis y procesamiento de Señales
##### Bioingeniería - Facultad de Ingeniería - UNSTA
##### 2026
**Dr. Ing. Facundo Adrián Lucianna**
**Ing. Facundo Roldán**

---

<!-- slide -->
## Diapositiva 2
### Redes Neuronales
- Las redes neuronales se plantean originalmente como {amarillo}(**algoritmos matemáticos**) que intentan imitar los cálculos del cerebro.
- Buscan replicar la enorme cantidad de {verde}(**unidades de procesamiento (neuronas)**) y su {verde}(**interconexión (sinapsis)**).
- Generaron dos grandes campos de aplicación: la {naranja}(**neurociencia computacional**) y el {naranja}(**Deep Learning**).
- El {amarillo}(**Deep Learning**) goza de una gran popularidad actual, con avances constantes y visibles para el público general.

---

<!-- slide -->
## Diapositiva 3
### Redes Neuronales
Un poquito de historia…
- {verde}(**1943 - Neurona de McCulloch-Pitts:**) Primera formulación matemática/algebraica del cálculo neuronal. La unidad actual de Deep Learning es muy similar a este modelo.
- {verde}(**1949 - Regla de Hebb:**) Donald Hebb creó una regla para modificar la intensidad de conexión entre neuronas ({amarillo}(**aprendizaje**)), concepto válido hasta hoy.
- {verde}(**1952 - Modelo de Hodgkin y Huxley:**) Modelo basado en conductancia mediante ecuaciones diferenciales. Explica la generación y propagación de {amarillo}(**potenciales de acción**). Premio Nobel en 1963.

![imagen](img/image2.png)

---

<!-- slide -->
## Diapositiva 4
### Redes Neuronales
- {verde}(**1947 - Alan Turing:**) Dio sus primeras lecciones en IA.
- Introdujo conceptos clave: el {amarillo}(**test de Turing**), {amarillo}(**aprendizaje automático**), {amarillo}(**algoritmos genéticos**) y {amarillo}(**aprendizaje por refuerzo**).
- Sugirió que sería más eficiente crear IA a nivel humano {verde}(**desarrollando algoritmos de aprendizaje**) y enseñando a la máquina, en lugar de programar cada regla a mano.

![imagen](img/image3.png)

---

<!-- slide -->
## Diapositiva 5
### Redes Neuronales
- En este estadio embrionario, las investigaciones estaban en su cúspide.
- {verde}(**1958 - Frank Rosenblatt:**) Realizó la primera implementación del {amarillo}(**perceptrón**) (basado en McCulloch-Pitts).
- Rosenblatt es considerado el {verde}(**padre del Deep Learning**).
- Perfeccionó el perceptrón moderno y experimentó con redes de dos o tres capas.

![imagen](img/image4.png)

---

<!-- slide -->
## Diapositiva 6
### Redes Neuronales
- {rojo}(**1969 - El Primer Invierno:**) Se publicó el libro *Perceptrons* de Minsky y Papert, enfatizando los límites de lo que los perceptrones podían hacer.
- Su popularidad {rojo}(**mató toda financiación**) en investigaciones hasta 1980.
- Crítica principal: El perceptrón no podía resolver la función lógica {amarillo}(**XOR**), algo que (se creía) una neurona biológica sí podía.
- Más tarde se comprobó que una sola neurona biológica tampoco puede resolver XOR, sino que necesita de una {verde}(**red**).
- *Curiosidad:* En 2020 se descubrió que algunas neuronas humanas ¡sí pueden!

![imagen](img/image5.png)

---

<!-- slide -->
## Diapositiva 8
### Redes Neuronales
- {verde}(**1980-1990 - Fin del Invierno:**) Desarrollos de Rumelhart, Hopfield, entre otros.
- Se desarrollaron hitos clave: el algoritmo de {amarillo}(**Backpropagation**), {amarillo}(**redes de memoria**) y el concepto de {amarillo}(**propiedades emergentes**). *Fuente de imagen: https://github.com/TarinZ/hopfield-nets*.
- {rojo}(**El Segundo Invierno:**) Llegada de algoritmos más sencillos de usar y sin necesidad de ajustar tantos hiperparámetros (ej. {verde}(**SVM**) y {verde}(**Random Forests**)). Rendían mucho mejor que las redes neuronales en esa época.

![imagen](img/image7.png)

---

<!-- slide -->
## Diapositiva 10
### Redes Neuronales
- Con la llegada de la World Wide Web y mejoras de hardware (Ley de Moore), surgen datasets enormes: {amarillo}(**Big Data**).
- Esto creó la necesidad de algoritmos que aprovecharan este volumen de información.
- El Big Data ayudó al {verde}(**Aprendizaje Automático (ML)**) y la IA a recuperar su atractivo comercial.
- {verde}(**2011:**) El sistema **IBM Watson** logró el nivel de un campeón humano en *Jeopardy!*

---

<!-- slide -->
## Diapositiva 11
### Redes Neuronales
- {verde}(**2010 - El Renacimiento:**) La IA vuelve a la vida y adopta oficialmente el nombre de {amarillo}(**Deep Learning**).
- Se incorporaron nuevas arquitecturas y características.
- Los algoritmos comenzaron a superar a los clásicos en clasificación de imágenes, video, voz y texto.
- **Claves del éxito:** {verde}(**Big Data**), mejora exponencial en {verde}(**procesamiento de cálculo (GPUs)**) y la fuerte inversión de gigantes como Google, Meta y Microsoft.

![imagen](img/image8.png)

---

<!-- slide -->
## Diapositiva 12
### Perceptrón y neuronas sigmoideas

---

<!-- slide -->
## Diapositiva 13
### Perceptrón
Repaso de fisiología:
- {verde}(**Cuerpo celular o soma:**) Contiene el núcleo y las organelas.
- {verde}(**Dendritas:**) Ramificaciones del soma donde se reciben las {amarillo}(**sinapsis**) de otras neuronas.
- {verde}(**Axón:**) Prolongación encargada de transmitir el {amarillo}(**impulso nervioso**). Es el canal de comunicación.

![imagen](img/image9.png)

---

<!-- slide -->
## Diapositiva 14
### Perceptrón
En estado de reposo, el interior de la célula tiene un voltaje negativo comparado con el exterior.

![imagen](img/image10.png)

---

<!-- slide -->
## Diapositiva 15
### Perceptrón
Si otra neurona la excita {amarillo}(**levemente**), aumenta el voltaje, pero rápidamente vuelve a su estado de reposo.

![imagen](img/image11.png)

---

<!-- slide -->
## Diapositiva 16
### Perceptrón
De manera similar, una sinapsis puede ser {rojo}(**inhibitoria**), reduciendo aún más el voltaje.

![imagen](img/image12.png)

---

<!-- slide -->
## Diapositiva 17
### Perceptrón
Pero si la excitación supera un {amarillo}(**umbral**), se genera un impulso mediante un efecto de {verde}(**"todo o nada"**).

![imagen](img/image13.png)

---

<!-- slide -->
## Diapositiva 18
### Perceptrón
Este impulso se propaga desde el cuerpo hasta el terminal axónico, y así la neurona envía su {amarillo}(**salida**).

![imagen](img/image14.png)

---

<!-- slide -->
## Diapositiva 19
### Perceptrón
Diferentes niveles de excitación producen diferentes {verde}(**tasas de disparo**) (frecuencia de impulsos).

![imagen](img/image15.png)

---

<!-- slide -->
## Diapositiva 20
### Perceptrón
Diferentes niveles de excitación producen diferentes {verde}(**tasas de disparo**).

![imagen](img/image16.png)

---

<!-- slide -->
## Diapositiva 21
### Perceptrón
Además, ante una misma excitación, existen {amarillo}(**sinapsis más sensibles**) que otras.

![imagen](img/image17.png)

---

<!-- slide -->
## Diapositiva 22
### Perceptrón
Con esto en mente, armemos nuestro {verde}(**modelo matemático de neurona**).

![imagen](img/image18.png)

$$z = w_1 x_1 + w_2 x_2 + w_3 x_3 + b$$ 
$$z = \sum_{i=1}^{3} w_i x_i + b$$
$$y = f(z)$$
$$y = f \left(\sum_{i=1}^{3} w_i x_i + b \right)$$

---

<!-- slide -->
## Diapositiva 23
### Perceptrón
Con esto en mente, armemos nuestro {verde}(**modelo matemático de neurona**).

![imagen](img/image22.png)

$$z = w_1 x_1 + w_2 x_2 + w_3 x_3 + 1 \cdot b$$ 
$$z = \sum_{i=1}^{4} w_i x_i$$
$$y = f(z)$$
$$y = f \left(\sum_{i=1}^{4} w_i x_i \right)$$

---

<!-- slide -->
## Diapositiva 24
### Perceptrón
- Si tenemos un vector (u observación) de $n$ atributos, la neurona tendrá $n$ entradas con $n+1$ {verde}(**pesos sinápticos**).
- La parte lineal del cálculo involucra los pesos sinápticos $w_i$ y el *bias* $b$.
- Representan si la conexión es {amarillo}(**excitatoria**) ($w_i > 0$), {rojo}(**inhibitoria**) ($w_i < 0$), o inexistente ($w_i = 0$).

$$\sum_{i=1}^{n} w_i x_i + b$$

![imagen](img/image27.png)

---

<!-- slide -->
## Diapositiva 25
### Perceptrón
Veamos la {verde}(**función de activación**): ¿Qué estamos modelando con ella?
- En este modelo no nos interesa el impulso nervioso exacto, sino modelar la {amarillo}(**tasa de impulsos**).
- *Experimento:* Si inyectamos voltaje y medimos la tasa de impulsos, vemos que antes de superar un {verde}(**umbral de disparo**), la neurona no dispara (tasa = 0 Hz).

![imagen](img/image28.png)

---

<!-- slide -->
## Diapositiva 26
### Perceptrón
Veamos la {verde}(**función de activación**): ¿Qué estamos modelando con ella?
- *Experimento:* Durante la etapa {verde}(**lineal**), si duplicamos el voltaje inyectado, la neurona dispara al doble de la frecuencia.

![imagen](img/image29.png)

---

<!-- slide -->
## Diapositiva 27
### Perceptrón
Veamos la {verde}(**función de activación**): ¿Qué estamos modelando con ella?
- *Experimento:* Cuando llegamos a un punto máximo de saturación, no importa cuánto más voltaje introducimos, la neurona dispara a su {rojo}(**máxima frecuencia posible**).

![imagen](img/image30.png)

---

<!-- slide -->
## Diapositiva 28
### Perceptrón
- Por lo tanto, la {verde}(**función de activación**) es una función *no lineal* que modela la variación de la tasa de disparo.
- Esta es la expresión mínima de una neurona: una unidad de cálculo {amarillo}(**no lineal**).

![imagen](img/image31a.png)

---

<!-- slide -->
## Diapositiva 29
### Perceptrón
La elección de la {verde}(**función de activación**) es una decisión de diseño para nuestra red:

![imagen](img/image33a.png)

---

<!-- slide -->
## Diapositiva 30
### Perceptrón
Otras funciones de activación muy comunes:

![imagen](img/image41a.png)

---

<!-- slide -->
## Diapositiva 31
### Perceptrón
Implementación de funciones lógicas usando un perceptrón:

![imagen](img/image49a.png)

---

<!-- slide -->
## Diapositiva 32
### Perceptrón
Implementación de funciones lógicas usando un perceptrón:

![imagen](img/image53a.png)

---

<!-- slide -->
## Diapositiva 33
### Perceptrón
Implementación de funciones lógicas usando un perceptrón:

![imagen](img/image57a.png)

---

<!-- slide -->
## Diapositiva 34
### Entrenando un Perceptrón

---

<!-- slide -->
## Diapositiva 35
### Entrenando un perceptrón
- Los sistemas neuronales biológicos no nacen programados con todo el conocimiento.
- Existe un proceso de {verde}(**aprendizaje**) que modifica la red para incluir nueva información.
- En nuestro modelo, el aprendizaje consiste en determinar el conjunto de {amarillo}(**pesos sinápticos**) que permite al perceptrón realizar el cálculo deseado correctamente.

$$\vec{W} = \begin{pmatrix} w_1 \\ w_2 \\ w_3 \\ b \end{pmatrix}$$

![imagen](img/image58a.png)

---

<!-- slide -->
## Diapositiva 36
### Entrenando un perceptrón
- Inicializamos los pesos al {verde}(**azar**) (usualmente entre -1 y 1 por problemas de escala).
- Entrenamos de forma {amarillo}(**iterativa**), mostrando muestras (aprendizaje supervisado) y ajustando pesos según la respuesta.

$$w_i(t + 1) = w_i(t) + \Delta w_i(t)$$

- Se usa una {rojo}(**función de costo**) (o evaluación) para medir cuánto se equivoca el modelo entre la salida estimada y la real (ej: SSE).

$$ E_{SSE} \left( \vec{W} \right) = \frac{1}{2} \sum_{j=1}^{p} \left( d_j - y_j \right)^{2} $$

---

<!-- slide -->
## Diapositiva 37
### Entrenando un perceptrón
{verde}(**Regla de Hebb:**)
- Una sinapsis aumenta su eficacia si las neuronas conectadas tienden a estar activas/inactivas simultáneamente. Caso contrario, se atenúa.
- Similar al *condicionamiento clásico* (Experimento de Pavlov):

![imagen](img/image61a.png)

---

<!-- slide -->
## Diapositiva 38
### Entrenando un perceptrón
{verde}(**Regla de Hebb:**)
- Una sinapsis aumenta en eficacia (peso sináptico) si las dos neuronas conectadas por ella tienden a estar activas o inactivas simultáneamente. En caso contrario, la fuerza de conexión se atenuará.
- Esto puede llevarse a una fórmula de actualización de pesos usando una {amarillo}(**constante de aprendizaje**).

$$\Delta w_{ij} = \eta \cdot x_i \cdot y$$

---

<!-- slide -->
## Diapositiva 39
### Entrenando un perceptrón

{verde}(**Regla del Perceptrón:**)

![imagen](img/image61b.png)

- Desarrollada por Frank Rosenblatt, mejora la Regla de Hebb.
- Las variaciones de los pesos son {amarillo}(**proporcionales al producto**) de las actividades de las neuronas emisoras y receptoras.
- Ante cada patrón, si la salida es {verde}(**correcta**), los pesos no cambian.
- Si es {rojo}(**incorrecta**), se incrementa cada $w_i$ proporcionalmente. (Válido si la salida es escalón).

$$\Delta w_{ij} = \eta \cdot (d_{ij} - y_{ij}) \cdot x_{ij}$$

---

<!-- slide -->
## Diapositiva 40
### Entrenando un perceptrón
{verde}(**Regla del Perceptrón:**)

![imagen](img/image61b.png)

- *Algoritmo de entrenamiento:*

```
while error > 0:
    x_train = reorder(x_train)
    for x in x_train:
        y = perceptron.output(x)
        if d != y:
            weights = perceptron.obtain_weight()
            for w in weights:
                w += eta * (y - d) * x
            perceptron.update_weight(weights)
    error = mse(x_train, perceptron)
```

---

<!-- slide -->
## Diapositiva 41
### Entrenando un perceptrón
{verde}(**Regla del Perceptrón: Interpretación gráfica**)

![imagen](img/image61b.png)

- La fórmula de la parte lineal es equivalente a un {amarillo}(**producto escalar**) (considerando al bias como un peso más asociado a una entrada constante de 1).

$$\sum_{i=1}^{n} w_i x_i + b$$

- Geométricamente, no es más que la ecuación de una {verde}(**recta**) (o hiperplano en dimensiones mayores).

$$\vec{W}^T \vec{X} + b = 0$$

---

<!-- slide -->
## Diapositiva 42
### Entrenando un perceptrón
{verde}(**Regla del Perceptrón: Interpretación gráfica**)
- Si tenemos un caso de dos entradas, podemos visualizar gráficamente la frontera de decisión.

![imagen](img/image82a.png)

---

<!-- slide -->
## Diapositiva 43
### Entrenando un perceptrón
{verde}(**Regla del Perceptrón: Interpretación gráfica**)
- Si tenemos un caso de dos entradas, podemos visualizar gráficamente la frontera de decisión.

![imagen](img/image87a.png)

---

<!-- slide -->
## Diapositiva 44
### Entrenando un perceptrón
{verde}(**Regla del Perceptrón: Interpretación gráfica**)
- Dado que las salidas pueden ser 1 o 0, el perceptrón divide y {amarillo}(**colorea su espacio de entrada**) en dos clases distintas.

![imagen](img/image92a.png)

---

<!-- slide -->
## Diapositiva 45
### Entrenando un perceptrón
{rojo}(**Problema de la Regla del Perceptrón:**)
- Falla si los datos {rojo}(**no son linealmente separables**).
- Si no hay una recta que separe perfectamente las clases, el error nunca será cero.
- Como consecuencia, el bucle de entrenamiento {rojo}(**nunca terminará**).

![imagen](img/image93a.png)

---

<!-- slide -->
## Diapositiva 46
### Entrenando un perceptrón
{verde}(**Aprendiendo por minimización del error**)
- Exigir un error de exactamente *cero* es un requisito demasiado estricto.
- Aún más problemático si usamos funciones de activación {verde}(**continuas**) (diferentes al escalón).
- *Solución:* Readaptar la regla para que {amarillo}(**minimice la función de costo**), haciendo pequeños cambios iterativos en los pesos hasta que el error sea "suficientemente" chico.

$$ E_{SSE} \left( \vec{W} \right) = \frac{1}{2} \sum_{j=1}^{p} \left( d_j - y_j \right)^{2} $$

$$ E_{SSE} \left( \vec{W} \right) = \frac{1}{2} \sum_{j=1}^{p} \left( d_j - f \left(\sum_{i=1}^{n} w_i x_i + b \right)\right)^{2} $$

---

<!-- slide -->
## Diapositiva 47
### Entrenando un perceptrón
{verde}(**Aprendiendo por minimización del error**)
- Con la Regla del Perceptrón original, buscábamos que la salida esté simplemente del lado correcto de la frontera.
- Ahora, buscamos que el vector de pesos se mueva para {amarillo}(**reducir continuamente la función de costo**).
- Esto requiere conocer cómo varía el costo a medida que cambian los pesos: el {amarillo}(**gradiente**).
- Si ajustamos los pesos en la dirección *contraria* al gradiente (descenso de gradiente), llegaremos a un mínimo.

---

<!-- slide -->
## Diapositiva 48
### Entrenando un perceptrón
{verde}(**Aprendiendo por minimización del error**)
- Si analizamos la función de error, observamos que **depende únicamente de los pesos** (las muestras de entrada son fijas).

$$ E_{SSE} \left( \vec{W} \right) = \frac{1}{2} \sum_{j=1}^{p} \left( d_j - y_j \right)^{2} $$

$$ E_{SSE} \left( \vec{W} \right) = \frac{1}{2} \sum_{j=1}^{p} \left( d_j - f \left(\sum_{i=1}^{n} w_i x_i + b \right)\right)^{2} $$
---

<!-- slide -->
## Diapositiva 49
### Entrenando un perceptrón
{verde}(**Aprendiendo por minimización del error**)
- Gráficamente, el descenso de gradiente busca el valle o punto más bajo en la superficie de error:

![imagen](img/image100a.png)

---

<!-- slide -->
## Diapositiva 50
### Entrenando un perceptrón
{verde}(**Aprendiendo por minimización del error**)
- En fórmula, para actualizar los pesos debemos calcular el gradiente:

$$\vec{W} (t + 1) = \vec{W} (t) - \eta \cdot \nabla E_{SSE} \left( \vec{W} (t) \right)$$

$$ \nabla E_{SSE} = \left[ \frac{ \partial E_{SSE} }{ \partial w_{1} }, \frac{ \partial E_{SSE} }{ \partial w_{2} }, \dots, \frac{ \partial E_{SSE} }{ \partial w_{n} } \right]^T $$

---

<!-- slide -->
## Diapositiva 51
### Entrenando un perceptrón
{verde}(**Aprendiendo por minimización del error**)
- Para calcular cómo afecta el peso $w_i$ al error total, aplicamos la {amarillo}(**Regla de la Cadena**):

$$ \frac{\partial E_{SSE}}{\partial w_i} = \sum_{j=1}^{p} \underbrace{ \frac{\partial E_j}{\partial y_j} }_{-(d_j - y_j)} \cdot \underbrace{ \frac{\partial y_j}{\partial z_j} }_{f'(z_j)} \cdot \underbrace{ \frac{\partial z_j}{\partial w_i} }_{x_i} $$

1. **Salida del perceptrón:** $\frac{\partial E_j}{\partial y_j} = -(d_j - y_j)$
2. **Derivada de la activación:** $\frac{\partial y_j}{\partial z_j} = f'(z_j)$
3. **Entrada correspondiente:** $\frac{\partial z_j}{\partial w_i} = x_i$

- Reemplazando todo, obtenemos la derivada parcial final:

$$ \frac{ \partial E_{SSE} }{ \partial w_{i} } = - \sum_{j=1}^{p} \left( d_j - y_j \right) f' \left( z_j \right) x_i $$

---

<!-- slide -->
## Diapositiva 52
### Entrenando un perceptrón
{verde}(**Aprendiendo por minimización del error**)

$$ \frac{ \partial E_{SSE} }{ \partial w_{i} } = - \sum_{j=1}^{p} \left( d_j - y_j \right) f' \left( z_j \right) x_i $$

Observaciones al calcular el gradiente:
  - Limita el uso a funciones de activación que sean {amarillo}(**derivables**).
  - En la práctica, se usan funciones con secciones derivables y se corrigen errores numéricos.
  - El gradiente cambia según la {amarillo}(**función de costo**) elegida.
  - Muchas librerías resuelven esto usando {verde}(**diferenciación automática/numérica**) para abstraer este cálculo.

---

<!-- slide -->
## Diapositiva 53
### Entrenando un perceptrón
{verde}(**Aprendiendo por minimización del error**)
- Esta nueva regla de aprendizaje se conoce como la {amarillo}(**Regla Delta**):

```
while error > threshold:
    x_train = reorder(x_train)
    for x in x_train:
        y = perceptron.output(x)
        error = mse(x_train, perceptron)
        for i, w in enumerate(weights):
            grad_error = gradiente(x[i])
            w = w - eta * grad_error
        perceptron.update_weight(weights)
```

---

<!-- slide -->
## Diapositiva 54
### Entrenando un perceptrón
{verde}(**Aprendiendo por minimización del error**)
El valor de la constante de aprendizaje (learning rate) es crucial:
  - Muy chico: {rojo}(**Demora mucho en aprender**).
  - Muy grande: Puede divergir y {rojo}(**nunca converger**).

![imagen](img/image111a.png)

---

<!-- slide -->
## Diapositiva 55
### Entrenando un perceptrón
{verde}(**Aprendiendo por minimización del error**)
- Este método {rojo}(**no asegura**) encontrar el mínimo global, ya que el descenso puede quedar atascado en un {amarillo}(**mínimo local**).
- *Estrategia:* Entrenar varias veces iniciando los pesos al azar y quedarse con el mejor resultado.

![imagen](img/image113a.png)

---

<!-- slide -->
## Diapositiva 56
### Entrenando un perceptrón
{verde}(**Aprendiendo por minimización del error**)
- Esta forma de aprendizaje nos permite ir más allá de la clasificación.
- Si usamos una función de activación lineal, la red realiza una {verde}(**regresión**).
- Alcanza el mismo resultado que Mínimos Cuadrados, pero mediante un {amarillo}(**proceso iterativo**), útil cuando hay enormes dimensiones u observaciones.

![imagen](img/image114a.png)

---

<!-- slide -->
## Diapositiva 57
### Entrenando un perceptrón
{rojo}(**Limitaciones de la Regla Delta pura:**)
- En cada iteración se debe calcular el error usando {rojo}(**todo el dataset**).
- Si el volumen de datos es inmenso (Big Data), cada paso puede demorar muchísimo tiempo.

```
while error > threshold:
    x_train = reorder(x_train)
    for x in x_train:
        y = perceptron.output(x)
        error = mse(x_train, perceptron)
        for i, w in enumerate(weights):
            grad_error = gradiente(x[i])
            w = w - eta * grad_error
        perceptron.update_weight(weights)
```

---

<!-- slide -->
## Diapositiva 58
### Entrenando un perceptrón
{verde}(**Aprendiendo por minimización del error**)
- Una forma de agilizar el entrenamiento es usando {amarillo}(**mini-batches**) (lotes).

```
while error > threshold:
    x_train = reorder(x_train)

    error = mse(x_train, perceptron)
    batch = subset(x_train)
    accum_delta = zeros(weights)
    
    for x in batch:
        y = perceptron.output(x)
        for i, w in enumerate(weights):
            accum_delta[i] += gradiente(x[i])

        w = w - eta * accum_delta[i]
            
    perceptron.update_weight(weights)
```

---

<!-- slide -->
## Diapositiva 59
### La correcta forma de implementar clasificadores

---

<!-- slide -->
## Diapositiva 60
### Implementación de clasificadores
- Hasta ahora vimos {verde}(**clasificadores binarios**) (dos clases, salida 0 o 1). 
- Para la activación final usábamos Sigmoide o Escalón.
- ¿Pero qué hacemos si tenemos {amarillo}(**más de dos clases**) (ej. Perro, Gato, Tero)?
- *Opción incorrecta:* Asignar un número por clase (0=Perro, 1=Gato, 2=Tero). Esto asume un orden irreal (variable categórica ordinal). ¿Qué significa una salida de 1.35?
- *Solución:* Usar una función de costo más apropiada: la {amarillo}(**Entropía Cruzada Categórica**).

---

<!-- slide -->
## Diapositiva 61
### Implementación de clasificadores
{verde}(**One-Hot Encoding**)
- Para solucionar esto usamos {amarillo}(**one-hot encoding**).
- Hacemos que la red tenga tantas neuronas de salida como clases haya (ej. 3 neuronas para animales).

![imagen](img/image120a.png)

- A este tipo de codificación no le importa si cambiamos el orden de las neuronas.
- Los valores de salida (ej. 0.35, 0.5, 0.15) se pueden interpretar directamente como {verde}(**probabilidades**) (qué tan seguro está el modelo de que es cada clase).

---

<!-- slide -->
## Diapositiva 62
### Implementación de clasificadores
{verde}(**Función de activación Softmax**)
- Ninguna de las funciones de activación que vimos sirve para la última capa en este caso.
- Si la salida es *lineal*, puede tomar valores fuera del rango $[0, 1]$ (no es probabilidad).
- Si usamos *sigmoide*, aunque esté en el rango, {rojo}(**no asegura que la suma de todas las salidas sea 1**).
- *Solución:* Usar la función de activación {amarillo}(**Softmax**).

Dada la salida lineal de la red: $\vec{O} = \vec{X} \vec{W} + b$, *Softmax* se define como:

$$ \vec{Y} = softmax(\vec{O}) $$

$$y_i = \frac{e^{o_i}}{\sum_{j} e^{o_{j}}}$$

---

<!-- slide -->
## Diapositiva 63
### Implementación de clasificadores
{verde}(**Función de activación Softmax**)
- Para definir la clase predicha, simplemente se elige la salida {verde}(**más grande**).

*Ejemplo:*
  - Salida lineal: $O = [1.25, 1.61, 0.40]$
  - Exponencial: $\exp(O) = [3.5, 5.0, 1.5]$
  - Normalizamos: $\text{softmax}(O) = [0.35, 0.5, 0.15]$
  - Hacemos 1 al mayor y el resto 0: $Y = [0, 1, 0]$
---

<!-- slide -->
## Diapositiva 64
### Implementación de clasificadores
{verde}(**Optimización de cálculo con Softmax**)
- Dado que la función exponencial mantiene la {verde}(**monotonía**) (si $a < b$, entonces $\exp(a) < \exp(b)$), no necesitamos calcularla si solo queremos predecir la clase.
- Con solo comparar $O = [1.25, 1.61, 0.40]$, sabemos que el del medio es mayor, dando $Y = [0, 1, 0]$.
- Esto {amarillo}(**ahorra cálculo**) durante la inferencia. Por eso, en muchos frameworks, si indicamos que usaremos entropía cruzada, la capa final no requiere tener Softmax explícitamente para predecir.
---

<!-- slide -->
## Diapositiva 65
### Implementación de clasificadores
{verde}(**Entropía Cruzada Categórica**)
- ¿Cómo obtenemos la función de costo? La salida softmax se puede interpretar como la {amarillo}(**probabilidad condicional**) de cada clase.
- Buscamos encontrar los pesos que {verde}(**maximicen esta probabilidad**) para la clase correcta.

$$P(\vec{Y} | \vec{X}) = \prod_{i=1}^{n} P(Y^{[i]} | X^{[i]})$$

- Queremos que, para todas las observaciones, la probabilidad asignada a la clase verdadera sea lo más cercana a 1.

---

<!-- slide -->
## Diapositiva 66
### Implementación de clasificadores
{verde}(**Entropía Cruzada Categórica**)
- Buscamos los pesos que hagan que el producto de estas probabilidades ({verde}(**verosimilitud**) o *likelihood*) sea lo más grande posible.

$$P(\vec{Y} | \vec{X}) = \prod_{i=1}^{n} P(Y^{[i]} | X^{[i]})$$

- Como maximizar multiplicaciones es numéricamente inestable, calculamos el {amarillo}(**logaritmo de la verosimilitud**) (convierte productos en sumas).
- Y calculamos su negativo para poder usar el algoritmo de {amarillo}(**gradiente descendiente**) (que busca minimizar, no maximizar).

$$-log P(\vec{Y} | \vec{X}) = -log \prod_{i=1}^{n} P(Y^{[i]} | X^{[i]}) = \sum_{i=1}^{n} - log P(Y^{[i]} | X^{[i]})$$

$$\sum_{i=1}^{n} - log P(Y^{[i]} | X^{[i]}) = \sum_{i=1}^{n} l(Y^{[i]}, D^{[i]})$$
---

<!-- slide -->
## Diapositiva 67
### Implementación de clasificadores
{verde}(**Entropía Cruzada Categórica**)
- Así llegamos a nuestra función de costo ideal para problemas multi-clase: la {amarillo}(**Entropía Cruzada Categórica**). Que se define como:

$$l(Y^{[i]}, D^{[i]}) = - \sum_{j} d_j \log(y_j)$$

- Permite encontrar los pesos sinápticos minimizando este error.

---

<!-- slide -->
## Diapositiva 68
### Implementación de clasificadores
{verde}(**Entropía Cruzada Categórica**)

$$l(Y^{[i]}, D^{[i]}) = - \sum_{j} d_j \log(y_j)$$

Analizando los componentes de la fórmula:
  - $d_j$: Salida *real* (del dataset).
  - $y_j$: Probabilidad *predicha* por el modelo.

---

<!-- slide -->
## Diapositiva 69
### Implementación de clasificadores
{verde}(**Entropía Cruzada Categórica**)
- Como tenemos un vector *one-hot encoding*, la salida esperada tiene todo ceros menos el elemento correspondiente a la clase.
- *Ejemplo:* Si la clase real es "Gato", el vector es $[0, 1, 0]$.

$$l(Y^{[i]}, D^{[i]}) = - d_{perro} \log(y_{perro}) - d_{gato} \log(y_{gato}) - d_{tero} \log(y_{tero})$$
$$l(Y^{[i]}, D^{[i]}) = - 0 \log(y_{perro}) - 1 \log(y_{gato}) - 0 \log(y_{tero})$$
$$l(Y^{[i]}, D^{[i]}) = - \log(y_{gato})$$
---

<!-- slide -->
## Diapositiva 70
### Implementación de clasificadores
{verde}(**Entropía Cruzada Categórica**)
- Y si la salida del modelo luego de Softmax es, por ejemplo, $[0.1, 0.8, 0.1]$:

$$l(Y^{[i]}, D^{[i]}) = - \log(y_{gato})$$
$$l(Y^{[i]}, D^{[i]}) = - \log \left( \frac{e^{o_{gato}}}{e^{o_{perro}} + e^{o_{gato}} + e^{o_{tero}}} \right)$$
$$l(Y^{[i]}, D^{[i]}) = - \log \left( e^{o_{gato}} \right) + \log \left( e^{o_{perro}} + e^{o_{gato}} + e^{o_{tero}} \right)$$
$$l(Y^{[i]}, D^{[i]}) = \log \left( e^{o_{perro}} + e^{o_{gato}} + e^{o_{tero}} \right) - o_{gato}$$
---

<!-- slide -->
## Diapositiva 71
### Implementación de clasificadores
{verde}(**El gradiente de Softmax + Entropía Cruzada**)
- Generalizando a cualquier problema, 

$$l(Y^{[i]}, D^{[i]}) = \log \left( \sum_j e^{o_j} \right) - \sum_j d_j o_j$$

- Si calculamos la derivada de la función de costo con respecto a la entrada a la capa:

$$ \frac{ \partial l(Y^{[i]}, D^{[i]}) }{ \partial o_{j} } = \frac{e^{o_{j}}}{ \sum_k e^{o_{k}} } - d_{j}$$

$$ \frac{ \partial l(Y^{[i]}, D^{[i]}) }{ \partial o_{j} } = \text{softmax}(o_j) - d_{j}$$

- Obtenemos que la derivada es, elegantemente, la {amarillo}(**diferencia directa**) entre la probabilidad asignada por el modelo y el verdadero valor (one-hot).

---