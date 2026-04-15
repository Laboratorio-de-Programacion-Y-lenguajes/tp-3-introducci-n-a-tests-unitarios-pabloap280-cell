"""Tests para la función add(a, b) -> float."""

import pytest

from src.calculator import add


# --- EJEMPLO (no borrar) ---
def test_add_suma_positivos():
    """Ejemplo: 1 + 2 debe dar 3."""
    assert add(1, 2) == 3


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Sumar dos números negativos
#   def test_add_suma_negativos():
    assert add(-1, -2) == -3
#   - Sumar un número positivo y uno negativo
def test_add_suma_positivo_negativo():
    assert add(5, -3) == 2
#   - Sumar con cero
def test_add_suma_con_cero():
    assert add(0, 5) == 5
    assert add(5, 0) == 5
#   - Sumar dos números decimales (float)
def test_add_suma_decimales():
    assert add(1.5, 2.5) == 4.0
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
#
# Ejemplo de test parametrizado:
#
# @pytest.mark.parametrize("a,b,expected", [
#     (..., ..., ...),
#     (..., ..., ...),
# ])
# def test_add_parametrizado(a, b, expected):
#     assert add(a, b) == expected
