"""
Wolf, Goat and Cabbage Puzzle in Python
By Robin Andrews - https://compucademy.co.uk/
"""
import os  # Only needed in console version
import time # Only needed in console version

names = {"F": "Farmer",
         "W": "Wolf",
         "G": "Goat",
         "C": "Cabbage"}

forbidden_states = [{"W", "G"}, {"G", "C"}, {"G", "C", "W"}]


def print_story():
    print("""
#### WOLF, GOAT and CABBAGE PROBLEM ####

Once upon a time a farmer went to a market and purchased a wolf, a goat, and a cabbage. On his way home, the farmer came
to the bank of a river and rented a boat. But crossing the river by boat, the farmer could carry only himself and a single
one of his purchases: the wolf, the goat, or the cabbage.

If left unattended together, the wolf would eat the goat, or the goat would eat the cabbage.

The farmer's challenge was to carry himself and his purchases to the far bank of the river, leaving each purchase intact.
How did he do it?
""")
    input("Press enter to continue.")

"""
Wolf, Goat and Cabbage Puzzle in Python
By Robin Andrews - https://compucademy.co.uk/
"""


names = {"F": "Farmer",
         "W": "Wolf",
         "G": "Goat",
         "C": "Cabbage"}

forbidden_states = [{"W", "G"}, {"G", "C"}, {"G", "C", "W"}] # each state is a set


def print_story():
    print("""
#### WOLF, GOAT and CABBAGE PROBLEM ####

Once upon a time a farmer went to a market and purchased a wolf, a goat, and a cabbage. On his way home, the farmer came
to the bank of a river and rented a boat. But crossing the river by boat, the farmer could carry only himself and a single
one of his purchases: the wolf, the goat, or the cabbage.

If left unattended together, the wolf would eat the goat, or the goat would eat the cabbage.

The farmer's challenge was to carry himself and his purchases to the far bank of the river, leaving each purchase intact.
How did he do it?
""")
    input("Press enter to continue.")


def section_break():
    print("*" * 50)


def print_state(state):
    left_bank, right_bank = state
    print("#### CURRENT STATE OF PUZZLE ####")
    print("")
    left_bank_display = [names[item] for item in left_bank]
    right_bank_display = [names[item] for item in right_bank]
    print(left_bank_display, "|", right_bank_display) # if right_bank else "[]" # Add brackets for Python 3
    print("")


def get_move():
    print("Which item do you wish to take across the river?")
    answer = ""
    while answer.upper() not in ["F", "W", "G", "C"]:
        answer = input("Just Farmer (f), Wolf (w), Goat (g) or Cabbage (c)? ")

    return answer.upper()


def process_move(move, state):
    # We need to "think ahead" to see if move is illegal.
    temp_state = [state[0].copy(), state[1].copy()]
    containing_set = 0 if move in state[0] else 1
    if "F" not in state[containing_set]:
        print("Not allowed - the farmer must accompany the item.")
        print("")
        return state
    if containing_set == 0:
        temp_state[0].difference_update({move, "F"})
        temp_state[1].update([move, "F"])
    elif containing_set == 1:
        temp_state[1].difference_update({move, "F"})
        temp_state[0].update([move, "F"])
    if temp_state[0] not in forbidden_states and temp_state[1] not in forbidden_states:
        state = [temp_state[0].copy(), temp_state[1].copy()]
    else:
        print("Not allowed - one of your items would be eaten!")
    print("")
    return state


def is_win(state):
    return state[1] == {"F", "W", "G", "C"}


def main():
    left_bank = {"F", "W", "G", "C"}
    right_bank = set()
    state = [left_bank, right_bank]
    print_story()
    while not is_win(state):
        section_break()
        print_state(state)
        move = get_move()
        state = process_move(move, state)

    print("Well done - you solved the puzzle!")


main()