import os
import copy

num_sequence = []
boards = []

with open(os.getcwd() + "\\2021\\day_4\\day_4-input.txt", 'r') as file:
    line = file.readline()

    num_sequence = line.strip().split(",")
    # Parse strings as integers
    for i in range(len(num_sequence)):
        num_sequence[i] = int(num_sequence[i])

    line = file.readline()

    board = []
    while line:
        line = line.strip()
        if line == "":
            if board != []:
                boards.append(board)
            board = []
        else:
            row = []
            for num in line.replace("  ", " ").split(" "):
                row.append(int(num))
            board.append(row)
        line = file.readline()
    
    boards.append(board)

boards_crossed = copy.deepcopy(boards)

last_num = -1
for num in num_sequence:
    # Cross off the number on all boards
    for b in range(len(boards)):
        for row in range(len(boards[b])):
            for col in range(len(boards[b][row])):
                if num == boards[b][row][col]:
                    boards_crossed[b][row][col] = -1
    
    complete_board = -1
    # Check whether we have a complete row or column anywhere
    for b in range(len(boards)):
        for row in range(len(boards[b])):
            complete_row = True
            for col in range(len(boards[b][row])):
                if boards_crossed[b][row][col] != -1:
                    complete_row = False
            if complete_row:
                complete_board = b
                last_num = num
                break
        if complete_board != -1:
            break
        
        for col in range(len(boards[b][0])):
            complete_col = True
            for row in range(len(boards[b])):
                if boards_crossed[b][row][col] != -1:
                    complete_col = False
            if complete_col:
                complete_board = b
                last_num = num
                break
        if complete_board != -1:
            break
    if complete_board != -1:
        break


unmarked_sum = 0

for row in boards_crossed[complete_board]:
    for entry in row:
        if entry != -1:
            unmarked_sum += entry

winning_score = unmarked_sum * last_num
print("Winning board:", complete_board, "- score:", winning_score)