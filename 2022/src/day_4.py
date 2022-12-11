from src.util import read_input, result_print

def solve(day_num, input_file_name):
    input_lst = create_input_list(input_file_name)
    fully_contained_ranges_count = count_fully_contained_ranges(input_lst)
    intersection_count = count_intersecting_ranges(input_lst)
    result_print(
        day_num,
        "Number of assignment pairs where one section assignment range contains the other",
        fully_contained_ranges_count,
        "Number of assignment pairs where section assignment ranges overlap/intersect",
        intersection_count
    )

def create_input_list(f_name):
    input_str_lst = read_input(f_name)
    input_lst = []
    for line in input_str_lst:
        line = line.strip()
        if line:
            range1, range2 = line.split(',', maxsplit=2)
            lo1, hi1 = range1.split('-', maxsplit=2)
            lo2, hi2 = range2.split('-', maxsplit=2)
            input_lst.append((set(range(int(lo1), int(hi1)+1)), set(range(int(lo2), int(hi2)+1))))
    return input_lst

def count_fully_contained_ranges(input_lst: list[tuple[set, set]]):
    count = 0
    for pair in input_lst:
        set1, set2 = pair
        if set1.issubset(set2) or set2.issubset(set1):
            count += 1
    return count

def count_intersecting_ranges(input_lst: list[tuple[set, set]]):
    count = 0
    for pair in input_lst:
        set1, set2 = pair
        if set1.intersection(set2):
            count += 1
    return count