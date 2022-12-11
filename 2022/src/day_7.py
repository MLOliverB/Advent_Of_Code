from src.util import read_input, result_print

def solve(day_num, input_file_name):
    input_instructions = parse_input(input_file_name)
    file_tree = build_file_tree(input_instructions)
    sum_small_directories = get_sum_small_directories(file_tree)
    deletion_free_up_size = get_min_free_up_directory_deletion(file_tree)
    result_print(
        day_num,
        "Sum of the total sizes of the directories with total size of at most 100000",
        sum_small_directories,
        "Total size of the smallest directory that, if deleted, would free up enough space on the filesystem to run the update",
        deletion_free_up_size
    )

def parse_input(f_name):
    input_str_lst = read_input(f_name)
    input_instructions = []
    command = ""
    output = []
    for line in input_str_lst:
        line = line.strip()
        if line[0] == '$': # Command
            if command:
                input_instructions.append((command, output))
            output = []
            command = tuple(line[2:].split(' '))
        else: # Output
            output.append(tuple(line.split(' ')))
    if command:
        input_instructions.append((command, output))
    return input_instructions

def build_file_tree(input_instructions):
    root_dir = None
    current_dir = None
    for instr in input_instructions:
        command, output = instr
        if command[0] == 'cd':
            destination_dir = command[1]
            if current_dir == None:
                root_dir = Node('dir', destination_dir, -1, None)
                current_dir = root_dir
            elif destination_dir == '..':
                current_dir = current_dir.parent
            else:
                new_dir = Node('dir', destination_dir, -1, current_dir)
                exist_child_nodes = [ child for child in current_dir.children if child.name == destination_dir ]
                if len(exist_child_nodes) == 0:
                    current_dir.add_child(new_dir)
                    current_dir = new_dir
                else:
                    current_dir = exist_child_nodes[0]
        elif command[0] == 'ls':
            for output_item in output:
                type_size, name = output_item
                if name not in [ child.name for child in current_dir.children ]:
                    if type_size == 'dir':
                        current_dir.add_child(Node('dir', name, -1, current_dir))
                    else:
                        current_dir.add_child(Node('file', name, int(type_size), current_dir))
    compute_dir_size(root_dir)
    return root_dir

def compute_dir_size(dir, update_dir_size=True):
    size = 0
    for child in dir.children:
        if child.type == 'file':
            size += child.size
        elif child.type == 'dir':
            size += compute_dir_size(child)
    if update_dir_size:
        dir.size = size
    return size

class Node:
    def __init__(self, type, name, size, parent):
        self.type = type
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        return f"- {self.name} ({self.type}) [size={self.size}]"

    def to_string(self, depth=0, delim=' '):
        print(f"{depth*delim}{self.__str__()}")
        for child in self.children:
            child.to_string(depth+1, delim=delim)



def get_sum_small_directories(file_tree):
    small_directories = []
    queue = [file_tree]
    while queue:
        dir = queue.pop(0)
        if dir.size <= 100000:
            small_directories.append(dir)
        for child in dir.children:
            if child.type == 'dir':
                queue.append(child)
    return sum(dir.size for dir in small_directories)


def get_min_free_up_directory_deletion(file_tree):
    total_space = 70000000
    update_space = 30000000
    used_space = file_tree.size
    required_free_up_space = update_space - (total_space - used_space)

    min_dir = file_tree
    min_size = used_space
    queue = [file_tree]
    while queue:
        dir = queue.pop(0)
        for child in dir.children:
            if child.type == 'dir':
                queue.append(child)
        if dir.size >= required_free_up_space and dir.size < min_size:
            min_dir = dir
            min_size = dir.size
    return min_size