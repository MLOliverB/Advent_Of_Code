from src.util import read_input, result_print

def solve(day_num, input_file_name):
    input_lst = create_input_list(input_file_name)
    strategy_guide_score = get_strategy_guide_score(input_lst)
    instruction_guide_score = get_instruction_guide_score(input_lst)
    result_print(
        day_num,
        "Own player score if interpreting X, Y, Z as rock, paper, scissors",
        strategy_guide_score,
        "Own player score if interpreting X, Y, Z as lose, draw, win",
        instruction_guide_score
    )

def create_input_list(f_name):
    input_str_lst = read_input(f_name)
    return [ (x[0], x[1]) for x in [ line.strip().split(' ') for line in input_str_lst if line.strip() != ''] ]

def score_conventional(round_tup):
    enemy_sym, ally_sym = round_tup
    enemy_n = ord(enemy_sym) - ord('A')
    ally_n = ord(ally_sym) - ord('X')
    symbol_score = ally_n + 1
    outcome_score = -1
    if ally_n == enemy_n: # Draw
        outcome_score = 3
    elif ally_n == (enemy_n + 1) % 3: # Winning
        outcome_score = 6
    else: # Losing
        outcome_score = 0
    return symbol_score + outcome_score

def get_strategy_guide_score(input_lst):
    return sum(score_conventional(round) for round in input_lst)


def score_instructive(round_tup):
    enemy_sym, ally_instr = round_tup
    enemy_n = ord(enemy_sym) - ord('A')
    ally_n = -1
    outcome_score = -1
    if ally_instr == 'X': # Need to lose
        outcome_score = 0
        ally_n = (enemy_n - 1) % 3
    elif ally_instr == 'Y': # Need to draw
        outcome_score = 3
        ally_n = enemy_n
    elif ally_instr == 'Z': # Need to win
        outcome_score = 6
        ally_n = (enemy_n + 1) % 3
    symbol_score = ally_n + 1
    return symbol_score + outcome_score

def get_instruction_guide_score(input_lst):
    return sum(score_instructive(round) for round in input_lst)