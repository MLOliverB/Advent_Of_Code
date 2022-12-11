from src.util import read_input, result_print

def solve(day_num, input_file_name):
    input_lst = create_input_list(input_file_name)
    sum_prio_dup_items = get_sum_priority_duplicate_item(input_lst)
    sum_prio_bade_items = get_sum_priority_bade_item(input_lst)
    result_print(
        day_num,
        "Sum of the priority of items that are duplicate in each rucksack's compartment",
        sum_prio_dup_items,
        "Sum of the priority of items that are used as badges for each group of three elves",
        sum_prio_bade_items
    )

def create_input_list(f_name):
    input_str_lst = read_input(f_name)
    input_list = []
    for l in input_str_lst:
        line = l.strip()
        if line:
            line_len = len(line)
            comp_len = int(line_len / 2)
            input_list.append((line[:comp_len], line[comp_len:]))
    return input_list


def get_sum_priority_duplicate_item(input_lst):
    acc = 0
    for rucksack in input_lst:
        comp1, comp2 = rucksack
        dup_item: str = None
        item_counts = dict()
        for i in comp1:
            if i not in item_counts:
                item_counts[i] = 1
        for i in comp2:
            if i in item_counts and item_counts[i] == 1:
                item_counts[i] = 2
        while True:
            item, count = item_counts.popitem()
            if count > 1:
                dup_item = item
                break
        if dup_item.islower():
            acc += ord(dup_item) - ord('a') + 1
        else:
            acc += ord(dup_item) - ord('A') + 27
    return acc

def get_sum_priority_bade_item(input_lst):
    acc = 0
    rucksack_lst = [ x[0] + x[1] for x in input_lst ]
    for i in range(0, len(rucksack_lst), 3):
        rucksack1, rucksack2, rucksack3 = rucksack_lst[i], rucksack_lst[i+1], rucksack_lst[i+2]
        rucksack1_item_counts = set()
        for i in rucksack1:
            rucksack1_item_counts.add(i)
        rucksack2_item_counts = set()
        for i in rucksack2:
            if i in rucksack1_item_counts:
                rucksack2_item_counts.add(i)
        rucksack3_item_counts = set()
        for i in rucksack3:
            if i in rucksack2_item_counts:
                rucksack3_item_counts.add(i)
        badge_item: str = rucksack3_item_counts.pop()
        if badge_item.islower():
            acc += ord(badge_item) - ord('a') + 1
        else:
            acc += ord(badge_item) - ord('A') + 27
    return acc
