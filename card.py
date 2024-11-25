from abc import ABC, abstractmethod

class Card(ABC):
    @abstractmethod
    def __init__(self, card_name, mana_cost, type):
        self.card_name = card_name
        self.mana_cost = mana_cost
        self.type = type

class Minion(Card):
    def __init__(self, card_name, mana_cost, type, minion_attack, minion_health, abilities):
        self.card_name = card_name
        self.mana_cost = mana_cost
        self.type = type
        self.minion_attack = minion_attack
        self.minion_health = minion_health
        self.abilities = abilities
    
    def attack_character(self):
        pass

    def take_damage(self):
        pass

class Spell(Card):
    def __init__(self, card_name, mana_cost, type, effect):
        self.card_name = card_name
        self.mana_cost = mana_cost
        self.type = type
        self.effect = effect

    def do_effect(self):
        pass