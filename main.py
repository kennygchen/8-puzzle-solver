from heapq import heappush, heappop
from helper import *
from solve import *
import time

default_puzzle = [
                # Trival
                [['1', '2', '3'],
                ['4', '5', '6'],
                ['7', '8', '0']],

                # Easy
                [['1', '2', '0'],
                ['4', '5', '3'],
                ['7', '8', '6']],

                # Oh boy
                [['8', '7', '1'],
                ['6', '0', '2'],
                ['5', '4', '3']],

                #Vary easy
                [['1', '2', '3'],
                ['4', '5', '6'],
                ['7', '0', '8']],

                # Doable
                [['0', '1', '2'],
                ['4', '5', '3'],
                ['7', '8', '6']],

                # Impossible
                [['1', '2', '3'],
                ['4', '5', '6'],
                ['8', '7', '0']]
                ]

def main():
    choice_of_puzzle = 0
    first_row = ""
    second_row = ""
    third_row = ""
    global initial_state
    global choice_of_algorithm

    # Opening and ask for puzzle to solve
    print("862312924 8 Puzzle Solver")
    print("[1] Use default puzzle")
    print("[2] Enter your own puzzle")
    choice_of_puzzle = int(input())
    if(choice_of_puzzle == 1):
        print("\n[1] Trival")
        print_state(default_puzzle[0])
        print("\n[2] Easy")
        print_state(default_puzzle[1])
        print("\n[3] Oh Boy")
        print_state(default_puzzle[2])
        print("\n[4] Very Easy")
        print_state(default_puzzle[3])
        print("\n[5] Doable")
        print_state(default_puzzle[4])
        print("\n[6] IMPOSSIBLE (This puzzle is not solvable)")
        print_state(default_puzzle[5])
        default = int(input("\nChoose a puzzle to solve: "))
        initial_state = default_puzzle[default - 1]

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
  
    # Ask for the choice of algorithm
    print("\nEnter your choice of algorithm:")
    print("[1] Uniform Cost Search")
    print("[2] A* with the Misplaced Tile Heuristic")
    print("[3] A* with the Euclidean Distance Heuristic")
    choice_of_algorithm = int(input())
    if(choice_of_algorithm < 1 or choice_of_algorithm > 3):
        print("Invalid input, using Uniform Cost Search")
        choice_of_algorithm = 1 # set algorithm to Uniform Cost Search
    
    input("\nPress Enter to continue...\n")

    # Initialize the problem and start to solve
    problem = Problem(initial_state)
    first = time.time()
    problem.solve(choice_of_algorithm)
    second = time.time()
    duration = second - first
    print(f"The time it took to solve: {duration} second")
    problem.printSolutionPath()

if __name__ == "__main__":
    main()