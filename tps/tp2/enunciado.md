# Trabajo práctico 2 - Diseño de filtro FIR e IIR

## Análisis y procesamiento de Señales - Bioingeniería - Fac. de Ingeniería - UNSTA

1. Deduzca en forma analítica los coeficientes de los filtros digitales FIR: pasa bajo, pasa altos, pasa bandas y banda stop. Recuerda estos resultados matemáticos:

   $$\int_{a}^{b} e^{-j n \omega} d\omega = \frac{j}{n}\left( e^{-j n b} - e^{-j n a} \right), \quad n \neq 0$$

   **Identidades:**

   - **Formula de Euler:** $e^{jn}= \cos(n)+j \sin(n)$
   - $\sin(\theta) = \frac{e^{j\theta}-e^{-j\theta}}{2j}$
   - $\cos(\theta) = \frac{e^{j\theta}+e^{-j\theta}}{2}$

2. Con los coeficientes obtenidos en el punto 1, implementa un filtro FIR pasa bajos en forma genérica (con $\omega$ entre 0 y $\pi$) y realiza lo siguientes:

   a) Grafica los infinitos coeficientes del filtro.

   b) Genera una ventana rectangular y aplícala a los coeficientes del FIR diseñado (usa 16, 32, 64 y 256 coeficientes) y grafica la respuesta en frecuencia del FIR (módulo y fase).

   c) Encuentra y grafica los polos y ceros del filtro en el plano Z.

   d) Encuentra su respuesta temporal al impulso unitario, escalón y pulso cuadrado. Usa 16 y 32 coeficientes.

3. Repita el punto anterior para un filtro FIR pasa-alto. Pero en este caso usa la función [scipy.signal.firwin](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.firwin.html) (para la cantidad de coeficientes usa 17, 33, 65 y 257).

4. Suponga que la siguiente función representa una señal de presión arterial, definida de la siguiente manera:

   $$p[n] = 80 + \sum_{k=0}^{2} \frac{16 \sqrt{80}}{2 \pi (k+1)^2 -1} \cos \left(2 \pi k \frac{f_c}{f_s} n - \left( 3 (k + 1)^3 - 1 \right) \frac{\pi}{7} \right)$$

   Donde $f_c$ es la frecuencia cardiaca y $f_s$ es la frecuencia de muestreo ($f_s = 400\,\text{Hz}$).

   a) Agrega ruido de línea de 50 Hz de baja amplitud a la señal $p$ y grafica. El ruido debe tener la forma:

   $$\text{Ruido}[n] = A \cos \left(2 \pi \cdot 50 \cdot \frac{n}{f_s}\right)$$

   b) Diseña un filtro (determina el tipo de filtro a usar) para filtrar toda frecuencia fuera del ancho de banda de la señal de presión. Puedes diseñar el filtro manualmente o usar la función [scipy.signal.firwin](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.firwin.html).

   c) Grafica en el plano Z los polos y ceros de la función de transferencia del filtro diseñado. Grafica la respuesta en frecuencia y la respuesta temporal del filtro (respuesta al impulso unitario).

   d) Grafica la señal filtrada y los espectros de la señal de presión sin ruido, la señal con ruido del inciso a, y la señal filtrada. Calcula el SNR previo al filtrado y post-filtrado.

5. Usando el archivo de datos `ecg50.csv`, se dispone de una señal de ECG con ruido de línea de aproximadamente 50 Hz. La señal fue muestreada a 290 Hz. Diseña un filtro FIR para extraer los 50 Hz. Sugerencia: determina el valor exacto del ruido usando el espectro de Fourier de la señal.

   a) Encuentra los coeficientes del filtro.

   b) Implementa ventanas rectangulares de 25 y 51 coeficientes y grafica la respuesta en frecuencia (módulo y fase) del filtro diseñado.

   c) Encuentra $H(z)$ y grafica los polos y ceros del filtro en el plano Z (para 25 y 51 coeficientes).

   d) Aplica ventanas de Hamming y Blackman (en forma separada, de 25 y 51 coeficientes) y grafica nuevamente la respuesta en frecuencia. Compara estos resultados con los coeficientes obtenidos en el inciso b.

   e) Grafica las señales sin filtrar y filtrada (eligiendo el filtro de 51 coeficientes en todos los casos: ventanas Uniforme, Hamming y Blackman).

   f) Grafica los espectros en frecuencia de la señal sin filtrar y las señales filtradas.

   g) Discute los resultados obtenidos.

   h) Encuentra la respuesta temporal (impulso unitario, escalón y pulso cuadrado) de los filtros diseñados con y sin ventanas. En todos los casos usa el filtro de 51 coeficientes.

6. Suponga que la siguiente función representa una señal de presión arterial, definida de la siguiente manera:

   $$p[n] = 80 + \sum_{k=1}^{4} A[k] \cos \left( \Omega_k n - \phi[k] \right)$$

   Donde:

   - $\Omega = [1, 2, 3, 4] \times 2 \pi f_c$, donde $f_c$ es la frecuencia cardiaca.
   - $A = [20,\; 10.024,\; 3.556,\; 0.98]$
   - $\phi = [0,\; -0.5655,\; 1.0053,\; -2.1363]$

   a) Muestre la señal. Elija la frecuencia de muestreo teniendo en cuenta que la frecuencia cardiaca puede ir de 40 a 160 latidos por minuto.

   b) Agrega ruido blanco de baja amplitud (SNR = 25 dB). Grafica la señal y el espectro de la misma.

   c) Diseña un filtro digital IIR pasa-bajo basado en un diseño de filtro analógico para quitar el ruido. El diseño debe realizarse paso a paso, desde el diseño normalizado hasta la aplicación de la transformada bilineal. Grafica la respuesta en frecuencia, la respuesta al impulso y el diagrama de polos y ceros.

   d) Filtra la señal usando el filtro. Grafica la señal y el espectro de la misma y compárala con la señal antes de filtrarse.

7. El archivo **pre_resp.csv** contiene una señal de presión aórtica modulada por la onda respiratoria, cuya frecuencia es significativamente más baja que la de la señal de presión. Sabiendo que la frecuencia cardíaca es de 90 ppm y la frecuencia de muestreo de 200 Hz, diseña un filtro IIR pasa-altos y un FIR pasa-altos para eliminar la onda respiratoria.

   a) Dada la señal, establece la respuesta en frecuencia esperada, determinando atenuaciones esperadas y frecuencias de la zona de transición.

   b) Encuentra los coeficientes de los filtros en función de las características establecidas en el punto anterior. ¿Qué cantidad de coeficientes se obtuvo para cada caso? Grafica la respuesta en frecuencia de los filtros.

   c) Obtén los diagramas de polos y ceros de ambos filtros.

   d) Obtén la respuesta al impulso de ambos filtros.

   e) Aplica los filtros a la señal. Grafica la señal filtrada y sin filtrar.

   f) Calcula el espectro de las señales filtradas y sin filtrar.

   g) Discute los resultados.
