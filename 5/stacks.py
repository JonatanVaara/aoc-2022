"""Check stacks of boxes, moves them and outputs the top boxes."""

import sys


def main(inputfile: str):
    """Do the stuff."""
    with open(inputfile, 'r', encoding='utf-8') as file:
        rows = file.readlines()
        stacks_list = extract_stacks(rows)
        moves = extract_moves(rows)
        move_boxes(stacks_list, moves)  # Changes stacks_list
        # print_nicely(stacks_list)
        # for move in moves:


def extract_stacks(rows: []) -> []:
    """Extract stack string into list of stacks."""
    stacks_list = [[], [], [], [], [], [], [], [], []]
    stack_length = 4
    for row in rows:
        if row[1].isnumeric():
            return stacks_list
        index = 0
        for i in range(0, len(row)-1, stack_length):
            if row[i] == '[':
                stacks_list[index].insert(0, row[i+1])
            index += 1
    return stacks_list


def extract_moves(rows):
    """Extract moves to list of dict moves."""
    return_list = []
    for row in rows:
        move = {"amount": 0,
                "from": 0,
                "to": 0}
        if row[0] != "m":
            continue
        data = row.rstrip().split(' ')
        move['amount'] = int(data[1])
        move['from'] = int(data[3])
        move['to'] = int(data[5])
        tmp = move.copy()
        return_list.append(tmp)
    return return_list


def move_boxes(stacks_list: [], moves: []) -> []:
    """Move the 'boxes' in stacks_list according to the moves."""
    for move in moves:
        print(f'Move: {move}')
        print(f'Moving {move["amount"]} boxes')
        print("Before moving")
        print_nicely(stacks_list)
        # for _ in range(1, move['amount']+1):
        #    print(f'Moving from stack {move["from"]}')
        #    box_moving = stacks_list[move['from']-1].pop()
        #    stacks_list[move['to']-1].append(box_moving)
        boxes_to_move = stacks_list[move['from']-1][-move['amount']:]
        stacks_list[move['from']-1] = stacks_list[move['from']-1][:-move['amount']]
        stacks_list[move['to']-1].extend(boxes_to_move)
        print("After moving")
        print_nicely(stacks_list)
    return stacks_list


def print_nicely(stacks_list: []):
    """Just print nicely."""
    for stack in stacks_list:
        print(stack)


if __name__ == "__main__":
    main(sys.argv[1])
