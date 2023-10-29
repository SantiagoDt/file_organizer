import os
import re

formatos_texto = [".txt", ".pdf", ".docx", ".html", ".json", ".xml", ".csv", ".ppx", ".accdb", ".pub", ".potx", ".dotx", ".xsn", ".mdb", ".xls", ".ppt", ".doc"]
formatos_imagen = [".jpg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".jpeg", ".ico"]
extensiones_validas =formatos_imagen+formatos_texto
print(extensiones_validas)
def esValido(ruta):
    _, extension = os.path.splitext(ruta)

    return extension in extensiones_validas


def esImg(ruta):
    _, extension = os.path.splitext(ruta)

    return extension in formatos_imagen

def esArchivo(ruta):
    _, extension = os.path.splitext(ruta)

    return extension in formatos_texto

# Directorio actual
directorio_actual = os.getcwd()

# Directorio de destino
directorio_destino = os.path.join(directorio_actual, "ArchivosOrdenados")

# Crea el directorio de destino si no existe
if not os.path.exists(directorio_destino):
    os.makedirs(directorio_destino)

# Lista de archivos en el directorio actual
archivos = os.listdir(directorio_actual)

for archivo in archivos:
    ruta_completa = os.path.join(directorio_actual, archivo)

    print(archivo)

    if esValido(ruta_completa):

        if esImg(ruta_completa):
            dir_destino_img = os.path.join(directorio_actual, "imagenes")
            if not os.path.exists(dir_destino_img ):
                os.makedirs(dir_destino_img)
            ruta_destino_img=os.path.join(dir_destino_img,archivo)
            os.rename(ruta_completa,ruta_destino_img)

        elif esArchivo(ruta_completa):
            dir_destino_archivo = os.path.join(directorio_actual,"archivos")
            if not os.path.exists(dir_destino_archivo):
                os.makedirs(dir_destino_archivo)
            ruta_destino_archivo = os.path.join(dir_destino_archivo,archivo)
            os.rename(ruta_completa,ruta_destino_archivo)

    print("{} no puede ser movido ya que no es una imagen ni un archivo".format(archivo))