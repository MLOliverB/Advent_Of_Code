from src.util import read_input, result_print

def solve(day_num, input_file_name):
    input_lst = build_input_lst(input_file_name)
    unique_tail_positions_count_short_rope = count_unique_tail_rope_positions(input_lst, rope_length=1)
    unique_tail_positions_count_long_rope = count_unique_tail_rope_positions(input_lst, rope_length=9)
    result_print(
        day_num,
        "Unique positions visited by the tail of rope length 1",
        unique_tail_positions_count_short_rope,
        "Unique positions visited by the tail of rope length 9",
        unique_tail_positions_count_long_rope
    )

def build_input_lst(f_name):
    input_str_lst = read_input(f_name)
    input_lst = []
    for line in input_str_lst:
        line = line.strip()
        direction, step = line.split(' ', maxsplit=2)
        input_lst.append((direction, int(step)))
    return input_lst

def count_unique_tail_rope_positions(input_lst, rope_length=1):
    tail_positions = set()
    rope_positions = (1+rope_length)*[(0, 0)]
    len_rope_positions = len(rope_positions)
    tail_positions.add(rope_positions[-1])
    for direction, step in input_lst:
        for s in range(step):
            head_x, head_y = rope_positions[0]
            if direction == 'U':
                head_y += 1
            elif direction == 'D':
                head_y -= 1
            elif direction == 'L':
                head_x -= 1
            elif direction == 'R':
                head_x += 1
            rope_positions[0] = (head_x, head_y)

            for i in range(1, len_rope_positions):
                fst_x, fst_y = rope_positions[i-1]
                sec_x, sec_y = rope_positions[i]
                x_diff = fst_x - sec_x
                y_diff = fst_y - sec_y
                new_sec_x, new_sec_y = sec_x, sec_y
                if abs(x_diff) > 1 or abs(y_diff) > 1: # We have a significant offset
                    if y_diff == 0: # Need to move tail along x
                        new_sec_x += x_diff//(abs(x_diff))
                    elif x_diff == 0: # Need to move tail along y
                        new_sec_y += y_diff//(abs(y_diff))
                    else: # We need to move tail diagonally
                        new_sec_x += x_diff//(abs(x_diff))
                        new_sec_y += y_diff//(abs(y_diff))
                    rope_positions[i] = (new_sec_x, new_sec_y)
            tail_positions.add(rope_positions[-1])
    return len(tail_positions)

def render(head_pos, tail_pos, size):
    grid = []
    for i in range(size[1]):
        row = []
        for j in range(size[0]):
            sym = '·'
            if tail_pos == (j, i):
                sym = 'T'
            if head_pos == (j, i):
                sym = 'H'
            row.append(sym)
        grid.append(row)
    grid.reverse()
    for line in grid:
        for char in line:
            print(char, end='')
        print()