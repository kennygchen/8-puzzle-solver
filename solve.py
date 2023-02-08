from queue import PriorityQueue
from h_n import euclideanDistance, misplacedTiles
from helper import *

class Node: 

    def __init__(self, state, g_n = 0):
        self.state = state
        self.parent = None
        self.g_n = g_n

    def getPossibleNodes(self):
        possible_nodes = []
        child_g_n = self.g_n + 1
        blank_row, blank_col = find_blank_tile(self.state)
  
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

    def solve(self, choice_of_algorithm):
        self.choice_of_algorithm = choice_of_algorithm
        if choice_of_algorithm == 1:
            self.uniformCost()
        elif choice_of_algorithm == 2:
            self.aStar(misplacedTiles)
        elif choice_of_algorithm == 3:
            self.aStar(euclideanDistance)

    def uniformCost(self):
        current_state = Node(self.initial_state)
        depth = 1
        num_nodes = 1
        print("Expanding state:")
        print_state(current_state.state)
        print()
        
        node = (current_state.g_n, depth, current_state)
        self.frontier.put(node)

        while not self.frontier.empty():
            self.max_num_in_queue = max(self.max_num_in_queue, self.frontier.qsize()) 
            
            poped_node = self.frontier.get()
            current_state_f_n = poped_node[0]
            current_state = poped_node[2]
            current_state_h_n = current_state_f_n - current_state.g_n
            if(current_state.state == self.goal_state):
                printResult(num_nodes, self.max_num_in_queue)
                self.getSolutionPath(current_state)
                return
            self.explored_node.append(current_state.state)
                
            print("The best state to expand with g(n) = {} is:". format(current_state.g_n))
            print_state(current_state.state)
            print("Expanding this node...")

            possible_nodes = current_state.getPossibleNodes()


            

    def aStar(self, h_n):
        pass