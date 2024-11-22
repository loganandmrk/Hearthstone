import json
from model import HearthstoneModel
from os import path
from const import PLAYER_1_DECK, PLAYER_2_DECK, FIRST_CARD_IN_HAND, SECOND_CARD_IN_HAND, THIRD_CARD_IN_HAND, FOURTH_CARD_IN_HAND, \
    FIFTH_CARD_IN_HAND, OPPONENT, SECOND_CHARACTER_FROM_ACTIVE_PERSPECTIVE, THIRD_CHARACTER_FROM_ACTIVE_PERSPECTIVE, \
    FOURTH_CHARACTER_FROM_ACTIVE_PERSPECTIVE, FIFTH_CHARACTER_FROM_ACTIVE_PERSPECTIVE

def verifyState(expected_state_name, inspect_state):
    f = None
    try:
        expected_file = f"expected/{expected_state_name}.json"
        print(path.join(path.dirname(__file__), expected_file))
        f = open(path.join(path.dirname(__file__), expected_file))
        expected_json = json.dumps(json.load(f), sort_keys=True)
        actual_json = json.dumps(inspect_state, sort_keys=True)
        passed = expected_json == actual_json
        print(f'Verifying State "{expected_state_name}"...{"passed" if passed else "failed"}')
        if not(passed):
            print(f"Expected: {expected_json}")
            print(f"Actual: {actual_json}")
    except:
        print(f"Could not read {expected_file}")
    finally:
        if f is not None: f.close()

model = HearthstoneModel(PLAYER_1_DECK, PLAYER_2_DECK)
verifyState("not_started_state", model.inspect())

model.start() # start game
verifyState("player1_turn1", model.inspect())

# player #1 turn 1
model.play(FOURTH_CARD_IN_HAND) # play Argent Squire
verifyState("player1_turn1_action1", model.inspect())
model.done() # end turn
verifyState("player2_turn1", model.inspect())

# player #2 turn 1
model.play(FIFTH_CARD_IN_HAND) # play The Coin
verifyState("player2_turn1_action1", model.inspect())
model.play(SECOND_CARD_IN_HAND) # attempt to play Spellbreaker
verifyState("player2_turn1_action2", model.inspect())
model.play(FIRST_CARD_IN_HAND) # play Loot Hoarder
verifyState("player2_turn1_action3", model.inspect())
model.attack(THIRD_CHARACTER_FROM_ACTIVE_PERSPECTIVE) # attempt to attack with Loot Hoarder
verifyState("player2_turn1_action4", model.inspect())
model.done() # end turn
verifyState("player1_turn2", model.inspect())

# player #1 turn 2
model.attack(THIRD_CHARACTER_FROM_ACTIVE_PERSPECTIVE, SECOND_CHARACTER_FROM_ACTIVE_PERSPECTIVE) # attack Loot Hoarder with Argent Squire
verifyState("player1_turn2_action1", model.inspect())
model.play(SECOND_CARD_IN_HAND) # play Bilefin Tidehunter
verifyState("player1_turn2_action2", model.inspect())
model.play(FIRST_CARD_IN_HAND) # attempt to play Loot Hoarder
verifyState("player1_turn2_action3", model.inspect())
model.done() # end turn
verifyState("player2_turn2", model.inspect())

# player #2 turn 2
model.play(THIRD_CARD_IN_HAND) # play Ancient Watcher
verifyState("player2_turn2_action1", model.inspect())
model.attack(FIFTH_CHARACTER_FROM_ACTIVE_PERSPECTIVE) # attempt to attack with Ancient Watcher
verifyState("player2_turn2_action2", model.inspect())
model.done() # end turn
verifyState("player1_turn3", model.inspect())

# player #1 turn 3
model.attack(FOURTH_CHARACTER_FROM_ACTIVE_PERSPECTIVE, SECOND_CHARACTER_FROM_ACTIVE_PERSPECTIVE) # attack Ancient Watcher with Bilefin Tidehunter
verifyState("player1_turn3_action1", model.inspect())
model.attack(FOURTH_CHARACTER_FROM_ACTIVE_PERSPECTIVE) # attack Player #2 with Ooze
verifyState("player1_turn3_action2", model.inspect())
model.attack(THIRD_CHARACTER_FROM_ACTIVE_PERSPECTIVE, FIFTH_CHARACTER_FROM_ACTIVE_PERSPECTIVE) # attempt to attack self with Argent Squire
verifyState("player1_turn3_action3", model.inspect())
model.play(FIRST_CARD_IN_HAND) # play Loot Hoarder
verifyState("player1_turn3_action4", model.inspect())
model.done() # end turn
verifyState("player2_turn3", model.inspect())

# player #2 turn 3
model.attack(FIFTH_CHARACTER_FROM_ACTIVE_PERSPECTIVE) # attempt to attack Player #1 with Ancient Watcher
verifyState("player2_turn3_action1", model.inspect())
model.done() # end turn
verifyState("player1_turn4", model.inspect())

# player #1 turn 4
model.play(FOURTH_CARD_IN_HAND, FIFTH_CHARACTER_FROM_ACTIVE_PERSPECTIVE) # play Spellbreaker targeting own Loot Hoarder
verifyState("player1_turn4_action1", model.inspect())
model.attack(FIFTH_CHARACTER_FROM_ACTIVE_PERSPECTIVE, SECOND_CHARACTER_FROM_ACTIVE_PERSPECTIVE) # attack Ancient Watcher with Loot Hoarder
verifyState("player1_turn4_action2", model.inspect())
model.done() # end turn
verifyState("player2_turn4", model.inspect())

# player #2 turn 4
model.play(FIRST_CARD_IN_HAND, OPPONENT) # attempt to play Spellbreaker targeting Player #1
verifyState("player2_turn4_action1", model.inspect())
model.play(FIRST_CARD_IN_HAND, FIFTH_CHARACTER_FROM_ACTIVE_PERSPECTIVE) # play Spellbreaker targeting own Ancient Watcher
verifyState("player2_turn4_action2", model.inspect())
model.attack(FIFTH_CHARACTER_FROM_ACTIVE_PERSPECTIVE) # attempt to attack Player #1 with Ancient Watcher
verifyState("player2_turn4_action3", model.inspect())
model.attack(FIFTH_CHARACTER_FROM_ACTIVE_PERSPECTIVE, THIRD_CHARACTER_FROM_ACTIVE_PERSPECTIVE) # attack Ooze with Ancient Watcher
verifyState("player2_turn4_action4", model.inspect())