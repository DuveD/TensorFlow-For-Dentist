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
>`--graph=tf_files/retrained_graph.pb \`  
>`--image=tf_files/prueba/original.jpeg`

## Comando para ejecutar TensorBoard: Una manera visual de consultar el entrenamiento de la red neuronal

Ejecutando el siguiente comando antes del entrenamiento y accediendo al enlace que se genera, podremos ver la evolución del a red neuronal de TensorFlow así como la **Training accuracy**, la **Validation accuracy** y el **Cross entropy** del entrenamiento.

>`tensorboard --logdir tf_files/training_summaries &`

## Desarollado con

* [Python](https://www.python.org/) - Lenguaje de la aplicación

  > [Pillow](http://pillow.readthedocs.io) - Python Imaging Library

* [TensorFlow](https://www.tensorflow.org/) - Framework de machine learning para el aprendizaje automático e identificación de patrones

## Enlaces

* [Pip](https://pip.pypa.io/) - Adminsitrador de paquetes de Python

* [TensorFlow for poets 2](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/) - Image Classifier with TensorFlow for Poets
