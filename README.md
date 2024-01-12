# entrenador-pronunciacion-japones

Este script de Python está diseñado para la reproducción auditiva de números en japonés junto con sus significados en español utilizando síntesis de voz. La intención es que puedas practicar la pronunciación de los números en voz alta mientras realizas tus actividades diarias, como ejercicio físico o desplazamientos.

## Requisitos

- Python 3.x
- Bibliotecas: `gtts`, `pygame`

Instala las dependencias usando:

```bash
pip install gtts pygame
```

Asegúrate de tener un archivo de sonido llamado `ding.mp3` en la misma carpeta que cada script. Este archivo se utiliza para el sonido de pitido.

## Scripts disponibles

### 1. entrenar_numeros_japoneses_spanish.py

Este script genera números aleatorios en japonés y reproduce su pronunciación y significado en español. Tendrás un margen de 10 segundos para reflexionar sobre el número y luego verificar su corrección (este parámetro es ajustable).

#### Uso

1. Clona o descarga este repositorio.
2. Ejecuta el script `1_entrenar_numeros_japoneses_spanish.py`.
3. El script generará 10 números aleatorios en japonés y reproducirá su pronunciación y significado en español.

#### Notas

- Es necesario tener una conexión a internet activa para que la síntesis de voz (gTTS) funcione correctamente.
- Los archivos de audio se generarán en una carpeta temporal llamada temp en el directorio donde se ejecute el script.
- Los números reproducidos van desde el 1 hasta el 99 y no se repetirán en cada ejecución del script.

### 2. entrenar_numeros_spanish_japoneses

Este script genera archivos de audio con la pronunciación en japonés y el significado en español de los números. Tienes un tiempo de 10 segundos para pensar en el número y luego comprobar su correspondencia (este parámetro es ajustable).

#### Uso

1. Clona o descarga este repositorio.
2. Ejecuta el script `2_entrenar_numeros_spanish_japoneses.py`.
3. El script generará 10 números aleatorios en japonés y reproducirá su pronunciación y significado en español.

#### Notas

- Asegúrate de tener una conexión a internet activa para que la síntesis de voz (`gTTS`) funcione correctamente.
- Los archivos de audio se generarán en una carpeta temporal llamada `temp` en el directorio donde se ejecuta el script.
- Los números reproducidos irán desde el 1 hasta el 99 y no se repetirán en cada ejecución del script.

### 3. generar_combinaciones_hiragana

Este script genera ejercicios de combinación entre pronunciación en japonés (romaji) y caracteres hiragana. Cada ejercicio consiste en 12 opciones aleatorias sin repeticiones, y se generan múltiples conjuntos de ejercicios. Puedes añadir y modificar los hiraganas con los que uses necesites!

#### Uso

1. Clona o descarga este repositorio.
2. Ejecuta el script `3_generar_combinaciones_hiragana.py`.
3. El script generará 15 conjuntos de ejercicios, cada uno con 12 opciones aleatorias de pronunciación en japonés y caracteres hiragana.

#### Notas

- Asegúrate de tener una conexión a internet activa para el correcto funcionamiento del script.
- Las opciones incluyen números y hiraganas, y no se repetirán dentro de cada conjunto de ejercicios.
- Los conjuntos de ejercicios y sus respuestas se imprimirán por separado en la consola.
- Los hiraganas se representan con el carácter "・" al final para indicar la separación en japonés.

Recuerda ajustar la cantidad de conjuntos (`numero_combinaciones`) según tus necesidades.

## Audios preparados

Audios preparados
Si prefieres evitar el uso del script, se incluyen 2 ejemplos de audio con números en japonés a español y viceversa en la carpeta "ipod":

```bash
ipod/jp_2_sp_intento1.mp3
ipod/jp_2_sp_intento2.mp3
ipod/sp_2_jp_intento1.mp3
ipod/sp_2_jp_intento2.mp3
```

Estos archivos ya contienen la reproducción de números con sus respectivos significados en los idiomas correspondientes para tu conveniencia.
