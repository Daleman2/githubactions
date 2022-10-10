import pandas as pd
from modeltools.preprocessing import get_numerical_features


def test_get_numerical_features_simple():
    """En este test vamos a probar que logra disnguir entre cadenas de texto
    y numeros enteros"""

    df = pd.DataFrame({"numerica": [5], "categorica": ["rojo"]})

    # Assert es "como un IF" pero que falle si la condicion es falsa. Esto es ideal para los test.

    assert get_numerical_features(df) == ["numerica"]


def test_get_numerical_features_empty():

    """Este test comprueba que se devuelve una lista vacía si no hay ninguna variable num."""

    df = pd.DataFrame({"categorica": ["rojo"]})

    # Assert es "como un IF" pero que falle si la condicion es falsa. Esto es ideal para los test.

    assert get_numerical_features(df) == []


"""
def test_get_numerical_features_ToFail():

    #Assert es "como un IF" pero que falle si la condicion es falsa. Esto es ideal para los test.

    assert get_numerical_features(1==2)
    """
