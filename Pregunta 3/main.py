from buddy_system import BuddySystem  # Importa las clases y funciones necesarias desde buddy_system.py

# Main que inicializa el El "buddy system" se refiere a un algoritmo utilizado para administrar la 
# asignación y liberación de bloques de memoria.
def main():
    particiones = []
    linea = ""
    instruccion = []

    orden_max = int(input("Ingrese el orden máximo de bloques: "))

    # Calcular el número binario en función del orden máximo
    binario = bin(2 ** orden_max - 1)[2:]

    particiones = []

    j = 0
    for i in range(len(binario) - 1, -1, -1):
        if binario[i] == '1':
            particiones.append(BuddySystem(j))
        j += 1


    print("Manejador de memoria que implementa el buddy system.")
    print("Acciones: RESERVAR, LIBERAR, MOSTRAR, AYUDA y SALIR.")

    # Constantemente le pide una acción al usuario.
    while True:
        linea = input("$> ")
        instruccion = linea.split()

        if instruccion[0].upper() == "RESERVAR":
            # Verificar si el proceso ya está en memoria antes de intentar la reserva
            proceso_existente = False
            for particion in particiones:
                if instruccion[2] in particion.nombre_proc:
                    proceso_existente = True
                    break
            
            if proceso_existente:
                print("\tError, el proceso ya está en memoria.")
            else:
                resultado = False
                for particion in particiones:
                    resultado = particion.reservar_bloque(instruccion[2], int(instruccion[1]))
                    if resultado:
                        print("\tPrograma reservado.")
                        break

                if not resultado:
                    print("\tError, no hay suficientes bloques disponibles de manera contigua.")

        elif instruccion[0].upper() == "LIBERAR":
            resultado = False
            particion_liberada = None  # Mantén un seguimiento de la partición liberada

            for particion in particiones:
                resultado = particion.liberar_bloque(instruccion[1])

                if resultado:
                    particion_liberada = particion  # Almacena la partición liberada
                    break

            if not resultado:
                print(f"\tError, no hay ningún {instruccion[1]} asociado a la memoria.")
            else:
                # Elimina la partición liberada de la lista particiones
                particiones.remove(particion_liberada)
                print(f"\t{instruccion[1]} liberado correctamente.")
        
        elif instruccion[0].upper() == "MOSTRAR":
            salida_memoria = ""

            for i in range(orden_max):
                bloques_disp = 0
                mem_disp = 2 ** i

                for particion in particiones:
                    bloques_disp += particion.num_bloques_disp()

                salida_memoria += f"\nBloques de tamaño {mem_disp} disponibles:\n\tHay {bloques_disp} bloques disponibles.\n"
        
            salida_memoria += "\nLista con los procesos que tienen bloques de memoria reservados.\n"

            for particion in particiones:
                for i in range(len(particion.nombre_proc)):
                    espacio = 2 ** particion.orden_proc[i]
                    salida_memoria += f"Nombre: {particion.nombre_proc[i]} -> Tamaño de bloque asignado: {espacio}\n"
            
            print(salida_memoria)

        elif instruccion[0].upper() == "SALIR":
            print("Adiós!") 
            break

        elif instruccion[0].upper() == "AYUDA":
            print("Instrucciones del programa:")
            print("1. Para reservar un bloque de memoria, escriba: RESERVAR tamaño_del_bloque nombre_del_proceso")
            print("   Ejemplo: RESERVAR Proceso1 32")
            print("2. Para liberar un bloque de memoria asociado a un proceso, escriba: LIBERAR nombre_del_proceso")
            print("   Ejemplo: LIBERAR Proceso1")
            print("3. Para mostrar el estado actual de la memoria y la lista de procesos, escriba: MOSTRAR")
            print("4. Para ver estas instrucciones nuevamente, escriba: AYUDA")
            print("5. Para salir del programa, escriba: SALIR.\n")

        else:
            print("Error, por favor intente nuevamente. Consulte el instructivo si necesita ayuda.")

if __name__ == "__main__":
    main()