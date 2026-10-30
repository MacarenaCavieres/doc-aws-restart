# Lab 189 Optimización de la Utilización (Derechos de Instancia, Limpieza de EBS y Calculadora de Precios)

![Amazon EC2](https://img.shields.io/badge/Compute-Amazon%20EC2-FF9900?logo=amazonec2&logoColor=white)
![AWS CLI](https://img.shields.io/badge/Tool-AWS%20CLI-232F3E?logo=amazon-aws&logoColor=white)
![AWS Pricing](https://img.shields.io/badge/Finance-AWS%20Pricing%20Calculator-232F3E?logo=amazon-aws&logoColor=white)

## Descripción General

En este laboratorio se implementó una estrategia de optimización y reducción de costos operativos sobre la arquitectura en la nube de la cafetería. Tras haber completado la migración de las bases de datos locales hacia un servicio administrado en **Amazon RDS**, se procedió a desinstalar el motor de base de datos obsoleto (`MariaDB`) de la instancia principal de **Amazon EC2** (`CafeInstance`) para disminuir los requisitos de almacenamiento y consumo de CPU. Asimismo, se redujo el tipo de instancia de `t3.small` a `t3.micro` de forma programática mediante la **AWS CLI**, y se cuantificó el impacto financiero utilizando la **Calculadora de Precios de AWS**.

## Objetivos del Laboratorio

- Optimizar una instancia de Amazon EC2 para alinearla con los requerimientos reales de carga de trabajo y reducir costos.
- Utilizar la AWS CLI para gestionar el ciclo de vida de las instancias y modificar atributos de hardware de forma remota.
- Emplear la **Calculadora de Precios de AWS** para modelar, comparar y estimar los costos mensuales antes y después de la optimización arquitectónica.

## Tarea 1: Optimización del Sitio Web para Reducir Costos

1. **Conexión a CafeInstance y Configuración de AWS CLI:**
   - Conectarse mediante SSH a la instancia de la cafetería utilizando el par de claves provisto (`labsuser.pem` o `labsuser.ppk`).
   - Descubrir la región de ejecución actual y configurar las credenciales de acceso ejecutando:
     ```bash
     aws configure
     ```
2. **Desinstalación del Motor de Base de Datos Local:**
   - Detener el servicio local de MariaDB y desinstalarlo por completo del sistema operativo huésped para liberar recursos de procesamiento y almacenamiento:
     ```bash
     sudo systemctl stop mariadb
     sudo yum -y remove mariadb-server
     ```
   - Cerrar la sesión SSH en `CafeInstance` tras completar la desinstalación.
3. **Redimensionamiento de la Instancia de EC2 (Right-Sizing):**
   - Desde una segunda sesión SSH conectada al host de comandos (`CLI Host`), determinar el identificador único de la instancia de la cafetería:
     ```bash
     aws ec2 describe-instances --filters "Name=tag:Name,Values=CafeInstance" --query "Reservations[*].Instances[*].InstanceId"
     ```
   - Detener la instancia para permitir cambios en su configuración de hardware:
     ```bash
     aws ec2 stop-instances --instance-ids <CafeInstance ID Instance>
     ```
   - Modificar el tipo de instancia de `t3.small` a `t3.micro`:
     ```bash
     aws ec2 modify-instance-attribute --instance-id <CafeInstance ID Instance> --instance-type "{\"Value\": \"t3.micro\"}"
     ```
   - Volver a iniciar la instancia y verificar su estado operativo junto con sus nuevos parámetros de red (`PublicDnsName` y `PublicIpAddress`):
     ```bash
     aws ec2 start-instances --instance-ids <CafeInstance ID Instance>
     aws ec2 describe-instances --instance-ids <CafeInstance ID Instance> --query "Reservations[*].Instances[*].[InstanceType,PublicDnsName,PublicIpAddress,State.Name]"
     ```
   - Validar el correcto funcionamiento del sitio web ingresando a la URL pública actualizada `http://<Downsized CafeInstance Public DNS Name>/cafe`.

## Tarea 2: Utilización de la Calculadora de Precios de AWS

1. **Cálculo de Costos Antes de la Optimización:**
   - Acceder a la [Calculadora de Precios de AWS](https://calculator.aws) y crear una estimación avanzada configurando los componentes previos:
     - **Amazon EC2:** Instancia `t3.small` (bajo demanda, uso constante al 100%) con un volumen EBS de **40 GB** (que incluía 20 GB ocupados por la base de datos local).
     - **Amazon RDS:** Instancia `db.t3.micro` con motor MariaDB y **20 GB** de almacenamiento SSD (gp2).
   - Guardar la estimación, exportar los resultados a un archivo CSV y registrar el costo mensual estimado (por ejemplo, **$35.60 USD**).
2. **Cálculo de Costos Tras la Optimización:**
   - Editar la estimación existente para reflejar los cambios arquitectónicos implementados:
     - **Amazon EC2:** Reducir el tipo de instancia a `t3.micro` y disminuir el almacenamiento del volumen EBS adjunto de 40 GB a **20 GB** (eliminando el espacio destinado a la base de datos desinstalada).
     - **Amazon RDS:** Mantener sin cambios el servicio administrado de bases de datos.
   - Exportar la nueva estimación a CSV y registrar el costo mensual optimizado (por ejemplo, **$25.18 USD**).
3. **Estimación del Ahorro de Costos Previsto:**
   - Comparar los totales mensuales para calcular la reducción financiera global lograda mediante la iniciativa de optimización:
     - _Costos mensuales previos:_ ~$65.60 USD
     - _Costos mensuales optimizados:_ ~$55.18 USD
     - _Ahorro mensual estimado:_ **~$10.42 USD**

## Resumen de Recursos y Componentes

| Servicio / Recurso         | Nombre del Componente           | Descripción y Función Técnica                                                                                         |
| :------------------------- | :------------------------------ | :-------------------------------------------------------------------------------------------------------------------- |
| **Amazon EC2**             | `CafeInstance` (`t3.micro`)     | Servidor web de la aplicación de la cafetería optimizado tras eliminar cargas redundantes de bases de datos locales.  |
| **Amazon EBS**             | Volúmenes gp2 (20 GB)           | Almacenamiento en bloques persistente cuyo dimensionamiento fue reducido al liberar espacio de datos obsoletos.       |
| **Amazon RDS**             | MariaDB (`db.t3.micro`)         | Servicio relacional administrado que centraliza de forma segura y escalable la persistencia de datos de la cafetería. |
| **AWS Pricing Calculator** | Modelo de Estimación Financiera | Herramienta de planificación de costos empleada para proyectar ahorros presupuestarios basados en el uso real.        |

## Conclusiones del Laboratorio

- **Eliminación de Cargas Redundantes:** Desinstalar componentes inactivos como bases de datos locales en servidores web permite disminuir significativamente la utilización de CPU y los costos de almacenamiento en bloques.
- **Derechos de Instancia (Right-Sizing):** Ajustar la capacidad de cómputo de EC2 (`t3.small` a `t3.micro`) de acuerdo con las demandas reales de la aplicación maximiza la eficiencia económica sin comprometer la disponibilidad del servicio.
- **Valor de la Planificación Financiera:** La integración de herramientas como la Calculadora de Precios de AWS facilita la toma de decisiones basada en datos, evidenciando de manera tangible el retorno de inversión de las iniciativas de optimización en la nube.
