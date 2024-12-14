from abc import ABC, abstractmethod
import csv
import keyboard

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
        return self.card_type.lower()

    @abstractmethod
    def get_action(self): str

class Minion(Card):

    def __init__(self, card_name: str = '', mana_cost: int = None, card_type: str = '', minion_attack: int = 0, minion_defense: int = 0, abilities: str = ''):
        super().__init__(card_name, mana_cost, card_type)
        self.minion_attack = minion_attack
        self.minion_defense = minion_defense
        self.abilities = abilities
    
    def get_action(self):
        """gets the minions abilities"""
        return self.abilities.lower()
    
    def get_attack(self):
        return self.minion_attack
    
    def get_defense(self):
        return self.minion_defense
    
    def __str__(self):
        return f"{self.card_name},{self.mana_cost},{self.card_type},{self.abilities},{self.minion_attack},{self.minion_defense}"
    
    def __repr__(self):
        return f"\nMinion: name='{self.card_name}', mana_cost={self.mana_cost}, card type='{self.card_type}', abilities='{self.abilities}', attack={self.minion_attack}, defense={self.minion_defense}"
    
class Spell(Card):
    def __init__(self, card_name: str = '', mana_cost: int = None, card_type: str = '', effect: str = ''):
        super().__init__(card_name, mana_cost, card_type)
        self.effect = effect

    def get_action(self):
        """get the spells effect"""
        return self.effect.lower()
    
    def __str__(self):
        return f"{self.card_name},{self.mana_cost},{self.card_type},{self.effect}"
    
    def __repr__(self):
        return f"\nSpell: name='{self.card_name}', mana_cost={self.mana_cost}, card type='{self.card_type}', abilities='{self.effect}'"

class Hero:
    def __init__(self, hero_name: str = '', hero_type: str = '', hero_class: str = '', max_health: int  = 30, hero_power: str = ''):
        self.hero_name = hero_name
        self.hero_type = hero_type
        self.hero_class = hero_class
        self.max_health = max_health
        self.hero_power = hero_power
    
    def get_action(self):
        return self.hero_power.lower()
    
    def get_name(self):
        return self.hero_name.lower()
    
    def get_type(self):
        return self.hero_type.lower()
    
    def __str__(self):
        return f"{self.hero_name},{self.hero_type},{self.hero_class},{self.max_health},{self.hero_power}"
    
    def __repr__(self):
        return f"\nHero: name='{self.hero_name}', type='{self.hero_type}', class='{self.hero_class}', health={self.max_health}, ability='{self.hero_power}'"

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

    def filter_mana_cost(self, filter_key: int = None):
        filtered_cards = []
        for item in range(len(self.collection_list)):
            if isinstance(self.collection_list[item], Spell) or isinstance(self.collection_list[item], Minion):
                if int(filter_key) == int(self.collection_list[item].get_cost()):
                    filtered_cards.append(self.collection_list[item])
        return filtered_cards
    
    def filter_name(self, filter_key: str = ""):
        filtered_cards = []
        for item in range(len(self.collection_list)):
            if filter_key.lower() in self.collection_list[item].get_name():
                filtered_cards.append(self.collection_list[item])
        return filtered_cards
    
    def filter_type(self, filter_key: str= ""):
        filtered_cards = []
        for item in range(len(self.collection_list)):
            if filter_key.lower() in self.collection_list[item].get_type():
                filtered_cards.append(self.collection_list[item])
        return filtered_cards
    
    def filter_stats(self, filter_attack: int = None, filter_defense: int = None):
        filtered_cards = []
        for item in range(len(self.collection_list)):
            if isinstance(self.collection_list[item], Minion):
                if int(filter_attack) == self.collection_list[item].get_attack() and int(filter_defense) == self.collection_list[item].get_defense():
                    filtered_cards.append(self.collection_list[item])
        return filtered_cards

    def prompt_filters(self):
        prompt = '\n'.join(['\n',
            '1. Abilities',
            '2. Mana Cost',
            '3. Name',
            '4. Type',
            '5. Stats (attack and health)',
            
            '\nWhat would you like to filter by? (1-5 Press enter to go back):'
        ])
        done: bool = False
        while not done:
            choice = input(prompt)
            match choice:
                case '':
                    done = True
                case '1':
                    ability = input("Enter a keyword: ") 
                    try:
                        print(self.filter_abilities(ability))
                    except:
                        print("Please provide a valid keyword")
                case '2':
                    mana_cost = input("Enter a mana cost: ")
                    try:
                        print(self.filter_mana_cost(mana_cost))
                    except:
                        print("Please provide a valid number")
                case '3':
                    name = input("Enter a name: ")
                    try:
                        print(self.filter_name(name))
                    except:
                        print("Please provide a valid name")
                case '4':
                    card_type = input("Enter a card type: ")
                    try:
                        print(self.filter_type(card_type))
                    except:
                        print("Please provide a valid type")
                case '5':
                    attack = input("Enter the minions attack: ")
                    defense = input("Enter the minions defense: ")
                    try: 
                        print(self.filter_stats(attack, defense))
                    except:
                        print("Please provide valid stats")

    def verify_integer(self, prompt):
        while True:
            user_input = input(prompt)
            if user_input.isdigit():
                return int(user_input)
            else:
                print("Please enter a valid number.")
    
    def verify_string(self, prompt):
        while True:
            user_input = input(prompt)
            if len(user_input.strip()) >= 1:
                return str(user_input)
            else:
                print("The card must have a name of at least 1 non-whitespace character.")
                
    def add_cards(self, filename):
        new_card_list = []
        done = False

        card_type = input("Enter a card type: ")
        while not done:
            if card_type.lower() == "minion":
                name: str = self.verify_string("Enter the card name: ")
                new_card_list.append(name)
                new_card_list.append(card_type)
                mana_cost: int = self.verify_integer("Enter the mana cost: ")
                new_card_list.append(mana_cost)
                abilities: str = input("Enter the abilities: ")
                new_card_list.append(abilities)
                attack: int = self.verify_integer("Enter the attack: ")
                new_card_list.append(attack)
                defense: int = self.verify_integer("Enter the defense: ")
                new_card_list.append(defense)
                done = True
            elif card_type.lower() == "spell":
                name: str = self.verify_string("Enter the card name: ")
                new_card_list.append(name)
                new_card_list.append(card_type)
                mana_cost: int = self.verify_integer("Enter the mana cost: ")
                new_card_list.append(mana_cost)
                effect: str = input("Enter the spells effect: ")
                new_card_list.append(effect)
                done = True
            elif card_type.lower() == "hero":
                name: str = self.verify_string("Enter the hero name: ")
                new_card_list.append(name)
                new_card_list.append(card_type)
                hero_class: str = input("Enter the hero class: ")
                new_card_list.append(hero_class)
                max_health: int = self.verify_integer("Enter a max health value: ")
                new_card_list.append(max_health)
                hero_power: str = input("Enter a hero power: ")
                new_card_list.append(hero_power)
                done = True
            else:
                card_type: str = input("The card type is not valid, enter a new one: ")
        
        
        
        with open(filename, "a", newline="") as new_collection:
            writer = csv.writer(new_collection)
            writer.writerow(new_card_list)

    def remove_cards(self, filename):
        
        with open(filename, 'r', newline='') as collection:
            reader = csv.reader(collection)
            rows = list(reader)
            
            updated_rows: list = []
            done: bool = False
            while not done:
                card_name = input("Enter a card name (or press enter to exit): ")
                if not card_name.strip():
                    print("No input provided, exiting")
                    break
                card_type = input("Enter a card type (or press enter to exit): ")
                if not card_type.strip().lower():
                    print("No input provided, exiting")
                    break
                
                found = False
                for row in rows:
                    if card_name.strip().lower() == row[0].strip().lower() and card_type.strip().lower() == row[1].strip().lower():
                        found = True
                        print("card found")
                        continue
                    updated_rows.append(row)
                if found:
                    break
                else:
                    print("card not found in file, try again.")
    
        with open(filename, mode='w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(updated_rows)

    def view_collection(self):
        print(self.collection_list)