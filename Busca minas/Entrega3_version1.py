import random
from IPython.display import clear_output
import time
import os
from funciones import *

c = 0
r1 = "si"
while r1 == "si":

    # Funcion que se encarga de pedir datos al usuario y validar las entradas
    Nombre,Numero_de_Filas,Numero_de_Columnas,Numero_de_Minas=pedir_datos()

    # Funcion que se encarga de imprimir el tablero 
    imprimir_tablero(Numero_de_Filas, Numero_de_Columnas)

    # Función que se encarga de generar las minas en posiciones aleatorias
    filas_minas, columnas_minas = generar_minas(Numero_de_Filas, Numero_de_Columnas, Numero_de_Minas)

    # Funcion que se encarga de crear el tablero visible para el usuario
    tablero = crear_tablero_visible(Numero_de_Filas, Numero_de_Columnas)

    # Función que se encarga de crear el tablero logico
    valores = crear_tablero_logico(Numero_de_Filas, Numero_de_Columnas)

    # Función que se encarga de ubicar las minas ene l tablero logico
    valores = ubicar_minas(valores, filas_minas, columnas_minas)

    # Función que se encarga de rellenar el tablero logico con los numeros correspondientea
    valores = rellenar_numeros(valores, Numero_de_Filas, Numero_de_Columnas)


    contador = Numero_de_Columnas * Numero_de_Filas - Numero_de_Minas

    movimiento = {}
    while contador > 0:
        respuesta = input("Desea seleccionar una casilla ingrese (si) o elejir una casilla aleatoria ingrese (no)")
        if respuesta == "no":
            fila = random.randint(0, Numero_de_Filas - 1)
            columna = random.randint(0, Numero_de_Columnas - 1)
            while tablero[fila][columna] != ".":
                fila = random.randint(0, Numero_de_Filas - 1)
                columna = random.randint(0, Numero_de_Columnas - 1)
            print(f"Se ha seleccionado la casilla fila {fila + 1}, columna {columna + 1} de forma aleatoria.")
            movimiento[f"{fila},{columna}"] = valores[fila][columna]
        else:
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
            movimiento[f"{fila},{columna}"] = valores[fila][columna]    
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
            c += 1
            estado = "Perdió"
            r1 = input("¿Desea jugar de nuevo? (si/no): ")
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
        c += 1
        estado = "Ganó"
        r1 = input("¿Desea jugar de nuevo? (si/no): ")
    
    # Escritura del archivo txt con los resultados
    with open("resultados_busca_minas.txt", "a") as archivo:
        archivo.write(f"=== Registro de Partida #{c} ===\n")
        archivo.write(f"Jugador: {Nombre}\n\n")
        archivo.write("--- Configuración ---\n")
        archivo.write(f"Tamaño del tablero: {Numero_de_Filas}X{Numero_de_Columnas}\n")
        archivo.write(f"Número de minas: {Numero_de_Minas}\n\n")
        archivo.write("--- Movimientos ---\n")
        for movimiento_clave, movimiento_valor in movimiento.items():
            archivo.write(f"({movimiento_clave}) -> Descubierto: {movimiento_valor}\n")
        archivo.write("\n\n")
        archivo.write("--- Resultado ---\n")
        archivo.write(f"Estado: {estado}\n")
        archivo.write(f"Casillas totales reveladas: {len(movimiento)}\n\n")
        # Tablero revelado al final del juego
        archivo.write("--- Tablero revelado ---\n")
        archivo.write(tablero_a_texto(valores))
        archivo.write("\n\n")


  