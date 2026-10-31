import os
import re

OUTPUT_FILE = "README.md"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_sort_key(folder_name):
    match = re.match(r"^(\d+)", folder_name)
    if match:
        return int(match.group(1))
    return float("inf")


def clean_name(folder_name):
    cleaned = re.sub(r"^\d+-", "", folder_name)
    cleaned = cleaned.replace("-", " ").title()
    return cleaned


def extract_summary_from_readme(readme_path):
    """
    Lee el README.md de un laboratorio y extrae el texto debajo de
    '## Descripción General' o '## Descripción'. Si no lo halla,
    busca '## Objetivos'. Si no encuentra nada, retorna un texto genérico.
    """
    if not os.path.exists(readme_path):
        return "*(Laboratorio en desarrollo)*"

    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Intentar buscar bajo ## Descripción General o ## Descripción
        match = re.search(
            r"##\s+(?:Descripción General|Descripción|Resumen|Objetivos)\n+(.*?)(?=\n##|\Z)",
            content,
            re.DOTALL | re.IGNORECASE,
        )
        
        if match:
            text = match.group(1).strip()
            # Eliminar saltos de línea y formatear en un solo párrafo corto
            lines = [line.strip() for line in text.split("\n") if line.strip() and not line.startswith("!")]
            if lines:
                summary = " ".join(lines)
                # Limitar longitud para que la tabla no se deforme
                return summary[:160] + "..." if len(summary) > 160 else summary

        # 2. Si no hay Descripción, intentar buscar el primer objetivo bullet point
        match_obj = re.search(r"##\s+Objetivos.*?\n((?:\s*-\s*.*?\n)+)", content, re.IGNORECASE)
        if match_obj:
            first_bullet = match_obj.group(1).strip().split("\n")[0]
            clean_bullet = re.sub(r"^\s*-\s*", "", first_bullet)
            return clean_bullet[:160]

    except Exception:
        pass

    return "Documentación y arquitectura práctica del laboratorio."


def generate_global_readme():
    markdown_content = []

    # --- ENCABEZADO Y BADGES ---
    markdown_content.append("# AWS Hands-On Cloud & DevOps Portfolio\n\n")
    markdown_content.append(
        "[![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/) "
        "[![CloudFormation](https://img.shields.io/badge/CloudFormation-FF4F00?style=for-the-badge&logo=awsmouth&logoColor=white)](https://aws.amazon.com/cloudformation/) "
        "[![Amazon S3](https://img.shields.io/badge/Amazon%20S3-569A31?style=for-the-badge&logo=amazons3&logoColor=white)](https://aws.amazon.com/s3/) "
        "[![Amazon EC2](https://img.shields.io/badge/Amazon%20EC2-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white)](https://aws.amazon.com/ec2/) "
        "[![Amazon VPC](https://img.shields.io/badge/Amazon%20VPC-232F3E?style=for-the-badge&logo=amazonvpc&logoColor=white)](https://aws.amazon.com/vpc/) "
        "[![AWS IAM](https://img.shields.io/badge/AWS%20IAM-DD344C?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/iam/) "
        "[![CloudWatch](https://img.shields.io/badge/CloudWatch-FF4F00?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/cloudwatch/) "
        "[![Lambda](https://img.shields.io/badge/AWS%20Lambda-FF9900?style=for-the-badge&logo=awslambda&logoColor=white)](https://aws.amazon.com/lambda/) "
        "[![RDS](https://img.shields.io/badge/Amazon%20RDS-527FFF?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/rds/) "
        "[![DynamoDB](https://img.shields.io/badge/DynamoDB-4053D6?style=for-the-badge&logo=amazondynamodb&logoColor=white)](https://aws.amazon.com/dynamodb/) "
        "[![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://www.kernel.org/) "
        "[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/) "
        "[![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/) \n\n"
    )

    # --- PRESENTACIÓN ---
    markdown_content.append("## Sobre este Portafolio\n\n")
    markdown_content.append(
        "Bienvenido/a a mi catálogo de laboratorios prácticos en **Amazon Web Services (AWS)**, **Linux**, **Redes**, **Seguridad** y **Bases de Datos**. "
        "Este repositorio consolida guías paso a paso, arquitectura de soluciones y evidencia de ejecución en video.\n\n"
    )
    markdown_content.append(
        "> 💡 *Este índice se construye y actualiza dinámicamente mediante un script de Python (`generate_readme.py`) "
        "que extrae automáticamente la descripción técnica de cada laboratorio.*\n\n"
    )

    # --- TABLAS POR MÓDULO ---
    markdown_content.append("## Módulos y Laboratorios Prácticos\n\n")

    items = sorted(os.listdir(BASE_DIR), key=get_sort_key)
    modules = [
        f
        for f in items
        if os.path.isdir(os.path.join(BASE_DIR, f)) and "modulo" in f.lower()
    ]

    for mod in modules:
        mod_path = os.path.join(BASE_DIR, mod)
        mod_title = clean_name(mod)

        mod_readme = os.path.join(mod_path, "README.md")
        if os.path.exists(mod_readme):
            markdown_content.append(f"### [{mod_title}](./{mod}/README.md)\n\n")
        else:
            markdown_content.append(f"### {mod_title}\n\n")

        raw_labs = [
            l
            for l in os.listdir(mod_path)
            if os.path.isdir(os.path.join(mod_path, l)) and "lab" in l.lower()
        ]
        labs = sorted(raw_labs, key=get_sort_key)

        if not labs:
            markdown_content.append("*(No hay laboratorios registrados aún en este módulo.)*\n\n")
        else:
            # Cabecera de la Tabla
            markdown_content.append("| Estado / Laboratorio | Descripción General | Enlaces |\n")
            markdown_content.append("| :--- | :--- | :---: |\n")

            for lab in labs:
                lab_path = os.path.join(mod_path, lab)
                lab_title = clean_name(lab)
                lab_readme = os.path.join(lab_path, "README.md")

                if os.path.exists(lab_readme):
                    status = "✅"
                    link = f"./{mod}/{lab}/README.md"
                    summary = extract_summary_from_readme(lab_readme)
                    lab_cell = f"{status} **[{lab_title}]({link})**"
                    links_cell = f"[📄 Doc]({link})"
                else:
                    status = "⏳"
                    summary = "*Laboratorio en construcción...*"
                    lab_cell = f"{status} {lab_title}"
                    links_cell = "—"

                markdown_content.append(f"| {lab_cell} | {summary} | {links_cell} |\n")

            markdown_content.append("\n")

    # --- STACK Y CONTACTO ---
    markdown_content.append("## Stack Tecnológico Dominado\n\n")
    markdown_content.append(
        "- **Cloud & Infraestructura:** AWS EC2, EC2 AutoScaling, VPC, CloudFormation, S3, IAM, CloudWatch, ELB, AWS Config, Systems Manager, Lambda, SNS, RDS, Aurora, DynamoDB, Route 53.\n"
        "- **Análisis & Automatización:** JMESPath, CloudTrail, Athena, AWS CLI, Infraestructura como Código (IaC).\n"
        "- **Sistemas Operativos & Shell:** Amazon Linux 2023, Ubuntu, Bash Scripting, Permisos, Logs, Servicios (systemd).\n"
        "- **Redes & Seguridad:** VPC Subnetting, Security Groups, NACLs, Hardening, Cifrado, Routing, Drift Detection.\n"
        "- **Bases de Datos & Lenguajes:** MySQL, SQL DQL/DDL/DML, Python 3, Boto3.\n\n"
    )

  
    markdown_content.append("## Contacto & Enlaces\n\n")
    markdown_content.append(
        "- **LinkedIn:** Conectemos para colaborar o conocer más sobre mis proyectos en la nube [MacarenaCavieres](https://www.linkedin.com/in/macarena-cavieres-rubio/)\n"
        "- **GitHub Profile:** [MacarenaCavieres](https://github.com/MacarenaCavieres)\n"
    )

    output_path = os.path.join(BASE_DIR, OUTPUT_FILE)
    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(markdown_content)

    print("¡README.md global con tablas descriptivas y badges actualizados generado con éxito!")


if __name__ == "__main__":
    generate_global_readme()