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

def test_list_objects_in_chest():
    chest = Chest(5)
    obj1 = Tresore("gold_coin", 1, 100)
    obj2 = Tresore("silver_coin", 1, 50)
    chest.add(obj1)
    chest.add(obj2)
    assert chest.get_tresors_list() == [obj1, obj2]

def test_add_object_weight_over_limit():
    chest = Chest(1)
    with pytest.raises(Exception):
        chest.add(Tresore("ruby", 2, 300))

def test_add_object():
    chest = Chest(15)
    treasor = Tresore("nom",5,10)
    chest.add(treasor)
    assert treasor in chest.tresore_list

def test_remove_object():
    chest = Chest(15)
    treasor = Tresore("nom",5,10)
    treasor2 = Tresore("nom2",3,5)
    chest.add(treasor)
    chest.add(treasor2)
    chest.remove(treasor)
    assert treasor not in chest.tresore_list
    assert treasor2 in chest.tresore_list

def test_remove_nonexistent_object():
    chest = Chest(15)
    treasor = Tresore("nom",5,10)
    with pytest.raises(ValueError):
        chest.remove(treasor)

def test_add_wrong_tresor():
    chest = Chest(15)
    fo_tresor= 2
    with pytest.raises(ValueError):
        chest.add(fo_tresor)

def test_avoid_duplicate_objects():
    chest = Chest(15)
    treasor = Tresore("nom",5,10)
    chest.add(treasor)
    with pytest.raises(Exception):
        chest.add(treasor)

def test_total_weight():
    chest = Chest(15)
    treasor = Tresore("nom",5,10)
    treasor2 = Tresore("nom2",3,5)
    chest.add(treasor)
    chest.add(treasor2)
    chest.total_weight()
    assert chest.total_weight() == 8

def test_search_tresore():
    chest = Chest(10)
    tresore1 = Tresore("Arc", 1, 10)
    tresore2 = Tresore("Linux", 5, 1000)

    chest.add(tresore1)
    chest.add(tresore2)

    assert chest.shearch_tresore("Linux") == tresore2
    assert chest.shearch_tresore("Miaou") == None

def test_total_value():
    chest = Chest(10)
    tresore1 = Tresore("Arc", 1, 10)
    tresore2 = Tresore("Linux", 5, 1000)
    assert chest.get_value() == 0
    chest.add(tresore1)
    assert chest.get_value() == 10
    chest.add(tresore2)
    assert chest.get_value() == 1010
    chest.remove(tresore1)
    assert chest.get_value() == 1000
    chest.remove(tresore2)
    assert chest.get_value() == 0
    