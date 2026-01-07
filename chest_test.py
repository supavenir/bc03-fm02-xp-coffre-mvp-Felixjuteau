import pytest

from chest import Chest
from tresore import Tresore

def test_create_chest():
    size = 10
    chest = Chest(size)
    assert chest.size == size

def test_create_chest_with_invalid_size():
    with pytest.raises(ValueError):
        Chest(-5)

def test_get_size():
    chest = Chest(15)
    assert chest.get_size() == 15


def test_add_object():
    chest = Chest(15)
    treasor = Tresore("nom",5,10)
    chest.add(treasor)
    assert treasor in chest.tresore_list