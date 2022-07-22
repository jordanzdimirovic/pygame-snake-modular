"""
    Everything related to game logic will be within this script.
    All definitions within this file:
        - Must be functions
        - Must maintain their names
    
    This file's purpose is to be modified by a given student,
    such that they can implement the logic, whilst abstracting away
    the rest of the implementation (i.e. rendering, PyGame things, etc.)
"""

#region LOGIC FUNCTIONS

def check_alive(snake, grid_size):
    """
        Returns True if the snake is alive.
        Otherwise, returns False.
    """
    print("ERROR - Function 'check_alive' is corrupted!")
    return True


def did_eat_apple(snake, apple_x, apple_y):
    """
        Returns True if the snake ate the apple.
        Otherwise, returns False.
    """
    print("ERROR - Function 'did_eat_apple' is corrupted!")
    return False

def update_snake(snake, apple_was_eaten, move_direction):
    """
        Determines the new state of the snake.
        
        You can either modify the snake, OR
        return a new copy of the snake.

        Note that returning a snake will override
        any modifications to the original snake.
    """
    print("ERROR - Function 'update_snake' is corrupted!")
    

def apple_eaten_score(snake):
    """
        Returns the number of points to
        gain when the snake eats an apple.
    """
    return len(snake)

#region KEYBOARD ARROW BUTTON LOGIC

def on_left_arrow(snake, move_direction):
    """
        Runs when the left arrow is pressed.
        You should return the relevant move
        direction (i.e. LEFT, RIGHT, etc).
    """
    return "LEFT"


def on_right_arrow(snake, move_direction):
    """
        Runs when the right arrow is pressed.
        You should return the relevant move
        direction (i.e. LEFT, RIGHT, etc).
    """
    return "RIGHT"


def on_up_arrow(snake, move_direction):
    """
        Runs when the up arrow is pressed.
        You should return the relevant move
        direction (i.e. LEFT, RIGHT, etc).
    """
    return "UP"


def on_down_arrow(snake, move_direction):
    """
        Runs when the down arrow is pressed.
        You should return the relevant move
        direction (i.e. LEFT, RIGHT, etc).
    """
    return "DOWN"

#endregion 

#endregion
