from queue import PriorityQueue
from h_n import euclideanDistance, misplacedTiles
from helper import *
from copy import *

class Node: 

    def __init__(self, state, g_n = 0):
        self.state = state
        self.parent = None
        self.g_n = g_n

    def getChild(self):
        possible_childs = []
        child_g_n = self.g_n + 1
        blank_row, blank_col = find_blank_tile(self.state)

        # check if the blank tile can move up
        if blank_row > 0:
            child = deepcopy(self.state)
            
            # swap the blank tile with the tile above it
            child[blank_row][blank_col] = self.state[blank_row - 1][blank_col]
            child[blank_row - 1][blank_col] = self.state[blank_row][blank_col]

            node = Node(child, child_g_n)
            possible_childs.append(node)

        # check if the blank tile can move down    
        if blank_row < len(self.state) - 1:
            child = deepcopy(self.state)
                      
            # swap the blank tile with the tile below it
            child[blank_row][blank_col] = self.state[blank_row + 1][blank_col]
            child[blank_row + 1][blank_col] = self.state[blank_row][blank_col]

            node = Node(child, child_g_n)
            possible_childs.append(node)


        # check if the blank tile can move left
        if blank_col > 0:
            child = deepcopy(self.state)
    
            # swap the blank tile with the tile left it
            child[blank_row][blank_col] = self.state[blank_row][blank_col - 1]
            child[blank_row][blank_col - 1] = self.state[blank_row][blank_col]

            node = Node(child, child_g_n)
            possible_childs.append(node)


        # check if the blank tile can move right    
        if blank_col < len(self.state[0]) - 1:
            child = deepcopy(self.state)
            
            # swap the blank tile with the tile right it
            child[blank_row][blank_col] = self.state[blank_row][blank_col + 1]
            child[blank_row][blank_col + 1] = self.state[blank_row][blank_col]

            node = Node(child, child_g_n)
            possible_childs.append(node)

        return possible_childs
  
class Problem:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.frontier = PriorityQueue()
        self.explored_node = []
        self.solution_path = []
        self.nodes_expand = 0
        self.max_num_in_queue = 0
        self.goal_state = [ ['1','2','3'],
                            ['4','5','6'],
                            ['7','8','0']]

    def getSolutionPath(self, node):
        nodes = []
        while node.parent != None:
            nodes.append(node.state)
            node = node.parent
        nodes = nodes[::-1]
        self.solution_path = nodes

    def printSolutionPath(self):
        print("\nThe solution path:")
        print_state(self.initial_state)
        print()
        for state in self.solution_path:
            print_state(state)
            print()

    def solve(self, choice_of_algorithm):
        self.choice_of_algorithm = choice_of_algorithm
        if choice_of_algorithm == 1:
            print("Using Uniform Cost Search")
            self.uniformCost()
        elif choice_of_algorithm == 2:
            print("Using A* with Misplaced Tiles Deuristic")
            self.aStar(misplacedTiles)
        elif choice_of_algorithm == 3:
            print("Using A* with Euclidean Distance Deuristic")
            self.aStar(euclideanDistance)
        elif choice_of_algorithm == 4:
            print("debug mode:")
            distance = euclideanDistance(self.initial_state, self.goal_state)
            print(distance)

    def uniformCost(self):
        current_state = Node(self.initial_state)
        depth = 1
        num_nodes = 1
        print("Expanding state:")
        print_state(current_state.state)
        print()
        
        if(current_state.state == self.goal_state):
            printResult(num_nodes, self.max_num_in_queue)
            self.getSolutionPath(current_state)
            return

        node = (current_state.g_n, depth, current_state)
        self.frontier.put(node)
        self.explored_node.append(node)

        while not self.frontier.empty():
            self.max_num_in_queue = max(self.max_num_in_queue, self.frontier.qsize()) 
            poped_node = self.frontier.get()
            current_state = poped_node[2]
            self.explored_node.append(current_state.state)
            if(current_state.state == self.goal_state):
                printResult(num_nodes, self.max_num_in_queue)
                self.getSolutionPath(current_state)
                return
                
            print("\nThe best state to expand with g(n) = {} is:". format(current_state.g_n))
            print_state(current_state.state)
            print("Expanding this node...")

            childs = current_state.getChild()

            for child in childs:
                depth += 1
                if child not in self.explored_node:
                    node = (child.g_n, depth, child)
                    self.frontier.put(node)
                    child.parent = current_state
                else:
                    print("VISITED!!!!!!!!!!!")

            num_nodes += 1         

    def aStar(self, h_n):
        pass
    