from src.util import read_input, result_print
from queue import LifoQueue
from re import match

def solve(day_num, input_file_name):
    input_lst = create_input_list(input_file_name)
    top_crates_str = get_top_crates_after_instructions(input_lst)
    input_lst = create_input_list(input_file_name)
    top_crates_str_2 = get_top_crates_after_instructions_batch_move(input_lst)
    result_print(
        day_num,
        "Crates on top of the stacks after the crate rearrangement procedure",
        top_crates_str,
        "Crates on top of the stacks after the batch crate movement rearrangement procedure",
        top_crates_str_2
    )

def create_input_list(f_name):
    input_str_lst = read_input(f_name)
    mode = 0
    regex_p = "^[a-z]{2}:(\w+)$"
    regex_p = "^move (\d+) from (\d+) to (\d+)$"
    stack_lines = []
    stack_queues = []
    instructions = []
    for line in input_str_lst:
        if line.strip() == '':
            mode += 1
            stack_indexes = stack_lines[-1]
            stack_lines = stack_lines[:-1]
            number_indexes = []
            for i in range(len(stack_indexes)):
                char = stack_indexes[i]
                if char.isdigit():
                    number_indexes.append(i)
            for i in range(len(number_indexes)):
                stack_queues.append(LifoQueue())
            stack_lines.reverse()
            for stack_line in stack_lines:
                len_line = len(stack_line)
                for i, ix in enumerate(number_indexes):
                    if len_line > ix and stack_line[ix] != ' ':
                        stack_queues[i].put(stack_line[ix])
            continue
        if mode == 0: # Build the starting stack queues
            stack_lines.append(line)
        else: # Construct instruction list
            line = line.strip()
            num_crates_str, from_stack_str, to_stack_str = match(regex_p, line).groups()
            num_crates, from_stack, to_stack = int(num_crates_str), int(from_stack_str), int(to_stack_str)
            instructions.append((num_crates, from_stack, to_stack))
    return (stack_queues, instructions)

def get_top_crates_after_instructions(input_lst):
    stacks, instructions = input_lst
    for instruction in instructions:
        num_crates, from_stack, to_stack = instruction
        for i in range(num_crates):
            stacks[to_stack-1].put(stacks[from_stack-1].get())
    top_crates_str = ""
    for stack in stacks:
        if stack.qsize() > 0:
            top_crates_str += stack.get()
    return top_crates_str

def get_top_crates_after_instructions_batch_move(input_lst):
    stacks, instructions = input_lst
    for instruction in instructions:
        num_crates, from_stack, to_stack = instruction
        intermediate_q = []
        for i in range(num_crates):
            intermediate_q.append(stacks[from_stack-1].get())
        intermediate_q.reverse()
        for crate in intermediate_q:
            stacks[to_stack-1].put(crate)
    top_crates_str = ""
    for stack in stacks:
        if stack.qsize() > 0:
            top_crates_str += stack.get()
    return top_crates_str