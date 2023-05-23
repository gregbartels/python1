#Este modulo contiene la funcion para generar el archivo de texto que guarda las estadisticas del juego

def guardar_datos(nombre_archivo, datos, append=False):
    mode = "a" if append else "w"
    with open(nombre_archivo, mode) as archivo:
        if isinstance(datos, list):
            archivo.write("\n".join(datos) + "\n")
        else:
            archivo.write(datos + "\n")

def cargar_datos(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            datos = archivo.read().splitlines()
            return datos
    except FileNotFoundError:
        return None
