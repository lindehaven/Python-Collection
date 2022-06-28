'''TODO'''
from random import randint

def is_a_hit(dice1, dice2):
    '''TODO'''
    dice_sum = dice1 + dice2
    return dice_sum == 7 or dice_sum == 11 or dice1 == dice2

def hits(throws):
    '''TODO'''
    dice_hits = 0
    for _ in range(throws):
        if is_a_hit(randint(1, 6), randint(1, 6)):
            dice_hits += 1
    return dice_hits

THROWS = 1000000
print("Probability = %.1f %%" % (hits(THROWS) * 100 / THROWS))
print("   Expected = %.1f %%" % (14 / 36 * 100))
