from card import Minion, Spell
from hero import Hero

class Collection(Minion, Spell, Hero):
    def __init__(self, collection = [{}], current_filters = ['']):
        self.collection = collection
        self.current_filters = current_filters
    
    """def import_cards(self, file):
        #import a csv file and create a collection based off of it
        with open(file, "r") as card_file:
            pass"""

    def add_card(self, card):
        self.collection.append(card)

    def remove_card(self, card):
        self.collection.pop(card)

    def filter(self):
        pass