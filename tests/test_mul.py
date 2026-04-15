"""Tests para la función mul(a, b) -> float."""

import pytest

from src.calculator import mul


# --- EJEMPLO (no borrar) ---
def test_mul_positivos():
    """Ejemplo: 3 * 4 debe dar 12."""
    assert mul(3, 4) == 12


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Multiplicar por cero
def test_mul_por_cero():
    assert mul(5, 0) == 0
    assert mul(0, 5) == 0
#   - Multiplicar dos números negativos (resultado positivo)
def test_mul_negativos():
    assert mul(-2, -3) == 6
#   - Multiplicar un positivo y un negativo (resultado negativo)
def test_mul_positivo_negativo():
    assert mul(5, -3) == -15
    assert mul(-5, 3) == -15
#   - Multiplicar por 1 (elemento neutro)
def test_mul_por_uno():
    assert mul(5, 1) == 5
    assert mul(1, 5) == 5
#   - Multiplicar dos decimales (float)
def test_mul_decimales():
    assert mul(1.5, 2.0) == 3.0
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
