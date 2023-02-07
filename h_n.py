def misplacedTiles(current_state, goal_state):
    count = 0
    for i in range(len(current_state)):
        for j in range(len(current_state[0])):
            if ((current_state[i][j]) and current_state[i][j] != goal_state[i][j]):
                count += 1
    return count - 1

def euclideanDistance(current_state, goal_state):
    total = 0
    for i in range(len(current_state)):
        for j in range(len(current_state[0])):
           pass 
    return total
