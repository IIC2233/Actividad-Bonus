import sys

import pyrematch as REmatch
import wikipedia


## -------------------------------------------------------------------
## Define aquí los patrons para cada expresióñ regular
## NO CAMBIAR LOS NOMBRES DE LAS VARIABLES

PATRON1 = ""
PATRON2 = ""
PATRON3 = ""
PATRON4 = ""
PATRON5 = ""
PATRON6 = ""


## -------------------------------------------------------------------
## Complete a continuación el código de cada consulta.
## Cada consulta recibe el patrón correspondiente para construir la 
## expresión regular, y el texto sobre el cual se aplicará.

## Deben retornar una lista de tuplas, donde cada tupla contiene 
## el match encontrado, su posición de inicio y su posición de término.

# CONSULTA 1
def consulta1(texto, patron):
    resultado = []
    return resultado

# CONSULTA 2
def consulta2(texto, patron):
    resultado = []
    return resultado

# CONSULTA 3
def consulta3(texto, patron):
    resultado = []
    return resultado

# CONSULTA 4
def consulta4(texto, patron):
    resultado = []
    return resultado

# CONSULTA 5
def consulta5(texto, patron):
    resultado = []
    return resultado

# CONSULTA 6
def consulta6(texto, patron):
    resultado = []
    return resultado


# Imprime y guarda el output con el fomrato necesario
def print_output(document, pattern, query, name, filename):
    with open(filename, "a") as file:
        for i in query(document, pattern):
            file.write(f"- {name}: '{i[0]}' - Posición: ({i[1]}, {i[2]})\n")
            print(f"- {name}: '{i[0]}' - Posición: ({i[1]}, {i[2]})")

# Imprime y guarda los separadores entre consultas
def print_header(text, filename, new=False):
    mode = "w" if new else "a"
    with open(filename, mode) as file:
        file.write(f"{text}\n")
        print(text)


if __name__ == "__main__":
    # Nombre del archivo a escribir
    path_archivo = "out.txt"

    # Recibe como argumento el nombre del país
    pais = sys.argv[1]

    # Descarga la página de wikipedia correspondiente
    documento = wikipedia.page(pais, auto_suggest=False).content

    # Ejecuta las consultas e imprime con el formato necesario
    print_header("# Consulta 1", path_archivo, True)
    print_output(documento, PATRON1, consulta1, "Título", path_archivo)

    print_header("\n# Consulta 2", path_archivo)
    print_output(documento, PATRON2, consulta2, "Subtítulo", path_archivo)

    print_header("\n# Consulta 3", path_archivo)
    print_output(documento, PATRON3, consulta3, "Subsubtítulo", path_archivo)

    print_header("\n# Consulta 4", path_archivo)
    print_output(documento, PATRON4, consulta4, "Título", path_archivo)

    print_header("\n# Consulta 5", path_archivo)
    print_output(documento, PATRON5, consulta5, "Subtítulo", path_archivo)

    print_header("\n# Consulta 6", path_archivo)
    print_output(documento, PATRON6, consulta6, "Subtítulo", path_archivo)