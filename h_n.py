from math import *

# Calculate the heuristic value based on number of misplaced tiles
def misplacedTiles(current_state, goal_state):
    count = 0
    for i in range(len(current_state)):
        for j in range(len(current_state[0])):
            if ((current_state[i][j]) and current_state[i][j] != goal_state[i][j]):
                count += 1
    return count


# Calculate the heuristic value based on the total euclidean distance
def euclideanDistance(current_state, goal_state):
    total = 0
    # Locate a misplaced tile
    for i in range(len(current_state)):
        for j in range(len(current_state[0])):
           if ((current_state[i][j]) and current_state[i][j] != goal_state[i][j]):
            # Locate the current position
            for x in range(len(current_state)):
                for y in range(len(current_state[0])):
                    if (goal_state[x][y] == current_state[i][j]):
                        # Calculate the euclidean distance sqrt
                        distance = sqrt(pow(i - x, 2) + pow(j - y, 2))
                        total += distance
    return total
