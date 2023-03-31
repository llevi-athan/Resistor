import pytest
from resistor import Resistor

def test_resistance():
    assert Resistor("черный", "коричневый", "красный").resistance() == 1200
    assert Resistor("красный", "красный", "красный", "золотой").resistance() == 2200
    assert Resistor("красный", "черный", "красный", "коричневый", "зеленый").resistance() == 200500

def test_tolerance():
    assert Resistor("красный", "красный", "черный", "коричневый").tolerance() == 1
    assert Resistor("желтый", "фиолетовый", "оранжевый", "серебро").tolerance() == 10
    assert Resistor("зеленый", "коричневый", "черный").tolerance() == None

def test_invalid_color():
    with pytest.raises(KeyError):
        Resistor("бирюзовый", "желтый", "коричневый").resistance()
    with pytest.raises(KeyError):
        Resistor("красный", "черный", "золотой", "фиолетовый", "фиолетовый", "фиолетовый").tolerance()

if __name__ == "__main__":
    pytest.main()

