from abc import ABC, abstractmethod

class Card(ABC):
    @abstractmethod
    def __init__(self, card_name: str = '', mana_cost: int = 0, type: str = ''):
        self.card_name = card_name
        self.mana_cost = mana_cost
        self.type = type

class Minion(Card):

    def __init__(self, card_name: str = '', mana_cost: int = 0, type: str = '', minion_attack: int = 0, minion_health: int = 0, abilities: str = ''):
        super().__init__(card_name, mana_cost, type)
        self.minion_attack = minion_attack
        self.minion_health = minion_health
        self.abilities = abilities
    
    def __str__(self):
        return f"{self.card_name, self.mana_cost, self.type, self.minion_attack, self.minion_health, self.abilities}"




class Spell(Card):
    def __init__(self, card_name: str = '', mana_cost: int = 0, type: str = '', effect: str = ''):
        super().__init__(card_name, mana_cost, type)
        self.effect = effect
    
    def __str__(self):
        return f"{self.card_name, self.mana_cost, self.type, self.effect}"