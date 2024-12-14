import pytest
from card import Spell

def test_spell():
    spell = Spell("spell", 1, "type", "damage")
    assert spell.get_action() == "damage"
    assert spell.get_name() == "spell"
    assert spell.get_type() == "type"
    assert spell.get_cost() == 1
    assert str(spell) == "spell,1,type,damage"