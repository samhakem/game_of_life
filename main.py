# Conways game of life - Python

# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
# These rules, which compare the behavior of the automaton to real life, can be condensed into the following:
#
# Any live cell with two or three live neighbours survives.
# Any dead cell with three live neighbours becomes a live cell.
# All other live cells die in the next generation. Similarly, all other dead cells stay dead.

import time
import pygame
import numpy

# I want to define color constants as I will be using them frequently throughout
color_bg = (255, 246, 213)
color_grid = (249, 237, 187)
color_die_next = (185, 157, 136)
color_alive_next = (93, 50, 43)

# Update will contain game logic and drawing process
# with_progress=False allows me to update the screen without moving to the next generation, if true executes the next
# generation
def update(screen, cells, size, with_progress=False):
    # empty numpy array creates the shape of the already existing cells and creates an empy array and within this
    # updated array apply changes
    updated_cells = numpy.empty((cells.shape[0], cells.shape[1]))
    # This takes each cell and lets me iterate over each cell by row and column going throuhg each and ecery one
    for row, col in numpy.ndindex(cells.shape):
        # Apply game rules here: calculate number of alive neighbouring cells, check all cells surrounding current
        # alive cell if any others are alive
        alive = numpy.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color = color_bg if cells[row, col] == 0 else color_alive_next

        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    color - color_die_next
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = color_alive_next
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                color = color_alive_next
        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))
        return updated_cells
