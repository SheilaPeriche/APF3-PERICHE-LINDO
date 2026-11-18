# APF-3: DETECTOR DE LAPTOPS MEDIANTE VISIÓN COMPUTACIONAL

**Estudiante:** Sheila Periche Lindo  
**Carrera:** Ingeniería Civil  
**Curso:** HERRAMIENTAS DE DESARROLLO PROFESIONAL EN IC - 49744
**Tecnologías:** Python, OpenCV, Haar Cascade, Cascade Trainer GUI y Visual Studio Code.

## 1. Descripción del proyecto

Este proyecto desarrolla una solución básica de Visión Computacional aplicada a Ingeniería Civil, orientada a la detección de laptops mediante un clasificador Haar Cascade.

El sistema procesa imágenes capturadas en tiempo real mediante una cámara conectada a través de DroidCam, utilizando OpenCV para identificar posibles objetos de interés.

## 2. Objeto seleccionado

El objeto seleccionado es una laptop, considerada un equipo tecnológico utilizado en actividades de diseño, supervisión, modelamiento y gestión de proyectos de Ingeniería Civil.

## 3. Construcción del dataset

Se elaboró un conjunto de datos propio compuesto por:

- Dataset positivo (p): 100 fotografías de laptops.
- Dataset negativo (N): 200 fotografías sin presencia de laptops.

Las imágenes fueron capturadas mediante DroidCam y recortadas a dimensiones de 38 × 36 píxeles.

Se buscó incorporar variaciones de posición, distancia, iluminación y fondo.

## 4. Entrenamiento del modelo

Para el entrenamiento se utilizó Cascade Trainer GUI versión 3.3.1.

Configuración empleada:

- Tipo de característica: HAAR.
- Tipo de característica Haar: BASIC.
- Dimensiones de muestra: 24 × 24 píxeles.
- Tipo de Boost: GAB.
- Número de etapas solicitado: 20.
- Número máximo de clasificadores débiles: 100.
- Tasa mínima de detección: 0.995.
- Tasa máxima de falsas alarmas: 0.500.

Como resultado se obtuvo el archivo `cascade.xml`, que posteriormente fue cargado mediante OpenCV.

## 5. Implementación

La programación se realizó en Python utilizando OpenCV.

El sistema incorpora:

- Conexión con DroidCam.
- Carga del clasificador Haar Cascade.
- Conversión de imágenes a escala de grises.
- Detección de posibles laptops.
- Representación de rectángulos y etiquetas.
- Visualización de resultados en tiempo real.

El archivo principal de ejecución es `APF3_NombreApellido.py`.

## 6. Resultados obtenidos

Durante las pruebas se verificó que OpenCV podía cargar correctamente el archivo `cascade.xml`.

Sin embargo, durante la detección en tiempo real se observaron múltiples rectángulos y falsos positivos, incluyendo objetos diferentes a una laptop.

La revisión del archivo XML permitió identificar que el clasificador generado contenía cinco etapas, aunque inicialmente se habían configurado veinte.

Por tanto, el funcionamiento técnico del detector fue comprobado, pero su capacidad de reconocimiento preciso requiere mejoras.

## 7. Limitaciones y posibles mejoras

Entre las principales limitaciones identificadas se encuentran:

- Cantidad limitada de imágenes positivas y negativas.
- Posibles similitudes visuales entre la laptop y otros objetos.
- Capacidad discriminativa limitada del clasificador generado.
- Necesidad de mejorar la preparación de muestras.
- Presencia de falsos positivos durante la detección.

Como mejoras se propone incrementar la diversidad del dataset, revisar la generación de muestras positivas, optimizar el entrenamiento y realizar nuevas pruebas de validación.

## 8. Aplicación en Ingeniería Civil

La identificación automatizada de equipos tecnológicos mediante Visión Computacional representa una aplicación potencial en entornos de construcción.

Este tipo de tecnología puede servir como base para desarrollar sistemas de reconocimiento de equipos, supervisión visual y automatización de procesos relacionados con la gestión de recursos en proyectos de Ingeniería Civil.

## 9. Conclusiones

Se desarrolló una experiencia práctica de Visión Computacional mediante OpenCV y clasificadores Haar Cascade, utilizando un dataset construido personalmente.

Se logró generar y cargar un modelo de clasificación, además de implementar un sistema de detección en tiempo real mediante DroidCam.

Las pruebas evidenciaron limitaciones en la identificación precisa de laptops, principalmente por la presencia de falsos positivos.

Finalmente, el proyecto permitió comprender las etapas de construcción de datasets, entrenamiento de clasificadores e implementación de modelos de reconocimiento visual, así como la importancia de validar los resultados antes de aplicar estas tecnologías en situaciones reales.