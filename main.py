'''
@autor Daniel Martinez Bielostotzky
03-03-2019

Irregular 6x6 Sudoku using A*, the board (state) will be a string like this:
'0-0-0-0-1-0
0-3-0-0-2-0
0-2-0-0-0-0
0-0-0-0-5-0
0-0-0-1-0-0
0-6-5-2-0-0'

where 0 means an empty cell. In order to control the groups inside the board another string is used.
The value of each position represents the group of that cell (from 1 to 6), for the example
above (https://i.imgur.com/ckQ8rn7.png) the string is:

'1-1-1-1-1-2
4-4-3-1-2-2
4-3-3-3-2-2
4-4-3-3-2-6
4-5-6-6-6-6
5-5-5-5-5-6'

Lists will be use to manage operations along the code.
'''
from __future__ import print_function

import sudokutils as utils
from simpleai.search import SearchProblem, astar

initial_board_str = '''0-0-0-0-1-0
0-3-0-0-2-0
0-2-0-0-0-0
0-0-0-0-5-0
0-0-0-1-0-0
0-6-5-2-0-0'''

initial_group_str = '''1-1-1-1-1-2
4-4-3-1-2-2
4-3-3-3-2-2
4-4-3-3-2-6
4-5-6-6-6-6
5-5-5-5-5-6'''

groups_list = utils.string_to_list(initial_group_str)

class IrregularSudokuProblem(SearchProblem):
    def actions(self, state):
        actual_row, actual_col = utils.find_actual_position(state)
        nums_in_rows = utils.possible_numbers_in_row(state, actual_row)
        nums_in_cols = utils.possible_numbers_in_column(state, actual_col)
        nums_in_gr = utils.possible_numbers_in_group(state, initial_group_str, int(groups_list[actual_row][actual_col]))
        
        posibilites = [value for value in nums_in_cols if value in nums_in_rows and value in nums_in_gr]
        return posibilites

    def result(self, state, action):
        actual_row, actual_col = utils.find_actual_position(state)
        state_list = utils.string_to_list(state)
        state_list[actual_row][actual_col] = action

        if not utils.check_if_complete(utils.list_to_string(state_list), initial_group_str):
            next_actual_row, next_actual_col = utils.find_next_actual(state, initial_group_str)
            state_list[next_actual_row][next_actual_col] = 'X'

        return utils.list_to_string(state_list)

    def is_goal(self, state):
        return utils.check_if_complete(state,initial_group_str)

    def cost(self, state, action, state2):
        return 1
    
    def heuristic(self, state):
        # how many empty cells are we to complete?
        h = 0
        rows = utils.string_to_list(state)
        for ir, row in enumerate(rows):
            for ic, element in enumerate(row):
                if element == '0':
                    h = h + 1
        return h 

initial_state_list = utils.string_to_list(initial_board_str)
next_actual_row, next_actual_col = utils.find_next_actual(initial_board_str, initial_group_str)
initial_state_list[next_actual_row][next_actual_col] = 'X'

initial_state = utils.list_to_string(initial_state_list) 

my_problem = IrregularSudokuProblem(initial_state=initial_state)
result = astar(my_problem)
for action, state in result.path():
    print('Insert number', action)
print(state)

# For visuals
'''
from simpleai.search.viewers import WebViewer
my_viewer = WebViewer()
my_problem = IrregularSudokuProblem(initial_state=initial_state)
result = astar(my_problem, viewer=my_viewer)
'''