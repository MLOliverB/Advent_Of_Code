import os

player_1_pos = None
player_2_pos = None

with open(os.getcwd() + "\\2021\\day_21\\day_21-input.txt", 'r') as file:
    line = file.readline().strip()
    player_1_pos = int(line.split(": ")[1])
    line = file.readline().strip()
    player_2_pos = int(line.split(": ")[1])

dirac_rolls = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1,
}

win_score = 21

player_1_pos = player_1_pos
player_2_pos = player_2_pos
player_1_wins = 0
player_2_wins = 0

def run(score_1, score_2, pos_1, pos_2, rolls, level):
    global player_1_wins
    global player_2_wins
    old_score_1 = score_1
    old_pos_1 = pos_1

    for rolls_1 in dirac_rolls:
        if level == 0:
            print("\r{}".format(rolls_1), end=' ')
        pos_1 = ((pos_1-1 + rolls_1) % 10) + 1
        score_1 += pos_1
        if score_1 >= win_score:
            player_1_wins += (dirac_rolls[rolls_1] * rolls)
            score_1 = old_score_1
            pos_1 = old_pos_1
            continue
        
        old_score_2 = score_2
        old_pos_2 = pos_2
        for rolls_2 in dirac_rolls:
            pos_2 = ((pos_2-1 + rolls_2) % 10) + 1
            score_2 += pos_2
            if score_2 >= win_score:
                player_2_wins += (dirac_rolls[rolls_2] * dirac_rolls[rolls_1] * rolls)
                score_2 = old_score_2
                pos_2 = old_pos_2
                continue
            
            run(score_1, score_2, pos_1, pos_2, dirac_rolls[rolls_2] * dirac_rolls[rolls_1] * rolls, level+1)

            score_2 = old_score_2
            pos_2 = old_pos_2

        score_1 = old_score_1
        pos_1 = old_pos_1

run(0, 0, player_1_pos, player_2_pos, 1, 0)

print("\r")
if player_1_wins > player_2_wins:
    print("Player 1 wins in {} universes".format(player_1_wins))
else:
    print("Player 2 wins in {} universes".format(player_2_wins))