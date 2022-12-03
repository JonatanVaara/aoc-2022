"""Advent of code Day 3"""

import sys

def main(input: str):
    """Main function."""
    summary = 0
    index = 3
    hello = 0
    with open(input, 'r', encoding="utf-8") as inputfile:
        rucksacks = inputfile.readlines()
        for index in range(3, len(rucksacks)+3, 3):
            # compartment_tuple = count_items_in_backpack(sack.strip())
            # wrong_item = find_wrong_item(compartment_tuple)
            badge = find_badge(rucksacks[index-3:index])
            summary += calculate_priority(badge)

        print(summary)


def find_badge(rucksacks):
    """Finds the common item"""
    for i in rucksacks[0].strip():
        if i in rucksacks[1].strip() and i in rucksacks[2].strip():
            return i

    else:
        return "something went wrong"

def count_items_in_backpack(items):
    """Extract list of items into two tuples."""
    compartment1 = []
    compartment2 = []

    for item in items[:int((len(items)/2))]:
        compartment1.extend(item)
    for item in items[int((len(items)/2)):]:
        compartment2.extend(item)
    return (compartment1, compartment2)


def find_wrong_item(compartment_tuple):
    """Compare two departments and find which item is in both."""
    for item in compartment_tuple[0]:
        if item in compartment_tuple[1]:
            return item

def calculate_priority(item):
    """Calculates priorty of item.
    Convert to ascii value and subtract to proper value.
    """
    if item.isupper():
        return ord(item)-38
    else:
        return ord(item)-96 



if __name__ == "__main__":
    main(sys.argv[1])