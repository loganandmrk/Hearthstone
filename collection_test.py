import pytest
from card import Collection, Minion

def test_collection():
    collection = Collection()
    minion = Minion("Loot Hoarder",2,"Minion",2,1,"Deathrattle: draw a card")
    collection.add(minion)
    assert isinstance(collection.collection_list[0], Minion)
    assert isinstance(collection.filter_abilities("deathrattle")[0], Minion)
    assert isinstance(collection.filter_mana_cost(2)[0], Minion)
    assert isinstance(collection.filter_name("Loot")[0], Minion)
    assert isinstance(collection.filter_stats(2,1)[0], Minion)
    assert isinstance(collection.view_collection(), list)