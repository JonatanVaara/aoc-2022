"""
Returns the number of calories that the elf carrying the most calories is carrying.

Uses 'input' file
"""


def main():
    """Iterate over input file and count the numbers."""
    elfs = []
    curr_calories = 0
    file = "input"

    with open(file, 'r', encoding='utf-8') as data:
        for line in data:
            if line == '\n':
                elfs.append(curr_calories)
                curr_calories = 0
            else:
                curr_calories += int(line)
    elfs.sort(reverse=True)
    print(sum(elfs[:3]))


if __name__ == '__main__':
    main()
