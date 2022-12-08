"""Fake file traversing."""

import sys


class Folder:  # pylint: disable=too-few-public-methods
    """Class for folder structure."""

    def __init__(self, name, files, folders, parent):
        """Init function."""
        self.name = name
        self.files = files
        self.folders = folders
        self.parent = parent
        self.depth = self.get_depth(0)

    def __str__(self):
        """Print as string."""
        tab_string = "  "*self.depth
        return f'{tab_string}{self.name}'

    def print_this_and_children(self):
        """Print stuff."""
        print(self)
        for folder in self.folders:
            folder.print_this_and_children()
        for file in self.files:
            print(file)

    def find_max_size_files(self, find_size, curr_size):
        """Find files smaller or equal to size."""
        curr_size = 0
        for file in self.files:
            if file.size <= find_size:
                curr_size += file.size
        for folder in self.folders:
            curr_size += folder.find_max_size_files(find_size, curr_size)
        return curr_size

    def get_depth(self, depth):
        """Calculate depth."""
        if self.parent:
            depth += 1
            return self.parent.get_depth(depth)
        return depth

    def get_dir_size(self):
        """Calculate the size of the dir."""
        size = 0
        for file in self.files:
            size += file.size
        for folder in self.folders:
            size += folder.get_dir_size()
        return size


class File:  # pylint: disable=too-few-public-methods
    """Class for representing file."""

    def __init__(self, name, size, parent):
        """Init function."""
        self.name = name
        self.size = int(size)
        self.parent = parent
        self.depth = self.get_depth(0)

    def __str__(self):
        """Print as string."""
        space_print = "  " * self.depth
        return f'{space_print}{self.name} - {self.size}'

    def get_depth(self, depth):
        """Calculate depth."""
        if self.parent:
            depth += 1
            return self.parent.get_depth(depth)
        return depth


def main(inputfile):
    """Do the thingy."""
    commands = []
    with open(inputfile, 'r', encoding='utf-8') as file:
        commands = extract_commands(file)
    root = do_commands(commands)
    unused_disk_space = 70000000 - root.get_dir_size()
    print(f'root size: {root.get_dir_size()}')
    needed = 30000000 - unused_disk_space
    size_list = calculate_sizes(root, [])
    print(sum(filter(lambda x: x <= 100000, size_list)))
    print(f'Unused_diskspace: {unused_disk_space}')
    print(f'Needed disc space: {needed}')
    smallest_size = get_size_smallest_needed(size_list, needed)
    print(f'smallest_size: {smallest_size}')


def calculate_sizes(root, acc):
    """Calculate sizes and sum values."""
    acc.append(root.get_dir_size())
    for folder in root.folders:
        acc.append(sum(calculate_sizes(folder, acc)))
    return acc


def get_size_smallest_needed(size_list, needed):
    """Return the size of the smallest size that a folder has.
    
    To be used later to look through all the folders to find the one we need to delete.
    Yes, it is fucking stupid. Yes, I am too lazy to re-write my previous solution."""
    size_list.sort()
    for size in size_list:
        if size >= needed:
            return size
    return 0


def do_commands(commands: []) -> Folder:
    """Iterate over commands and create Folder and files."""
    root = Folder("root", [], [], None)
    curr_folder = root
    for command in commands:
        if command[0] == 'cd':
            if command[1] == '/':
                continue
            if command[1] == '..':
                try:
                    curr_folder = curr_folder.parent
                except:  # noqa: E722 pylint: disable=bare-except
                    print("ERROR: Folder does not have parent!!")
            else:
                new_folder = Folder(command[1], [], [], curr_folder)
                curr_folder.folders.append(new_folder)
                curr_folder = new_folder
        if command[0] == 'ls':
            continue
        if command[0].isnumeric():
            new_file = File(command[1], command[0], curr_folder)
            curr_folder.files.append(new_file)
    return root


def extract_commands(file):
    """Extract commands from file."""
    command_list = []
    for line in file.readlines():
        line = line.rstrip()
        if line[0] == '$':
            command_list.append(line.split(' ')[1:])
        else:
            command_list.append(line.split(' '))
    return command_list


if __name__ == '__main__':
    main(sys.argv[1])
