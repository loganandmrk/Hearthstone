
from card import Minion, Spell, Collection, Hero
import csv

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




def main():
    filename = "cards.csv"
    done: bool = False
    while not done:
        with open(filename, "r") as data:
            reader = csv.reader(data)
            rows = [row for row in reader if any(field.strip() for field in row)]
            collection = Collection()
            for row in rows:
                if row[1].lower() == "hero":
                    name, hero_type, hero_class, health, ability = row
                    hero = Hero(name, hero_type, hero_class, int(health), ability)
                    collection.add(hero)
                elif row[1].lower() == "minion":
                    name, card_type, mana_cost, abilities, attack, defense = row
                    minion = Minion(name, int(mana_cost), card_type, int(attack), int(defense), abilities)
                    collection.add(minion)
                elif row[1].lower() == "spell":
                    name, card_type, mana_cost, effect = row
                    spell = Spell(name, int(mana_cost), card_type, effect)
                    collection.add(spell)
                    

            prompt = "\n".join(['\n',
                '1. Filter Collection',
                '2. Add Cards',
                '3. Remove Cards',
                '4. View Collection',
                
                '\nWhat would you like to do? (Enter 1-4 press Enter for DONE): '
            ])      

            choice = input(prompt)
            match choice:
                case '':
                    done = True
                case '1':
                    collection.prompt_filters()
                case '2':
                    collection.add_cards(filename)
                case '3':
                    collection.remove_cards(filename)
                case '4':
                    print(collection.view_collection())

if __name__ == "__main__":
    main()