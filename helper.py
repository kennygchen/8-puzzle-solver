def print_state(state):
    matrix = '\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in state])
    print(matrix)

def find_blank_tile(state):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if(state[i][j] == '0'):
                return [i, j]

def printResult(num_nodes, max_num_in_queue):
    print()
    print("Goal!!")
    print("Number of nodes expanded to solve this problem:")
    print(num_nodes)
    print("The maximum number of nodes in the queue at any one time:")
    print(max_num_in_queue)