# Jennifer Gámez 1610396

import pytest
import math
from modulo_aritmetica import Vector

# Prueba la suma de dos objetos vectores
@pytest.mark.parametrize("a, b, expected", [
    (Vector(1, 2, 3), Vector(4, 5, 6), Vector(5, 7, 9)),  # Caso positivo
    (Vector(0, 0, 0), Vector(4, 5, 6), Vector(4, 5, 6)),  # Vector nulo
    (Vector(-1, -2, -3), Vector(-4, -5, -6), Vector(-5, -7, -9)),  # Vector negativo
    (Vector(1, 2, 3), Vector(-4, -5, -6), Vector(-3, -3, -3)),  # Vector positivo y negativo
])
def test_suma_dos_vectores(a, b, expected):
    resultado = a + b # suma de dos vectores
    assert round(resultado.x, 2) == round(expected.x, 2) 
    assert round(resultado.y, 2) == round(expected.y, 2)
    assert round(resultado.z, 2) == round(expected.z, 2)

# Prueba la suma de un vector mas un número por la derecha.
@pytest.mark.parametrize("a, scalar, expected", [
    (Vector(1, 2, 3), 5, Vector(6, 7, 8)), # Escalar positivo
    (Vector(1, 2, 3), 1.5, Vector(2.5, 3.5, 4.5)), # Escalar negativo
    (Vector(0, 0, 0), -1, Vector(-1, -1, -1)), # Vector negativo
    (Vector(0, 0, 0), 0, Vector(0, 0, 0)), # Vector nul
])
def test_suma_vector_escalar(a, scalar, expected):
    resultado = a + scalar
    assert round(resultado.x, 2) == round(expected.x, 2)
    assert round(resultado.y, 2) == round(expected.y, 2)
    assert round(resultado.z, 2) == round(expected.z, 2)

# Prueba la resta de dos objetos vectores
@pytest.mark.parametrize("a, b, expected", [
    (Vector(1, 2, 3), Vector(4, 5, 6), Vector(-3, -3, -3)), # Vectores positivos
    (Vector(4, 1, 3), Vector(-2, -1, -6), Vector(6, 2, 9)), # Vector positivo y negativo
    (Vector(0, 0, 0), Vector(0, 0, 0), Vector(0, 0, 0)), # Vector nul
])
def test_resta_de_vectores(a, b, expected):
    resultado = a - b
    assert round(resultado.x, 2) == round(expected.x, 2)
    assert round(resultado.y, 2) == round(expected.y, 2)
    assert round(resultado.z, 2) == round(expected.z, 2)

# Prueba la resta de un vector mas un número por la derecha.
@pytest.mark.parametrize("a, scalar, expected", [
    (Vector(1, 2, 5), 5, Vector(-4, -3, 0)), # Escalar positivo
    (Vector(1, 2, 3), 0, Vector(1, 2, 3)), # Escalar nulo
])
def test_resta_vector_escalar(a, scalar, expected):
    resultado = a - scalar
    assert round(resultado.x, 2) == round(expected.x, 2)
    assert round(resultado.y, 2) == round(expected.y, 2)
    assert round(resultado.z, 2) == round(expected.z, 2)

# Prueba el producto cruz de dos objetos vectores
@pytest.mark.parametrize("a, b, expected", [
    (Vector(1, 2, 3), Vector(4, 5, 6), Vector(-3, 6, -3)),
    (Vector(1, 2, 3), Vector(-2, -1, 3), Vector(9, -9, 3)),
    (Vector(0, 0, 0), Vector(-2, -1, 3), Vector(0, 0, 0)),
])
def test_producto_cruz_de_vectores(a, b, expected):
    resultado = a * b
    assert round(resultado.x, 2) == round(expected.x, 2)
    assert round(resultado.y, 2) == round(expected.y, 2)
    assert round(resultado.z, 2) == round(expected.z, 2)

# Prueba la multiplicación de un vector por un número por la derecha. Producto cruz.
@pytest.mark.parametrize("a, scalar, expected", [
    (Vector(1, 2, 3), 2, Vector(2, 4, 6)),  # Escalar positivo
    (Vector(0, 0, 0), 100, Vector(0, 0, 0)),  # Escalar grande con vector nulo
    (Vector(1, 1, 1), 0, Vector(0, 0, 0)),  # Escalar nulo
    (Vector(1, 2, 3), 0.5, Vector(0.5, 1, 1.5)),  # Escalar flotante
    (Vector(1e100, 1e100, 1e100), 2, Vector(2e100, 2e100, 2e100)),  # Valores grandes
])
def test_multiplicacion_por_escalar(a, scalar, expected):
    resultado = a * scalar
    assert round(resultado.x, 2) == round(expected.x, 2)
    assert round(resultado.y, 2) == round(expected.y, 2)
    assert round(resultado.z, 2) == round(expected.z, 2)

# Prueba el cálculo del producto punto de dos objetos vectores
@pytest.mark.parametrize("a, b, expected", [
    (Vector(1, 2, 3), Vector(4, 5, 6), 32),
    (Vector(1e100, 1e100, 1e100), Vector(1e100, 1e100, 1e100), 3e200),  # Valores grandes
])
def test_producto_punto_de_vectores(a, b, expected):
    resultado = a % b
    if isinstance(resultado, Vector):
        assert round(resultado.x, 2) == round(expected.x, 2)
        assert round(resultado.y, 2) == round(expected.y, 2)
        assert round(resultado.z, 2) == round(expected.z, 2)
    else:
        assert resultado == expected
    
# Prueba el cálculo de la norma
@pytest.mark.parametrize("a, expected_norm", [
    (Vector(1, 2, 3), math.sqrt(14)),
    (Vector(4, 0, 0), 4.0),
])
def test_norma_de_vector(a, expected_norm):
    resultado = a.norm()
    assert round(resultado, 2) == round(expected_norm, 2)

# Prueba la operación (a * b) + c
@pytest.mark.parametrize("a, b, c, expected", [
    (Vector(1, 2, 3), Vector(4, 5, 6), Vector(7, 8, 9), Vector(4, 14, 6)),
    (Vector(0, 0, 0), Vector(0, 0, 0), Vector(0, 0, 0), Vector(0, 0, 0)),  # Ejemplo con vectores nulos
])
def test_operacion_a_b_mas_c(a, b, c, expected):
    resultado = (a * b) + c
    assert round(resultado.x, 2) == round(expected.x, 2)
    assert round(resultado.y, 2) == round(expected.y, 2)
    assert round(resultado.z, 2) == round(expected.z, 2)

# Prueba la operación: a * 3.0 + b.norm()
@pytest.mark.parametrize("a, b, expected", [
    (Vector(1, 2, 3), Vector(4, 5, 6), Vector(11.77, 14.77, 17.77)),
    (Vector(0, 0, 0), Vector(4, 5, 6), Vector(8.77, 8.77, 8.77)),
])
def test_operacion_a_por_escalar_mas_b_norma(a, b, expected):
    resultado = a * 3.0 + b.norm() # uso de .norm() en lugar de &b debido a que no se puede sobrecargar & en pyhon
    assert round(resultado.x, 2) == round(expected.x, 2)
    assert round(resultado.y, 2) == round(expected.y, 2)
    assert round(resultado.z, 2) == round(expected.z, 2)

# Prueba la operación (b + b) * (c - a)
@pytest.mark.parametrize("a, b, c, expected", [(Vector(1, 2, 3), Vector(4, 5, 6), Vector(7, 8, 9), Vector(-12, 24, -12))])
def test_operacion_b_mas_b_por_c_menos_a(a, b, c, expected):
    resultado = (b + b) * (c - a)
    assert round(resultado.x, 2) == round(expected.x, 2)
    assert round(resultado.y, 2) == round(expected.y, 2)
    assert round(resultado.z, 2) == round(expected.z, 2)

# Prueba la operación: a * 3.0 + b.norm()
@pytest.mark.parametrize("a, b, expected", [
    (Vector(1, 2, 3), Vector(4, 5, 6), Vector(11.77, 14.77, 17.77)),
    (Vector(0, 0, 0), Vector(4, 5, 6), Vector(8.77, 8.77, 8.77)),
])
def test_operacion_a_por_escalar_mas_b_norma(a, b, expected):
    resultado = a * 3.0 + b.norm() # uso de .norm() en lugar de &b debido a que no se puede sobrecargar & en pyhon
    assert round(resultado.x, 2) == round(expected.x, 2)
    assert round(resultado.y, 2) == round(expected.y, 2)
    assert round(resultado.z, 2) == round(expected.z, 2)

