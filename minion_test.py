import pytest
from card import Minion

def test_spell():
    minion = Minion("minion", 1, "type",4,5,"battlecry")
    assert minion.get_action() == "battlecry"
    assert minion.get_name() == "minion"
    assert minion.get_type() == "type"
    assert minion.get_cost() == 1
    assert minion.get_attack() == 4
    assert minion.get_defense() == 5
    assert str(minion) == "minion,1,type,battlecry,4,5"