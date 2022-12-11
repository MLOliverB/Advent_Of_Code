def read_input(f_name):
    str_lst = []
    with open(f_name, 'r') as f:
        str_lst = f.readlines()
    return str_lst

def result_print(day_num, part_1_description, part_1_result, part_2_description, part_2_result):
    max_text_len = max((len(str(part_1_description)), len(str(part_1_result)), len(str(part_2_description)), len(str(part_2_result))))
    dash_len = max(3, int((max_text_len-(len(f" Day {day_num} ")))/2)+1)
    dashes = dash_len*'─'
    print(f"\n\n {dashes} Day {day_num} {dashes}")
    print('|')
    print('|', "Part 1")
    print('|', part_1_description)
    if type(part_1_result) == list:
        for item in part_1_result:
            print('|', item)
    else:
        print('|', part_1_result)
    print('|')
    print('|', "Part 2")
    print('|', part_2_description)
    if type(part_2_result) == list:
        for item in part_2_result:
            print('|', item)
    else:
        print('|', part_2_result)