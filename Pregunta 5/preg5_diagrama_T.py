class Lenguaje:
    def __init__(self, nombre):
        self.nombre = nombre

class Programa:
    def __init__(self, nombre, lenguaje):
        self.nombre = nombre
        self.lenguaje = lenguaje

class Interprete:
    def __init__(self, lenguaje_base, lenguaje):
        self.lenguaje_base = lenguaje_base
        self.lenguaje = lenguaje

class Traductor:
    def __init__(self, lenguaje_base, lenguaje_origen, lenguaje_destino):
        self.lenguaje_base = lenguaje_base
        self.lenguaje_origen = lenguaje_origen
        self.lenguaje_destino = lenguaje_destino

class Simulador:
    def __init__(self):
        self.lenguajes = {}
        self.programas = {}
        self.interpretes = {}
        self.traductores = {}

    def definir(self, tipo, argumentos):
        if tipo == "PROGRAMA":
            nombre, lenguaje = argumentos
            if nombre not in self.programas:
                self.programas[nombre] = Programa(nombre, lenguaje)

                self.lenguajes[lenguaje] = Lenguaje(lenguaje)

                print(f"Se definió el programa '{nombre}', ejecutable en '{lenguaje}'")
            else:
                print(f"Error: El programa '{nombre}' ya tiene un programa asociado.")

        elif tipo == "INTERPRETE":
            lenguaje_base, lenguaje = argumentos
            self.interpretes[lenguaje] = Interprete(lenguaje_base, lenguaje)
            self.lenguajes[lenguaje] = Lenguaje(lenguaje)
            self.lenguajes[lenguaje_base] = Lenguaje(lenguaje_base)
            
            print(f"Se definió un intérprete para '{lenguaje}', escrito en '{lenguaje_base}'")

        elif tipo == "TRADUCTOR":
            lenguaje_base, lenguaje_origen, lenguaje_destino = argumentos
            self.traductores[(lenguaje_origen, lenguaje_destino)] = Traductor(lenguaje_base, lenguaje_origen, lenguaje_destino)
            
            self.lenguajes[lenguaje_base] = Lenguaje(lenguaje_base)  # Agregar lenguaje base al diccionario
            self.lenguajes[lenguaje_origen] = Lenguaje(lenguaje_origen)  # Agregar lenguaje origen al diccionario
            self.lenguajes[lenguaje_destino] = Lenguaje(lenguaje_destino)  # Agregar lenguaje destino al diccionar

            print(f"Se definió un traductor de '{lenguaje_origen}', hacia '{lenguaje_destino}', escrito en '{lenguaje_base}'")

    def ejecutable(self, nombre):
        if nombre in self.programas:
            programa = self.programas[nombre]

            if programa.lenguaje == "LOCAL":
                print(f"Sí, es posible ejecutar el programa '{nombre}'")
                return

            if programa.lenguaje in self.lenguajes:
                lenguaje_destino = "LOCAL"  # Lenguaje destino inicial

                # Crear un conjunto para realizar un seguimiento de los lenguajes visitados
                visited = set()

                def es_ejecutable(desde, hacia):
                    visited.add(desde)

                    # Verificar si hay una ruta válida a través de intérpretes y traductores
                    if desde == hacia:
                        return True

                    if desde in self.interpretes:
                        if self.interpretes[desde].lenguaje_base not in visited and es_ejecutable(self.interpretes[desde].lenguaje_base, hacia):
                            return True

                    for (origen, destino) in self.traductores:
                        if origen == desde and destino not in visited and es_ejecutable(destino, hacia):
                            return True

                    return False

                if es_ejecutable(programa.lenguaje, lenguaje_destino):
                    print(f"Sí, es posible ejecutar el programa '{nombre}'")
                else:
                    print(f"No es posible ejecutar el programa '{nombre}' debido a la falta de una ruta adecuada.")
            else:
                print(f"No se puede ejecutar '{nombre}' debido a la falta de soporte para el lenguaje '{programa.lenguaje}'.")
        else:
            print(f"Error: El programa '{nombre}' no está definido.")



    def salir(self):
        exit()

    def main(self):
        print("Simulador de programas, intérpretes y tarductores.")
        print("Ingrese una acción: DEFINIR, EJECUTABLE y SALIR")

        while True:
            linea = input("$> ").upper()
            accion = linea.split()
            tipo = accion[0]

            if tipo == "DEFINIR":
                if len(accion) >= 3:
                    self.definir(accion[1], accion[2:])
                else:
                    print("Error: Falta información en la acción DEFINIR.")

            elif tipo == "EJECUTABLE":
                if len(accion) == 2:
                    self.ejecutable(accion[1])
                else:
                    print("Error: Acción EJECUTABLE debe tener un argumento.")

            elif tipo == "SALIR":
                self.salir()

            else:
                print("Acción no válida. Las acciones válidas son DEFINIR, EJECUTABLE y SALIR.")

if __name__ == "__main__":
    simulador = Simulador()
    simulador.main()
