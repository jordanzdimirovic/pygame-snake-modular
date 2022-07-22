"""
    This script brings every component together,
    and handles many of the PyGame intricacies
    required.

    It is not intended for modification by
    a given student. However, the code is designed
    to be as simple as possible, using preliminary
    concepts and avoiding any OO paradigms.
"""

# LIBRARY IMPORTS
# ---------------

# Disables message from PyGame library
from os import environ
from random import randint
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

import logic_3 as logic
import render
from colours import *

# ---------------
#  END LIBRARIES

#region CONSTANTS

"""
Screen is a square.
Here, we defined the screen
size in pixels, which will be
used for both width and height.
"""
SCREEN_SIZE_PIXELS = 800

"""
The number of grid squares on
the x and y axes.
"""
NO_GRID_SQUARES = 15

SQUARE_SIZE_PIXELS = SCREEN_SIZE_PIXELS // NO_GRID_SQUARES

"""
The starting size of
the snake
This is inclusive of the
head
"""
SNAKE_START_SIZE = 3

"""
How many times a second the game
will continue to the next state.

The higher this number, the more
difficult the game will be!
"""
GAME_TICK_RATE = 4
ORIG_GAME_TICK_RATE = GAME_TICK_RATE

#endregion

#region GAMEPLAY VARIABLES

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
The apple's x and y coordinates
"""
apple_x = 0
apple_y = 0

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

#region HELPER FUNCTIONS

DEBUG_MODE = False
def debug_log(msg):
    if DEBUG_MODE: print("DEBUG --> " + msg)


def shutdown():
    global game_open
    game_open = False


def reset_variables():
    global snake, apple_x, apple_y, is_alive, move_direction, player_score, GAME_TICK_RATE
    snake = []
    apple_x, apple_y = get_new_apple_location()
    is_alive = True
    move_direction = "UP"
    player_score = 0
    GAME_TICK_RATE = ORIG_GAME_TICK_RATE


def initialise_game():
    global snake
    reset_variables()
    # Get middle square and grow down
    snake = [[NO_GRID_SQUARES // 2, NO_GRID_SQUARES // 2 + i] for i in range(SNAKE_START_SIZE)]
    

EVENT_OKAY = 1
EVENT_QUIT = 0

KEYBOARD_EVENTS = {
    pygame.K_LEFT: lambda: logic.on_left_arrow(snake, move_direction),
    pygame.K_RIGHT: lambda: logic.on_right_arrow(snake, move_direction),
    pygame.K_UP: lambda: logic.on_up_arrow(snake, move_direction),
    pygame.K_DOWN: lambda: logic.on_down_arrow(snake, move_direction),

    pygame.K_ESCAPE: shutdown,
    pygame.K_r: initialise_game
}

DIRECTIONS = ("UP", "DOWN", "LEFT", "RIGHT")

def handle_keydown(key):
    global move_direction
    debug_log(f"Key: '{key}' was pressed.")
    if key in KEYBOARD_EVENTS:
        result = KEYBOARD_EVENTS[key]()
        if result and result.upper() in DIRECTIONS:
            move_direction = result.upper()


def handle_event(event):
    if event.type == pygame.QUIT:
        return EVENT_QUIT
    elif event.type == pygame.KEYDOWN:
        handle_keydown(event.key)


#endregion

#region VALIDATION

def validate_snake(snake):
    if type(snake) != list or any(len(part) != 2 for part in snake):
        return False, "The snake needs to be a list of [x,y] pairs."
    elif len(snake) < SNAKE_START_SIZE:
        return False, "The snake lost its length!"
    else:
        return True, ""

#endregion

#region GAME LOGIC (DELEGATED)

def get_new_apple_location():
    return randint(0, NO_GRID_SQUARES - 1), randint(0, NO_GRID_SQUARES - 1) 

apple_pending = False
def next_step():
    global snake, is_alive, apple_pending, apple_x, apple_y, player_score, GAME_TICK_RATE
    
    ate_apple = logic.did_eat_apple(snake, apple_x, apple_y)

    if ate_apple:
        player_score += logic.apple_eaten_score(snake)
        print(f"Nice! Your current score is: {player_score}")
        apple_x, apple_y = get_new_apple_location()

    value = logic.update_snake(
        snake,
        ate_apple,
        move_direction
    )

    result, reason = None, None
    new_snake = None
    if value:
        result, reason = validate_snake(value)
        new_snake = value
    
    else:
        result, reason = validate_snake(snake)
        new_snake = snake

    if not result:
        raise ValueError(f"There was an error when updating the snake:\n{reason}")
    
    else:
        snake = new_snake

    if not logic.check_alive(snake, NO_GRID_SQUARES):
        is_alive = False
        GAME_TICK_RATE = 18
        return
        
#endregion

#region GAME LOOP

game_open = True

# Initialise screen
render.setup_screen(SCREEN_SIZE_PIXELS)

# Initialise game
initialise_game()

previous_tick = pygame.time.get_ticks() / 1000

while game_open:
    for event in pygame.event.get():
        if handle_event(event) == EVENT_QUIT:
            shutdown()

    current_tick = pygame.time.get_ticks() / 1000
    if current_tick - previous_tick < 1 / GAME_TICK_RATE:
        continue

    if is_alive:
        next_step()

    else:
        render.draw_gameover_pane(100)
        pygame.display.flip()

    

    if is_alive:
        render.draw_background(LIGHTGREY)
        render.draw_grid(NO_GRID_SQUARES, SQUARE_SIZE_PIXELS, DARKGREY, 2)
        render.draw_apple(apple_x, apple_y, RED, SQUARE_SIZE_PIXELS, 0.5)
        render.draw_snake(snake, GREEN, SQUARE_SIZE_PIXELS, 0.8)
        pygame.display.flip()
    
    previous_tick = current_tick

#endregion