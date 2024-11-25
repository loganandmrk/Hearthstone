from card import Minion, Spell
from hero import Hero

class Collection(Minion, Spell, Hero):
    def __init__(self, collection = [{}], current_filters = ['']):
        pass
    
    def battlefield_stats(self):
        pass

    def remove_minion(self):
        pass