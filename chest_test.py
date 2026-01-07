import pytest

from chest import Chest
from Tresore import Tresore


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

def test_list_objects_in_chest():
    chest = Chest(5)
    chest.add_object(Tresore("gold_coin", 1, 100))
    chest.add_object(Tresore("silver_coin", 1, 50))
    assert chest.get_tresors_list() == [("gold_coin", 1, 100), ("silver_coin", 1, 50)]

def test_add_object_to_full_chest():
    chest = Chest(1)
    chest.add_object(Tresore("diamond", 2, 500))
    with pytest.raises(Exception):
        chest.add_object(Tresore("ruby", 1, 300))

def test_add_object():
    chest = Chest(15)
    treasor = Tresore("nom",5,10)
    chest.add(treasor)
    assert treasor in chest.tresore_list
