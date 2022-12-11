from src.util import read_input, result_print

def solve(day_num, input_file_name):
    input_lst = create_input_list(input_file_name)
    max_cals = get_max_cals(input_lst)
    top_3_max_cals = get_top_3_max_cals(input_lst)
    result_print(
        day_num,
        "The largest number of calories carried by a single elf",
        max_cals,
        "The sum of the three largest numbers of calories carried by any single elf",
        top_3_max_cals
    )

def create_input_list(f_name):
    input_str_lst = read_input(f_name)
    elf_cal_lists = []
    curr_cal_list = []
    for line in input_str_lst:
        if line.strip() == '':
            if curr_cal_list:
                elf_cal_lists.append(curr_cal_list)
                curr_cal_list = []
        else:
            curr_cal_list.append(int(line.strip()))
    return elf_cal_lists
        

def get_max_cals(input_lst): # Part 1
    cal_sum_lst = [ sum(lst) for lst in input_lst ]
    return max(cal_sum_lst)

def get_top_3_max_cals(input_lst): # Part 2
    cal_sum_lst = [ sum(lst) for lst in input_lst ]
    cal_sum_lst.sort(reverse=True)
    return sum(cal_sum_lst[0:3])