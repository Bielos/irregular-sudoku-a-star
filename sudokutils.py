def string_to_list(string_):
    '''Convert puzzle string to list.
       Returns a list'''
    return [row.split('-') for row in string_.split('\n')]

def list_to_string(list_):
    '''Convert puzzle list to string.
       Returns a string'''
    return '\n'.join(['-'.join(row) for row in list_])

def find_actual_position(board):
    '''Find the location of the actual position piece in the puzzle.
       Returns a tuple: row, column'''
    rows = string_to_list(board)
    for ir, row in enumerate(rows):
        for ic, element in enumerate(row):
            if element == 'X':
                return ir, ic

def possible_numbers_in_row(board, row_):
    '''Find all valid numbers inside a row.
       Returns a list of strings''' 
    rows = string_to_list(board)
    elements = []
    for ir, row in enumerate(rows):
        for ic, element in enumerate(row):
            if ir == row_:
                elements.append(element)    
    result = []
    for number in range(1,7):
        if str(number) not in elements:
            result.append(str(number))
    return result

def possible_numbers_in_column(board, column):
    '''Find all valid numbers inside a column.
       Returns a list of strings''' 
    rows = string_to_list(board)
    elements = []
    for ir, row in enumerate(rows):
        for ic, element in enumerate(row):
            if ic == column:
                elements.append(element)
    result = []
    for number in range(1,7):
        if str(number) not in elements:
            result.append(str(number))
    return result

def possible_numbers_in_group(board, groups, group):
    '''Find all valid numbers inside a group.
       Returns a list of strings''' 
    board_list = string_to_list(board) 
    rows = string_to_list(groups)
    elements = []
    for ir, row in enumerate(rows):
        for ic, gr in enumerate(row):
            if gr == str(group):
                elements.append(board_list[ir][ic])
    result = []
    for number in range(1,7):
        if str(number) not in elements:
            result.append(str(number))
    return result

def find_next_actual(board, groups):
    '''Find the next cell to expand based on the number of posible numbers in the cell.
        Returns a tuple: row, column'''
    min_posibilities = 16
    next_actual_row = None
    next_actual_col = None

    groups_list = string_to_list(groups) 
    rows = string_to_list(board)
    for ir, row in enumerate(rows):
        for ic, element in enumerate(row):
            if element == '0':
                nums_in_rows = possible_numbers_in_row(board, int(ir))
                nums_in_cols = possible_numbers_in_row(board, int(ic))
                nums_in_gr = possible_numbers_in_group(board, groups, int(groups_list[ir][ic]))
                posibilites = [value for value in nums_in_cols if value in nums_in_rows and value in nums_in_gr]
                if len(posibilites) < min_posibilities:
                    next_actual_row = ir 
                    next_actual_col = ic
                    min_posibilities = len(posibilites)
    return next_actual_row, next_actual_col
    
def check_if_complete(board, groups):
    '''Returns true if there is no empty cells in a board.
    '''
    rows = string_to_list(board)    
    for ir, row in enumerate(rows):
        for ic, element in enumerate(row):
            if element == '0' or element == 'X':
                return False
    return True  
