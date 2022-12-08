"""Count trees visible."""

import sys


def main(inputfile):
    """Do the main thing."""
    tree_list = convert_to_list(inputfile)
    nr_of_visible_trees = calculate_nr_of_visible_trees(tree_list)
    print(f'Number of visible trees: {nr_of_visible_trees}')
    scenic_score = calculate_scenic_score(tree_list)
    print(f'Highest scenic score possible is: {scenic_score}')


def calculate_scenic_score(tree_list):
    """Calculate scenic score."""
    highest_scenic_score = 0
    for row in range(len(tree_list[0])):
        for column in range(len(tree_list)):
            curr_scenic_score = check_scenic_score(row, column, tree_list)
            if curr_scenic_score > highest_scenic_score:
                highest_scenic_score = curr_scenic_score
    
    return highest_scenic_score


def check_scenic_score(row, column, tree_list):
    """Check scenic score of current tree"""
    tree_height = tree_list[row][column]
    scores = [0, 0, 0, 0]
    if not column == 0:
        for i in range(column-1, -1, -1): #  right to left
            curr_tree = tree_list[row][i]
            if curr_tree < tree_height:
                scores[0] += 1
            if curr_tree >= tree_height:
                scores[0] += 1
                break


    if not column == len(tree_list)-1:
        for i in range(column+1, len(tree_list[0])): #  left to right
            curr_tree = tree_list[row][i]
            if curr_tree < tree_height:
                scores[1] += 1
            if curr_tree >= tree_height:
                scores[1] += 1
                break

    if not row == 0:
        for i in range(row-1, -1, -1): #  Bottom to top
            curr_tree = tree_list[i][column]
            if curr_tree < tree_height:
                scores[2] += 1
            if curr_tree >= tree_height:
                scores[2] += 1
                break

    if not row == len(tree_list[0]):
        for i in range(row+1, len(tree_list)): #  Top to bottom
            curr_tree = tree_list[i][column]
            if curr_tree < tree_height:
                scores[3] += 1
            if curr_tree >= tree_height:
                scores[3] += 1
                break

    return (scores[0] * scores[1] * scores[2] * scores[3])



def pp(the_list):
    print()
    for i in the_list:
        print(f'{i}')
    print()


def calculate_nr_of_visible_trees(tree_list):
    """Calculate nr of visible trees."""
    list_check = copy_list_to_0(tree_list)
    amount = 0
    for row in range(0, len(tree_list[0])):
        amount += calculate_left_to_right(tree_list, row, list_check)
        amount += calculate_right_to_left(tree_list, row, list_check)
    
    for column in range(0, len(tree_list)):
        amount += calculate_top_to_bottom(tree_list, column, list_check)
        amount += calculate_bottom_to_top(tree_list, column, list_check)
    
    #pp(tree_list)
    #pp(list_check)
    return amount


def calculate_bottom_to_top(tree_list, column, list_check):
    """Check visible trees bottom to top."""
    visible_trees = 0
    starting_row = len(tree_list[0])-1
    prev_tree = tree_list[starting_row][column]
    if not_checked(starting_row, column, list_check):
        visible_trees += 1
    for row in reversed(range(starting_row-1)):
        if tree_list[row][column] > prev_tree:
            prev_tree = tree_list[row][column]
            if not_checked(row, column, list_check):
                visible_trees += 1
    return visible_trees

def calculate_top_to_bottom(tree_list, column, list_check):
    """Check visible trees top to bottom."""    
    visible_trees = 0
    prev_tree = tree_list[0][column]
    if not_checked(0, column, list_check):
        visible_trees += 1
    for row in range(1, len(tree_list)):
        if tree_list[row][column] > prev_tree:
            prev_tree = tree_list[row][column]
            if not_checked(row, column, list_check):
                visible_trees += 1
    return visible_trees


def calculate_right_to_left(tree_list, row, list_check):
    """Check visible trees right to left."""
    visible_trees = 0
    starting_column = len(tree_list)-1
    prev_tree = tree_list[row][starting_column]
    if not_checked(row, starting_column, list_check):
        visible_trees += 1
    for column in reversed(range(starting_column)):
        if tree_list[row][column] > prev_tree:
            prev_tree = tree_list[row][column]
            if not_checked(row, column, list_check):
                visible_trees += 1
    return visible_trees


def calculate_left_to_right(tree_list, row, list_check):
    """Check visible trees left to right."""
    visible_trees = 0
    prev_tree = tree_list[row][0]
    if not_checked(row, 0, list_check):
        visible_trees += 1
    for column in range(1, len(tree_list[row])):
        if tree_list[row][column] > prev_tree:
            prev_tree = tree_list[row][column]
            if not_checked(row, column, list_check):
                visible_trees += 1
    return visible_trees


def not_checked(row, column, list_check):
    """Return true if this tree has not been checked already."""
    if list_check[row][column] == 0:
        list_check[row][column] = 1
        
        return True
    return False


def copy_list_to_0(tree_list):
    """Make a copy of given list but with 0"""
    new_list = []
    for i in range(0, len(tree_list)):
        new_line = []
        for _ in range(0, len(tree_list[i])):
            new_line.append(0)
        new_list.append(new_line)

    return new_list



def convert_to_list(inputfile):
    tree_list = []
    with open(inputfile, 'r', encoding='utf-8') as tree_file:
        for line in tree_file.readlines():
            tree_list.append(line_to_list(line.rstrip()))
    return tree_list

def line_to_list(line):
    """Convert string to list of int."""
    tree_line = []
    for tree in line:
        tree_line.append(int(tree))
    return tree_line


if __name__ == "__main__":
    main(sys.argv[1])
