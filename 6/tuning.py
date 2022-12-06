"""Day 6 of AOC-2022."""

import sys


def main(inputfile: str):
    """Do the thing."""
    with open(inputfile, 'r', encoding='utf-8') as file:
        the_thing = do_the_thing(file.readlines())
        print(the_thing)


def do_the_thing(lines: []) -> []:
    """Do a smaller thing."""
    amount = 14
    message_length = 14
    for line in lines:
        line = line.rstrip()
        for _ in range(message_length-1, len(line)):
            print(line[amount-message_length:amount])
            if len(line[amount-message_length:amount]) == len(set(line[amount-message_length:amount])):
                return amount
            amount += 1

    return 0


if __name__ == "__main__":
    main(sys.argv[1])
