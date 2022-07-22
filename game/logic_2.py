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
    snake_head_x = snake[0][0]
    snake_head_y = snake[0][1]
    return (snake_head_x == apple_x and snake_head_y == apple_y)

def update_snake(snake, apple_was_eaten, move_direction):
    """
        Determines the new state of the snake.
        
        You can either modify the snake, OR
        return a new copy of the snake.

        Note that returning a snake will override
        any modifications to the original snake.
    """
    current_snake_head = snake[0]
    new_snake_head = current_snake_head[:]
    if move_direction == "UP": new_snake_head[1] -= 1
    elif move_direction == "DOWN": new_snake_head[1] += 1
    elif move_direction == "LEFT": new_snake_head[0] -= 1
    elif move_direction == "RIGHT": new_snake_head[0] += 1

    new_snake = [new_snake_head]
    new_snake.extend(snake)
    if not apple_was_eaten:
        new_snake.pop()
    
    return new_snake
    

def apple_eaten_score(snake):
    """
        Returns the number of points to
        gain when the snake eats an apple.
    """
    return 100 * len(snake)

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
