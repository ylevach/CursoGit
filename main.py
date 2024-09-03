
# Constante con el nombre del fichero
FILENAME = "150.csv"
x=9
y=3
print(x/y)
def nada():
# Hago unos cuantos trucos para convertir los valores que vienen en el excel en numeros
def to_number(value: str):
    value = value.replace(",", ".")
    parts = value.split("-")
    fraction = 0
    if len(parts) > 1:
        if parts[1] == "1/4": 
            fraction = 0.25        
        if parts[1] == "1/2": 
            fraction = 0.5
        if parts[1] == "3/4": 
            fraction = 0.75
    return float(parts[0]) + fraction

# Funcion que procesa las lineas
def process_lines(lines: list[str]):
    # Las lineas del fichero vienen en una lista de string
    # Pero las dos primeras lineas no me interesan, asi q las excluyo haciendo lines[2:]
    lines = lines[2:]

    last_height = 0
    # Luego puedo iterar por todas las lineas
    for line in lines:
        # Cada linea tiene el mismo formato: numero;numero;numero;numero
        # Asi que separo la cadena usando como separador el caracter ;
        # El metodo split hace la separacion y devuelve un arreglo de 4 elementos
        items = line.split(";")

        # Obtengo los parametros por separado 
        width = items[0]
        height = items[1] if items[1] != "" else last_height
        pressure1 = items[2] if items[2] != "-" else "0"
        pressure2 = items[3] if items[3] != "-" else "0"
        last_height = height

        # Imprimo
        tuple = (to_number(width), to_number(height), to_number(pressure1), to_number(pressure2))
        print(tuple)

# Funcion para leer el fichero
def read_csv():

    # Aca abro el fichero, obtengo todas las lineas y luego cierro el fichero
    f = open(FILENAME, "r")
    lines = f.readlines()
    f.close()

    f = open(FILENAME, "r")
    lines = f.readlines()
    f.close()


# Este es el punto de entrada del programa
if __name__ == "__main__":
    # Llamo a la funcion que lee el fichero
     def read_csv():
         import csv
