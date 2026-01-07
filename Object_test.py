from tresore import Tresore
import pytest


def test_create_object() :
  obj = Tresore("Arc", 5, 1000000)
  
  assert obj.getWeight() == 5
  