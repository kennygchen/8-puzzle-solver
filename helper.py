import sys
from h_n import *

# Print input state into matrix format
def print_state(state):
    matrix = '\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in state])
    print(matrix)

# Calculate the postion of blank tile and return as [row, col]
def find_blank_tile(state):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if(state[i][j] == '0'):
                return [i, j]

# Print the result with goal message
def printResult(num_nodes, max_num_in_queue, depth, found_goal):
    if(found_goal):
        print()
        print("Goal!!")
        print(f"Solution found at depth: {depth}")
        print(f"Number of nodes expanded to solve this problem: {num_nodes}")
        print(f"The maximum number of nodes in the queue at any one time: {max_num_in_queue}")
    else:
        print()
        print("No solution found!!")
        print(f"Search ends at depth: {depth}")
        print(f"Number of nodes expanded for this problem: {num_nodes}")
        print(f"The maximum number of nodes in the queue at any one time: {max_num_in_queue}")