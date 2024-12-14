
from card import Minion, Spell, Collection, Hero
import csv


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
                    collection.view_collection()
        
        



if __name__ == "__main__":
    main()