import random

class Cell():
    def __init__(self,x,y):
        self.x, self.y = x,y
        self.walls = {'N':True, 'E':True, 'W':True, 'S':True,}
        self.opp_wall = {'N':'S','E':'W','W':'E','S':'N'}
        self.parent = (0,0)
        self.G, self.H = 0,0
    
    def break_wall(self,neighbour,direction):
        self.walls[direction] = False
        neighbour.walls[self.opp_wall[direction]] = False

class Maze():
    def __init__(self,nx,ny,ix=0,iy=0):
        self.nx,self.ny = nx,ny
        self.ix,self.iy = ix,iy
        self.maze = [[Cell(x,y) for x in range(nx)] for y in range(ny)]
        self.visited = []
        self.done = []

    def cell_at(self,x,y):
        return self.maze[y][x]

    def __str__(self):
        rows = ['-'*self.nx*2]
        for y in range(self.ny):
            row = ['|']
            for x in range(self.nx):
                if self.maze[y][x].walls['E']:
                    row.append(' |')
                else:
                    row.append('  ')
            rows.append(''.join(row))
            row = ['|']
            for x in range(self.nx):
                if self.maze[y][x].walls['S']:
                    if x==self.nx-1:
                        row.append('-|')
                    else:
                        row.append('-+')

                else:
                    if x==self.nx-1:
                        row.append(' |')
                    else:
                        row.append(' +')
            rows.append(''.join(row))
        return '\n'.join(rows)
    
    def nearest_neighbours(self,cell):
        move = [('N',(0,-1)),
                ('E',(1,0)),
                ('W',(-1,0)),
                ('S',(0,1))]
        neighbours = []
        for direction, (dx,dy) in move:
            x2,y2 = cell.x + dx, cell.y + dy
            if 0<=x2<self.nx and 0<=y2<self.ny:
                if (x2,y2) not in self.visited and (x2,y2) not in self.done:
                    neighbour = self.cell_at(x2,y2)
                    neighbours.append((direction,neighbour))
        return neighbours
    
    def build_maze(self):
        ix,iy = self.ix,self.iy
        count = 0
        while count<self.nx*self.ny-1:
            start_cell,ix,iy,count = self.maze_builder(ix,iy,count)

    def maze_builder(self,ix,iy,count):
        start_cell = self.cell_at(ix,iy)
        valid_neighbours = self.nearest_neighbours(start_cell)
        if valid_neighbours==[]:
            self.done.append((ix,iy))
            if len(self.visited)>0:
                ix,iy = self.visited[-1]
                self.visited = self.visited[:-1]
        else:
            next_direction, next_cell = random.choice(valid_neighbours)
            start_cell.break_wall(next_cell,next_direction)
            self.visited.append((ix,iy))
            ix,iy = next_cell.x,next_cell.y
            count += 1
        return start_cell, ix,iy,count
    
    def write_svg(self, filename):
        """Write an SVG image of the maze to filename."""

        aspect_ratio = self.nx / self.ny
        # Pad the maze all around by this amount.
        padding = 10
        # Height and width of the maze image (excluding padding), in pixels
        height = 500
        width = int(height * aspect_ratio)
        # Scaling factors mapping maze coordinates to image coordinates
        scy, scx = height / self.ny, width / self.nx

        def write_wall(ww_f, ww_x1, ww_y1, ww_x2, ww_y2):
            """Write a single wall to the SVG image file handle f."""

            print('<line x1="{}" y1="{}" x2="{}" y2="{}"/>'
                  .format(ww_x1, ww_y1, ww_x2, ww_y2), file=ww_f)

        # Write the SVG image file for maze
        with open(filename, 'w') as f:
            # SVG preamble and styles.
            print('<?xml version="1.0" encoding="utf-8"?>', file=f)
            print('<svg xmlns="http://www.w3.org/2000/svg"', file=f)
            print('    xmlns:xlink="http://www.w3.org/1999/xlink"', file=f)
            print('    width="{:d}" height="{:d}" viewBox="{} {} {} {}">'
                  .format(width + 2 * padding, height + 2 * padding,
                          -padding, -padding, width + 2 * padding, height + 2 * padding),
                  file=f)
            print('<defs>\n<style type="text/css"><![CDATA[', file=f)
            print('line {', file=f)
            print('    stroke: #000000;\n    stroke-linecap: square;', file=f)
            print('    stroke-width: 5;\n}', file=f)
            print(']]></style>\n</defs>', file=f)
            # Draw the "South" and "East" walls of each cell, if present (these
            # are the "North" and "West" walls of a neighbouring cell in
            # general, of course).
            for x in range(self.nx):
                for y in range(self.ny):
                    if self.cell_at(x, y).walls['S']:
                        x1, y1, x2, y2 = x * scx, (y + 1) * scy, (x + 1) * scx, (y + 1) * scy
                        write_wall(f, x1, y1, x2, y2)
                    if self.cell_at(x, y).walls['E']:
                        x1, y1, x2, y2 = (x + 1) * scx, y * scy, (x + 1) * scx, (y + 1) * scy
                        write_wall(f, x1, y1, x2, y2)
            # Draw the North and West maze border, which won't have been drawn
            # by the procedure above.
            print('<line x1="0" y1="0" x2="{}" y2="0"/>'.format(width), file=f)
            print('<line x1="0" y1="0" x2="0" y2="{}"/>'.format(height), file=f)
            print('</svg>', file=f)
      
# maze = Maze(15,15)
# maze.build_maze()
# print(maze)
# maze.write_svg('maze.svg')