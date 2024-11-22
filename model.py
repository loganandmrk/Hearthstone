from const import *
from json import load
from os import path

with open(path.join(path.dirname(__file__), "cards.json")) as f:
    cards = load(f)
    cards[ARGENT_SQUIRE]["abilities"] = ["Divine Shield"]
    cards[LOOT_HOARDER]["abilities"] = ["Deathrattle"]
    cards[LOOT_HOARDER]["actions"] = {"Deathrattle": "defendingPlayer.draw()"}
    cards[THE_COIN]["effect"] = "self.activePlayer.mana += 1"
    cards[BILEFIN_TIDEHUNTER]["battlecry"] = "self.activePlayer.battlefield.append(Minion('Ooze', 1, 1, ['Taunt']))"
    cards[ANCIENT_WATCHER]["abilities"] = ["Passive"]
    cards[SPELLBREAKER]["targetable"] = lambda target: isinstance(target, Minion)
    cards[SPELLBREAKER]["battlecry"] = "target.silence()"

class Player:
    def __init__(self, deck):
        self.deck = deck
        self.hand = []
        self.mana = 0
        self.crystals = 0
        self.battlefield = []
        self.health = 30
    
    def draw(self, drawnCards = 1):
        for x in range(drawnCards):
            self.hand.append(self.deck.pop(0))
    
    def startTurn(self):
        if self.crystals < 10:
            self.crystals += 1
        self.mana = self.crystals
        self.draw()
        for minion in self.battlefield:
            minion.asleep = False


    def inspect(self):
        return {
            "battlefield": [minion.inspect() for minion in self.battlefield], 
            "deck": self.deck, 
            "hand": self.hand, 
            "health": self.health, 
            "mana": self.mana
        }

class Minion:
    def __init__(self, name, health, attack, abilities, actions = {}):
        self.name = name
        self.health = health
        self.attack = attack
        self.abilities = abilities
        self.actions = actions
        self.asleep = True
    
    def inspect(self):
        return {
            "name": self.name,
            "health": self.health,
            "attack": self.attack,
            "abilities": self.abilities
        }

    def silence(self):
        self.abilities = []
        self.actions = {}

class HearthstoneModel:
    def __init__(self, player1deck, player2deck):
        self.player1 = Player(player1deck)
        self.player2 = Player(player2deck)
        self.activePlayer = None
        self.inactivePlayer = None

    def inspect(self):
        return {
            "players": [
                self.player1.inspect(),
                self.player2.inspect(),
            ]
        }
    
    def start(self):
        self.player1.draw(3)
        self.player2.draw(4)
        self.player2.hand.append(THE_COIN)
        self.activePlayer = self.player1
        self.inactivePlayer = self.player2
        self.activePlayer.startTurn()
        
    def play(self, handIndex, targetBfIndex = None):
        if self.activePlayer is not None:
            card = cards[self.activePlayer.hand[handIndex]]
            targetable = True
            if targetBfIndex is not None:
                target = self.getCharacter(targetBfIndex)
                targetable = card["targetable"](target)
            if card["cost"] <= self.activePlayer.mana and targetable:
                self.activePlayer.mana -= card["cost"]
                self.activePlayer.hand.pop(handIndex)
                if "attack" in card:
                    self.activePlayer.battlefield.append(Minion(
                        card["name"], 
                        card["health"],
                        card["attack"], 
                        card["abilities"] if "abilities" in card else [], 
                        card["actions"] if "actions" in card else {}
                    ))
                    if "battlecry" in card:
                        exec(card["battlecry"])
                elif "effect" in card:
                    exec(card["effect"])

    def done(self):
        if self.activePlayer is self.player1:
            self.activePlayer = self.player2
            self.inactivePlayer = self.player1
        elif self.activePlayer is self.player2:
            self.activePlayer = self.player1
            self.inactivePlayer = self.player2
        self.activePlayer.startTurn()
    
    def getCharacter(self, bfIndex):
        if bfIndex < 0: return None
        if bfIndex == OPPONENT: return self.inactivePlayer
        inactivePlayerBfSize = len(self.inactivePlayer.battlefield)
        activePlayerBfSize = len(self.activePlayer.battlefield)
        if bfIndex <= inactivePlayerBfSize: return self.inactivePlayer.battlefield[bfIndex - 1]
        if bfIndex <= inactivePlayerBfSize + activePlayerBfSize: return self.activePlayer.battlefield[bfIndex - inactivePlayerBfSize - 1]
        if bfIndex == inactivePlayerBfSize + activePlayerBfSize + 1: return self.activePlayer
        return None

    def attack(self, attackerBfIndex, defenderBfIndex = OPPONENT): 
        attacker = self.getCharacter(attackerBfIndex)
        if isinstance(attacker, Minion) and not(attacker.asleep) and "Passive" not in attacker.abilities:
            defender = self.getCharacter(defenderBfIndex)
            if ((isinstance(defender, Minion) and "Taunt" in defender.abilities) or not(bool([minion for minion in self.inactivePlayer.battlefield if "Taunt" in minion.abilities]))):
                if isinstance(defender, Player) and defender is not self.activePlayer:
                    defender.health -= attacker.attack
                elif isinstance(defender, Minion) and defender not in self.activePlayer.battlefield:
                    self.fight(attacker, defender, self.inactivePlayer)
                    self.fight(defender, attacker, self.activePlayer)

    def fight(self, attacker, defender, defendingPlayer):
        if attacker.attack > 0 and "Divine Shield" in defender.abilities:
            defender.abilities.remove("Divine Shield")
        else:
            defender.health -= attacker.attack
            if defender.health <= 0:
                defendingPlayer.battlefield.remove(defender)
                if "Deathrattle" in defender.actions:
                    exec(defender.actions["Deathrattle"])