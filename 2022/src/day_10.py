from src.util import read_input, result_print
import numpy as np

def solve(day_num, input_file_name):
    input_lst = build_input_lst(input_file_name)
    reg_vals = compute(input_lst)
    signal_strength_sum = get_sum_signal_strength(reg_vals)
    screen_grid = render_display_screen_instructions(reg_vals)
    result_print(
        day_num,
        "Sum of the signal strengths during the 20th, 60th, 100th, 140th, 180th, and 220th cycles",
        signal_strength_sum,
        "Rendered text of the CRT display",
        render(screen_grid, return_string=True)
    )

def build_input_lst(f_name):
    input_str_lst = read_input(f_name)
    input_lst = []
    for line in input_str_lst:
        line = line.strip()
        split = line.split(' ', maxsplit=2)
        if len(split) == 1:
            input_lst.append((split[0], None))
        else:
            input_lst.append((split[0], int(split[1])))
    return input_lst

def compute(input_lst: list):
    during_cycle_reg_vals = []
    after_cycle_reg_vals = []
    tasks = input_lst.copy()
    current_task = None
    ttc = 0
    cycle = 0
    reg_val = 1
    while tasks or current_task != None:
        if current_task == None: # Switch in a new task
            current_task = tasks.pop(0)
            if current_task[0] == 'noop':
                ttc = 1
            elif current_task[0] == 'addx':
                ttc = 2

        ttc -= 1 # Compute task i.e. decrease ttc

        # Record register value during cycle
        during_cycle_reg_vals.append(reg_val)

        if ttc == 0:
            if current_task[0] == 'noop':
                pass
            elif current_task[0] == 'addx':
                reg_val += current_task[1]
            current_task = None

        cycle += 1 # End of cycle
        after_cycle_reg_vals.append(reg_val)
        # print(cycle, reg_val)
    print(during_cycle_reg_vals)
    print(after_cycle_reg_vals)
    return during_cycle_reg_vals

def get_sum_signal_strength(reg_vals: list):
    acc = 0
    len_reg_vals = len(reg_vals)
    cycle_counter = 20
    i = 19
    while i < len_reg_vals:
        if (cycle_counter-20)%40 == 0:
            print(cycle_counter, reg_vals[i], (cycle_counter * reg_vals[i]))
            acc += (cycle_counter * reg_vals[i])
        i += 1
        cycle_counter += 1
    return acc

def render_display_screen_instructions(reg_vals):
    grid_a = np.full((6, 40), ' ')
    len_reg_vals = len(reg_vals)
    i = 0
    while i < len_reg_vals:
        drawing_x = i % 40
        drawing_y = int(i / 40)
        sprite_pos = [reg_vals[i]-1, reg_vals[i], reg_vals[i]+1]
        if drawing_x in sprite_pos:
            grid_a[drawing_y][drawing_x] = '█'
        i += 1
    return grid_a

def render(grid_a, return_string=False):
    if return_string:
        strings = []
        for i in range(grid_a.shape[0]):
            strings.append("".join(list(grid_a[i])))
        return strings
    else:
        for i in range(grid_a.shape[0]):
            print("".join(list(grid_a[i])))