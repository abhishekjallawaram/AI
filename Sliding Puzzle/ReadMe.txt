Name : Abhishek Jallawaram
GMU_ID : G01373042

Class : CS 580 - 001 (Project 2: Sliding Puzzle)
Professor : Dr.Erion Plaku
*****************************************************************************************************************
requirements.txt containts the packages required to be installed to run the program

py SolvePuzzle.py problem.txt method tmax solution.txt

1) SolvePuzzle.py : Python program name
2) problem.txt : input file

    problem.txt is the name of the file providing the problem description. The input file is formatted as follows:
    N M (e.g 4 4)

    initialState (e.g 4 2 1 2 7 1 5 -1 2 1 6 3 7 0 -1 -1)

    goalState (e.g 4 0 1 2 1 2 5 -1 7 2 6 3 7 1 -1 -1)

3) method: DFS, BFS, AStarH0, AStarH1, AStarH2
    BFS - Breadth First Search
    DFS - Depth First Search (Brute Force apprach - may not find the solution always)
    AStarH0 - Astar algorithm with heuristic value as zero, cost was calculated by using the depth
    AStarH1 - Astar algorithm with heuristic value calculated using number for tiles which are not in goal state (Hamming distance)
    AstarH2 - Astar algorithm with heuristic value as Manhattan distance
    AstarH3 - Astar algorithm with heuristic value as max(Hamming distance,Manhattan_varinat function distance) - Dominant Function

4) tmax : Max time the program can run

5) solution.txt : Final solution containing the path taken to reach the goal. Contains position of zero/space for each move.

*****************************************************************************************************************

