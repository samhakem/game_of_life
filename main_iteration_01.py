# Conways game of life - Python

# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
# These rules, which compare the behavior of the automaton to real life, can be condensed into the following:

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
    updated_cells = numpy.zeros((cells.shape[0], cells.shape[1]))
    # This takes each cell and lets me iterate over each cell by row and column going throuhg each and ecery one
    for row, col in numpy.ndindex(cells.shape):
        # Apply game rules here: calculate number of alive neighbouring cells, check all cells surrounding current
        # alive cell if any others are alive
        # Calculate from top left cell to bottom right cell any 1 cells, sdubstract the 1 cell that is alive
        alive = numpy.sum(cells[row - 1:row + 2, col - 1:col + 2]) - cells[row, col]
        # Sets cells to background color if not alive = 0 else sets to alive next color
        color = color_bg if cells[row, col] == 0 else color_alive_next

        if cells[row, col] == 1:
            # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
            # Any live cell with more than three live neighbours dies, as if by overpopulation.
            if alive < 2 or alive > 3:
                if with_progress:
                    color = color_die_next
            # Any live cell with two or three live neighbours lives on to the next generation.
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = color_alive_next
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = color_alive_next
        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

    return updated_cells


# Main functionality
def main():
    # Initialise pygame
    pygame.init()
    # Create a screen
    screen = pygame.display.set_mode((1920, 1080))
    cells = numpy.zeros((108, 192))
    # Fills screen with grid color unless a cell is dead in which case it applies the background color to that cell
    screen.fill((color_grid))
    update(screen, cells, 10)
    pygame.display.flip()
    pygame.display.update()

    # Game loop
    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                # Toggle running with spacebar
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 10)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 1
                pygame.display.update()
                screen.fill(color_grid)

            if running:
                cells = update(screen, cells, 10, with_progress=True)
                pygame.display.update()

            time.sleep(0.001)


if __name__ == '__main__':
    main()
