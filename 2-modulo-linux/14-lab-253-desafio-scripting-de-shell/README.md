# Lab 253 Desafío Bash: Script de Generación Dinámica de Archivos con Control de Estado

![Linux](https://img.shields.io/badge/OS-Amazon%20Linux%202-orange?logo=amazon)
![Bash](https://img.shields.io/badge/Shell-Bash-4EAA25?logo=gnu-bash&logoColor=white)
![AWS](https://img.shields.io/badge/Environment-AWS%20EC2-232F3E?logo=amazon-aws)
![Tool](https://img.shields.io/badge/Tool-Automation-4D4D4D?logo=windowsterminal&logoColor=white)

## Descripción General

Este laboratorio consiste en un desafío práctico de automatización mediante _Shell Scripting_ en Linux. El objetivo es desarrollar un script funcional en Bash que genere lotes consecutivos de 25 archivos vacíos en cada ejecución, garantizando que la numeración sea incremental y persistente entre ejecuciones mediante la gestión de un archivo de estado interno (`counter.txt`).

## Requisitos del Desafío

- Crear 25 archivos vacíos de 0 KB por cada ejecución del script.
- Nombrar los archivos siguiendo el patrón `<nombreEstudiante>-<número>`.
- Garantizar que los números no estén estáticos (_hardcoded_), sino que se calculen automáticamente comenzando desde el último número generado.
- Mantener la persistencia del contador entre distintas ejecuciones.
- Validar la creación mediante una inspección detallada del directorio.

## Solución Implementada

### Archivo de Control de Estado (`counter.txt`)

Para almacenar el estado del lote actual de forma persistente, se inicializa el archivo `counter.txt` con el valor base:

```bash
echo 1 > counter.txt
```

### Script de Automatización (create_files.sh)

```bash
#!/bin/bash
student_name="Macarena"

# Lectura del indice inicial desde el archivo de control
MIN=$(cat counter.txt)
MAX=$(($MIN + 24))
NEW_COUNTER=$(($MAX + 1))

# Generacion del lote de 25 archivos
for x in $(seq $MIN$MAX)
do
    touch "/home/$USER/challenge/${student_name}-${x}"
done

# Actualizacion del archivo de control para la siguiente ejecucion
echo $NEW_COUNTER | tee counter.txt

echo "Good job"
```

### Pruebas de Validación y Ejecución

```bash
# Asignar permisos de ejecucion al script
chmod +x create_files.sh

# Primera ejecucion (genera del 1 al 25)
./create_files.sh

# Segunda ejecucion (genera del 26 al 50)
./create_files.sh

# Confirmar la creacion de archivos y sus tamaños (0 KB)
ls -la /home/$USER/challenge
```

## Resumen de Comandos y Sintaxis

| Comando | Opción / Flag | Descripción / Caso de Uso                                                             |
| :------ | :------------ | :------------------------------------------------------------------------------------ |
| `touch` | Directa       | Crea archivos vacíos o actualiza la marca de tiempo de archivos existentes.           |
| `seq`   | `MIN MAX`     | Genera una secuencia numérica desde un valor inicial hasta uno final.                 |
| `cat`   | Directa       | Lee el contenido del archivo de estado para asignar el valor inicial al script.       |
| `tee`   | Directa       | Escribe el nuevo valor del contador en `counter.txt` mientras lo muestra en pantalla. |
| `chmod` | `+x`          | Otorga permisos de ejecución al script de Bash.                                       |

## Evidencia en Video

Mira la ejecución de este laboratorio paso a paso en mi canal de YouTube: \
[![Ver Video en YouTube](https://img.shields.io/badge/YouTube-Ver_Laboratorio_Práctico-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/watch?v=YY8_8l5dL34)

## Aprendizajes Clave

- **Persistencia de Estado**: El uso de archivos auxiliares como `counter.txt` permite conservar variables entre distintas ejecuciones sin depender de procesos secundarios en segundo plano.

- **Aritmética en Bash**: La sintaxis `$((expresión))` facilita el cálculo de límites de iteración dinámicos dentro del entorno de la terminal.

- **Estructuras de Control Iterativas**: El bucle `for` combinado con la utilidad `seq` optimiza la creación masiva y secuencial de recursos en el sistema de archivos.
