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
def printResult(num_nodes, max_num_in_queue, depth):
    print()
    print("Goal!!")
    print("Solution found at depth: {}".format(depth))
    print("Number of nodes expanded to solve this problem: {}".format(num_nodes))
    print("The maximum number of nodes in the queue at any one time: {}".format(max_num_in_queue))