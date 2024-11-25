from card import Minion
from hero import Hero

class Battlefield(Minion, Hero):
    def __init__(self, player_minions, minion_data, minion_damage, max_minions, turn_number = 0):
        self.player_minions = player_minions
        self.minion_data = minion_data
        self.minion_damage = minion_damage
        self.max_minions = max_minions
        self.turn_number = turn_number
    
    def battlefield_stats(self):
        pass

    def target(self):
        pass

    def remove_minion(self):
        pass