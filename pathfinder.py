import pygame
import time
from maze import Maze
from dfs import *
from bfs import *

# Light theme
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# RED = (255,0,0)
# GREEN = (0,160,0)
# ORANGE = (255, 117, 24)
# YELLOW = (255, 191, 0)

# Dark theme 
BLACK = (255, 255, 255) # white
WHITE = (0, 0, 20)      # black
RED = (255,0,0)         # red
GREEN = (0,160,0)       # green
ORANGE = (255, 16, 240) # pink
YELLOW = (127, 0, 255)  # violet

def print_path(maze,start_cell,end_cell,algorithm):
    global SCREEN, CLOCK, WINDOW_WIDTH, WINDOW_HEIGHT, blockSize
    blockSize = 20
    WINDOW_WIDTH = WINDOW_HEIGHT = blockSize*maze.nx

    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)

    display_maze(maze)
    xs,ys = start_cell
    ix,iy = xs,ys
    xe,ye = end_cell
    end_point = pygame.Rect(xe*blockSize, ye*blockSize, blockSize, blockSize)
    pygame.draw.rect(SCREEN, GREEN, end_point, 0)

    next_time = 0
    flag = 1
    last = 0
    backtrack_list = []

    while True:

        curr_time = pygame.time.get_ticks()
        if curr_time > next_time:
            next_time = curr_time+100
            if flag==1:             
                if ix==xe and iy==ye and last==0: 
                    last = 1
                    if algorithm.name == 'bfs':
                        while((ix,iy) != (xs,ys)):
                            last_cell = maze.cell_at(ix,iy)
                            ix,iy = last_cell.parent
                            backtrack_list.append((ix,iy))
                    elif algorithm.name == 'dfs':
                        backtrack_list = algorithm.visited[::-1]
                elif last==1:
                    if len(backtrack_list)>0:
                        bx,by = backtrack_list.pop(0)
                        new_cell = maze.cell_at(bx,by)
                    backtrack(bx,by,new_cell)     
                else:
                    start_cell,ix,iy = algorithm.run(maze,ix,iy)
                    draw_path(start_cell,ix,iy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                flag = -1*flag
            
        pygame.display.update()

def display_maze(maze):
    for j in range(0,maze.ny):
        for i in range(0,maze.nx):
            cell = maze.cell_at(i,j)
            x,y = i*blockSize, j*blockSize
            draw_wall(cell,x,y)

def draw_path(start_cell,ix,iy):
    ix = ix*blockSize
    iy = iy*blockSize
    px = start_cell.x*blockSize
    py = start_cell.y*blockSize
    path_pointer = pygame.Rect(ix+1, iy+1, blockSize-1, blockSize-1)
    pygame.draw.rect(SCREEN, RED, path_pointer, 0)
    pygame.draw.rect(SCREEN, YELLOW, (px,py,blockSize,blockSize), 0)
    draw_wall(start_cell,px,py)

def draw_wall(cell,x,y):
    if cell.walls['N']:
        pygame.draw.line(SCREEN,BLACK,(x,y),(x+blockSize,y),1)
    if cell.walls['E']:
        pygame.draw.line(SCREEN,BLACK,(x+blockSize,y),(x+blockSize,y+blockSize),1)
    if cell.walls['W']:
        pygame.draw.line(SCREEN,BLACK,(x,y),(x,y+blockSize),1)
    if cell.walls['S']:
        pygame.draw.line(SCREEN,BLACK,(x,y+blockSize),(x+blockSize,y+blockSize),1)

def backtrack(ix,iy,cell):
    ix = ix*blockSize
    iy = iy*blockSize
    path_pointer = pygame.Rect(ix, iy, blockSize, blockSize)
    pygame.draw.rect(SCREEN, ORANGE, path_pointer, 0)
    draw_wall(cell,ix,iy)

if __name__ == '__main__':
    grid_size = 20
    maze = Maze(grid_size,grid_size)
    maze.build_maze() 
    # start_cell = (maze.nx-1,maze.ny-1)
    start_cell = (maze.nx//2,maze.ny//2)
    end_cell = (0,0)
    # end_cell = (maze.nx//2,maze.ny//2)

    dfs = DFS(maze,start_cell,end_cell)
    print_path(maze,start_cell,end_cell,dfs)

    # bfs = BFS(maze,start_cell,end_cell)
    # print_path(maze,start_cell,end_cell,bfs)