try:
    entrada = input("Ingresar el nombre del archivo: ")
    archivo = open("paises.txt", "r", encoding="UTF-8")
    for linea in archivo:
        print(linea.upper())
except:
    print("Error, no existe el archivo")