# Jennifer Gamez 16-10396

import math

# Vector: es una clase que tiene como métodos la sobrecarga de las operaciones
# +, -, * y %, para operar vectores de tres dimensiones (x, y, z), las operaciones
# estan definidas por la derecha.
# en Python el operador &, no se puede sobrecargar por lo que para calcular la norma
# de un vector ya que no es un operador aritmético estandar es necesario usar el 
# método .norm()
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Suma: sobrecarga de la operación +, para dos vectores, o para la suma de un vector
    # y un numero (entero o flotante) por la derecha.
    def __add__(self, other):
        if isinstance(other, Vector):
            # Suma dos objetos Vector
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, (int, float)):
            # Suma un número al vector
            return Vector(self.x + other, self.y + other, self.z + other)

    # Resta: sobrecarga de la operación -, para dos vectores,  o para la resta de un vector
    # y un numero (entero o flotante) por la derecha.
    def __sub__(self, other):
        if isinstance(other, Vector):
            # Resta dos objetos Vector
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, (int, float)):
            # Resta un número al vector
            return Vector(self.x - other, self.y - other, self.z - other)

    # Multiplicación, producto cruz: sobrecarga de la operación *, para dos vectores,
    # y un vector y un número (entero o flotante) por la derecha.
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            # Producto cruz de un vector con un numero
            return Vector(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector):
            # Producto cruz de dos objetos vectores
            x = self.y * other.z - self.z * other.y
            y = self.z * other.x - self.x * other.z 
            z = self.x * other.y - self.y * other.x
            return Vector(x, y, z)
        
    # Producto punto (modulo %): sobrecarga de la operación %, para dos vectores
    # como la operación del producto punto.
    def __mod__(self, other):
        if isinstance(other, Vector):
            # Producto punto
            return self.x * other.x + self.y * other.y + self.z * other.z
        

    # En python el operador & no se puede sobrecargar, se propone entonces el uso de norm
    # para el calculo de la norma de un vector.
    #def __and__(self, other):
    #    # Norma
    #    return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    # Norma: calcula la norma de un vector. 
    def norm(self):
        # Calcular la norma y redondear a dos decimales
        return round(math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2), 2)

    # Muestra el vector como un string.                                                                                                                                                                                                                                                                                                                                 
    #def __str__(self):
    #    return f"({self.x}, {self.y}, {self.z})"
