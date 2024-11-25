class Hero:
    def __init__(self, hero_name = '', max_health  = 30, max_hand = 10, hero_power = '', mana = 0, available_mana = 0, cards_in_hand = [], cards_in_deck = [], weapon = '', armor = 0, attack = 0):
        self.hero_name = hero_name
        self.max_health = max_health
        self.max_hand = max_hand
        self.hero_power = hero_power
        self.mana = mana
        self.available_mana = available_mana
        self.cards_in_hand = cards_in_hand
        self.cards_in_deck = cards_in_deck
        self.weapon = weapon
        self.armor = armor
        self.attack = attack

    def use_hero_power(self):
        pass

    def play_card(self, card):
        pass

    def attack_with_hero(self, card):
        pass

    def draw_card(self, number):
        pass

    def spend_mana(self, spent):
        pass

    def gain_mana_crystal(self):
        pass

    def fatigue_draw(self):
        pass

    def take_damage(self):
        pass

    def equip_weapon(self, card):
        pass

    def gain_armor(self):
        pass
