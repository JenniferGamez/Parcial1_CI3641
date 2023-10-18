from collections import deque
"""
El "buddy system" se refiere a un algoritmo utilizado para administrar la 
asignación y liberación de bloques de memoria. Este sistema divide la 
memoria en bloques de tamaños específicos, y cada bloque se puede dividir_bloques 
en dos bloques "hermanos" del mismo tamaño hasta conseguir un bloque con el tamaño
del programa a reservar.
"""

class Bloque:
    def __init__(self):
        self.proceso = ""
        self.bloque_mayor = None
        self.hijoDer = None
        self.hijoIzq = None
        self.bloque_disp = True
        self.posicion = 0

    def bloque_libre(self):
        return self.bloque_disp

    def orden(self):
        return self.posicion

class BuddySystem:
    def __init__(self, n):
        self.orden = n
        self.memoria = [deque() for _ in range(n + 1)]
        self.nombre_proc = []
        self.orden_proc = []
        self.memoria[n].append(Bloque())
        self.memoria[n][0].posicion = n

    # buscar_bloque busca un bloque libre en la memoria de tamaño n o superior, 
    # sino hay bloques libres retorna none (no hay bloques disponibles), de lo 
    # contrario retorna el bloque libre.
    def buscar_bloque(self, n):
        bloque_encontrado = None

        if n > self.orden:
            return None
        
        for i in self.memoria[n]:
            if i.bloque_libre():
                bloque_encontrado = i
                break
        if bloque_encontrado is None:
            bloque_encontrado = self.buscar_bloque(n + 1)

        return bloque_encontrado
    
    # dividir_bloques divide el bloque en dos partes hasta que alcance el tamaño
    # n de forma recursiva.
    def dividir_bloques(self, bloque, n):
        bloque_dividido = bloque
        if bloque_dividido.orden() > n:
            hijo_der = Bloque()
            hijo_izq = Bloque()
            hijo_der.bloque_mayor = bloque_dividido
            hijo_izq.bloque_mayor = bloque_dividido
            hijo_der.posicion = bloque_dividido.orden() - 1
            hijo_izq.posicion = bloque_dividido.orden() - 1
            bloque_dividido.hijoDer = hijo_der
            bloque_dividido.hijoIzq = hijo_izq
            bloque_dividido.bloque_disp = False
            self.memoria[bloque_dividido.orden() - 1].append(hijo_der)
            self.memoria[bloque_dividido.orden() - 1].append(hijo_izq)
            bloque_dividido = self.dividir_bloques(hijo_izq, n)
            bloque_dividido.bloque_disp = False
        return bloque_dividido
    
    # unir_bloque une dos bloques si ambos estan disponibles.
    def unir_bloques(self, bloque_1, bloque_2):
        if bloque_1.bloque_libre() and bloque_2.bloque_libre():
            self.memoria[bloque_1.orden()].remove(bloque_1)
            self.memoria[bloque_1.orden()].remove(bloque_2)
            bloque_1.bloque_mayor.bloque_disp = True
            if bloque_1.bloque_mayor.bloque_mayor is not None:
                self.unir_bloques(bloque_1.bloque_mayor.bloque_mayor.hijoDer, bloque_1.bloque_mayor.bloque_mayor.hijoIzq)
    
    # reservar_bloque se encarga de buscar un bloque de memoria adecuado para asignar un proceso y realiza la 
    # asignación teniendo en cuenta las restricciones del algoritmo Buddy System. Si no se puede encontrar un 
    # bloque adecuado o si el proceso ya está en memoria, la función devuelve False. De lo contrario, devuelve 
    # True después de asignar con éxito el proceso al bloque correspondiente.
    def reservar_bloque(self, nombre_proceso, n):
        if nombre_proceso in self.nombre_proc:
            return False

        bloque_reservado = None
        i = self.orden

        while i > 0:
            if 2 ** (i - 1) < n < 2 ** i + 1:
                break
            i -= 1

        if 2 ** i < n:
            return False

        bloque_reservado = self.buscar_bloque(i)

        if bloque_reservado is not None and bloque_reservado.orden() > i:
            bloque_reservado = self.dividir_bloques(bloque_reservado, i)

        elif bloque_reservado is None:
            return False

        bloque_reservado.proceso = nombre_proceso
        bloque_reservado.bloque_disp = False

        if nombre_proceso in self.nombre_proc:
            self.orden_proc[self.nombre_proc.index(nombre_proceso)] = i
        else:
            self.nombre_proc.append(nombre_proceso)
            self.orden_proc.append(i)

        return True

    # liberar_bloque libera el proceso si este se encuentra en memoria.
    def liberar_bloque(self, nombre_proceso):
        bloque_liberado = False

        if nombre_proceso in self.nombre_proc:
            i = self.nombre_proc.index(nombre_proceso)
            bloque_liberado = True
            orden = self.orden_proc[i]

            for bloque in self.memoria[orden]:
                if bloque.proceso == nombre_proceso:
                    bloque.proceso = ""
                    bloque.bloque_disp = True

                    if bloque.bloque_mayor is not None:
                        self.unir_bloques(bloque.bloque_mayor.hijoDer, bloque.bloque_mayor.hijoIzq)

            self.orden_proc.pop(i)
            self.nombre_proc.pop(self.nombre_proc.index(nombre_proceso))

        return bloque_liberado

    
    # num_bloque_disp este muestra el numero de bloque disponible
    def num_bloques_disp(self):
        n_bloques = 0
        for lista in self.memoria:
            for bloque in lista:
                if bloque.bloque_disp:
                    n_bloques += 1
        return n_bloques
