"""Count trees visible."""

import sys


def main(inputfile):
    """Do the main thing."""
    tree_list = convert_to_list(inputfile)
    print(tree_list)
    nr_of_visible_trees = calculate_nr_of_visible_trees(tree_list)


def calculate_nr_of_visible_trees(tree_list):
    """Calculate nr of visible trees."""
    
    nr_of_visible_trees = calculate_left_right()
    for i in range(1, len(tree_list)+1):



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
