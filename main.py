
from hero import Hero
from card import Minion, Spell
import csv

def main():

    with open("cards.csv", "r") as data:
        rows = csv.reader(data)

        heroes = []
        minions = []
        spells = []

        for row in rows:
            if row[1] == "hero":
                name, type, hero_class, health, ability = row
                hero = Hero(name, type, hero_class, int(health), ability)
                heroes.append(hero)
            elif row[1] == "minion":
                name, type, mana_cost, abilities, attack, health = row
                minion = Minion(name, int(mana_cost), type, int(attack), int(health), abilities)
                minions.append(minion)
            elif row[1] == "spell":
                name, type, mana_cost, effect = row
                spell = Spell(name, type, int(mana_cost), effect)
                spells.append(spell)
        card_list = heroes + minions + spells

        for item in range(len(card_list)):
            if isinstance(card_list[item], Minion) or isinstance(card_list[item], Spell):
                substring = "damage"
                if substring in card_list[item].get_action():
                    print(card_list[item])
if __name__ == "__main__":
    main()