# State (game state, application state)
state = {
    "player_information": {
        "health": 100,
        "position": ("x", "y", "z")
    }
}

from copy import deepcopy

new_state = deepcopy(state)

new_state['player_information']['health'] -= 20

state = new_state

print("\n\n", state, "\n\n")