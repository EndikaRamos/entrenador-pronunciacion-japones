

# Captura de audio con Parec

Instrucciones para capturar audio utilizando parec, una herramienta de la suite PulseAudio en sistemas Linux. Se puede realizar la captura de audio con los siguientes parámetros:

```bash
parec --format=s16le --rate=44100 --channels=2 --device="dispositivo" | tee >(sox -t raw -r 44100 -e signed -b 16 -c 2 - output.wav) > /dev/null
```

## Requisitos previos
- Sistema operativo Linux
- Instalación de PulseAudio
- Herramienta sox para el procesamiento de audio

## Instrucciones de uso
- Asegúrate de tener instalado PulseAudio y sox en tu sistema.
- Reemplaza "dispositivo" con el nombre del dispositivo de audio que desees capturar. Puedes encontrar los dispositivos disponibles ejecutando el comando pactl list sources.
- Ejecuta el comando proporcionado en la terminal para capturar audio con los parámetros especificados.
- El audio capturado se almacenará en un archivo llamado output.wav en el directorio actual.

## Detalles del comando
parec: Herramienta de PulseAudio para capturar audio desde un dispositivo.
--format=s16le: Formato de audio PCM de 16 bits en little-endian.
--rate=44100: Frecuencia de muestreo de 44100 Hz (comúnmente utilizada para audio de calidad CD).
--channels=2: Dos canales de audio (estéreo).
--device="dispositivo": Reemplaza "dispositivo" con el nombre del dispositivo de audio a capturar.
tee: Permite ver la salida mientras se redirige a otro proceso.
sox -t raw -r 44100 -e signed -b 16 -c 2 - output.wav: Procesa la salida cruda de parec y la guarda en un archivo de audio llamado output.wav.
/dev/null: Descarta la salida de tee en la terminal para mantenerla limpia.
