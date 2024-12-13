from abc import ABC, abstractmethod

class Card(ABC):
    @abstractmethod
    def __init__(self, card_name: str = '', mana_cost: int = 0, card_type: str = ''):
        self.card_name = card_name
        self.mana_cost = mana_cost
        self.card_type = card_type

    def get_name(self):
        return self.card_name.lower()

    def get_cost(self):
        return self.mana_cost

    def get_type(self):
        return self.card_type

    @abstractmethod
    def get_action(self): str

class Minion(Card):

    def __init__(self, card_name: str = '', mana_cost: int = 0, card_type: str = '', minion_attack: int = 0, minion_health: int = 0, abilities: str = ''):
        super().__init__(card_name, mana_cost, card_type)
        self.minion_attack = minion_attack
        self.minion_health = minion_health
        self.abilities = abilities
    
    def get_action(self):
        """gets the minions abilities"""
        return self.abilities.lower()
    
    def __repr__(self):
        return f"name='{self.card_name}' mana_cost={self.mana_cost} card type='{self.card_type}' abilities='{self.abilities}' attack={self.minion_attack} defense={self.minion_health}"




class Spell(Card):
    def __init__(self, card_name: str = '', mana_cost: int = 0, card_type: str = '', effect: str = ''):
        super().__init__(card_name, mana_cost, card_type)
        self.effect = effect

    def get_action(self):
        """get the spells effect"""
        return self.effect.lower()
    
    def __repr__(self):
        return f"name='{self.card_name}' mana_cost={self.mana_cost} card type='{self.card_type}' abilities='{self.effect}'"

class Hero:
    def __init__(self, hero_name: str = '', type: str = '', hero_class: str = '', max_health: int  = 30, hero_power: str = ''):
        self.hero_name = hero_name
        self.type = type
        self.hero_class = hero_class
        self.max_health = max_health
        self.hero_power = hero_power
    
    def get_action(self):
        return self.hero_power.lower()
    
    def get_name(self):
        return self.hero_name.lower()
    
    def __repr__(self):
        return f"name='{self.hero_name}' type='{self.type}' class='{self.hero_class}' health={self.max_health} ability='{self.hero_power}'"


class Collection:
    def __init__(self):
        self.collection_list = []

    def add(self, item: list):
        self.collection_list.append(item)

    def filter_abilities(self, filter_key: str = ""):
        filtered_cards = []
        for item in range(len(self.collection_list)):
            if filter_key.lower() in self.collection_list[item].get_action():
                filtered_cards.append(self.collection_list[item])
                
        return filtered_cards

    def filter_mana_cost(self, filter_key: int = 0):
        filtered_cards = []
        for item in range(len(self.collection_list)):
            if isinstance(self.collection_list[item], Spell) or isinstance(self.collection_list[item], Minion):
                if filter_key == self.collection_list[item].mana_cost:
                    filtered_cards.append(self.collection_list[item])
    
    def filter_name(self, filter_key: str = ""):
        filtered_cards = []
        for item in range(len(self.collection_list)):
            if filter_key.lower() in self.collection_list[item].get_name():
                filtered_cards.append(self.collection_list[item])
        return filtered_cards