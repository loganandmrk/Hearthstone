import pytest
from card import Hero

def test_hero():
    hero = Hero("hero", "type", "rogue", 30, "equip")
    assert hero.get_action() == "equip"
    assert hero.get_name() == "hero"
    assert hero.get_type() == "type"
    assert str(hero) == "hero,type,rogue,30,equip"