import sys

def main(inputfile):
    contained_sections = 0
    with open(inputfile, 'r', encoding='utf-8') as file:
        pairs_list = file.readlines()
        for pair in pairs_list:
            pairs_tuple = extract_sections(pair.strip())
            converted_tuple = convert_pair_to_ints(pairs_tuple)
            #contained_sections += check_if_contained(converted_tuple)
            contained_sections += check_if_overlap(converted_tuple)
    print(contained_sections)



def extract_sections(pair):
    pairs_list = pair.split(',')
    first_pair_list = pairs_list[0].split('-')
    second_pair_list = pairs_list[1].split('-')
    return (first_pair_list, second_pair_list)
    

def convert_pair_to_ints(pairs_tuple):
    first_pair_ints = convert_to_ints(pairs_tuple[0])
    second_pair_ints = convert_to_ints(pairs_tuple[1])
    return (first_pair_ints, second_pair_ints)
    

def convert_to_ints(pair):
    return_list = []
    for i in range(int(pair[0]), int(pair[1])+1):
        return_list.append(i)
    return return_list


def check_if_contained(pairs_int_tuple):
    if set(pairs_int_tuple[0]).issubset(pairs_int_tuple[1]) or set(pairs_int_tuple[1]).issubset(pairs_int_tuple[0]):
        return 1
    else:
        return 0
    

def check_if_overlap(pairs_int_tuple):
    if any(a for a in pairs_int_tuple[0] if a in pairs_int_tuple[1]):
        return 1
    else:
        return 0


if __name__ == "__main__":
    main(sys.argv[1])