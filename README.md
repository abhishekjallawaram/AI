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

Classifications & Predictions 

A) Analysis of Bank Marketing Dataset

Problem Scenario : 

You have been provided with a dataset related to the direct marketing campaigns of a Portuguese banking institution. The dataset, named bank-additional-full.csv, contains information about phone calls made to clients, and the goal is to predict whether a client will subscribe to a term deposit or not.

The dataset can be found at the following URL: Bank Marketing Dataset (https://archive.ics.uci.edu/dataset/222/bank+marketing)

Your task is to implement the following classifiers:

1) K-Nearest Neighbors (KNN) classifier
2) Decision Tree classifier
3) Random Forest classifier
4) Another classifier of your choice with the objective of improving the classification performance as much as possible.

Task:

Your ultimate objective is to improve the classification accuracy by selecting suitable classifiers, preprocessing the data if necessary, and leveraging the strengths of the additional classifier you choose.

B) Prediction of Motion-Planning Distance

Problem Scenario:

The objective of motion planning is to compute a path from an initial position to a goal position while avoiding collisions with obstacles. One of the simplest algorithms used for motion planning is called Bug2 (https://www.youtube.com/watch?v=Z70hrAUewhI) . The Bug2 algorithm tries to move directly toward the goal. When it encounters an obstacle, it moves along the boundary of the obstacle until a straight path to the goal becomes available. You can refer to the following YouTube video to see a solution achieved using the Bug2 algorithm: Bug2 Algorithm Solution

Your task is to predict the distance of the solution found by the Bug2 algorithm given the start position (sx, sy) and the goal position (gx, gy). Each row in the dataset represents a specific scenario, providing the start position, the goal position, and the distance of the solution found by the Bug2 algorithm.

To accomplish this task, you should implement the following regression models:

1) K-Nearest Neighbors (KNN) regressor
2) Decision Tree regressor
3) Random Forest regressor
4) Another regressor of your choice with the objective of improving the prediction accuracy as much as possible.

Task:

Your aim is to enhance the prediction accuracy by selecting appropriate regressors and leveraging the strengths of the additional regressor you choose.

**************

