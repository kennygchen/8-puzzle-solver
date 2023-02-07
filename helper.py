def print_state(state):
    matrix = '\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in state])
    print(matrix)

def find_blank_tile(state):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if(state[i][j] == 0):
                return [i, j]