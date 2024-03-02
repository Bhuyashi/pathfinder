from maze import *

class AStar():
    def __init__(self,maze,start_cell,end_cell):
        self.xs,self.ys = start_cell
        self.xe,self.ye = end_cell
        self.visited = []
        self.done = []
        self.queue = []
        self.move = [('S',(0,1)),
                    ('E',(1,0)),
                    ('N',(0,-1)),               
                    ('W',(-1,0))]
        self.name = 'astar'

    def nearest_neighbours(self,cell,maze):
        neighbours = []
        for direction, (dx,dy) in self.move:
            if cell.walls[direction] == False:
                x2,y2 = cell.x + dx, cell.y + dy
                if (x2,y2) not in self.visited and (x2,y2) not in self.done:
                    neighbour = maze.cell_at(x2,y2)
                    neighbour.parent = (cell.x,cell.y)
                    neighbour.G = cell.G+1
                    neighbour.H = abs(self.xe-x2)+abs(self.ye-y2)               # Manhattan distance
                    neighbours.append(neighbour)
        return neighbours
    
    def insertCell(self,cell):
        sum = cell.G + cell.H
        n = len(self.queue)
        if n == 0:
            self.queue.append(cell)
        elif sum > self.queue[-1].G+self.queue[-1].H:
            self.queue.append(cell)
        else:
            for i in range(n):
                if sum < self.queue[i].G+self.queue[i].H:
                    self.queue.insert(i,cell)
                    break
                elif sum == self.queue[i].G+self.queue[i].H:
                    if cell.H < self.queue[i].H:
                        self.queue.insert(i,cell)
                    else:
                        self.queue.insert(i+1,cell)
                    break
  
    def run(self,maze,ix,iy):
        if (ix,iy) not in self.visited:
            self.visited.append((ix,iy))
        cell = maze.cell_at(ix,iy)
        valid_neighbours = self.nearest_neighbours(cell,maze)
        for cells in valid_neighbours:
            self.insertCell(cells)
            self.visited.append((cells.x,cells.y))
        if valid_neighbours==[]:
            self.done.append((ix,iy))
        
        next_cell = self.queue.pop(0)
        ix,iy = next_cell.x,next_cell.y
        return cell,ix,iy

