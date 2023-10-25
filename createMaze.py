import pygame
from maze import *
# import sys

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
BLUE = (0, 102, 204)
RED = (255,0,0)


def main(num):
    global SCREEN, CLOCK, WINDOW_WIDTH, WINDOW_HEIGHT, blockSize
    blockSize = 20
    WINDOW_WIDTH = WINDOW_HEIGHT = blockSize*num

    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLUE)
    
    drawGrid()
    next_time = 0
    count = 0
    ix = iy = 0
    flag = 1
    
    while True:

        curr_time = pygame.time.get_ticks()
        if curr_time > next_time:
            next_time = curr_time+100
            if count<maze.nx*maze.ny-1 and flag==1:
                scell,ix,iy,count = maze.maze_builder(ix,iy,count)
                drawPointer(scell,ix,iy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # sys.exit()
                return
            if event.type == pygame.KEYDOWN:
                flag = -1*flag

        pygame.display.update()

def drawGrid():
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)

def drawPointer(scell,ix,iy):
    x = scell.x*blockSize
    y = scell.y*blockSize
    ix = ix*blockSize
    iy = iy*blockSize
    pointer = pygame.Rect(ix, iy, blockSize, blockSize)
    pygame.draw.rect(SCREEN, RED, pointer, 0)
    pygame.draw.rect(SCREEN, BLACK, (x,y,blockSize,blockSize), 0)

    if scell.walls['N']:
        pygame.draw.line(SCREEN,WHITE,(x,y),(x+blockSize,y),1)
    if scell.walls['E']:
        pygame.draw.line(SCREEN,WHITE,(x+blockSize,y),(x+blockSize,y+blockSize),1)
    if scell.walls['W']:
        pygame.draw.line(SCREEN,WHITE,(x,y),(x,y+blockSize),1)
    if scell.walls['S']:
        pygame.draw.line(SCREEN,WHITE,(x,y+blockSize),(x+blockSize,y+blockSize),1)

grid_size = 15
maze = Maze(grid_size,grid_size)
main(grid_size)
maze.write_svg('maze.svg')
