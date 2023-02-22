# 8-puzzle Solver

The 8 puzzle is a sliding puzzle having 8 square tiles numbered 1–8 in a frame that is 3 tiles high and 3 tiles wide, leaving one unoccupied tile position. The goal of the puzzle is to place the tiles in numerical order by sliding one tile at a time.
<p align="center">
  <img width="20%"src="https://user-images.githubusercontent.com/55712285/220530459-9ec8c07e-8767-4b7d-bb16-23b7b20333cc.png">
</p>

## Search Algorithms
When running the program, the user can chose the following search algorithms to solve the puzzle:
### Uniform Cost Search
It expand the node with the cheaptest path cost first.
### A* with the Misplaced Tile heuristic.
The heuristic function is the number of misplaced tile in a given state compared to the goal state.
### A* with the Euclidean Distance heuristic
The heuristic function is the sum of each tile's euclidean distance between its current position and the correct position.

## How to Run
First clone this repo to your local machine and run the following command:
```
python main.py
```

## Output
```
8 Puzzle Solver
[1] Use default puzzle
[2] Enter your own puzzle
1

[1] Trival
1  2  3
4  5  6
7  8  0

[2] Very Easy
1  2  3
4  5  6
7  0  8

[3] Easy
1  2  0
4  5  3
7  8  6

[4] Doable
0  1  2
4  5  3
7  8  6

[5] Oh Boy
8  7  1
6  0  2
5  4  3

[6] IMPOSSIBLE (This puzzle is not solvable)
1  2  3
4  5  6
8  7  0

Choose a puzzle to solve: 3

The puzzle:
1  2  0
4  5  3
7  8  6

Enter your choice of algorithm:
[1] Uniform Cost Search
[2] A* with the Misplaced Tile Heuristic
[3] A* with the Euclidean Distance Heuristic
1

Press Enter to continue...

Using Uniform Cost Search
Expanding state:
1  2  0
4  5  3
7  8  6


The best state to expand with g(n) = 0 and h(n) = 0 is:
1  2  0
4  5  3
7  8  6
Expanding this node...

The best state to expand with g(n) = 1 and h(n) = 0 is:
1  2  3
4  5  0
7  8  6
Expanding this node...

The best state to expand with g(n) = 1 and h(n) = 0 is:
1  0  2
4  5  3
7  8  6
Expanding this node...

Goal!!
Solution found at depth: 2
Number of nodes expanded to solve this problem: 4
The maximum number of nodes in the queue at any one time: 4
The time it took to solve: 0.0019981861114501953 second

The solution path:
1  2  0
4  5  3
7  8  6

1  2  3
4  5  0
7  8  6

1  2  3
4  5  6
7  8  0
```

## Challenges
- The list of the explored nodes is not working. Nodes are added to the list but when comparing the current node it did not match any explored node in the list even though it has been explored. I noticed this when running test cases and found it is expanding a node that has been visited.
- Another problem is when calculating the euclidean distance. The math part is incorrect at first and fixed later.
- The pseudo-code in the reading material says to replace the node in frontier with the child node of the same state but lower path cost. I couldn't check if the frontier has a node with the same state as the child node because the priority queue in python is not iterable and can’t update the value after being pushed to the queue.
