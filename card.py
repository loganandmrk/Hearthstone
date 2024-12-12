from abc import ABC, abstractmethod

class Card(ABC):
    @abstractmethod
    def __init__(self, card_name: str = '', mana_cost: int = 0, type: str = ''):
        self.card_name = card_name
        self.mana_cost = mana_cost
        self.type = type

    def get_name(self):
        pass

    def get_cost(self):
        pass

    def get_type(self):
        pass

    @abstractmethod
    def get_action(self):
        pass

class Minion(Card):

    def __init__(self, card_name: str = '', mana_cost: int = 0, type: str = '', minion_attack: int = 0, minion_health: int = 0, abilities: str = ''):
        super().__init__(card_name, mana_cost, type)
        self.minion_attack = minion_attack
        self.minion_health = minion_health
        self.abilities = abilities
    
    def get_action(self):
        """gets the minions abilities"""
        return self.abilities
    
    def __repr__(self):
        return f"name='{self.card_name}', mana_cost={self.mana_cost}, abilities='{self.abilities}', attack={self.minion_attack}, defense={self.minion_health}"




class Spell(Card):
    def __init__(self, card_name: str = '', mana_cost: int = 0, type: str = '', effect: str = ''):
        super().__init__(card_name, mana_cost, type)
        self.effect = effect

    def get_action(self):
        """get the spells effect"""
        return self.effect
    
    def __repr__(self):
        return f"name='{self.card_name}', mana_cost={self.mana_cost}, abilities='{self.effect}'"