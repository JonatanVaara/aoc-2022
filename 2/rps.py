"""Advent of Code Day 2."""

import sys
from typing import BinaryIO


def main(inputfile):
    """Calculate points from move list."""
    with open(inputfile, "r", encoding="utf-8") as file:
        moves_list = extract_moves_as_tuples(file)
        new_moves_list = create_new_move_list(moves_list)
        points = calculate_points(new_moves_list)
        print(points)


def create_new_move_list(moves: []):
    """Create a new file with moves.

    X = Loss
    Y = Draw
    Z = Win
    """
    rock = "X"
    paper = "Y"
    scissors = "Z"
    new_moves_list = []
    for move in moves:
        if move[0] == "A":  # Rock
            if move[1] == "X":  # Loss
                new_moves_list.append((move[0], scissors))
            if move[1] == "Y":  # Draw
                new_moves_list.append((move[0], rock))
            if move[1] == "Z":  # Win
                new_moves_list.append((move[0], paper))
        if move[0] == "B":  # Paper
            if move[1] == "X":  # Loss
                new_moves_list.append((move[0], rock))
            if move[1] == "Y":  # Draw
                new_moves_list.append((move[0], paper))
            if move[1] == "Z":  # Win
                new_moves_list.append((move[0], scissors))
        if move[0] == "C":  # Scissors
            if move[1] == "X":  # Loss
                new_moves_list.append((move[0], paper))
            if move[1] == "Y":  # Draw
                new_moves_list.append((move[0], scissors))
            if move[1] == "Z":  # Win
                new_moves_list.append((move[0], rock))
    return new_moves_list


def calculate_points(moves: []) -> int:
    """Calculate points for moves and win.

    Moves Points List:
        1 = Rock
        2 = Paper
        3 = Scissors
    Winnings Points List:
        0 = Loss
        3 = Draw
        6 = Win
    """
    points = 0
    for move in moves:
        points += calculate_win(move[0], move[1])
        points += calculate_move(move[1])

    return points


def calculate_win(their_move: str, my_move: str) -> int:
    """Calculate points for win and returns as int."""
    points = 0
    if their_move == "A":  # Rock
        if my_move == "X":  # Rock
            points = 3
        if my_move == "Y":  # Paper
            points = 6
        if my_move == "Z":  # Scissors
            points = 0

    if their_move == "B":  # Paper
        if my_move == "X":  # Rock
            points = 0
        if my_move == "Y":  # Paper
            points = 3
        if my_move == "Z":  # Scissor
            points = 6

    if their_move == "C":  # Scissors
        if my_move == "X":  # Rock
            points = 6
        if my_move == "Y":  # Paper
            points = 0
        if my_move == "Z":  # Scissors
            points = 3
    return points


def calculate_move(my_move: str) -> int:
    """Calculate points for move used."""
    if my_move == "X":  # Rock
        return 1
    if my_move == "Y":  # Paper
        return 2
    if my_move == "Z":  # Scissors
        return 3
    return 0


def extract_moves_as_tuples(file: BinaryIO) -> []:
    """Extract moves from file and put into list of tuples."""
    moves_list = []
    for line in file.readlines():
        moves = line.rstrip().split(" ")
        if moves[0]:
            moves_list.append(tuple((moves[0], moves[1])))

    return moves_list


if __name__ == "__main__":
    main(sys.argv[1])
