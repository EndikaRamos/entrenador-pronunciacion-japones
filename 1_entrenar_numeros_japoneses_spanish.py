# -*- coding: utf-8 -*-
from gtts import gTTS
import pygame
import time
import os
import random

# Configuración de Pygame para reproducir el sonido
pygame.init()
pygame.mixer.init()
ruta_pitido = os.path.join('assets', f'ding.mp3')
ding_sound = pygame.mixer.Sound(ruta_pitido)  # Archivo de sonido corto (puedes usar tu propio archivo)

# Definir el tiempo de espera global
tiempo_espera = 10  # Puedes ajustar este valor según sea necesario

# Crear carpeta 'temp' si no existe
if not os.path.exists('temp'):
    os.makedirs('temp')

# Diccionario con los números en japonés y su lectura en romaji
numeros_japoneses = {
    1: 'ichi',
    2: 'ni',
    3: 'san',
    4: 'shi/yon',
    5: 'go',
    6: 'roku',
    7: 'shichi/nana',
    8: 'hachi',
    9: 'kyū/ku',
    10: 'jū',
    11: 'jūichi',
    12: 'jūni',
    13: 'jūsan',
    14: 'jūshi/jūyon',
    15: 'jūgo',
    16: 'jūroku',
    17: 'jūshichi/jūnana',
    18: 'jūhachi',
    19: 'jūkyū/jūku',
    20: 'nijū',
    21: 'nijūichi',
    22: 'nijūni',
    23: 'nijūsan',
    24: 'nijūshi/nijūyon',
    25: 'nijūgo',
    26: 'nijūroku',
    27: 'nijūshichi/nijūnana',
    28: 'nijūhachi',
    29: 'nijūkyū/nijūku',
    30: 'sanjū',
    31: 'sanjūichi',
    32: 'sanjūni',
    33: 'sanjūsan',
    34: 'sanjūshi/sanjūyon',
    35: 'sanjūgo',
    36: 'sanjūroku',
    37: 'sanjūshichi/sanjūnana',
    38: 'sanjūhachi',
    39: 'sanjūkyū/sanjūku',
    40: 'yonjū',
    41: 'yonjūichi',
    42: 'yonjūni',
    43: 'yonjūsan',
    44: 'yonjūshi/yonjūyon',
    45: 'yonjūgo',
    46: 'yonjūroku',
    47: 'yonjūshichi/yonjūnana',
    48: 'yonjūhachi',
    49: 'yonjūkyū/yonjūku',
    50: 'gojū',
    51: 'gojūichi',
    52: 'gojūni',
    53: 'gojūsan',
    54: 'gojūshi/gojūyon',
    55: 'gojūgo',
    56: 'gojūroku',
    57: 'gojūshichi/gojūnana',
    58: 'gojūhachi',
    59: 'gojūkyū/gojūku',
    60: 'rokuju',
    61: 'rokujuichi',
    62: 'rokujun',
    63: 'rokujuusan',
    64: 'rokujuushi/rokujuuyon',
    65: 'rokujuugo',
    66: 'rokujuuroku',
    67: 'rokujuushichi/rokujuunana',
    68: 'rokujuuhachi',
    69: 'rokujuukyuu/rokujuuku',
    70: 'nanajuu',
    71: 'nanajuuichi',
    72: 'nanajuuni',
    73: 'nanajuusan',
    74: 'nanajuushi/nanajuuyon',
    75: 'nanajuugo',
    76: 'nanajuuroku',
    77: 'nanajuushichi/nanajuunana',
    78: 'nanajuuhachi',
    79: 'nanajuukyuu/nanajuuku',
    80: 'hachijuu',
    81: 'hachijuichi',
    82: 'hachijuuni',
    83: 'hachijuusan',
    84: 'hachijuushi/hachijuuyon',
    85: 'hachijuugo',
    86: 'hachijuuroku',
    87: 'hachijuushichi/hachijuunana',
    88: 'hachijuuhachi',
    89: 'hachijuukyuu/hachijuuku',
    90: 'kyuujuu',
    91: 'kyuujuuichi',
    92: 'kyuujuuni',
    93: 'kyuujuusan',
    94: 'kyuujuushi/kyuujuuyon',
    95: 'kyuujuugo',
    96: 'kyuujuuroku',
    97: 'kyuujuushichi/kyuujuunana',
    98: 'kyuujuuhachi',
    99: 'kyuujuukyuu/kyuujuuku'
}

# Diccionario con los significados de los números
significados = {
    1: 'Uno',
    2: 'Dos',
    3: 'Tres',
    4: 'Cuatro',
    5: 'Cinco',
    6: 'Seis',
    7: 'Siete',
    8: 'Ocho',
    9: 'Nueve',
    10: 'Diez',
    11: 'Once',
    12: 'Doce',
    13: 'Trece',
    14: 'Catorce',
    15: 'Quince',
    16: 'Dieciséis',
    17: 'Diecisiete',
    18: 'Dieciocho',
    19: 'Diecinueve',
    20: 'Veinte',
    21: 'Veintiuno',
    22: 'Veintidós',
    23: 'Veintitrés',
    24: 'Veinticuatro',
    25: 'Veinticinco',
    26: 'Veintiséis',
    27: 'Veintisiete',
    28: 'Veintiocho',
    29: 'Veintinueve',
    30: 'Treinta',
    31: 'Treinta y uno',
    32: 'Treinta y dos',
    33: 'Treinta y tres',
    34: 'Treinta y cuatro',
    35: 'Treinta y cinco',
    36: 'Treinta y seis',
    37: 'Treinta y siete',
    38: 'Treinta y ocho',
    39: 'Treinta y nueve',
    40: 'Cuarenta',
    41: 'Cuarenta y uno',
    42: 'Cuarenta y dos',
    43: 'Cuarenta y tres',
    44: 'Cuarenta y cuatro',
    45: 'Cuarenta y cinco',
    46: 'Cuarenta y seis',
    47: 'Cuarenta y siete',
    48: 'Cuarenta y ocho',
    49: 'Cuarenta y nueve',
    50: 'Cincuenta',
    51: 'Cincuenta y uno',
    52: 'Cincuenta y dos',
    53: 'Cincuenta y tres',
    54: 'Cincuenta y cuatro',
    55: 'Cincuenta y cinco',
    56: 'Cincuenta y seis',
    57: 'Cincuenta y siete',
    58: 'Cincuenta y ocho',
    59: 'Cincuenta y nueve',
    60: 'Sesenta',
    61: 'Sesenta y uno',
    62: 'Sesenta y dos',
    63: 'Sesenta y tres',
    64: 'Sesenta y cuatro',
    65: 'Sesenta y cinco',
    66: 'Sesenta y seis',
    67: 'Sesenta y siete',
    68: 'Sesenta y ocho',
    69: 'Sesenta y nueve',
    70: 'Setenta',
    71: 'Setenta y uno',
    72: 'Setenta y dos',
    73: 'Setenta y tres',
    74: 'Setenta y cuatro',
    75: 'Setenta y cinco',
    76: 'Setenta y seis',
    77: 'Setenta y siete',
    78: 'Setenta y ocho',
    79: 'Setenta y nueve',
    80: 'Ochenta',
    81: 'Ochenta y uno',
    82: 'Ochenta y dos',
    83: 'Ochenta y tres',
    84: 'Ochenta y cuatro',
    85: 'Ochenta y cinco',
    86: 'Ochenta y seis',
    87: 'Ochenta y siete',
    88: 'Ochenta y ocho',
    89: 'Ochenta y nueve',
    90: 'Noventa',
    91: 'Noventa y uno',
    92: 'Noventa y dos',
    93: 'Noventa y tres',
    94: 'Noventa y cuatro',
    95: 'Noventa y cinco',
    96: 'Noventa y seis',
    97: 'Noventa y siete',
    98: 'Noventa y ocho',
    99: 'Noventa y nueve'
}

numeros_disponibles = list(numeros_japoneses.keys())  # Lista de números disponibles

# Función para limpiar los archivos temporales en la carpeta 'temp/'
def limpieza_temporales():
    carpeta_temp = 'temp'

    # Verificar si la carpeta 'temp/' existe
    if os.path.exists(carpeta_temp):
        archivos_temporales = os.listdir(carpeta_temp)
        for archivo in archivos_temporales:
            ruta_archivo = os.path.join(carpeta_temp, archivo)
            os.remove(ruta_archivo)
        print("Archivos temporales eliminados correctamente.")
    else:
        print("La carpeta 'temp/' no existe.")

# Función para reproducir el sonido de pitido
def reproducir_pitido():
    pygame.mixer.Sound.play(ding_sound)
    time.sleep(0.5)  # Breve pausa

# Función para obtener la pronunciación en japonés y su significado
def obtener_pronunciacion(numero):

    pronunciacion = numeros_japoneses.get(numero)
    significado = significados.get(numero)

    return pronunciacion, significado

# Función para dar la bienvenida con "Konnichiwa" y reproducir un pitido
def bienvenida_entrenamiento_numeros():
    # Saludo "Konnichiwa" en japonés
    saludo = "Konnichiwa"
    
    # Crear carpeta 'temp/' si no existe
    if not os.path.exists('temp'):
        os.makedirs('temp')
    
    # Crear archivo de audio para el saludo en japonés en 'temp/'
    ruta_saludo = os.path.join('temp', 'saludo.mp3')
    tts_saludo = gTTS(saludo, lang='ja')
    tts_saludo.save(ruta_saludo)  # Guardar el saludo en 'temp/saludo.mp3'

    # Reproducir saludo "Konnichiwa" en japonés
    pygame.mixer.music.load(ruta_saludo)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    
    reproducir_pitido()  # Reproducir sonido de pitido después del saludo
    
    time.sleep(1)  # Esperar 1 segundo
    
    # Eliminar archivo de saludo al finalizar
    os.remove(ruta_saludo)

def despedida_entrenamiento_numeros():
    # Despedida "ja ne" en japonés
    despedida = "ja ne"
    
    # Crear carpeta 'temp/' si no existe
    if not os.path.exists('temp'):
        os.makedirs('temp')
    
    # Crear archivo de audio para la despedida en japonés en 'temp/'
    ruta_despedida = os.path.join('temp', 'despedida.mp3')
    tts_despedida = gTTS(despedida, lang='ja')
    tts_despedida.save(ruta_despedida)  # Guardar la despedida en 'temp/despedida.mp3'

    # Reproducir despedida "ja ne" en japonés
    pygame.mixer.music.load(ruta_despedida)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    
    reproducir_pitido()  # Reproducir sonido de pitido después de la despedida
    
    time.sleep(1)  # Esperar 1 segundo
    
    # Eliminar archivo de despedida al finalizar
    os.remove(ruta_despedida)

# Función para generar el audio de la pronunciación y el significado
def decir_numero(numero):

    global tiempo_espera  # Usar la variable global

    pronunciacion = numeros_japoneses[numero]
    significado = significados[numero]

    # Crear archivos de audio para la pronunciación y el significado
    tts_pronunciacion = gTTS(pronunciacion, lang='ja')
    tts_significado = gTTS(significado, lang='es')

    # Guardar archivos de audio en 'temp/'
    ruta_pronunciacion = os.path.join('temp', f'pronunciacion_{numero}.mp3')
    ruta_significado = os.path.join('temp', f'significado_{numero}.mp3')

    tts_pronunciacion.save(ruta_pronunciacion)
    tts_significado.save(ruta_significado)

    # Reproducir archivos de audio y sonido de pitido
    pygame.mixer.music.load(ruta_pronunciacion)
    pygame.mixer.music.play()
    
    time.sleep(tiempo_espera)  # Esperar 5 segundos
    reproducir_pitido()  # Reproducir sonido de pitido

    pygame.mixer.music.load(ruta_significado)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    reproducir_pitido()  # Reproducir sonido de pitido

    # Eliminar archivos de audio
    os.remove(ruta_pronunciacion)
    os.remove(ruta_significado)

# Función para reproducir el sonido de pitido
def reproducir_pitido():
    pygame.mixer.Sound.play(ding_sound)
    time.sleep(0.6)  # Breve pausa

# Función para obtener un número aleatorio y decirlo
def obtener_numero_aleatorio_y_decirlo():
    if numeros_disponibles:  # Si todavía hay números disponibles
        numero = random.choice(numeros_disponibles)  # Seleccionar número aleatorio
        numeros_disponibles.remove(numero)  # Quitar número seleccionado de la lista
        decir_numero(numero)  # Decir el número en japonés y su significado
    else:
        print("Ya no hay más números disponibles.")

# Eliminar ficheros temporales
limpieza_temporales()

#Primero bienvenida
bienvenida_entrenamiento_numeros()

# Ahora digo un número
for _ in range(100):
    obtener_numero_aleatorio_y_decirlo()

#Fin del programa
despedida_entrenamiento_numeros()