import sys
import random
from pprint import pprint
import time
import math
import copy


# import numpy as np

#Setup Initial Board
def initial_board_print(row, col):
    ##Creating List for each position in the row - E,Q,K
    Element = ['E'*col] * col
    #Dictionary for each individual row
    Space_dict = {i+1: Element[i] for i in range(0, len(Element), 1)}
    return Space_dict



#Generate Random Positions of Queens and Knoghts
def random_generator(row, col, queens, knights):
    # print(row*col)
    # print(queens+knights)
    random_list = []
    if knights>0:
        random_list = random.sample(range(1, (row * col) + 1), queens + knights)
        return random_list
    elif(knights==0):
        for i in range(0,queens):
            index = random.randint(1, col)
            random_list.append((i*row)+index)
        return random_list


#Get Co-ordinates 
def get_coordinates(value, row, col):
    value_row = value // row
    value_col = value % row

    if value_row < row and value_col > 0:
        return value_row + 1, value_col
    elif value % row == 0 and value_col == 0:
        return value_row, col
    elif value % row == 0 and value_col > 0:
        return value_row, value_col
    elif value_row < row and value_col == 0:
        return value_row + 1, col

#Define Positions of Queens
def perm_position_Q1(Space_dict, row, col, queens, knights, random_list):
    final_list = []
    perm_Queens = queens
    # perm_Knights = knights
    position_list_Q = []
    position_list_K = []
    if (len(random_list) == 0):
        random_list = random_generator(row, col, queens, knights)
    Space_dict, position_list_K = perm_position_K1(Space_dict, row, col, queens, knights, random_list)

    # print("Random list:")
    # print(random_list)

    for i in range(queens):
        random_number = random_list[i]
        rand_row = random_number // row
        rand_col = random_number % row
        # print(random_number, rand_row, rand_col)

        #
        if (perm_Queens) > 0 and rand_row < row and rand_col > 0:
            if Space_dict[rand_row + 1][(rand_col - 1)] == "E":
                # place a queen
                # print("A")
                Space_dict[rand_row + 1] = Space_dict[rand_row + 1][:rand_col - 1] + 'Q' + Space_dict[rand_row + 1][rand_col:]

                perm_Queens -= 1
                position_list_Q.append(random_number)
                # print(Space_dict)

        # mth row and nth column placement for queen
        elif (perm_Queens) > 0 and random_number % row == 0 and rand_col == 0:
            if Space_dict[rand_row][(col - 1)] == "E":
                # print("B")
                Space_dict[rand_row] = Space_dict[rand_row][:col - 1] + 'Q'
                perm_Queens -= 1
                position_list_Q.append(random_number)
                # print(Space_dict)


        elif (perm_Queens) > 0 and random_number % row == 0 and rand_col > 0:
            if Space_dict[rand_row][(rand_col - 1)] == "E":
                # print("C")
                Space_dict[rand_row] = Space_dict[rand_row][:rand_col - 1] + 'Q' + Space_dict[rand_row][rand_col:]
                perm_Queens -= 1
                position_list_Q.append(random_number)
                # print(Space_dict)

        elif (perm_Queens) > 0 and rand_row < row and rand_col == 0:
            if Space_dict[rand_row + 1][(col - 1)] == "E":
                # print("D")
                # place a queen
                Space_dict[rand_row + 1] = Space_dict[rand_row + 1][:col - 1] + 'Q'
                perm_Queens -= 1
                position_list_Q.append(random_number)
                # print(Space_dict)

        else:
            i -= 1
            # print(Space_dict)
    initial_list = position_list_Q+position_list_K
    return Space_dict, initial_list

#Define Positions of Knights
def perm_position_K1(Space_dict, row, col, queens, knights, random_list):
    # perm_Queens = queens
    perm_Knights = knights
    # position_list_Q = []
    position_list_K = []
    # random_list = random_generator(row, col, queens, knights)
    final_list = []

    for i in range(queens, len(random_list)):
        random_number = random_list[i]
        rand_row = random_number // row
        rand_col = random_number % row
        # print(random_number, rand_row, rand_col)

        if (perm_Knights) > 0 and rand_row < row and rand_col > 0:
            if Space_dict[rand_row + 1][(rand_col - 1)] == "E":
                # place a Knight
                # print("A")
                Space_dict[rand_row + 1] = Space_dict[rand_row + 1][:rand_col - 1] + 'K' + Space_dict[rand_row + 1][
                                                                                           rand_col:]
                perm_Knights -= 1
                position_list_K.append(random_number)
                # print(Space_dict)


        elif (perm_Knights) > 0 and random_number % row == 0 and rand_col == 0:
            if Space_dict[rand_row][(col - 1)] == "E":
                # print("B")
                Space_dict[rand_row] = Space_dict[rand_row][:col - 1] + 'K'
                perm_Knights -= 1
                position_list_K.append(random_number)
                # print(Space_dict)


        elif (perm_Knights) > 0 and random_number % row == 0 and rand_col > 0:
            if Space_dict[rand_row][(rand_col - 1)] == "E":
                # print("C")
                Space_dict[rand_row] = Space_dict[rand_row][:rand_col - 1] + 'K' + Space_dict[rand_row][rand_col:]
                perm_Knights -= 1
                position_list_K.append(random_number)
                # print(Space_dict)


        elif (perm_Knights) > 0 and rand_row < row and rand_col == 0:
            if Space_dict[rand_row + 1][(col - 1)] == "E":
                # print("D")
                # place a Knight
                Space_dict[rand_row + 1] = Space_dict[rand_row + 1][:col - 1] + 'K'
                perm_Knights -= 1
                position_list_K.append(random_number)
                # print(Space_dict)

        else:
            i -= 1
            # print(i)
            # print(Space_dict)
    # return Space_dict, position_list_Q, position_list_K
    return Space_dict, position_list_K

#Define Collision function; No queen can attack another queen & No knight can attack another knight or queen 
def collisions_1(position_list_Q1, position_list_K1, row, col):
    all_position = position_list_Q1 + position_list_K1
    # all_position = sorted(all_position)
    totol_collitiion = 0
    temp_rx = 0
    temp_lx = 0
    temp_rxv = 0
    temp_lxv = 0
    temp_ry = 0
    temp_ly = 0
    temp_ryv = 0
    temp_lyv = 0
    temp_l1dx = 0
    temp_l1dy = 0
    temp_l1v = 0
    temp_l2dx = 0
    temp_l2dy = 0
    temp_l2v = 0
    temp_r1dx = 0
    temp_r1dy = 0
    temp_r1v = 0
    temp_r2dx = 0
    temp_r2dy = 0
    temp_r2v = 0

    for piece_1 in all_position:
        for piece_2 in all_position:
            piece_1_x = 0
            piece_1_y = 0
            piece_2_x = 0
            piece_2_y = 0
            piece_1_x, piece_1_y = get_coordinates(piece_1, row, col)
            piece_2_x, piece_2_y = get_coordinates(piece_2, row, col)
            if piece_1 == piece_2:
                continue

            # Row collisions
            elif (piece_1 in position_list_Q1):
                if (piece_1_x == piece_2_x):
                    if (piece_1_y > piece_2_y):
                        if (temp_lyv == 0):
                            temp_ly = piece_2_y
                            if piece_2 in position_list_Q1:
                                temp_lyv = 1
                            elif piece_2 in position_list_K1:
                                temp_lyv = 2
                        elif (temp_ly < piece_2_y):
                            temp_ly = piece_2_y
                            if piece_2 in position_list_Q1:
                                temp_lyv = 1
                            elif piece_2 in position_list_K1:
                                temp_lyv = 2
                    elif (piece_1_y < piece_2_y):
                        if (temp_ryv == 0):
                            temp_ry = piece_2_y
                            if piece_2 in position_list_Q1:
                                temp_ryv = 1
                            elif piece_2 in position_list_K1:
                                temp_ryv = 2
                        elif (temp_ry > piece_2_y):
                            temp_ry = piece_2_y
                            if piece_2 in position_list_Q1:
                                temp_ryv = 1
                            elif piece_2 in position_list_K1:
                                temp_ryv = 2

                # Column Collisions
                elif (piece_1_y == piece_2_y):
                    if (piece_1_x > piece_2_x):
                        if (temp_lxv == 0):
                            temp_lx = piece_2_x
                            if piece_2 in position_list_Q1:
                                temp_lxv = 1
                            elif piece_2 in position_list_K1:
                                temp_lxv = 2
                        elif (temp_lx < piece_2_x):
                            temp_lx = piece_2_x
                            if piece_2 in position_list_Q1:
                                temp_lxv = 1
                            elif piece_2 in position_list_K1:
                                temp_lxv = 2
                    elif (piece_1_x < piece_2_x):
                        if (temp_rxv == 0):
                            temp_rx = piece_2_x
                            if piece_2 in position_list_Q1:
                                temp_rxv = 1
                            elif piece_2 in position_list_K1:
                                temp_rxv = 2
                        elif (temp_rx > piece_2_x):
                            temp_rx = piece_2_x
                            if piece_2 in position_list_Q1:
                                temp_rxv = 1
                            elif piece_2 in position_list_K1:
                                temp_rxv = 2

                # Diagonal Collisions
                elif (abs(piece_1_x - piece_2_x)) == (abs(piece_1_y - piece_2_y)) or (piece_1_x + piece_1_y) == (
                        piece_2_x + piece_2_y):
                    if (piece_1_x < piece_2_x):
                        if (piece_1_y < piece_2_y):
                            if (temp_r1v == 0):
                                temp_r1dx = piece_2_x
                                temp_r1dy = piece_2_y
                                if piece_2 in position_list_Q1:
                                    temp_r1v = 1
                                elif piece_2 in position_list_K1:
                                    temp_r1v = 2
                            elif (temp_r1dx > piece_2_x & temp_r1dy > piece_2_y):
                                temp_r1dx = piece_2_x
                                temp_r1dy = piece_2_y
                                if piece_2 in position_list_Q1:
                                    temp_r1v = 1
                                elif piece_2 in position_list_K1:
                                    temp_r1v = 2
                        elif (piece_1_y > piece_2_y):
                            if (temp_r2v == 0):
                                temp_r2dx = piece_2_x
                                temp_r2dy = piece_2_y
                                if piece_2 in position_list_Q1:
                                    temp_r2v = 1
                                elif piece_2 in position_list_K1:
                                    temp_r2v = 2
                            elif (temp_r2dx > piece_2_x & temp_r2dy < piece_2_y):
                                temp_r2dx = piece_2_x
                                temp_r2dy = piece_2_y
                                if piece_2 in position_list_Q1:
                                    temp_r2v = 1
                                elif piece_2 in position_list_K1:
                                    temp_r2v = 2
                    elif (piece_1_x > piece_2_x):
                        if (piece_1_y < piece_2_y):
                            if (temp_l1v == 0):
                                temp_l1dx = piece_2_x
                                temp_l1dy = piece_2_y
                                if piece_2 in position_list_Q1:
                                    temp_l1v = 1
                                elif piece_2 in position_list_K1:
                                    temp_l1v = 2
                            elif (temp_l1dx < piece_2_x & temp_l1dy > piece_2_y):
                                temp_l1dx = piece_2_x
                                temp_l1dy = piece_2_y
                                if piece_2 in position_list_Q1:
                                    temp_l1v = 1
                                elif piece_2 in position_list_K1:
                                    temp_l1v = 2
                        elif (piece_1_y > piece_2_y):
                            if (temp_l2v == 0):
                                temp_l2dx = piece_2_x
                                temp_l2dy = piece_2_y
                                if piece_2 in position_list_Q1:
                                    temp_l2v = 1
                                elif piece_2 in position_list_K1:
                                    temp_l2v = 2
                            elif (temp_l2dx < piece_2_x & temp_l2dy < piece_2_y):
                                temp_l2dx = piece_2_x
                                temp_l2dy = piece_2_y
                                if piece_2 in position_list_Q1:
                                    temp_l2v = 1
                                elif piece_2 in position_list_K1:
                                    temp_l2v = 2


            elif (piece_1 in position_list_K1):
                if (piece_1_x + 1 == piece_2_x):
                    if (piece_1_y + 2 == piece_2_y):
                        totol_collitiion += 1
                    elif (piece_1_y - 2 == piece_2_y):
                        totol_collitiion += 1
                elif (piece_1_x - 1 == piece_2_x):
                    if (piece_1_y + 2 == piece_2_y):
                        totol_collitiion += 1
                    elif (piece_1_y - 2 == piece_2_y):
                        totol_collitiion += 1
                elif (piece_1_x + 2 == piece_2_x):
                    if (piece_1_y + 1 == piece_2_y):
                        totol_collitiion += 1
                    elif (piece_1_y - 1 == piece_2_y):
                        totol_collitiion += 1
                elif (piece_1_x - 2 == piece_2_x):
                    if (piece_1_y + 1 == piece_2_y):
                        totol_collitiion += 1
                    elif (piece_1_y - 1 == piece_2_y):
                        totol_collitiion += 1

        if temp_r1v == 1:
            totol_collitiion += 1

        if temp_r2v == 1:
            totol_collitiion += 1

        if temp_l1v == 1:
            totol_collitiion += 1

        if temp_l2v == 1:
            totol_collitiion += 1

        if temp_rxv == 1:
            totol_collitiion += 1

        if temp_ryv == 1:
            totol_collitiion += 1

        if temp_lxv == 1:
            totol_collitiion += 1

        if temp_lyv == 1:
            totol_collitiion += 1

        temp_rx = 0
        temp_lx = 0
        temp_rxv = 0
        temp_lxv = 0
        temp_ry = 0
        temp_ly = 0
        temp_ryv = 0
        temp_lyv = 0
        temp_l1dx = 0
        temp_l1dy = 0
        temp_l1v = 0
        temp_l2dx = 0
        temp_l2dy = 0
        temp_l2v = 0
        temp_r1dx = 0
        temp_r1dy = 0
        temp_r1v = 0
        temp_r2dx = 0
        temp_r2dy = 0
        temp_r2v = 0
    return totol_collitiion

#Generaters Neighbour positions of current state
def generate_neighbours1(initial_list, row, col,current_conflicts):
    current_state = initial_list
    neighbour_list = []
    #index = random.randint(0, len(current_state) - 1)
    total = row * col
    neighbour = list(range(1, total + 1))
    #print(neighbour)
    new_state = initial_list
    index = random.randint(0, len(current_state) - 1)
    index_x,index_y = get_coordinates(new_state[index],row,col)
    for i in range(len(neighbour)-1):
        i_x,i_y = get_coordinates(neighbour[i],row,col)
        equal_list = []
        equal_conf = -1
        if neighbour[i] in current_state:
            continue
        elif(knights == 0):
            if i_x == index_x or i_y == index_y:
                # print(i)
                # print(neighbour[i])
                new_state[index] = neighbour[i]
                # print(new_state)
                equal_list = []
                equal_conf = -1
                conflict = collisions_1(new_state[:queens], new_state[queens:], row, col)
                # print(conflict,current_conflicts)

                if (conflict == 0):
                    return new_state, conflict
                elif (conflict < current_conflicts):
                    current_state = new_state.copy()
                    # print("Here")
                    # print(current_state, current_conflicts)
                    # print(current_conflicts)
                    current_conflicts = conflict
                elif conflict == current_conflicts:
                    equal_list.append(new_state.copy())
                    equal_conf = conflict
                else:
                    continue

            if equal_conf == current_conflicts:
                if len(equal_list) == 1:
                    current_state = equal_list[0].copy()
                else:
                    temp_4 = random.randint(0, len(equal_list) - 1)
                    current_state = equal_list[temp_4].copy()

        else:
            #print(i)
            #print(neighbour[i])
            new_state[index] = neighbour[i]
            #print(new_state)

            conflict = collisions_1(new_state[:queens], new_state[queens:], row, col)
            #print(conflict,current_conflicts)

            if (conflict == 0):
                return new_state,conflict
            elif (conflict < current_conflicts):
                current_state = new_state
                #print("Here")
                #print(current_state, current_conflicts)
                #print(current_conflicts)
                current_conflicts = conflict
            elif conflict == current_conflicts:
                equal_list.append(new_state.copy())
                equal_conf = conflict
            else:
                continue

        if equal_conf == current_conflicts:
            if len(equal_list) == 1:
                current_state = equal_list[0].copy()
            else:
                temp_4 = random.randint(0,len(equal_list)-1)
                current_state = equal_list[temp_4].copy()





    #print(current_state,current_conflicts)
    return current_state,current_conflicts

#Implementation of Hill climbing Algorithm
def hill_climb_1(initial_board,row,col,queens,knights):
    current_state = initial_board
    current_conflicts = collisions_1(current_state[:queens],current_state[queens:], row, col)
    max_iterations = 20000
    counter = 25
    best = False
    for i in range(max_iterations):
        counter-=1
        current_conflicts = collisions_1(current_state[:queens], current_state[queens:], row, col)
        if (current_conflicts == 0):
            print(current_state,current_conflicts)
            return current_state,current_conflicts
        next_state,conflicts = generate_neighbours1(current_state,row,col,current_conflicts)
        #next_state = next_state_1.copy()
        #print(current_state,next_state)
        if (current_state == next_state or counter == 0):
            #print("########")
            next_state = random_generator(row, col, queens, knights)
            counter = 25


        if(conflicts == 0):

            #print(next_state,conflicts)
            return current_state,conflicts

        current_state = next_state.copy()

#Implementation of Simulated Annealing Algorithm
def simulated_annealing(initial_board,row,col,queens,knights,TEMPERATURE):
    current_state = initial_board

    #current_state = copy.deepcopy(initial_state)
    current_conflicts = collisions_1(current_state[:queens], current_state[queens:], row, col)
    #current_conflicts = copy.deepcopy(current_conf)

    t = 1000000
    sch = 0.99999
    total = row*col


    while t > 0.01:
        current_state_1 = current_state
        t *= sch
        neighbour = list(range(1, total + 1))
        # print(neighbour)
        index = random.randint(0, len(current_state) - 1)
        index_1 = random.randint(0, len(neighbour) - 1)
        if neighbour[index_1] not in current_state:
            current_state_1[index] = neighbour[index_1]
        else:
            continue

        # print(current_state)

        conflict = collisions_1(current_state_1[:queens], current_state_1[queens:], row, col)
        #conflict = copy.deepcopy(conf)

        if (current_conflicts == 0 or conflict==0):
            return current_state,current_conflicts

        delta = conflict - current_conflicts
        if delta<0:
            current_state = current_state_1
            #current_state = copy.deepcopy(temp)
            #print("Here")
             #print(current_conflicts)
            current_conflicts = conflict
            #current_conflicts = copy.deepcopy(temp_1)
        else:
            delta = -delta
            #print(delta)
            p = 1/math.exp(delta/t)
            #print(p)
            #print(conflict,current_conflicts)
            if(p<0.5):
                current_state = current_state_1
                #current_state = copy.deepcopy(temp)
                # print("Here")
                # print(current_conflicts)
                current_conflicts = conflict
                #current_conflicts = copy.deepcopy(temp_1)
        if (current_conflicts == 0 or conflict==0):
            return current_state,current_conflicts


        #t = TEMPERATURE

    if (current_conflicts == 0):
        #print("Result")
        #print(current_conflicts)
        #print(final_list)
        return current_state, current_conflicts

#Main Fuction to collected arguments and call the requested algorithm
if __name__ == "__main__":
    row = int(sys.argv[1])
    col = int(sys.argv[2])
    queens = int(sys.argv[3])
    knights = int(sys.argv[4])
    tmax = int(sys.argv[5])
    filename = sys.argv[6]
    methodName = sys.argv[7]
    start_time = time.time()
# Arguments passed


Space_dict = initial_board_print(row,col)
initial_list = random_generator(row,col,queens,knights).copy()
print(initial_list)

TEMPERATURE = 10000

if (methodName.lower() =='hc'):
    final_state,collision = hill_climb_1(initial_list,row,col,queens,knights)
    #print("Completed")
    #print(final_state)
    Space_dict = initial_board_print(row,col)
    Output_dict,final_list = perm_position_Q1(Space_dict,row,col,queens,knights,final_state)
    #for k in Output_dict:
    #    print(Output_dict[k])
    #print(collision)
    end_time = time.time()
    with open(filename, 'w') as f:
        for k in Output_dict:
            f.write("%s\n" % Output_dict[k])

        f.write("%s\n" %collision)
    #print(end_time-start_time)

if (methodName.lower() =='sa'):
    final_state,collision = simulated_annealing(initial_list,row,col,queens,knights,TEMPERATURE)
    #print("Completed")
    #print(final_state)
    Space_dict = initial_board_print(row, col)
    Output_dict, final_list = perm_position_Q1(Space_dict, row, col, queens, knights, final_state)
    #for k in Output_dict:
    #    print(Output_dict[k])
    #print(collision)
    end_time = time.time()
    #print(end_time - start_time)
    with open(filename, 'w') as f:
        for k in Output_dict:
            f.write("%s\n" % Output_dict[k])

        f.write('0')
