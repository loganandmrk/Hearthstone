
from hero import Hero
from card import Minion, Spell
from battlefield import Collection
import sys

def main():
    file = sys.argv[1]
    with open(file, "r") as collection:
        collection.readlines()
    minion1 = Minion("Wisp", 0, "Minion", 1, 1, "")
    spell1 = Spell("Fireball", 4, "Spell", "Deal 6 damage to any target.")
    print(minion1.type)
    print(minion1)
    print(spell1.type)
    print(spell1)
if __name__ == "__main__":
    main()