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
last_winner = -1
complete_boards = []
for num in num_sequence:
    for b in range(len(boards)):
        if b in complete_boards:
            continue
        else:
            # Cross of matching numbers on board
            for row in range(len(boards[b])):
                for col in range(len(boards[b][row])):
                    if num == boards[b][row][col]:
                        boards_crossed[b][row][col] = -1

            # Check if there is a crossed off row
            for row in range(len(boards[b])):
                complete_row = True
                for col in range(len(boards[b][row])):
                    if boards_crossed[b][row][col] != -1:
                        complete_row = False
                if complete_row:
                    complete_boards.append(b)
                    complete_boards.sort()
                    last_num = num
                    last_winner = b
                    break
            if b in complete_boards:
                continue
                
            # Check if there is a crossed off column
            for col in range(len(boards[b][0])):
                complete_col = True
                for row in range(len(boards[b])):
                    if boards_crossed[b][row][col] != -1:
                        complete_col = False
                if complete_col:
                    complete_boards.append(b)
                    complete_boards.sort()
                    last_num = num
                    last_winner = b
                    break
            if b in complete_boards:
                continue


unmarked_sum = 0

for row in boards_crossed[last_winner]:
    for entry in row:
        if entry != -1:
            unmarked_sum += entry

winning_score = unmarked_sum * last_num
print("Last Winning board:", last_winner, "- score:", winning_score)