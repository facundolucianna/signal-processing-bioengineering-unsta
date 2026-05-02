import random
import os

def asignar_ejercicios(alumnos_path, puntos_path, output_path):
    # Leer alumnos
    with open(alumnos_path, 'r', encoding='utf-8') as f:
        alumnos = [line.strip() for line in f if line.strip()]
    
    # Leer ejercicios
    with open(puntos_path, 'r', encoding='utf-8') as f:
        puntos = [line.strip() for line in f if line.strip()]
    
    if not alumnos or not puntos:
        print("Error: No se encontraron alumnos o puntos.")
        return

    # Asignar al azar (con repetición)
    asignaciones = []
    for alumno in alumnos:
        ejercicio_raw = random.choice(puntos)
        # Limpiar el nombre del ejercicio (quitar el prefijo "N - ") para coincidir con el formato preferido del usuario
        if " - " in ejercicio_raw:
            ejercicio = ejercicio_raw.split(" - ", 1)[1]
        else:
            ejercicio = ejercicio_raw
        asignaciones.append(f"| {alumno} | {ejercicio} |")

    # Guardar en markdown
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# Asignación de Ejercicios para el Parcial\n\n")
        f.write("| Alumno | Ejercicio Asignado |\n")
        f.write("| :--- | :--- |\n")
        f.write("\n".join(asignaciones))
        f.write("\n")

    print(f"Asignaciones guardadas en: {output_path}")

if __name__ == "__main__":
    base_path = "/Users/facundolucianna/Docencia/UNSTA/procesamiento_bio/parcial"
    alumnos_file = os.path.join(base_path, "alumnos.md")
    puntos_file = os.path.join(base_path, "puntos.md")
    output_file = os.path.join(base_path, "asignaciones.md")
    
    asignar_ejercicios(alumnos_file, puntos_file, output_file)
