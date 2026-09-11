import os
import re

OUTPUT_FILE = "README.md"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_sort_key(folder_name):
    # Extrae el numero al inicio de la carpeta (ej. '1' de '1-lab225' o '10' de '10-lab-...')
    match = re.match(r"^(\d+)", folder_name)
    if match:
        return int(match.group(1))
    return float("inf")  # Si no tiene numero al inicio, lo manda al final


def clean_name(folder_name):
    cleaned = re.sub(r"^\d+-", "", folder_name)
    cleaned = cleaned.replace("-", " ").title()
    return cleaned


def generate_global_readme():
    markdown_content = []

    markdown_content.append("# AWS Hands-On Cloud & DevOps Portfolio\n")
    markdown_content.append(
        "Documentación práctica, diagramas de arquitectura y evidencias en video de laboratorios en AWS.\n"
    )
    markdown_content.append(
        " > *Este README fue generado automáticamente mediante un script de Python.* \n"
    )
    markdown_content.append("---\n")
    markdown_content.append("## Tabla de Contenidos por Módulo\n")

    # Ordenamiento natural aplicado a los modulos
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
            markdown_content.append(f"### [{mod_title}](./{mod}/README.md)\n")
        else:
            markdown_content.append(f"### {mod_title}\n")

        # Ordenamiento natural aplicado a los laboratorios
        raw_labs = [
            l
            for l in os.listdir(mod_path)
            if os.path.isdir(os.path.join(mod_path, l)) and "lab" in l.lower()
        ]
        labs = sorted(raw_labs, key=get_sort_key)

        if not labs:
            markdown_content.append(
                " - *No hay laboratorios registrados aún en este módulo.*\n"
            )
        else:
            for lab in labs:
                lab_path = os.path.join(mod_path, lab)
                lab_title = clean_name(lab)
                lab_readme = os.path.join(lab_path, "README.md")

                if os.path.exists(lab_readme):
                    status = "✅"
                    link = f"./{mod}/{lab}/README.md"
                    markdown_content.append(f"- {status} [{lab_title}]({link})\n")
                else:
                    status = "⏳ *(En construcción)*"
                    markdown_content.append(f"- {status} {lab_title}\n")

        markdown_content.append("\n")

    markdown_content.append("---\n")
    markdown_content.append("### Tecnologías Utilizadas\n")
    markdown_content.append("- **Cloud Provider:** Amazon Web Services (AWS)\n")
    markdown_content.append(
        "- **Sistemas Operativos:** Linux (Amazon Linux 2023 / Ubuntu)\n"
    )
    markdown_content.append(
        "- **Automatización & Lenguajes:** Python (Boto3 / Scripts), Bash\n"
    )

    output_path = os.path.join(BASE_DIR, OUTPUT_FILE)
    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(markdown_content)

    print("¡README.md global actualizado exitosamente desde Windows!")


if __name__ == "__main__":
    generate_global_readme()
