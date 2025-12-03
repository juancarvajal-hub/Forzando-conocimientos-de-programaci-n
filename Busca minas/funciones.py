import random
from IPython.display import clear_output
import time
import os


def pedir_datos():
    while True:
        Nombre = input("Ingrese su nombre: ")
        if Nombre == "":
            print("Por favor, debe ingresar su nombre.")
        else:
            break

    while True:
        Numero_de_Filas = int(input("Ingrese el número de filas: "))
        if Numero_de_Filas <= 0 or Numero_de_Filas > 9:
            print("Debe ingresar un número mayor a 0 y menor o igual a 9.")
        else:
            break

    while True:
        Numero_de_Columnas = int(input("Ingrese el número de columnas: "))
        if Numero_de_Columnas <= 0 or Numero_de_Columnas > 9:
            print("Debe ingresar un número mayor a 0 y menor o igual a 9.")
        else:
            break

    while True:
        Numero_de_Minas = int(input("Ingrese el número de minas: "))
        if Numero_de_Minas <= 0 or Numero_de_Minas > (Numero_de_Filas * Numero_de_Columnas):
            print("Debe ingresar un número mayor a 0 y menor o igual al tamaño del tablero.")
        else:
            break

    return Nombre, Numero_de_Filas, Numero_de_Columnas, Numero_de_Minas



def imprimir_tablero(Numero_de_Filas, Numero_de_Columnas):
    # Imprimir encabezado de columnas
    for i in range(Numero_de_Columnas):
        if i == 0:
            print("  ", end="")
        elif i == Numero_de_Columnas - 1:
            print(f"{i} {i+1}")
        else:
            print(f"{i} ", end="")

    # Línea superior
    print(" +" + "- " * Numero_de_Columnas + "+")

    # Filas del tablero
    for i in range(Numero_de_Filas):
        print(f"{i+1}|", ". " * Numero_de_Columnas, "|", sep="")

    # Línea inferior
    print(" +" + "- " * Numero_de_Columnas + "+")


def generar_minas(Numero_de_Filas, Numero_de_Columnas, Numero_de_Minas):
    filas_minas = []
    columnas_minas = []

    while len(filas_minas) < Numero_de_Minas:
        fila = random.randint(1, Numero_de_Filas)
        columna = random.randint(1, Numero_de_Columnas)

        # Verificar que no exista la mina ya
        if (fila, columna) not in list(zip(filas_minas, columnas_minas)):
            filas_minas.append(fila)
            columnas_minas.append(columna)

    return filas_minas, columnas_minas    

def crear_tablero_visible(Numero_de_Filas, Numero_de_Columnas):
    tablero = []
    for i in range(Numero_de_Filas):
        fila = []
        for j in range(Numero_de_Columnas):
            fila.append(".")
        tablero.append(fila)
    return tablero

def crear_tablero_logico(Numero_de_Filas, Numero_de_Columnas):
    valores = []
    for i in range(Numero_de_Filas):
        fila = []
        for j in range(Numero_de_Columnas):
            fila.append(0)
        valores.append(fila)
    return valores

def ubicar_minas(valores, filas_minas, columnas_minas):
    for fila, columna in zip(filas_minas, columnas_minas):
        valores[fila - 1][columna - 1] = "X"
    return valores

def rellenar_numeros(valores, Numero_de_Filas, Numero_de_Columnas):
    for i in range(Numero_de_Filas):
        for j in range(Numero_de_Columnas):
            if valores[i][j] == "X":
                continue

            # Caso general: celda en el centro
            if i-1 >= 0 and i+1 < Numero_de_Filas and j-1 >= 0 and j+1 < Numero_de_Columnas:
                count = 0
                for FV in range(-1, 2):
                    for CV in range(-1, 2):
                        if valores[i+FV][j+CV] == "X":
                            count += 1
                valores[i][j] = str(count)

            # Esquina superior izquierda
            elif i-1 < 0 and j-1 < 0:
                count = 0
                for FV in range(0, 2):
                    for CV in range(0, 2):
                        if valores[i+FV][j+CV] == "X":
                            count += 1
                valores[i][j] = str(count)

            # Esquina superior derecha
            elif i-1 < 0 and j+1 >= Numero_de_Columnas:
                count = 0
                for FV in range(0, 2):
                    for CV in range(-1, 1):
                        if valores[i+FV][j+CV] == "X":
                            count += 1
                valores[i][j] = str(count)

            # Esquina inferior izquierda
            elif i+1 >= Numero_de_Filas and j-1 < 0:
                count = 0
                for FV in range(-1, 1):
                    for CV in range(0, 2):
                        if valores[i+FV][j+CV] == "X":
                            count += 1
                valores[i][j] = str(count)

            # Esquina inferior derecha
            elif i+1 >= Numero_de_Filas and j+1 >= Numero_de_Columnas:
                count = 0
                for FV in range(-1, 1):
                    for CV in range(-1, 1):
                        if valores[i+FV][j+CV] == "X":
                            count += 1
                valores[i][j] = str(count)

            # Borde superior
            elif i-1 < 0:
                count = 0
                for FV in range(0, 2):
                    for CV in range(-1, 2):
                        if valores[i+FV][j+CV] == "X":
                            count += 1
                valores[i][j] = str(count)

            # Borde inferior
            elif i+1 == Numero_de_Filas:
                count = 0
                for FV in range(-1, 1):
                    for CV in range(-1, 2):
                        if valores[i+FV][j+CV] == "X":
                            count += 1
                valores[i][j] = str(count)

            # Borde izquierdo
            elif j-1 < 0:
                count = 0
                for FV in range(-1, 2):
                    for CV in range(0, 2):
                        if valores[i+FV][j+CV] == "X":
                            count += 1
                valores[i][j] = str(count)

            # Borde derecho
            elif j+1 == Numero_de_Columnas:
                count = 0
                for FV in range(-1, 2):
                    for CV in range(-1, 1):
                        if valores[i+FV][j+CV] == "X":
                            count += 1
                valores[i][j] = str(count)

    return valores

def tablero_a_texto(valores):
    filas = len(valores)
    columnas = len(valores[0])
    texto = ""

    # Encabezado de columnas
    for i in range(columnas):
        if i == 0:
            texto += "  "
        elif i == columnas - 1:
            texto += f"{i} {i+1}\n"
        else:
            texto += f"{i} "

    # Línea superior
    texto += " +" + "- " * columnas + "+\n"

    # Filas
    for i in range(filas):
        texto += f"{i+1}|"
        texto += " ".join(valores[i])
        texto += " |\n"

    # Línea inferior
    texto += " +" + "- " * columnas + "+\n"

    return texto