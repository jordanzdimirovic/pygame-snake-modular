"""
    Everything related to game logic will be within this script.
    All definitions within this file:
        - Must be functions
        - Must maintain their names
    
    This file's purpose is to be modified by a given student,
    such that they can implement the logic, whilst abstracting away
    the rest of the implementation (i.e. rendering, PyGame things, etc.)
"""

#region LOGIC VARIABLES

"""
A list of lists that represents
each part of the snake.
The left-most sub-list is the head,
whilst the right-most sub-list is the tail.
[[head_x, head_y], ..., [tail_x, tail_y]]
Example: 
"""
snake = []

"""
Is the snake alive or dead?
"""
is_alive = True

"""
What direction is the snake
currently moving?

Possible values:
    - "UP"
    - "DOWN"
    - "LEFT"
    - "RIGHT"
"""
move_direction = "UP"

"""
Represents the score that
the player has currently acquired.
"""
player_score = 0

#endregion

#region LOGIC FUNCTIONS

#region KEYBOARD ARROW BUTTON LOGIC

# Runs when the left arrow is pressed
def on_left_arrow():
    pass

# Runs when the right arrow is pressed
def on_right_arrow():
    pass

# Runs when the up arrow is pressed
def on_up_arrow():
    pass

# Runs when the down arrow is pressed
def on_down_arrow():
    pass

#endregion 

#endregion
