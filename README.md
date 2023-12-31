# pathfinder

## Setup

The aim of this project is to first create a maze and then compare various path-finding algorithms. The purpose of each of the files is as follows:

1. **maze.py** - It has the class Maze which constructs the maze in which the search algorithms will work
2. **createMaze.py** - It provides a visual representation of how the maze is constructed using a depth-first search
3. **pathfinder.py** - It constructs a maze and runs different path-finding algorithms given any start and end point
4. **dfs.py** - It contains the DFS class which helps perform a Depth-First Search on the maze

## Result

The maze.py code creates an svg image of the maze. A screenshot of a 15x15 maze is shown below

<p align="center">
  <img width="400" src="images/maze_10_10.png">
</p>

With the createMaze.py we can view how the algorithm constructs the maze. The video shows how the above maze is built.

<div align="center">
<video src='https://github.com/Bhuyashi/pathfinder/assets/28145026/4fc3dae7-fd64-4ddb-8ca5-f9761b191d89' />
</div>

The pathfinder.py creates a maze of size 15x15 and runs the DFS algorithm on it. The start point is the center of the maze and the end point is marked in green. Once it reaches the end it backtracks the optimal path in pink.

<div align="center">
<video src='https://github.com/Bhuyashi/pathfinder/assets/28145026/8234b6c8-8462-4aae-a621-884812a7033e' />
</div>



