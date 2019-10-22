from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue

import Utility
from Puzzle8 import Puzzle8


class Search:

    def __init__(self):
        pass

    def bfs(self, puzzle: Puzzle8):
        queue_bfs = Queue()
        self.help_search(queue_bfs, puzzle)

    def dfs(self, puzzle: Puzzle8):
        stack = LifoQueue()
        self.help_search(stack, puzzle)

    def ucs(self, puzzle: Puzzle8):
        queue_pro = PriorityQueue()

        queue_pro.put((puzzle.get_priority(), puzzle))

        while not queue_pro.empty():
            puzzle_help = queue_pro.get()
            print(puzzle_help)

            if Utility.is_goal(puzzle_help):
                print("GOAL Found ")
                return

            possible_states = puzzle_help.expand()

            for p in possible_states:
                queue_pro.put((puzzle.get_priority(), p))

    def a_star(self, puzzle: Puzzle8):
        queue_pro = PriorityQueue()

        queue_pro.put((puzzle.get_priority() + Utility.get_hurestic1(puzzle), puzzle))

        while not queue_pro.empty():
            puzzle_help = queue_pro.get()
            print(puzzle_help)

            if Utility.is_goal(puzzle_help):
                print("GOAL Found ")
                return

            possible_states = puzzle_help.expand()

            for p in possible_states:
                queue_pro.put((p.get_priority() + Utility.get_hurestic1(p), p))

    def a_star_heuristic_2(self, puzzle: Puzzle8):
        queue_pro = PriorityQueue()

        queue_pro.put((puzzle.get_priority() + Utility.get_hurestic2(puzzle), puzzle))

        while not queue_pro.empty():
            puzzle_help = queue_pro.get()
            print(puzzle_help)

            if Utility.is_goal(puzzle_help):
                print("GOAL Found ")
                return

            possible_states = puzzle_help.expand()

            for p in possible_states:
                queue_pro.put((p.get_priority() + Utility.get_hurestic2(p), p))

    def ids(self):
        pass

    def help_search(self, collect, puzzle):
        # add initial state to queue:
        collect.put(puzzle)

        while not collect.empty():
            puzzle_help = collect.get()
            print(puzzle_help)

            if Utility.is_goal(puzzle_help):
                print("GOAL Found ")
                return

            possible_states = puzzle_help.expand()

            for state in possible_states:
                collect.put(state)
