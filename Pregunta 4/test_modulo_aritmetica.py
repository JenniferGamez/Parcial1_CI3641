# Jennifer Gámez 1610396

import pytest
import math
from modulo_aritmetica import Vector
  
# Prueba la suma de dos objetos vectores
@pytest.mark.parametrize("a, b, expected", [(Vector(1, 2, 3), Vector(4, 5, 6), Vector(5, 7, 9))])
def test_suma_dos_vectores(a, b, expected):
    resultado = a + b
    assert math.isclose(resultado.x, expected.x, rel_tol=1e-9)
    assert math.isclose(resultado.y, expected.y, rel_tol=1e-9)
    assert math.isclose(resultado.z, expected.z, rel_tol=1e-9)

# Prueba la suma de un vector mas un número por la derecha.
@pytest.mark.parametrize("a, scalar, expected", [(Vector(1, 2, 3), 5, Vector(6, 7, 8))])
def test_suma_vector_escalar(a, scalar, expected):
    resultado = a + scalar
    assert math.isclose(resultado.x, expected.x, rel_tol=1e-9)
    assert math.isclose(resultado.y, expected.y, rel_tol=1e-9)
    assert math.isclose(resultado.z, expected.z, rel_tol=1e-9)

# Prueba la resta de dos objetos vectores
@pytest.mark.parametrize("a, b, expected", [(Vector(1, 2, 3), Vector(4, 5, 6), Vector(-3, -3, -3))])
def test_resta_de_vectores(a, b, expected):
    resultado = a - b
    assert math.isclose(resultado.x, expected.x, rel_tol=1e-9)
    assert math.isclose(resultado.y, expected.y, rel_tol=1e-9)
    assert math.isclose(resultado.z, expected.z, rel_tol=1e-9)

# Prueba la resta de un vector mas un número por la derecha.
@pytest.mark.parametrize("a, scalar, expected", [(Vector(1, 2, 3), 5, Vector(-4, -3, -2))])
def test_resta_vector_escalar(a, scalar, expected):
    resultado = a - scalar
    assert math.isclose(resultado.x, expected.x, rel_tol=1e-9)
    assert math.isclose(resultado.y, expected.y, rel_tol=1e-9)
    assert math.isclose(resultado.z, expected.z, rel_tol=1e-9)

# Prueba el producto cruz de dos objetos vectores
@pytest.mark.parametrize("a, b, expected", [(Vector(1, 2, 3), Vector(4, 5, 6), Vector(-3, 6, -3))])
def test_producto_cruz_de_vectores(a, b, expected):
    resultado = a * b
    assert math.isclose(resultado.x, expected.x, rel_tol=1e-9)
    assert math.isclose(resultado.y, expected.y, rel_tol=1e-9)
    assert math.isclose(resultado.z, expected.z, rel_tol=1e-9)

# Prueba la multiplicación de un vector por un número por la derecha. Producto cruz.
@pytest.mark.parametrize("a, scalar, expected", [(Vector(1, 2, 3), 5, Vector(5, 10, 15))])
def test_multiplicacion_por_escalar(a, scalar, expected):
    resultado = a * scalar
    assert math.isclose(resultado.x, expected.x, rel_tol=1e-9)
    assert math.isclose(resultado.y, expected.y, rel_tol=1e-9)
    assert math.isclose(resultado.z, expected.z, rel_tol=1e-9)

# Prueba el cálculo del producto punto de dos objetos vectores
@pytest.mark.parametrize("a, b, expected", [(Vector(1, 2, 3), Vector(4, 5, 6), 32)])
def test_producto_punto_de_vectores(a, b, expected):
    resultado = a % b
    assert resultado == expected

# Prueba el cálculo de la norma
@pytest.mark.parametrize("a, expected_norm", [
    (Vector(1, 2, 3), math.sqrt(14)),
    (Vector(4, 0, 0), 4.0),  # Ejemplo con vector en el eje X
    (Vector(0, 5, 0), 5.0),  # Ejemplo con vector en el eje Y
    (Vector(0, 0, 6), 6.0),  # Ejemplo con vector en el eje Z
])
def test_norma_de_vector(a, expected_norm):
    resultado = a.norm()
    assert round(resultado, 2) == round(expected_norm, 2)

# Prueba la operación (a * b) + c
@pytest.mark.parametrize("a, b, c, expected_result", [
    (Vector(1, 2, 3), Vector(4, 5, 6), Vector(7, 8, 9), Vector(4, 14, 6)),
    (Vector(0, 0, 0), Vector(0, 0, 0), Vector(0, 0, 0), Vector(0, 0, 0)),  # Ejemplo con vectores nulos
])
def test_operacion_a_b_mas_c(a, b, c, expected_result):
    resultado = (a * b) + c
    assert resultado.x == expected_result.x
    assert resultado.y == expected_result.y
    assert resultado.z == expected_result.z

# Prueba la operación a % (c * b) = 0
@pytest.mark.parametrize("a, b, c, expected_result", [(Vector(1, 2, 3), Vector(4, 5, 6), Vector(7, 8, 9), 0)])
def test_operacion_a_modulo_c_por_b(a, b, c, expected_result):
    resultado = a % (c * b)
    assert resultado == expected_result

# Prueba la operación (b + b) * (c - a)
@pytest.mark.parametrize("a, b, c, expected_result", [(Vector(1, 2, 3), Vector(4, 5, 6), Vector(7, 8, 9), Vector(-12, 24, -12))])
def test_operacion_b_mas_b_por_c_menos_a(a, b, c, expected_result):
    resultado = (b + b) * (c - a)
    assert resultado.x == expected_result.x
    assert resultado.y == expected_result.y
    assert resultado.z == expected_result.z

# Prueba la operación (b + b) * (c % a)
@pytest.mark.parametrize("a, b, c, expected_result", [(Vector(1, 2, 3), Vector(4, 5, 6), Vector(7, 8, 9), Vector(400, 500, 600))])
def test_operacion_b_mas_b_por_c_modulo_a(a, b, c, expected_result):
    resultado = (b + b) * (c % a)
    assert resultado.x == expected_result.x
    assert resultado.y == expected_result.y
    assert resultado.z == expected_result.z

# Prueba la operación: a * 3.0 + b.norm()
@pytest.mark.parametrize("a, b, c, expected_result", [(Vector(1, 2, 3), Vector(4, 5, 6), Vector(7, 8, 9), Vector(11.77, 14.77, 17.77))])
def test_operacion_a_por_escalar_mas_b_norma(a, b, c, expected_result):
    resultado = a * 3.0 + b.norm() # uso de .norm() en lugar de &b debido a que no se puede sobrecargar & en pyhon
    assert resultado.x == expected_result.x
    assert resultado.y == expected_result.y
    assert resultado.z == expected_result.z

def test_precisión():
    a = Vector(1.0, 2.0, 3.0)
    b = Vector(0.1, 0.2, 0.3)
    resultado = a + b
    assert math.isclose(resultado.x, 1.1, rel_tol=1e-9)
    assert math.isclose(resultado.y, 2.2, rel_tol=1e-9)
    assert math.isclose(resultado.z, 3.3, rel_tol=1e-9)

def test_operaciones_con_vectores_nulos():
    vector_nulo = Vector(0, 0, 0)
    resultado = vector_nulo + vector_nulo
    assert resultado.x == 0.0
    assert resultado.y == 0.0
    assert resultado.z == 0.0

def test_operaciones_con_vectores_negativos():
    a = Vector(-1, -2, -3)
    b = Vector(-4, -5, -6)
    resultado = a + b
    assert resultado.x == -5.0
    assert resultado.y == -7.0
    assert resultado.z == -9.0

def test_límites_de_precisión():
    a = Vector(1e-100, 1e-200, 1e-300)
    b = Vector(1e-1000, 1e-2000, 1e-3000)
    resultado = a + b
    # Verificar que resultado sea aproximadamente igual a a, ya que b es extremadamente pequeño
    assert math.isclose(resultado.x, a.x, rel_tol=1e-100)


@pytest.mark.parametrize("a, b, expected_result", [(Vector(1, 2, 3), Vector(0, 0, 0), Vector(0,0, 0))])
def test_operacion_b_mas_b_por_c_menos_a(a, b, expected_result):
    resultado = a * b
    assert resultado.x == expected_result.x
    assert resultado.y == expected_result.y
    assert resultado.z == expected_result.z