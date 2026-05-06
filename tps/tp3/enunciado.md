# Trabajo práctico 3 - Perceptrones y Multilayer Perceptrons

## Análisis y procesamiento de Señales - Bioingeniería - Fac. de Ingeniería - UNSTA

Para este trabajo práctico, vamos a trabajar con el dataset [Sleep-EDF Expanded](https://www.physionet.org/content/sleep-edfx/1.0.0/sleep-cassette), una colección de grabaciones polisomnográficas (PSG) publicada en PhysioNet. En estas grabaciones se registraron datos de 82 pacientes sanos y 24 pacientes con insomnio, tratados con placebo o temazepam. A cada paciente se le realizaron dos sesiones de sueño separadas. En este trabajo práctico, utilizaremos únicamente los registros de los pacientes sanos.

Los canales registrados durante las sesiones de sueño son los siguientes:

- EEG bipolar FPz-Cz
- EEG bipolar Pz-Oz
- EOG horizontal
- Respiración nasal
- EMG submentoniano
- Temperatura rectal

Las señales de EEG y EOG fueron muestreadas a **100 Hz**.
La señal de EMG fue procesada para obtener su envolvente, y luego muestreada a **1 Hz**.
La respiración y la temperatura corporal también fueron muestreadas a **1 Hz**.

Las grabaciones se realizaron entre 1987 y 1991 en pacientes caucásicos, con edades entre 25 y 101 años. A cada uno se le realizó un PSG de aproximadamente 20 horas durante dos noches consecutivas. Se incluye un [archivo de Excel](aux/sc-subjects.csv) con la descripción de cada paciente.

Los archivos que almacenan los registros PSG siguen la siguiente nomenclatura:
SC4**ssN**, donde **ss** representa el identificador del paciente y **N** la noche correspondiente.
Se incluye un archivo de Excel con la descripción detallada de cada paciente.

Una vez finalizadas las sesiones, técnicos especializados anotaron manualmente las etapas del sueño en ventanas de 30 segundos, usando las siguientes etiquetas:

- **W**: El paciente está despierto
- **R**: Fase REM del sueño
- **1**: Fase 1 del sueño
- **2**: Fase 2 del sueño
- **3, 4**: Fase 3 del sueño (anteriormente separadas en dos fases)
- **M**: Movimiento (el paciente se está moviendo)
- **?**: Fase no identificada

Para simplificar el trabajo, hemos preprocesado las señales, dividiéndolas en ventanas de 30 segundos con sus correspondientes etiquetas. Cada señal ha sido almacenada individualmente en archivos **.parquet**. Para cada PSG de cada paciente, se dispone de los siguientes archivos:

- SC4**ssN**_eeg__fpz_cz.parquet
- SC4**ssN**_eeg__pz_oz.parquet
- SC4**ssN**_eog__horizontal.parquet
- SC4**ssN**_emg__submental.parquet
- SC4**ssN**_resp__oro_nasal.parquet
- SC4**ssN**_temp__rectal.parquet
- SC4**ssN**_labels.parquet

Cada archivo contiene una de las señales indicadas en su nombre, mientras que *SC4ssN_labels.parquet* incluye la clasificación de las fases del sueño correspondientes a cada ventana.

1. El primer objetivo de este trabajo práctico es leer las señales de al menos una sesión de un paciente y extraer características (features) de cada ventana de 30 segundos. Para esto, se deben realizar las siguientes tareas:

   a) Leer las señales desde los archivos .parquet.

   b) Descartar las ventanas de 30s correspondientes a **M** y **?**. Unificar las etiquetas **3** y **4** en una sola etiqueta **3**.

   c) Calcular características en el dominio del tiempo, como las vistas en la materia *Señales y Sistemas*, por ejemplo:
      - Valor RMS
      - Media, desviación estándar, etc.

   d) Calcular características en el dominio de la frecuencia, como:
      - Frecuencia dominante
      - Potencia espectral en diferentes bandas.

   e) Realizar visualizaciones comparativas de los atributos extraídos en función de las distintas fases del sueño. Algunas sugerencias:
      - Histogramas
      - Diagramas de caja (boxplots)
      - Gráficos de dispersión (scatter plots)

      Se busca que analicen si alguna de estas características permite distinguir visualmente las fases del sueño. Elijan entre 3 y 5 visualizaciones representativas, e incluya una breve explicación de lo que se observa en cada una. 

   f) En el caso de las señales EEG, se espera además calcular características específicas en las **bandas cerebrales**:
      - Delta (0.5–4 Hz)
      - Theta (4–8 Hz)
      - Alpha (8–12 Hz)
      - Beta (12–30 Hz)
      - Gamma (>30 Hz)


2. Usando un perceptrón, se deberá construir un clasificador que, a partir de los atributos extraídos en el punto 1, determine si el paciente está despierto o dormido.
   Instrucciones:

   a) Trabaje con **al menos una sesión** de PSG, aunque se recomienda usar **dos o tres** para obtener resultados más generalizables.

   b) Defina el label binario:
      - **0** si el paciente está despierto (**label = "W"**)
      - **1** si el paciente está dormido (cualquier otra fase válida)

      Indique cuántas observaciones hay de cada clase (0 y 1).

   c) Divida el conjunto de datos en:
      - 60% entrenamiento
      - 30% testeo
      - 10% validación

      La separación debe realizarse de **forma aleatoria**, pero manteniendo en lo posible **la proporción de clases**. Haga el preprocesamiento necesario para el dataset. Por ejemplo, normalizar, completar nulos.

   d) Diseñe un modelo baseline para comparación. Por ejemplo:
      - Elegir un único atributo
      - Establecer un umbral para decidir si el paciente está dormido o no (por ejemplo: dormido si RMS de EEG Fpz - Cz ≤ 30)

   e) Defina e implemente un perceptrón para este problema:
      - Elija función de activación
      - Elija el tamaño de bache
      - Seleccione una función de costo
      - Elija un algoritmo de entrenamiento e implemente el código de entrenamiento
      - Justifique las decisiones

   f) Evalúe el modelo utilizando:
      - Accuracy
      - Precision, Recall y F1-score para cada clase

      Compare los resultados con el baseline. ¿Fue mejor el modelo? ¿En qué clase se desempeñó mejor? Argumente.

   g) Calcule la curva ROC y el AUC del modelo para la clase "el paciente está dormido". Incluya la curva y discuta los resultados obtenidos.

3. De manera similar al punto anterior, en este caso se deberá implementar un clasificador binario utilizando un Multilayer Perceptron (MLP), con el objetivo de determinar si el paciente está durmiendo o despierto a partir de los atributos extraídos.
   Instrucciones:

   a) Trabaje con **al menos una sesión** de PSG, aunque se recomienda usar **dos o tres** para obtener resultados más generalizables.

   b) Defina el label binario:
      - **0** si el paciente está despierto (**label = "W"**)
      - **1** si el paciente está dormido (cualquier otra fase válida)

      Indique cuántas observaciones hay de cada clase (0 y 1).

   c) Divida el conjunto de datos en:
      - 60% entrenamiento
      - 30% testeo
      - 10% validación

      La separación debe realizarse de **forma aleatoria**, pero manteniendo en lo posible **la proporción de clases**. Haga el preprocesamiento necesario para el dataset. Por ejemplo, normalizar, completar nulos.

   d) Defina e implemente un MLP para este problema:
      - Defina la capas a usar y cantidad de neuronas por capa (se recomienda no extender a más de 3 capas y mantener el número bajo de neuronas).
      - Defina las funciones de activación en las capas.
      - Elija el tamaño de bache
      - Seleccione una función de costo
      - Elija un algoritmo de entrenamiento e implemente el código de entrenamiento
      - Justifique las decisiones

   e) Evalúe el modelo utilizando:
      - Accuracy
      - Precision, Recall y F1-score para cada clase

      Compare los resultados con el baseline y el perceptrón. ¿Fue mejor el modelo? ¿En qué clase se desempeñó mejor? Argumente.

   f) Calcule la curva ROC y el AUC del modelo para la clase "el paciente está dormido". Incluya la curva y discuta los resultados obtenidos.

4. Siguiendo un procedimiento similar a los puntos anteriores, en este caso se deberá implementar un clasificador multiclase utilizando un Multilayer Perceptron (MLP) para identificar la fase del sueño en la que se encuentra el paciente.
   Instrucciones:

   a) Trabaje con **al menos una sesión** de PSG, aunque se recomienda usar **dos o tres** para obtener resultados más generalizables.

   b) Defina el label multiclase con todas las fases del sueño. Indique cuántas observaciones hay de cada clase.

   c) Divida el conjunto de datos en:
      - 60% entrenamiento
      - 30% testeo
      - 10% validación

      La separación debe realizarse de **forma aleatoria**, pero manteniendo en lo posible **la proporción de clases**. Haga el preprocesamiento necesario para el dataset. Por ejemplo, normalizar, completar nulos.

   d) Diseñe un modelo baseline para comparación. Busque una función heurística con pocos atributos para clasificar.

   e) Defina e implemente un MLP para este problema:
      - Defina la capas a usar y cantidad de neuronas por capa (se recomienda no extender a más de 3 capas y mantener el número bajo de neuronas).
      - Defina las funciones de activación en las capas.
      - Elija el tamaño de bache
      - Seleccione una función de costo
      - Elija un algoritmo de entrenamiento e implemente el código de entrenamiento
      - Justifique las decisiones

   f) Evalúe el modelo utilizando:
      - Accuracy global
      - Precision, Recall y F1-score para cada clase
      
      Compare los resultados con el baseline. ¿Fue mejor el modelo? ¿En qué clase se desempeñó mejor? Argumente.

   g) Calcule la curva ROC y el AUC del modelo para la clase "el paciente está en fase REM". Incluya la curva y discuta los resultados obtenidos.