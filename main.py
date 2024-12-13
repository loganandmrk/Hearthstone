
from card import Minion, Spell, Collection, Hero
import csv

def main():

    with open("cards.csv", "r") as data:
        rows = csv.reader(data)
        collection = Collection()

        for row in rows:
            if row[1].lower() == "hero":
                name, hero_type, hero_class, health, ability = row
                hero = Hero(name, hero_type, hero_class, int(health), ability)
                collection.add(hero)
            elif row[1].lower() == "minion":
                name, card_type, mana_cost, abilities, attack, health = row
                minion = Minion(name, int(mana_cost), card_type, int(attack), int(health), abilities)
                collection.add(minion)
            elif row[1].lower() == "spell":
                name, card_type, mana_cost, effect = row
                spell = Spell(name, int(mana_cost), card_type, effect)
                collection.add(spell)
        print(collection.filter_abilities("damage"))
        print(collection.filter_mana_cost(3))
        print(collection.filter_name("Sylvanas Windrunner"))

if __name__ == "__main__":
    main()