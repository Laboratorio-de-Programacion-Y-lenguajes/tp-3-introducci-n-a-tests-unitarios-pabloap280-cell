"""Tests para la función sub(a, b) -> float."""

import pytest

from src.calculator import sub


# --- EJEMPLO (no borrar) ---
def test_sub_resta_positivos():
    """Ejemplo: 5 - 2 debe dar 3."""
    assert sub(5, 2) == 3


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Restar un número mayor al primero (resultado negativo)
def test_sub_resultado_negativo():
    assert sub(2, 5) == -3
#   - Restar cero
def test_sub_resta_cero():
    assert sub(5, 0) == 5
#   - Restar dos números negativos
def test_sub_resta_negativos():
    assert sub(-2, -5) == 3
#   - Restar dos números decimales (float)
def test_sub_resta_decimales():
    assert sub(5.5, 2.2) == 3.3
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
