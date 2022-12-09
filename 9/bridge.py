"""Bridge thing AOC 2022 Day 9."""

import sys


def main(input):
    """Do the thing."""
    moves = get_moves(input)
    matrix = get_size_of_matrix(moves)
    matrix_copy = copy_matrix(matrix)
    visited = traverse(moves, matrix, matrix_copy)
    #visited_positions = calculate_visited(matrix_copy)
    #print(f'Positions visited: {visited_positions}')


def traverse(moves, matrix, matrix_copy):
    """Traverse the matrix and check off matrix_copy."""
    visited = 1
    h_pos = [0, 0]
    t_pos = [0, 0]
    for move in moves:
        visited += move_h(move, matrix, matrix_copy, h_pos, t_pos)

    pp(matrix, h_pos)
    return visited


def move_t(matrix, matrix_copy, h_pos, l_pos):
    """Move T and switch coordinate points."""
    visited = 0
    if h_pos[0] == l_pos[0]:  # Same row
        if h_pos[1] == l_pos[1] - 2:  # two steps left
            l_pos[0] -= 1
        if h_pos[1] == l_pos[1] + 2:  # Two steps right
            l_pos[1] += 1

    if h_pos[1] == l_pos[1]:  # Same column
        if h_pos[0] == l_pos[0] - 2:
            l_pos[0] -= 1
        if h_pos[0] == l_pos[0] + 2:
            l_pos[0] += 1

    if h_pos[0] == l_pos[0] - 1 and h_pos[1] == l_pos[1] - 2:  # up 1 left 2
        l_pos[0] -= 1
        l_pos[1] -= 1

    if h_pos[0] == l_pos[0] - 2 and h_pos[1] == l_pos[1] - 1:  # up 2 left 1
        l_pos[0] -= 1
        l_pos[1] -= 1

    if h_pos[0] == l_pos[0] + 1 and h_pos[1] == l_pos[1] - 2:  # down 1 left 2
        l_pos[0] += 1
        l_pos[1] -= 1

    if h_pos[0] == l_pos[0] + 2 and h_pos[1] == l_pos[1] - 1:  # down 2 left 1
        l_pos[0] += 1
        l_pos[1] -= 1

    if h_pos[0] == l_pos[0] - 2 and h_pos[1] == l_pos[1] +1 :  # up 2 right 1 
        l_pos[0] -= 1
        l_pos[1] += 1

    if h_pos[0] == l_pos[0] - 1 and h_pos[1] == l_pos[1] + 2: # up 1 right 2
        l_pos[0] -= 1
        l_pos[1] += 1



def move_h(move, matrix, matrix_copy, h_pos):
    """Move the H marker and check if already traversed."""
    if move['direction'] == 'U':
        move_up(move['steps'], matrix, matrix_copy, h_pos)
    if move['direction'] == 'D':
        move_down(move['steps'], matrix, matrix_copy, h_pos)
    if move['direction'] == 'L':
        move_left(move['steps'], matrix, matrix_copy, h_pos)
    if move['direction'] == 'R':
        move_right(move['steps'], matrix, matrix_copy, h_pos)
    return visited(matrix, matrix_copy, h_pos, l_pos)

def move_up(steps, matrix, matrix_copy, h_pos):
    """Move H up."""
    h_pos[1] = h_pos[1] + steps


def move_down(steps, matrix, matrix_copy, h_pos):
    """Move H down."""
    h_pos[1] = h_pos[1] - steps


def move_left(steps, matrix, matrix_copy, h_pos):
    """Move H left."""
    h_pos[0] = h_pos[0] - steps


def move_right(steps, matrix, matrix_copy, h_pos):
    """Move H right."""
    h_pos[0] = h_pos[0] + steps


def copy_matrix(matrix):
    """Deep copy a matrix and return an equal one."""
    new_matrix = []
    for i in range(0, len(matrix[0])-1):
        new_matrix.append([])
        for _ in range(0, len(matrix)+1):
            new_matrix[i].append(0)
    new_matrix[0][0] = 1
    return new_matrix


def get_size_of_matrix(moves):
    """Copy Matrix."""
    matrix = []
    curr_horizontal = 0
    max_horizontal = 0
    min_horizontal = 0
    for move in moves:
        if move['direction'] == 'R':
            if curr_horizontal + move['steps'] > max_horizontal:
                max_horizontal += ((curr_horizontal + move['steps']) - max_horizontal)
            curr_horizontal += move['steps']

        if move['direction'] == 'L':
            if curr_horizontal - move['steps'] < min_horizontal:
                min_horizontal -= (curr_horizontal + move['steps']) - min_horizontal
            curr_horizontal -= move['steps']

    curr_vertical = 0
    min_vertical = 0
    max_vertical = 0
    for move in moves:
        if move['direction'] == 'D':
            if curr_vertical + move['steps'] > max_vertical:
                max_vertical += ((curr_vertical + move['steps']) - max_vertical)
            curr_vertical += move['steps']
        if move['direction'] == 'U':
            if curr_vertical - move['steps'] < min_vertical:
                min_vertical -= (curr_vertical + move['steps']) - min_vertical
            curr_horizontal -= move['steps']

    for i in range(0, (max_horizontal - min_horizontal)):
        matrix.append([])
        for _ in range(0, (max_vertical - min_vertical)):
            matrix[i].append(0)
    return matrix


def get_moves(inputfile):
    """Extract moves from file to list."""
    return_list = []
    with open(inputfile, 'r', encoding='utf-8') as infile:
        for line in infile.readlines():
            move = line.split(' ')
            return_list.append({'direction': move[0], 'steps': int(move[1])})
    return return_list


def pp(list_to_print, h_pos):
    """Print list pretty."""
    list_to_print[h_pos[0]][h_pos[1]] = 'H'
    for thing in reversed(list_to_print):
        print(f'{thing}')
    print()


if __name__ == '__main__':
    main(sys.argv[1])
