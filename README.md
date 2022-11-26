# Informe Escrito

## Autor

| **Nombre y Apellidos** |         **Correo**         |               **GitHub**               |
| :--------------------: | :------------------------: | :------------------------------------: |
|  Ariel Plasencia Díaz  | arielplasencia00@gmail.com | [@ArielXL](https://github.com/ArielXL) |

## Notas de la tarea

La tarea consiste en la comparación de una imagen digital en escala de grises con su respectiva imagen, pero con los bordes resaltados, en cuanto a varios algoritmos que miden la calidad de las imágenes digitales.

### Implementación

La tarea está implementada en [python 3](https://es.wikipedia.org/wiki/Python). Nos apoyamos fundamentalmente en las librerías [pil](https://pillow.readthedocs.io/en/stable/reference/Image.html), [numpy](https://numpy.org/doc/stable/), [matplotlib](https://matplotlib.org/stable/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py), [opencv](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html) y [skimage](https://scikit-image.org/docs/dev/user_guide.html).

Para la instalación de las mismas ejecutamos el siguiente comando:

```bash
pip install -r requirements.txt
```

### Ejecución

Para ejecutar nuestra propuesta de implementación escribimos en una terminal abierta en este mismo directorio:

```bash
cd src/
python main.py
```

En la carpeta [img](./img/) podemos encontrar varias imágenes de muestra. Nuestra tarea fue probada con varias imágenes digitales en escala de grises, muy conocidas y reconocidas en la literatura consultada. También dejamos al usuario la elección de varios algoritmos para el resaltado de los bordes, el cual debe especificar al ejecutar esta tarea.

## Detección de bordes en imágenes digitales

### Algoritmo mediante el operador Canny

* Es un operador desarrollado por John F. Canny en 1986.

* Es un algoritmo de múltiples etapas para detectar una amplia gama de bordes en imágenes.

* Utiliza el cálculo de variaciones, una técnica que encuentra la función que optimiza un funcional indicado. La función óptima en el algoritmo  de Canny es descrito por la suma de cuatro términos exponenciales, pero  se puede aproximar por la primera derivada de una gaussiana.

* Podemos encontrar nuestra propuesta de implementación [aquí](./src/edge_detection/canny.py).

### Algoritmo mediante el operador Sobel

* Es un operador diferencial discreto que calcula una aproximación al gradiente de la función de intensidad de una imagen. Para cada punto de la imagen a procesar, el resultado del operador Sobel es tanto el vector gradiente correspondiente como la norma de este vector.

* Calcula el gradiente de la intensidad de una imagen en cada píxel. Así, para cada píxel, este operador da la magnitud del mayor cambio  posible, la dirección y el sentido desde oscuro a claro.

* Podemos encontrar nuestra propuesta de implementación [aquí](./src/edge_detection/sobel.py).

### Algoritmo mediante el operador Laplace

* Es un operador diferencial de segundo orden con invariancia de rotación.

* Es fácilmente afectado por el ruido.

* No puede detectar la dirección del borde, generalmente no se usa directamente para detectar bordes, sino para juzgar cambios entre claros y oscuros.

* Se usa principalmente para determinar si los píxeles de borde se tratan como áreas brillantes u oscuras de la imagen.

* Podemos encontrar nuestra propuesta de implementación [aquí](./src/edge_detection/laplace.py).

### Algoritmo mediante el operador Scharr

* Es es un método de filtrado utilizado para identificar y resaltar bordes (características) de degradado utilizando la primera derivada.
* Normalmente se utiliza para identificar gradientes a lo largo del eje x (dx = 1, dy = 0) y el eje y (dx = 0, dy = 1) de forma independiente.
* El rendimiento es bastante similar al del filtro Sobel y se utiliza principalmente para detectar bordes (cambios) en la intensidad de los píxeles.
* Podemos encontrar nuestra propuesta de implementación [aquí](./src/edge_detection/scharr.py).

### Algoritmo mediante el operador Prewitt

* Fue desarrollado por Judith Prewitt.
* Se utiliza en el procesamiento de imágenes, particularmente dentro de los algoritmos de detección de bordes.
* Técnicamente, es un operador de diferenciación discreta que calcula una aproximación del gradiente de la función de intensidad de la imagen. En cada punto de la imagen, el resultado del operador es el vector de gradiente correspondiente o la norma de este vector.
* Se basa en convolucionar la imagen con un filtro pequeño, separable y de valor entero en direcciones horizontales y verticales y, por lo tanto, es relativamente económico en términos de cálculos.
* La aproximación de gradiente que produce es relativamente tosca, en particular para variaciones de alta frecuencia en la imagen.
* Podemos encontrar nuestra propuesta de implementación [aquí](./src/edge_detection/prewitt.py).

### Algoritmo mediante el operador Farid

* Es el más invariantes rotacionalmente, porque requiere de un kernel más grande, que es computacionalmente más intensivo que los kernels utilizados anteriormente.
* Propone usar un par de núcleos, uno para interpolación y otro para diferenciación.
* Estos núcleos, de tamaños fijos, están optimizados para que la Transformada de Fourier se aproxime a su relación derivada correcta.
* Podemos encontrar nuestra propuesta de implementación [aquí](./src/edge_detection/farid.py).

### Algoritmo mediante el operador Roberts

* Realiza una medición de gradiente espacial simple y rápida de calcular en una imagen.
* Resalta regiones de alta frecuencia espacial que a menudo corresponden a bordes. En su uso más común, la entrada al operador es una imagen en escala de grises, al igual que la salida.
* Los valores de píxeles en cada punto de la salida representan la magnitud absoluta estimada del gradiente espacial de la imagen de entrada en ese punto.
* En teoría, el operador consta de un par de núcleos de convolución. Esto es muy similar al operador de Sobel.
* Podemos encontrar nuestra propuesta de implementación [aquí](./src/edge_detection/roberts.py).

## Medidas para medir la calidad de las imágenes

### Error cuadrático medio (mean squared error)

1. Lo llamaremos *MSE* (mean squared error) por sus siglas en inglés.

2. Es un estimador que mide el promedio de los errores al cuadrado, es decir, la diferencia entre el estimador y lo que se estima.

3. Es una función de riesgo correspondiente al valor esperado de la pérdida del error al cuadrado.

4. Cuanto menor sea el valor de *MSE*, mejor será la calidad de la imagen reconstruida.

5. Dada una imagen $I$ cuyas dimensiones son $m × n$ y su aproximación $K$ . El error cuadrático
   medio se define como:
$$
MSE = \frac{1}{m n} \sum_{i = 0}^{m -1} \sum_{j = 0}^{n - 1} (I(i, j) - K(i, j))^2
$$

### **Proporción máxima de señal a ruido** (peak signal-to-noise ratio)

1. Lo llamaremos *PSNR* (peak signal-to-noise ratio) por sus siglas en inglés.

2. Evalúa la relación entre la imagen y el ruido luego de aplicar algoritmos de mejora de la calidad de la imagen.

3. Se expresa generalmente en escala logarítmica, utilizando como unidad el decibelio.

4. Cuanto más alto sea el *PSNR*, mejor será la calidad de la imagen reconstruida.

5. Se define como:
   $$
   PSNR = 20 \log_{10}({MAX_{I}}) - 10 \log_{10}({MSE})
   $$
   donde $MAX_{I}$ es el máximo valor posible de píxeles en la imagen.

### Índice de similitud estructural (structural similarity)

1. Lo llamaremos *SSIM* (structural similarity) por sus siglas en inglés.

2. Se utiliza para medir la similitud entre dos imágenes y se basa en la sistema de visión humana.

3. Es un modelo basado en  la percepción que considera la degradación de la imagen como un cambio  percibido en la información estructural, al tiempo que incorpora  importantes fenómenos de percepción, incluidos términos de  enmascaramiento de luminancia y enmascaramiento de contraste.

4. La diferencia con medidas como *MSE* o *PSNR* es que estos enfoques se computan con información global de toda la imagen.

5. Se calcula en varias ventanas de una imagen. La medida entre dos ventanas $x$ y $y$ de igual tamaño $N x N$ es:
    $$
    SSIM(x, y) = \frac{(2 \mu_{x} \mu_{y} + c_{1})(2 \sigma_{xy} + c_{2})}{(\mu_{x}^{2} + \mu_{y}^{2} + c_{1})(\sigma_{x}^{2} + \sigma_{y}^{2} + c_{2})}
    $$
    donde $\mu_{x}$ es la media de $x$, $\mu_{y}$ es la media de $y$, $\sigma_{x}^{2}$ es la varianza de $x$, $\sigma_{y}^{2}$ es la varianza de $y$, $\sigma_{xy}^{2}$ es la covarianza de $x$ y $y$, $c_{1} = (k_{1}L)^{2}$ y $c_{2} = (k_{2}L)^{2}$ son dos variables para estabilizar la división en el denominador, $L$ es el rango dinámico de la imagen (diferencia entre la mayor y menor intensidad de gris), $k_{1} = 0.01$ y $k_{2} = 0.03$ son tomados valores por defecto.

### Contraste de Michelson

1. Mide la utilización del rango de luminosidad.

2. El contraste de Michelson varı́a de 0 a 1.

3. Se calcula mediante la formula:
   $$
   C_{Michelson} = \dfrac{f_{max} - f_{min}}{f_{max} + f_{min}}
   $$
   donde $f_{max}$ y $f_{min}$ son la mayor y la menor intensidad de los píxeles respectivamente.
