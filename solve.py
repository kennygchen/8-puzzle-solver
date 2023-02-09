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
        self.max_num_in_queue = 0
        self.goal_state = [ ['1','2','3'],
                            ['4','5','6'],
                            ['7','8','0']]

    # Create a the path from solution to initial state
    def getSolutionPath(self, node):
        nodes = []
        while node.parent != None:
            nodes.append(node.state)
            node = node.parent
        nodes = nodes[::-1]
        self.solution_path = nodes

    # Print the path from solution to initial state
    def printSolutionPath(self):
        print("\nThe solution path:")
        print_state(self.initial_state)
        print()
        for state in self.solution_path:
            print_state(state)
            print()

    # Solve the problem based on the choice of algorithm from user
    def solve(self, choice_of_algorithm):
        self.choice_of_algorithm = choice_of_algorithm
        if choice_of_algorithm == 1:
            print("Using Uniform Cost Search")
            self.graphSearch(lambda *args, **kwargs: 0)     # Uniform Cost is just heuristic hard coded to 0
        elif choice_of_algorithm == 2:
            print("Using A* with Misplaced Tiles Heuristic")
            self.graphSearch(misplacedTiles)
        elif choice_of_algorithm == 3:
            print("Using A* with Euclidean Distance Heuristic")
            self.graphSearch(euclideanDistance)

    # Implementation of Graph Search
    def graphSearch(self, h_function):
        # Creates a Node object from initial state
        current_state = Node(self.initial_state)
        depth = 1
        num_nodes = 1
        print("Expanding state:")
        print_state(current_state.state)
        print()

        # First check if the initial is the goal state
        if(current_state.state == self.goal_state):
            printResult(num_nodes, self.max_num_in_queue, current_state.g_n)
            self.getSolutionPath(current_state)
            return

        # Calculate the f value based on the choice of h function + g_n
        f_n = h_function(current_state.state, self.goal_state) + current_state.g_n
    
        # Put the initial state into the frontier and the list of explored node
        node = (f_n, depth, current_state)
        self.frontier.put(node)
        self.explored_node.append(node)

        while not self.frontier.empty():
            # Check max number of node in the frontier
            self.max_num_in_queue = max(self.max_num_in_queue, self.frontier.qsize()) 
            poped_node = self.frontier.get()        # Pop a node from frontier
            current_state = poped_node[2]           # Capture the poped node
            current_f_n = poped_node[0]
            current_h_n = current_f_n - current_state.g_n       # Get the poped node's h value
            self.explored_node.append(current_state.state)      # Add to explored node list
            
            # Poped node goal check
            if(current_state.state == self.goal_state):
                printResult(num_nodes, self.max_num_in_queue, current_state.g_n)
                self.getSolutionPath(current_state)
                return
                
            print("\nThe best state to expand with g(n) = {} and h(n) = {} is:". format(current_state.g_n, current_h_n))
            print_state(current_state.state)
            print("Expanding this node...")

            # Get possible move
            childs = current_state.getChild()

            for child in childs:
                depth += 1

                # If child is not explored, put it in the frontier and assign its parent
                if child.state not in self.explored_node:
                    # Calculate the child node f value
                    f_n = h_function(child.state, self.goal_state) + child.g_n
                    node = (f_n, depth, child)
                    self.frontier.put(node)
                    child.parent = current_state
                else:
                    print("visited!!!")

            num_nodes += 1
    