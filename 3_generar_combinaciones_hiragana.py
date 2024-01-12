# -*- coding: utf-8 -*-
import random

kanjis_hiragana = [
    ("Ichi", "一"),
    ("Ni", "二"),
    ("San", "三"),
    ("Yon", "四"),
    ("Go", "五"),
    ("Roku", "六"),
    ("Shichi", "七"),
    ("Hachi", "八"),
    ("Kyuu", "九"),
    ("Juu", "十"),
    ("A", "あ"),
    ("I", "い"),
    ("U", "う"),
    ("E", "え"),
    ("O", "お"),
    ("Ka", "か"),
    ("Ki", "き"),
    ("Ku", "く"),
    ("Ke", "け"),
    ("Ko", "こ"),
    ("Ga", "が"),
    ("Gi", "ぎ"),
    ("Gu", "ぐ"),
    ("Ge", "げ"),
    ("Go", "ご")
]

# Seleccionar 12 opciones aleatorias sin repeticiones
opciones_aleatorias = random.sample(kanjis_hiragana, 12)

# Número de combinaciones deseadas
numero_combinaciones = 15

# Almacenar las combinaciones en un array
combinaciones_guardadas = []

for _ in range(numero_combinaciones):
    combinacion_actual = random.sample(kanjis_hiragana, 12)
    combinaciones_guardadas.append(combinacion_actual)

# Imprimir los ejercicioes guardadas
for i, combinacion in enumerate(combinaciones_guardadas, start=1):
    print(f"Ejercicio {i}: {' '.join([f'{j} ・' for j, k in combinacion])}")

# Imprimir las respuestas guardadas
for i, combinacion in enumerate(combinaciones_guardadas, start=1):
    print(f"Respuesta {i}: {' '.join([f'{k} ・ ' for j, k in combinacion])}")
