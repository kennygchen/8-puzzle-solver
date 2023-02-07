import numpy as np
from queue import PriorityQueue
from heapq import heappush, heappop

n = 3

initial_state = [[1, 2, 0],
                [4, 5, 3],
                [7, 8, 6]]

goal_state = [[1, 2, 3],
                [6, 5, 4],
                [7, 8, 0]]

explored_set = []

class priorityQueue:
    
    def __init__(self):
        self.heap = []

    def push(self, key):
        heappush(self.heap, key)

    def pop(self):
        return heappop(self.heap)

    def empty(self):
        if not self.heap:
            return True
        else:
            return False

class Node: 

    def __init__(self, state, parent, blank_tile_pos, heuristic, depth):
        self.state = state
        self.parent = parent
        self.blank_tile_pos = blank_tile_pos
        self.heuristic = heuristic
        self.depth = depth
        self.cost = self.depth + self.heuristic

    def __lt__(self, next):
        return self.cost < next.cost



def calculate_heuristic(state):
    count = 0
    if(choice_of_algorithm == 1):    # Uniform Cost
        return count
    elif(choice_of_algorithm == 2):  # Misplaced Tile Heuristic
        for i in range(n):
            for j in range(n):
                if ((state[i][j]) and state[i][j] != goal_state[i][j]):
                    count +=1
        return count
    elif(choice_of_algorithm == 3):  # Euclidean Distance Heuristic
        pass



def solve():
    blank_tile_pos = find_blank_tile(initial_state)
    heuristic = calculate_heuristic(initial_state)
    p = Node(initial_state, None, blank_tile_pos, heuristic, 0)

def main():
    choice_of_puzzle = 0
    first_row = ""
    second_row = ""
    third_row = ""
    global initial_state
    global choice_of_algorithm    

    print("862312924 8 Puzzle Solver")
    print("[1] Use default puzzle")
    print("[2] Enter your own puzzle")
    choice_of_puzzle = int(input())
    if(choice_of_puzzle == 1):
        pass
    elif(choice_of_puzzle == 2):
        first_row = input("\nEnter your puzzle, use a zero to represnet the blank\nEnter the first row, use space between numbers\n")
        second_row = input("\nEnter the second row, use space between numbers\n")
        third_row = input("\nEnter the third row, use space between numbers\n")
        initial_state[0] = first_row.split(" ")
        initial_state[1] = second_row.split(" ")
        initial_state[2] = third_row.split(" ")
    else:
        print("Invalid input, using default puzzle")

    print("\nThe puzzle:")
    print_state(initial_state)
  
    print("\nEnter your choice of algorithm:")
    print("[1] Uniform Cost Search")
    print("[2] A* with the Misplaced Tile Heuristic")
    print("[3] A* with the Euclidean Distance Heuristic")
    choice_of_algorithm = int(input())
    if(choice_of_algorithm < 1 or choice_of_algorithm > 3):
        print("Invalid input, using Uniform Cost Search")
        choice_of_algorithm = 1 # set algorithm to Uniform Cost Search
    
    input("\nPress Enter to continue...")

    solve()

if __name__ == "__main__":
    main()