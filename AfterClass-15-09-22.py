#print("Hola")
#input("Ingrese un dato: ")

#variable_dinamica = input("Introduzca su mensaje: ")
#print(variable_dinamica)

#print(primer_variable)
#print(segunda_variable)

#print(len(sys.argv))
#print(list(sys.argv))


import sys

if len(sys.argv) == 3:

    primer_variable = sys.argv[1]
    segunda_variable = sys.argv[2]

    print(primer_variable)
else:
    print(f"Ha ingresado {(len(sys.argv)-1)} variables, ingrese solamente dos")

#######################################################################################################################

import requests

import sys

sys.argv

# desps del igual se le pone el nombre de cualquier lugar en el buscador y te arroja esos datos
url = "https://apis.datos.gob.ar/georef/api/provincias?nombre={sys.argv[1]}"

print(requests.get(url))

respuesta = requests.get(url)

print(respuesta.json())
