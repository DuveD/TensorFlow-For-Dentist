# TensorFlow For Dentist

## Visión general

Este repositorio contiene una versión simplificada y reducida de las aplicaciones de clasificación de imágenes básicas de tensorflow.

## Empezando

La aplicación está basada en el código de la serie "TensorFlow for poets 2" de codelabs orientado al reconocimiento de implantes bucales para la asignatura de PAE de la Facultad de Informática de Barcelona.

## Usage

#### Comando para entrenar tensorflow con flag de iteraciones en 500

>`python3 -m scripts.retrain \`  
>`--how_many_training_steps=500`

#### Comando para entrenar tensorflow con 4000 iteraciones por defecto

>`python3 -m scripts.retrain`

#### Comando para probar a identificar un imagen

>`python3 -m scripts.label_image \`  
>`--graph=tf_files/retrained_graph.pb  \`  
>`--image=tf_files/trainning/BranemarkMkIII+/28906.jpg`

#### Variables de entorno posiblemente necesarias para los scripts

>`IMAGE_SIZE=224`  
>`ARCHITECTURE="mobilenet_0.50_${IMAGE_SIZE}"`

## Desarollado con

* [Python 3.5.2](https://www.python.org/) - Lenguaje de la aplicación

* [Pip 9.0.3](https://pip.pypa.io/) - Adminsitrador de paquetes de Python

* [TensorFlow](https://www.tensorflow.org/) - Framework de machine learning para el aprendizaje automático e identificación de patrones

## Enlaces

* [TensorFlow for poets 2](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/) - Image Classifier with TensorFlow for Poets
