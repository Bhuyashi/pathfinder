from maze import *

class BFS():
    def __init__(self,maze,start_cell,end_cell):
        self.visited = []
        self.done = []
        self.queue = []
        self.move = [('S',(0,1)),
                    ('E',(1,0)),
                    ('N',(0,-1)),               
                    ('W',(-1,0))]
        self.name = 'bfs'

    def nearest_neighbours(self,cell,maze):
        neighbours = []
        for direction, (dx,dy) in self.move:
            if cell.walls[direction] == False:
                x2,y2 = cell.x + dx, cell.y + dy
                if (x2,y2) not in self.visited and (x2,y2) not in self.done:
                    neighbour = maze.cell_at(x2,y2)
                    neighbour.parent = (cell.x,cell.y)
                    neighbours.append(neighbour)
        return neighbours
    
    def run(self,maze,ix,iy):
        if (ix,iy) not in self.visited:
            self.visited.append((ix,iy))
        cell = maze.cell_at(ix,iy)
        valid_neighbours = self.nearest_neighbours(cell,maze)
        self.queue = self.queue + valid_neighbours
        for cells in valid_neighbours:
            self.visited.append((cells.x,cells.y))
        if valid_neighbours==[]:
            self.done.append((ix,iy))
            # if len(self.visited)>0:
            #     ix,iy = self.visited.pop(-1)
        
        next_cell = self.queue.pop(0)
        # print(next_cell.x,next_cell.y)
        # print(self.visited)
        # self.visited.append((ix,iy))
        ix,iy = next_cell.x,next_cell.y
        return cell,ix,iy

