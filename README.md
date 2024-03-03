# pathfinder

## Setup

This project aims to first create a maze and then compare various path-finding algorithms. The purpose of each of the files is as follows:

1. **maze.py** - It has the class Maze which constructs the maze in which the search algorithms will work
2. **createMaze.py** - It provides a visual representation of how the maze is constructed using a depth-first search
3. **pathfinder.py** - It constructs a maze and runs different path-finding algorithms given any start and end point
4. **dfs.py** - It contains the DFS class which helps perform a Depth-First Search on the maze
5. **dfs.py** - It contains the BFS class which helps perform a Breadth-First Search on the maze
6. **astar.py** - It contains the AStar class which helps perform a heuristic-based search on the maze

## Result

The maze.py code creates an svg image of the maze. A screenshot of a 15x15 maze is shown below

<p align="center">
  <img width="400" src="images/maze_10_10.png">
</p>

With the createMaze.py we can view how the algorithm constructs the maze. The video shows how the above maze is built.

<div align="center">
<video src='https://github.com/Bhuyashi/pathfinder/assets/28145026/4fc3dae7-fd64-4ddb-8ca5-f9761b191d89' />
</div>

### Depth First Search (DFS)

Below the pathfinder.py creates a maze of size 20x20 and runs the DFS algorithm on it. The start point is the right-bottom corner of the maze and the end point is marked in green. Once it reaches the end it backtracks the optimal path in pink.

<div align="center" >
<video src='https://github.com/Bhuyashi/pathfinder/assets/28145026/de7597ab-a6c6-4603-aa58-7e28fa69e949' />
</div>

### Breadth First Search (BFS)

The BFS algorithm is run on the same maze to compare the algorithms.

<div align="center">
  <video src='https://github.com/Bhuyashi/pathfinder/assets/28145026/3d5dfeb4-2bde-4440-8374-f7146f286d20' />
</div>

### A-Star

The A-Star algorithm uses a heuristic rather than blindly trying to find a path. The heuristic used here is Manhattan distance. The A-Star algorithm on the above maze is shown below.

<div align="center">
<video src='https://github.com/Bhuyashi/pathfinder/assets/28145026/a0dc3197-c9d6-4a91-9242-14d24b646603' />
</div>































