# Segunda entrega 

import random
from IPython.display import clear_output
import time
import os

#Mensaje de Bienvenida.
Mensaje=("Un saludo buscador de minas 💣")
print(Mensaje)

# Validaciones de entrada ya incluidas en la primera parte.
# Si el usuario cumple con todas las condiciones de los campos de entrada, se le permitirá continuar.
# Si no, cada campo volverá a solicitar la información hasta que se ingrese correctamente.

while True:
    Nombre=input("Ingrese su nombre:")
    if Nombre == "":
        print("Por favor,debe ingresar su nombre")
    else:
        break
    
while True:
    Numero_de_Filas = int(input("Ingrese el numero de filas:"))
    if Numero_de_Filas < 0 or Numero_de_Filas > 9:
        print("Debe ingresar un numero de filas mayor a 0 y menor o igual a 9")
    else:
        break

while True:
    Numero_de_Columnas=int(input("Ingrese el numero de columnas:"))
    if Numero_de_Columnas < 0 or Numero_de_Columnas > 9:
        print("Debe ingresar un numero de columnas mayor a 0")
    else:
        break
while True:
    Numero_de_Minas=int(input("Ingrese el numero de minas:"))
    if Numero_de_Minas <= 0 or Numero_de_Minas > (Numero_de_Filas*Numero_de_Columnas):
        print("Debe ingresar un numero mayor 0 y menor o igual al tamaño de su tablero")
    else:
        break       


# Generación del tablero dinamico

for i in range(Numero_de_Columnas): # Controla los numeros de las columnas.
    if i == 0:
        print("  ",end="")
    elif i == Numero_de_Columnas-1:
        print(f"{i} {i+1}",sep="\n")       
    elif i != 0:
        print(f"{i} ",end="")
print(f" +{"- "*Numero_de_Columnas}+")     

for i in range(Numero_de_Filas):  # Los numeros de los titulos de las columnas estan fijos en el primer print y  los de las filas los controla el for
  print(str(i+1)+"|",". "*Numero_de_Columnas,"|",sep="")

print(f" +{"- "*Numero_de_Columnas}+")   

# Generación de las minas en posiciones aleatorias
filas_minas = []
columnas_minas = []

while len(filas_minas) < Numero_de_Minas: # Se utiliza la funcion randint para generar los numeros 
    fila = random.randint(1, Numero_de_Filas)
    columna = random.randint(1, Numero_de_Columnas)
    if (fila, columna) not in list(zip(filas_minas, columnas_minas)): # Se asegura que no se repitann las posiciones 
        filas_minas.append(fila)
        columnas_minas.append(columna)


# Para el ejercicio se crea un tablaro visible y un tablero logico.
# Crear tablero visible (lo que ve el jugador)
tablero = []
for i in range(Numero_de_Filas):
    fila = []
    for j in range(Numero_de_Columnas):
        fila.append(".")
    tablero.append(fila)

# Crear tablero lógico (con minas y números)
valores = []
for i in range(Numero_de_Filas):
    fila = []
    for j in range(Numero_de_Columnas):
        fila.append(0)
    valores.append(fila)


# Se ubican las minas dentro del tablero logico, con respecto a las posiciones generadas anteriormente.
for fila,columna in zip(filas_minas, columnas_minas):
    valores[fila-1][columna-1] = "X"

# Rellenar tableros de numeros alrededor de las minas
# La logica de este codigo es revvisar cada celda del tablero logico y dependiendo de su posición 
# (Centro,esquina,columna borde) se revisan las celdas adyacentes correspondientes para contar las minas.


for i in range(Numero_de_Filas):
    for j in range(Numero_de_Columnas):
        if valores[i][j] == "X":
            continue
        elif  i-1 >= 0 and i+1 < Numero_de_Filas and j-1 >= 0 and j+1 < Numero_de_Columnas:
            count = 0
            for FV in range(-1,2):
                for CV in range(-1,2):
                    if valores[i+FV][j+CV] == "X":
                        count += 1
            valores[i][j] = str(count)
        elif i-1 < 0 and j-1 < 0:
            count = 0
            for FV in range(0,2):
                for CV in range(0,2):
                    if valores[i+FV][j+CV] == "X":
                        count += 1
            valores[i][j] = str(count)
        elif i-1 < 0 and j+1 >= Numero_de_Columnas:
            count = 0
            for FV in range(0,2):
                for CV in range(-1,1):
                    if valores[i+FV][j+CV] == "X":
                        count += 1
            valores[i][j] = str(count)
        elif i+1 >= Numero_de_Filas and j-1 < 0:
            count = 0
            for FV in range(-1,1):
                for CV in range(0,2):
                    if valores[i+FV][j+CV] == "X":
                        count += 1
            valores[i][j] = str(count)
        elif i+1 >= Numero_de_Filas and j+1 >= Numero_de_Columnas:
            count = 0
            for FV in range(-1,1):
                for CV in range(-1,1):
                    if valores[i+FV][j+CV] == "X":
                        count += 1
            valores[i][j] = str(count)
        elif i-1 < 0:
            count = 0
            for FV in range(0,2):
                for CV in range(-1,2):
                    if valores[i+FV][j+CV] == "X":
                        count += 1
            valores[i][j] = str(count)
        elif i+1 == Numero_de_Filas:
            count = 0
            for FV in range(-1,1):
                for CV in range(-1,2):
                    if valores[i+FV][j+CV] == "X":
                        count += 1
            valores[i][j] = str(count)
        elif j-1 < 0:
            count = 0
            for FV in range(-1,2):
                for CV in range(0,2):
                    if valores[i+FV][j+CV] == "X":
                        count += 1
            valores[i][j] = str(count)
        elif j+1 == Numero_de_Columnas:
            count = 0
            for FV in range(-1,2):
                for CV in range(-1,1):
                    if valores[i+FV][j+CV] == "X":
                        count += 1
            valores[i][j] = str(count)      

# Inicio de la partida 
contador = Numero_de_Columnas * Numero_de_Filas - Numero_de_Minas

while contador > 0:
    # Solicitar al usuario que ingrese la fila y columna a descubrir
    while True:
        fila = int(input("Ingrese la fila a descubrir: ")) 
        if fila < 1 or fila > Numero_de_Filas:
            print("Fila inválida. Por favor, ingrese una fila válida entre.",1, "y", Numero_de_Filas)
        else:
            fila = fila - 1
            break
    while True :
        columna = int(input("Ingrese la columna a descubrir: ")) 
        if columna < 1 or columna > Numero_de_Columnas:
            print("Columna inválida. Por favor, ingrese una columna válida entre.",1, "y", Numero_de_Columnas)
        else:
            columna = columna - 1
            break
    clear_output(wait=True)   
    # Verificar si el usuario ha descubierto una mina
    if valores[fila][columna] == "X":
        # Imprimer tablero visible o logico para el jugador
        #clear_output(wait=True)
        for i in range(Numero_de_Columnas): # Controla los numeros de las columnas.
            if i == 0:
                print("  ",end="")
            elif i == Numero_de_Columnas-1:
              print(f"{i} {i+1}",sep="\n")       
            elif i != 0:
              print(f"{i} ",end="")
        
        print(f" +{"- "*Numero_de_Columnas}+")
        for i in range(Numero_de_Filas):  # Los numeros de los titulos de las columnas estan fijos en el primer print y  los de las filas los controla el for
         print(str(i+1)+"|",(" ").join(valores[i])," |",sep="")
        print(f" +{"- "*Numero_de_Columnas}+")
        print("🧨🤯¡Has descubierto una mina!🤣 ¡Juego terminado!👎")
        break
    else:
        tablero[fila][columna] = valores[fila][columna]
        # Imprimir el tablero visible actualizado
        #clear_output(wait=True)
        for i in range(Numero_de_Columnas): # Controla los numeros de las columnas.
            if i == 0:
                print("  ",end="")
            elif i == Numero_de_Columnas-1:
                print(f"{i} {i+1}",sep="\n")       
            elif i != 0:
                print(f"{i} ",end="")
        print(f" +{"- "*Numero_de_Columnas}+")
        for i in range(Numero_de_Filas):  # Los numeros de los titulos de las columnas estan fijos en el primer print y  los de las filas los controla el for
            print(str(i+1)+"|",(" ").join(tablero[i])," |",sep="")
        print(f" +{"- "*Numero_de_Columnas}+")
        print("¡Casilla descubierta con éxito! 🎉, siguiente elección 🧐")
        contador -= 1
# Verificar si el jugador ha ganado        
if contador == 0:
    print("🎉🎉¡Felicidades! Has descubierto todas las casillas sin minas. ¡Has ganado el juego!🏆🥳")

