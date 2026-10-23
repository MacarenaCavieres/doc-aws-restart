# Módulo: Arquitectura en la Nube de AWS (AWS Cloud Architecture)

![AWS Architecture](https://img.shields.io/badge/Architecture-AWS%20Well--Architected-FF9900?logo=amazonaws&logoColor=white)
![AWS CAF](https://img.shields.io/badge/Framework-AWS%20CAF-8C4FFF?logo=amazon-aws&logoColor=white)
![Cloud Adoption](https://img.shields.io/badge/Cloud-Migration%20%26%20HA-232F3E?logo=amazon-aws&logoColor=white)

## Descripción General

Este módulo aborda los marcos teóricos, principios de diseño y mejores prácticas fundamentales para estructurar e implementar arquitecturas sólidas, escalables y eficientes en la nube de AWS. A través del estudio del **AWS Cloud Adoption Framework (CAF)**, el **AWS Well-Architected Framework**, conceptos clave de **Alta Disponibilidad y Tolerancia a Fallos**, y las estrategias de **Transición desde Centros de Datos Tradicionales hacia la Nube**, este compendio establece la base teórica necesaria para la toma de decisiones arquitectónicas en proyectos cloud.

## 1. AWS Cloud Adoption Framework (AWS CAF)

El **AWS CAF** organiza la transformación e innovación digital agrupando las mejores prácticas en **6 perspectivas organizacionales**. Facilita la identificación de brechas en habilidades y procesos, estructurando el camino hacia la adopción acelerada de la nube.

```text
               +---------------------------------------------------+
               |        AWS Cloud Adoption Framework (CAF)         |
               +---------------------------------------------------+
               |  PERSPECTIVAS DE NEGOCIO | PERSPECTIVAS TÉCNICAS  |
               +--------------------------+------------------------+
               |  • Negocio (Business)    |  • Seguridad (Security)|
               |  • Personas (People)     |  • Operaciones (Ops)   |
               |  • Gobernanza (Gov)      |  • Plataforma (Platform)|
               +--------------------------+------------------------+
```

### Principales Perspectivas:

- **Negocio (Business):** Asegura que las inversiones en la nube se alineen con los objetivos estratégicos y resultados comerciales medibles.
- **Personas (People):** Prepara a la organización para el cambio cultural, desarrollando habilidades y modelos organizacionales modernos.
- **Gobernanza (Governance):** Define políticas, gestión de portafolios y programas para optimizar el valor de las inversiones de TI.
- **Plataforma (Platform):** Diseña y construye soluciones en la nube optimizando la infraestructura, arquitectura de aplicaciones y servicios.
- **Seguridad (Security):** Garantiza la conformidad, confidencialidad, integridad y disponibilidad de los datos y cargas de trabajo.
- **Operaciones (Operations):** Define la entrega y ejecución de servicios mediante automatización, observabilidad y continuidad del negocio.

## 2. AWS Well-Architected Framework

Proporciona un enfoque estructurado para evaluar arquitecturas y diseñar sistemas eficientes, seguros y de alto rendimiento. Se fundamenta en **6 pilares principales**:

| Pilar                          | Enfoque Principal                                                                              | Concepto Clave                                                                                       |
| :----------------------------- | :--------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------- |
| **Excelencia Operativa**       | Ejecución y monitoreo de sistemas para aportar valor al negocio.                               | Automatización mediante infraestructura como código (IaC) y aprendizaje continuo de fallos.          |
| **Seguridad**                  | Protección de información, sistemas y activos bajo el principio de mínimo privilegio.          | Implementación de defensa en profundidad, cifrado en reposo y en tránsito.                           |
| **Fiabilidad (Reliability)**   | Capacidad de una carga de trabajo para recuperarse de interrupciones y cumplir con la demanda. | Pruebas de procedimientos de recuperación automatizados y escalado horizontal.                       |
| **Eficiencia del Rendimiento** | Uso eficiente de los recursos informáticos según los requisitos del sistema.                   | Selección adecuada de tipos de instancias, bases de datos y arquitectura serverless.                 |
| **Optimización de Costos**     | Capacidad para ejecutar sistemas al precio más bajo posible.                                   | Adopción de modelos de pago por uso, dimensionamiento correcto (_rightsizing_) y análisis de gastos. |
| **Sostenibilidad**             | Minimización del impacto ambiental de las cargas de trabajo ejecutadas en la nube.             | Maximización de la utilización de recursos y selección de regiones con energía limpia.               |

## 3. Fiabilidad, Alta Disponibilidad y Tolerancia a Fallos

El diseño de aplicaciones modernas exige mitigar los puntos únicos de fallo (_Single Points of Failure - SPOF_) utilizando patrones de resiliencia:

- **Alta Disponibilidad (High Availability - HA):** Garantiza que un sistema permanezca operativo y accesible sin interrupción mediante la redundancia en múltiples Zonas de Disponibilidad (AZs) y el balanceo de carga (_Elastic Load Balancing_).
- **Tolerancia a Fallos (Fault Tolerance):** Capacidad de un sistema para seguir funcionando sin degradación perceptible ante la falla de uno o más de sus componentes.
- **Auto Scaling:** Ajuste dinámico de la capacidad de cómputo en función de métricas de demanda operativa para evitar la sobrecarga del sistema.
- **RTO y RPO:**
  - **RTO (Recovery Time Objective):** Tiempo máximo aceptable en el que un servicio puede estar inactivo tras un incidente.
  - **RPO (Recovery Point Objective):** Cantidad máxima aceptable de pérdida de datos medida en tiempo.

```text
[Tráfico de Clientes] ──► [Elastic Load Balancer]
                                │
                 ┌──────────────┴──────────────┐
                 ▼                             ▼
       [Subred Privada AZ-A]         [Subred Privada AZ-B]
       └── Instancia EC2             └── Instancia EC2
                 │                             │
                 └──────────────┬──────────────┘
                                ▼
                   [Amazon RDS Multi-AZ DB]
```

## 4. Transición de un Centro de Datos Tradicional a la Nube

Estrategias y consideraciones arquitectónicas para migrar infraestructuras físicas/on-premises hacia la nube de AWS:

### Las 6 "R"s de la Migración (Migration Strategies):

1. **Rehost (Lift and Shift):** Mover aplicaciones a la nube sin cambios estructurales (ej. migrar VMs físicas a instancias Amazon EC2).
2. **Replatform (Lift, Tinker and Shift):** Optimización menor de componentes sin cambiar la arquitectura central (ej. reemplazar MySQL en VM por Amazon RDS).
3. **Refactor / Re-architect:** Rediseño completo de la aplicación aprovechando características nativas de la nube (Serverless, Microservicios, Containers).
4. **Repurchase (Drop and Replace):** Reemplazar la aplicación existente por una solución Software as a Service (SaaS).
5. **Retain:** Mantener ciertas aplicaciones en el centro de datos local debido a requisitos normativos o dependencias heredadas.
6. **Retire:** Eliminar componentes e infraestructura que ya no son necesarios dentro del portafolio TI.

## Conclusiones del Módulo

- **Alineación Estratégica:** El **AWS CAF** permite cerrar la brecha entre los objetivos del negocio y la implementación técnica, guiando la adopción tecnológica en todas las áreas organizacionales.
- **Diseño Resiliente por Defecto:** La implementación del **AWS Well-Architected Framework** asegura que las arquitecturas construidas en AWS no solo sean funcionales, sino también seguras, rentables, eficientes y preparadas para soportar fallos a escala.
- **Modernización Continuada:** La migración a la nube no finaliza con el patrón _Lift and Shift_; la verdadera ventaja competitiva radica en evolucionar hacia arquitecturas gestionadas, sin servidor (_Serverless_) y distribuidas globalmente.
