# AI

Knights and Queens

Problem Scenario:
You are given a chessboard of size N * M, where N represents the number of rows and M represents the number of columns. Your task is to arrange K knights and Q queens on the board in such a way that no queens attack each other and no knight attacks another knight or a queen. The goal is to find a valid configuration that satisfies these conditions.

Constraints:

4 ≤ N, M ≤ 16 (The chessboard can have a maximum size of 10 * 10).
0 ≤ K ≤ N * M (There can be at most N * M knights on the board).
0 ≤ Q ≤ N * M (There can be at most N * M queens on the board).

Note:

1) Knights attack in an L-shaped pattern, where they can move two squares in one direction (horizontally or vertically) and then one square perpendicular to that direction.
2) Queens attack horizontally, vertically, and diagonally.

Task:

You need to come up with an algorithm or a strategy to determine the valid arrangement of K knights and Q queens on the given N * M chessboard, ensuring that the conditions mentioned above are met.

Algorithms Implemented: 

1) Simulated Annealing 
2) Hill Climbing (Random-Restart)

*****************

Sliding Puzzle

Problem Scenario:

You are given a sliding puzzle problem on a rectangular board with dimensions M * N. The board contains several tiles with numbers from 1 to K, where K is a positive integer, and special tiles marked as -1, which cannot be moved. Your task is to rearrange the tiles on the board to reach a specific target configuration.

Note:

1) The sliding puzzle is played by moving the tiles horizontally or vertically into an empty space, creating a new configuration. Only tiles adjacent to the empty space can be moved, and the -1 tile is fixed and cannot be moved.

2) The objective is to find a sequence of moves that transforms the initial configuration into the target configuration. The target configuration will be a valid arrangement of the numbered tiles and the fixed -1 tile.

Task:
You need to come up with an algorithm or a strategy to solve the sliding puzzle problem by finding a sequence of valid moves to reach the target configuration on the given M * N board, considering the constraints mentioned above.

Algorithms Implemented: 

1) Breadth First Search (BFS)
2) Depth First Search (DFS)
3) A-Star (0-Heuristic, Misplaced Tiles Heuristic & Manhattan Distance Heuristic) 


*****************

Predictions 
