from queue import PriorityQueue
from h_n import euclideanDistance, misplacedTiles

class Node: 

    def __init__(self, state, g_n = 0):
        self.state = state
        self.parent = None
        self.g_n = g_n
  
class Problem:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.frontier = PriorityQueue()
        self.explored_node = set()
        self.solution_path = []
        self.goal_state = [ ['1','2','3'],
                            ['4','5','6'],
                            ['7','8','0']]

    def solve(self, choice_of_algorithm):
        self.type = choice_of_algorithm
        if type == 1:
            self.uniformCost()
        elif type == 2:
            self.aStar(misplacedTiles)
        elif type == 3:
            self.aStar(euclideanDistance)

    def uniformCost(self):
        pass

    def aStar(self, h_n):
        pass