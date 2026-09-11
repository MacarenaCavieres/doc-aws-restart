# Lab 245 Revisión de Archivos de Registro Seguros y Auditoría de Inicios de Sesión en Linux

![Linux](https://img.shields.io/badge/OS-Amazon%20Linux%202-orange?logo=amazon)
![Bash](https://img.shields.io/badge/Shell-Bash-4EAA25?logo=gnu-bash&logoColor=white)
![AWS](https://img.shields.io/badge/Environment-AWS%20EC2-232F3E?logo=amazon-aws)
![Tool](https://img.shields.io/badge/Tool-Text%20Processing-4D4D4D?logo=windowsterminal&logoColor=white)

## Descripción General

Este laboratorio se enfoca en el análisis y auditoría de seguridad del sistema operativo Linux mediante la inspección de registros del sistema (_system logs_). Se revisan eventos de autenticación, intentos de acceso fallidos mediante `/var/log/secure` y el historial de inicio de sesión de los usuarios del sistema a través de la herramienta `lastlog`.

## Objetivos del Laboratorio

- Inspeccionar archivos de registros de autenticación seguros (`/tmp/log/secure`).
- Identificar direcciones IP de origen, puertos e intentos fallidos de autenticación.
- Auditar el historial del último inicio de sesión de todos los usuarios registrados en el sistema operativo usando `lastlog`.
- Utilizar paginadores de terminal (`less`) para la navegación eficiente en archivos de texto extensos.

## Tarea 1: Inspección del Archivo de Registro Seguro (`secure`)

Se analizó la actividad de autenticación y accesos en el sistema utilizando el paginador `less`.

```bash
# Confirmar el directorio de trabajo actual
pwd

# Inspeccionar el archivo de registro de autenticacion seguro
sudo less /tmp/log/secure
```

_Nota arquitectónica: En entornos de producción estándar de Linux (como RHEL o Amazon Linux), el archivo de registro seguro se ubica en la ruta `/var/log/secure`. En este laboratorio, se utilizó una copia de prueba localizada en `/tmp/log/secure`._

### Datos extraídos durante la inspección:

- Direcciones IP de origen de las solicitudes de conexión.
- Estado de las autenticaciones (éxitos y fallos de credenciales).
- Puertos e identificadores de procesos (PIDs) asociados a los intentos de acceso SSH/SUDO.
- Para finalizar la visualización y salir del visor less, se presiona la tecla q.

## Tarea 2: Auditoría del Historial de Inicios de Sesión (`lastlog`)

Se ejecutó la utilidad `lastlog` para inspeccionar la fecha y hora del último acceso registrado para cada cuenta del sistema.

```bash
# Consultar el ultimo inicio de sesion de todos los usuarios del sistema
sudo lastlog
```

### Salida Esperada:

El comando genera un reporte estructurado que incluye el nombre de usuario (Username), el puerto de acceso (Port), la IP de origen (From) y la marca de tiempo (Latest). Cuentas de servicio del sistema (como `root`, `bin`, `daemon`) muestran el estado **Never logged in** si nunca han iniciado una sesión interactiva.

## Resumen de Comandos y Sintaxis

| Comando   | Opción / Flag | Descripción / Caso de Uso                                                                          |
| :-------- | :------------ | :------------------------------------------------------------------------------------------------- |
| `pwd`     | Directa       | Muestra la ruta del directorio de trabajo actual.                                                  |
| `less`    | Directa       | Paginador de texto para navegar archivos extensos sin cargar todo su contenido en memoria.         |
| `lastlog` | Directa       | Consulta el archivo `/var/log/lastlog` y muestra el último inicio de sesión de todos los usuarios. |

## Evidencia en Video

Mira la ejecución de este laboratorio paso a paso en mi canal de YouTube: \
[![Ver Video en YouTube](https://img.shields.io/badge/YouTube-Ver_Laboratorio_Práctico-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/watch?v=qaYgLfYzWak)

## Aprendizajes Clave

- **Monitoreo de Autenticación**: El archivo `secure` es la fuente primaria para detectar ataques de fuerza bruta, accesos no autorizados e interacciones con el comando sudo.

- **Auditoría de Cuentas Inactivas**: La herramienta `lastlog` facilita la identificación de cuentas de usuario en desuso o de servicios del sistema que jamás deberían tener sesiones interactivas abiertas.

- **Navegación con `less`**: Herramienta fundamental para administradores de sistemas (SysAdmins) que permite buscar, avanzar y retroceder eficientemente en archivos de log de gran tamaño.
