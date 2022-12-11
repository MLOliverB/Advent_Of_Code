from src.util import read_input, result_print

def solve(day_num, input_file_name):
    input_iter = create_input_list(input_file_name)
    first_start_of_packet_marker_index = get_first_start_of_packet_marker_index(input_iter)
    input_iter = create_input_list(input_file_name)
    first_start_of_message_marker_index = get_first_start_of_message_marker_index(input_iter)
    result_print(
        day_num,
        "Characters processed before the first start-of-packet marker is detected",
        first_start_of_packet_marker_index,
        "Characters processed before the first start-of-message marker is detected",
        first_start_of_message_marker_index
    )

def create_input_list(f_name):
    input_str_lst = read_input(f_name)
    return (char for char in input_str_lst[0].strip())

def get_first_start_of_packet_marker_index(input_iter):
    buffer_size = 4
    buffer = []
    len_buffer = 0
    for i, char in enumerate(input_iter):
        buffer.append(char)
        len_buffer += 1
        if len_buffer > buffer_size:
            buffer.pop(0)
            len_buffer -= 1
        if len_buffer == buffer_size:
            if len_buffer == len(set(buffer)):
                return i+1

def get_first_start_of_message_marker_index(input_iter):
    buffer_size = 14
    buffer = []
    len_buffer = 0
    for i, char in enumerate(input_iter):
        buffer.append(char)
        len_buffer += 1
        if len_buffer > buffer_size:
            buffer.pop(0)
            len_buffer -= 1
        if len_buffer == buffer_size:
            if len_buffer == len(set(buffer)):
                return i+1