import os

class DeterministicDice:
    def __init__(self):
        self.rolls = 0
        self.next_roll = 1

    def roll(self):
        self.rolls += 1
        roll = self.next_roll
        self.next_roll += 1
        if self.next_roll > 100:
            self.next_roll = 1
        return roll

player_1_pos = None
player_2_pos = None

with open(os.getcwd() + "\\2021\\day_21\\day_21-input.txt", 'r') as file:
    line = file.readline().strip()
    player_1_pos = int(line.split(": ")[1])
    line = file.readline().strip()
    player_2_pos = int(line.split(": ")[1])

dice = DeterministicDice()

score_1 = 0
score_2 = 0
while True:
    rolls = 0
    for i in range(3):
        rolls += dice.roll()
    player_1_pos = ((player_1_pos-1 + rolls) % 10) + 1
    score_1 += player_1_pos
    #print(score_1, end=' ')
    if score_1 >= 1000:
        break
    rolls = 0
    for i in range(3):
        rolls += dice.roll()
    player_2_pos = ((player_2_pos-1 + rolls) % 10) + 1
    score_2 += player_2_pos
    #print(score_2)
    if score_2 >= 1000:
        break

#print()
if score_1 >= 1000:
    print("Player 1 wins")
    print("Losing score times total dice rolls, {} * {} = {}".format(score_2, dice.rolls, score_2 * dice.rolls))
else:
    print("Player 2 wins")
    print("Losing score {} * total dice rolls {} = {}".format(score_1, dice.rolls, score_1 * dice.rolls))