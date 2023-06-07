import sys
import numpy as np
import heapq
import time

#Class to define the puzzle state based on the inputs
class puzzle_state:
    previous_state = None
    state = None
    moves = 0
    cost = 0
    space_index = -1
    direction = ""
    hvalue = 0
    row = 0
    col = 0
    max_time = 0
    sol = 0

    # constructor for the puzzle state
    def __init__(self, state, goal_state, rows, cols,tmax,previous_state=None, moves=0, direction="", h_value=0):
        self.previous_state = previous_state
        self.state = np.array(state)
        self.moves = moves
        self.direction = direction
        self.hvalue = h_value
        self.row = rows
        self.col = cols
        self.goal_state = np.array(goal_state)
        self.max_time = tmax
        
     #Verify whether goal state is achieved
    def goal(self):
        goal_state = self.goal_state
        if np.array_equal(self.state, goal_state):
            return True
        return False

    def __lt__(self, other_state):
        if self.cost != other_state.cost:
            return self.cost < other_state.cost

#Class to define the movement of the tile
class movement:
    visited = None
    rows = 0
    cols = 0

    def __init__(self, visited,row,col,goalState):
        self.visited = visited
        self.rows = row
        self.cols = col
        self.space_index = self.zero_index()
        self.goal_state = goalState

    def zero_index(self):     # find the place of the empty tile
        for i in range(self.rows*self.cols):
            #print(self.visited.state)
            if (self.visited.state[i] == 0):
                return i
        return -1
    # function that returns a new object with the given elements switch places

    def swap(self, element1, element2):
        temp_state = np.array(self.visited.state)
        temp_state[element1], temp_state[element2] = temp_state[element2], temp_state[element1]
        return temp_state

    def move_up(self):
        # valid to move up
        temp_state = np.array(self.visited.state)
        if(self.space_index > self.cols-1):
            if temp_state[self.space_index] or temp_state[self.space_index - self.cols] == -1:
                return None
            else:
                return puzzle_state(self.swap(self.space_index, self.space_index - self.cols),self.goal_state,self.rows,self.cols,self.visited.max_time,self.visited, self.visited.moves+1, "UP", self.visited.hvalue)
        else:
            return None

    def move_down(self):
        temp_state = np.array(self.visited.state)
        # valid to move down
        if(self.space_index < self.cols*(self.rows-1)):
            if temp_state[self.space_index] or temp_state[self.space_index + self.cols] == -1:
                return None
            else:
                return puzzle_state(self.swap(self.space_index, self.space_index + self.cols),self.goal_state,self.rows,self.cols,self.visited.max_time,self.visited, self.visited.moves+1, "DOWN", self.visited.hvalue)
        else:
            return None

    def move_left(self):
        temp_state = np.array(self.visited.state)
        # valid to move left
        if(self.space_index % self.rows != 0):
            if temp_state[self.space_index] or temp_state[self.space_index - 1] == -1:
                return None
            else:
                return puzzle_state(self.swap(self.space_index, self.space_index - 1),self.goal_state,self.rows,self.cols,self.visited.max_time,self.visited, self.visited.moves+1, "LEFT", self.visited.hvalue)
        else:
            return None

    def move_right(self):
        temp_state = np.array(self.visited.state)
        # valid to move right
        if(self.space_index % self.rows != self.cols-1):
            if temp_state[self.space_index] or temp_state[self.space_index + 1] == -1:
                return None
            else:
                return puzzle_state(self.swap(self.space_index, self.space_index + 1),self.goal_state,self.rows,self.cols,self.visited.max_time,self.visited, self.visited.moves+1, "RIGHT", self.visited.hvalue)
        else:
            return None

    def find_neighbours(self):  # generate all possible neighbours for a state
        neighbours = []
        neighbours.append(self.move_left())
        neighbours.append(self.move_right())
        neighbours.append(self.move_down())
        neighbours.append(self.move_up())
        return list(filter(None, neighbours))

def createid(x):
     return str(x)

#Class to Solve the puzzle using different search algorithms
class puzzle_solver:
    solved_puzzle = None
    total_cost = 0
    nodes_expanded = 0

    def dfs_search(self, puzzle):
        t0 = time.time()
        t1 = 0
        stack_dfs= {}
        explored = {}
        stack_dfs.update({createid(puzzle.state): puzzle})
        while (len(stack_dfs) != 0):
            while(t1-t0<puzzle.max_time):
                t1 = time.time()
                visited = stack_dfs.popitem()[1]
                #print(visited.moves)
                explored.update({createid(visited.state): visited})
                #if visited.goal():
                    #self.solved_puzzle = visited
                    #self.nodes_expanded = len(explored)-1
                    #return
                neigbours = movement(visited,puzzle.row,puzzle.col,puzzle.goal_state).find_neighbours()
                for neighbour in neigbours[::-1]:
                    if (explored.get(createid(neighbour.state)) == None and ((stack_dfs.get(createid(neighbour.state)) == None))):
                        stack_dfs.update({createid(neighbour.state): neighbour})
                        if neighbour.goal():
                            self.solved_puzzle = neighbour
                            self.nodes_expanded = len(explored)
                            return
                if(t1-t0>=puzzle.max_time):
                    puzzle.sol = 1
                    return





    def bfs_search(self, puzzle):
        queue_bfs = {}
        explored = {}
        list_bfs = list()
        queue_bfs.update({createid(puzzle.state): puzzle})
        list_bfs.append(puzzle)
        t0 = time.time()
        t1 = 0
        while(len(queue_bfs) != 0):
            while (t1 - t0 < puzzle.max_time):
                t1 = time.time()
                visited = list_bfs.pop(0)
                queue_bfs.pop(str(visited.state))
                explored.update({createid(visited.state): visited})
                #if visited.goal():
                #    self.solved_puzzle = visited
                #    self.nodes_expanded = len(list_bfs)-1
                #    return
                neigbours = movement(visited,puzzle.row,puzzle.col,puzzle.goal_state).find_neighbours()
                for neighbour in (neigbours):
                    if ((explored.get(createid(neighbour.state)) == None) and ((queue_bfs.get(createid(neighbour.state)) == None))):
                        queue_bfs.update({createid(neighbour.state): neighbour})
                        list_bfs.append(neighbour)
                        if neighbour.goal():
                            self.solved_puzzle = neighbour
                            self.nodes_expanded = len(explored)
                            return

                if (t1 - t0 >= puzzle.max_time):
                    print(t1-t0)
                    puzzle.sol = 1
                    return

    def A_star_search(self, puzzle):
        neighbours_heap = []
        explored_states_list = {}
        t0 = time.time()
        t1 = 0
        if puzzle.hvalue == 1:
            puzzle.cost = puzzle.moves + self.misplaced_cost(puzzle)
        elif puzzle.hvalue == 2:
            puzzle.cost = puzzle.moves + self.manhattan_cost(puzzle)
        elif puzzle.hvalue == 3:
            puzzle.cost = puzzle.moves + self.dominant_cost(puzzle)
        elif puzzle.hvalue == 0:
            puzzle.cost = puzzle.moves + 0

        heapq.heappush(neighbours_heap,puzzle)
        while(len(neighbours_heap) != 0):
            while (t1 - t0 < puzzle.max_time):
                t1 = time.time()
                visited = heapq.heappop(neighbours_heap)
                explored_states_list.update({createid(visited.state): visited})
                #if least_cost_state.check_for_goal():
                #    self.solved_puzzle = least_cost_state
                #    self.nodes_expanded = len(explored_states_list)-1
                #    return
                neigbours = movement(visited, puzzle.row, puzzle.col, puzzle.goal_state).find_neighbours()
                for neighbour in neigbours:
                    if (explored_states_list.get(createid(neighbour.state)) == None):
                        if neighbour.hvalue == 1:
                            neighbour.cost = neighbour.moves + self.misplaced_cost(neighbour)
                        elif neighbour.hvalue == 2:
                            neighbour.cost = neighbour.moves + self.manhattan_cost(neighbour)
                        elif neighbour.hvalue == 3:
                            neighbour.cost = neighbour.moves + self.dominant_cost(neighbour)
                        elif neighbour.hvalue == 0:
                            neighbour.cost = neighbour.moves + 0
                        if neighbour.goal():
                            self.solved_puzzle = neighbour
                            self.nodes_expanded = len(explored_states_list)
                            return
                        heapq.heappush(neighbours_heap,neighbour)

                if (t1-t0 >= puzzle.max_time):
                    puzzle.sol = 1
                    return

#Manhattan distance heuristic function
    def manhattan_cost1(self, puzzle):
        state = puzzle.state
        goal = puzzle.goal_state
        value = np.sum((np.absolute(state // puzzle.row - goal // puzzle.row) + np.absolute(state % puzzle.row - goal % puzzle.row)))
        return int(value)

    def manhattan_cost(self, puzzle):
        state = puzzle.state
        goal = puzzle.goal_state
        value = 0
        cost = -1
        visited_index = []
        visited_index.append(np.where(goal==0)[0][0])
        for i in range(len(state)):
            temp = 99999
            for j in range(len(goal)):
                if state[i] == goal[i] or state[i]!=0:
                    if j not in visited_index:
                        cost = abs(i//puzzle.row - j//puzzle.row) + abs(i%puzzle.row - j%puzzle.row)
                        visited_index.append(j)
                        if cost < temp:
                            temp = cost
            value += temp

        return value

    #Misplaced Tiles heuristic function
    def misplaced_cost(self, puzzle):
        state = puzzle.state
        goal = puzzle.goal_state
        value = 0
        for i in range(len(state)):
            if puzzle.state[i]!=puzzle.goal_state[i]:
                value+=1
        return value

    def dominant_cost(self,puzzle):
        return max(self.misplaced_cost(puzzle),self.manhattan_cost1(puzzle))

    #Fuction to determine the best path
    def get_best_path(self):
        path_list_array = []
        path_list_objects = []
        current_state = self.solved_puzzle
        path_list_objects.append(current_state)
        path_list_array.append(current_state.state)
        while current_state.previous_state != None:
            current_state = current_state.previous_state
            path_list_objects.append(current_state)
            path_list_array.append(current_state.state)
        path_list_array.reverse()
        path_list_objects.reverse()
        return path_list_array, path_list_objects

    #Function to determine the steps involved to reach the goal
    def get_goal_directions(self):
        b, path_obj_list = self.get_best_path()
        direction_list = []
        for item in path_obj_list:
            if item.direction != "":
                direction_list.append(item.direction)
        return direction_list

    #Function to determine the total number of steps to reach the goal
    def get_total_cost(self):
        _, path_list_obj = self.get_best_path()
        return len(path_list_obj)-1


def main():
    input_file_name = sys.argv[1]
    method_name = sys.argv[2]
    tmax = float(sys.argv[3])
    output_filename = sys.argv[4]
    file_input = []
    with open(input_file_name) as infile:
        lines = infile.readlines()
        for line in lines:
            for n in line.split()[:]:
                file_input.append(int(n))
    rows = file_input[0]
    cols= file_input[1]
    input_state = np.array(file_input[2:2 + rows * cols])
    goal_state = np.array(file_input[2 + rows * cols:])
    hvalue = 0

    if method_name.lower() == 'astarh0':
        havlue = 0
    elif method_name.lower() == 'astarh1':
        havlue = 1
    elif method_name.lower() == 'astarh2':
        havlue = 2
    elif method_name.lower() == 'astarh3':
        havlue = 3


    #print(rows)
    #print(cols)
    #print(input_state)
    #print(goal_state)
    puzzle_helper = puzzle_solver()
    value_sol = 0

    puzzle = puzzle_state(input_state,goal_state,rows,cols,tmax,None, 0, "", hvalue)
    if method_name.lower() == 'bfs':
        #print("you chose BFS algorithm")
        t0 = time.time()
        puzzle_helper.bfs_search(puzzle)
        t1 = time.time()
    elif method_name.lower() == 'dfs':
        #print("you chose DFS algorithm")
        t2 = time.time()
        puzzle_helper.dfs_search(puzzle)
        t3 = time.time()
    elif method_name.lower() == 'astarh0':
        #print("you chose A* algorithm")
        t4 = time.time()
        #puzzle1 = puzzle_state(input_state,goal_state,rows,cols,tmax,None, 0, "", 0)
        puzzle_helper.A_star_search(puzzle)
        t5 = time.time()
    elif method_name.lower() == 'astarh1':
        #print("you chose A* algorithm : Hamming Distance")
        t6 = time.time()
        #puzzle1 = puzzle_state(input_state,goal_state,rows,cols,tmax,None, 0, "", 1)
        puzzle_helper.A_star_search(puzzle)
        t7 = time.time()
    elif method_name.lower() == 'astarh2':
        #print("you chose A* algorithm :Manhattan Distance")
        t8 = time.time()
        #puzzle1 = puzzle_state(input_state,goal_state,rows,cols,tmax,None, 0, "", 2)
        puzzle_helper.A_star_search(puzzle)
        t9 = time.time()
    elif method_name.lower() == 'astarh3':
        #print("you chose A* algorithm :Dominant Function")
        t10 = time.time()
        #puzzle1 = puzzle_state(input_state,goal_state,rows,cols,tmax,None, 0, "", 3)
        puzzle_helper.A_star_search(puzzle)
        t11 = time.time()
    index_val = 0
    index_row = 0
    index_col = 0
    if puzzle.sol == 0:
        with open(output_filename, 'w') as f:
            index_val = 1+np.where(input_state == 0)[0][0]
            index_row = 1+index_val//rows
            index_col = index_val% rows
            if index_col == 0:
                index_col = cols
                index_row-=1
            f.write("%d \t" %index_row)
            f.write("%d \n" % index_col)
            directions = puzzle_helper.get_goal_directions()
            for pos in directions:
                if pos =="DOWN":
                    index_val+=puzzle.col
                    index_row = 1+index_val / rows
                    index_col = index_val % rows
                    if index_col == 0:
                        index_col = cols
                        index_row -= 1
                    f.write("%d \t" % index_row)
                    f.write("%d \n" % index_col)
                elif pos =="UP":
                    index_val-=puzzle.col
                    index_row = 1+index_val / rows
                    index_col = index_val % rows
                    if index_col == 0:
                        index_col = cols
                        index_row -= 1
                    f.write("%d \t" % index_row)
                    f.write("%d \n" % index_col)
                elif pos =="RIGHT":
                    index_val+=1
                    index_row = 1+index_val // rows
                    index_col = index_val % rows
                    if index_col == 0:
                        index_col = cols
                        index_row -= 1
                    f.write("%d \t" % index_row)
                    f.write("%d \n" % index_col)
                elif pos =="LEFT":
                    index_val-=1
                    index_row = 1+index_val / rows
                    index_col = index_val % rows
                    if index_col == 0:
                        index_col = cols
                        index_row -= 1
                    f.write("%d \t" % index_row)
                    f.write("%d \n" % index_col)

    else:
        with open(output_filename, 'w') as f:
            f.write("%s \n" %"Solution impossible within given time")
    #path, n = puzzle_helper.get_best_path()
    #print("path taken to reach goal >> ", path)
    #print("direction taken to reach goal >> ", puzzle_helper.get_goal_directions())
    #print("goal reached >> ", puzzle_helper.solved_puzzle.state)
    #print("total cost to reach goal is ", puzzle_helper.get_total_cost())
    #print("nodes expanded >> ", puzzle_helper.nodes_expanded)
    #print("depth is ", puzzle_helper.solved_puzzle.moves)
    #if method_name.lower() == 'bfs':
    #    print("running time of BFS is >> {} secs".format(t1-t0))
    #elif method_name.lower() == 'dfs':
    #    print("running time of DFS is >> {} secs".format(t3-t2))
    #elif method_name.lower() == 'astarh0':
    #    print("running time of A* is >> {} secs".format(t5-t4))
    #elif method_name.lower() == 'astarh1':
    #    print("running time of A* is >> {} secs".format(t7-t6))
    #elif method_name.lower() == 'astarh2':
    #    print("running time of A* is >> {} secs".format(t9-t8))
    #elif method_name.lower() == 'astarh3':
    #    print("running time of A* is >> {} secs".format(t11-t10))



if __name__ == "__main__":
    main()
