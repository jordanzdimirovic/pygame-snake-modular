"""
    Everything related to rendering will be within this script.
"""

# LIBRARY IMPORTS
# ---------------

from math import sqrt
import pygame
from colours import GREEN, RED, WHITE, DARKGREY

# ---------------
#  END LIBRARIES

screen = None
txt_gameover = None
txt_restart_prompt = None

#region HELPER FUNCTIONS

def grid_to_pixel(grid_x, grid_y, SQUARE_SIZE_PIXELS):
    """
        Converts a grid location to screen position
        in pixels.
    """
    return (
        grid_x * SQUARE_SIZE_PIXELS,
        grid_y * SQUARE_SIZE_PIXELS
    )


#endregion


def setup_screen(screen_size, window_name = "Snake Game", background_colour = WHITE):
    """
        Sets up everything PyGame related.
    """
    global screen, txt_gameover, txt_restart_prompt
    pygame.init()

    screen = pygame.display.set_mode((screen_size, screen_size))

    # TODO: is this best?
    screen.fill(background_colour)

    pygame.display.set_caption(window_name)

    # Configure font
    pygame.font.init()
    sysfont = pygame.font.SysFont('Comic Sans MS', 30)
    txt_gameover = sysfont.render("Game Over - You Died!", True, (RED))
    txt_restart_prompt = sysfont.render("Press 'R' to restart...", True, (GREEN))
    

def draw_background(colour):
    """
        Draws a background of the
        specified colour.
    """
    screen_size = screen.get_size()
    bg = pygame.Surface(screen_size)
    pygame.draw.rect(bg, colour, [0, 0, screen_size[0], screen_size[1]])
    screen.blit(bg, (0, 0))


def draw_overlay(score):
    """
        Draws the overlay, including any text
        (such as score, etc).
    """
    pass


def draw_grid(n_grid, grid_size, colour, thickness):
    """
        Draws the game grid.
    """
    half_grid_size = grid_size // 2
    for i in range(n_grid):
        for j in range(n_grid):
            x, y = i * grid_size, j * grid_size
            pygame.draw.rect(screen, colour, [x, y, grid_size, grid_size], thickness)
            

def draw_snake(snake, colour, square_size, snake_part_prop):
    """
        Draws the snake on the
        grid, given the list that 
        represents its parts.
    """
    chopped = (1 - snake_part_prop) * square_size // 2
    for sx, sy in snake:
        x, y = grid_to_pixel(sx, sy, square_size)
        x += chopped
        y += chopped
        pygame.draw.rect(screen, colour, [x, y, square_size - 2 * chopped, square_size - 2 * chopped], 0)


def draw_apple(apple_x, apple_y, colour, square_size, apple_prop):
    """
        Draws the apple on the grid.
    """
    chopped = (1 - apple_prop) * square_size // 2
    x, y = grid_to_pixel(apple_x, apple_y, square_size)
    x += chopped
    y += chopped
    pygame.draw.rect(screen, colour, [x, y, square_size - 2 * chopped, square_size - 2 * chopped], 0)

def draw_gameover_pane(sep = 40):
    screensize = screen.get_size()
    sx,sy = screensize
    pane = pygame.Surface(screensize)
    pane.set_alpha(128)
    pane.fill(DARKGREY)
    screen.blit(pane, (0,0))
    pane.set_alpha(255)
    screen.blit(txt_gameover, txt_gameover.get_rect(center = (sx//2, sy//2 - sep // 2)))
    screen.blit(txt_restart_prompt, txt_restart_prompt.get_rect(center = (sx//2, sy//2 + sep // 2)))
    