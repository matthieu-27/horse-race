#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randrange

MIN_HORSES, MAX_HORSES, MAX_LENGTH, DICE, DISTANCE = 10, 12, 2400, 6, 23
HORSE_STR = 'Cheval '
SPEED_LIST = [[0,1,1,1,2,2], [0,0,1,1,1,2], [0,0,1,1,1,2], [-1,0,0,1,1,1], [-1,0,0,0,1,1], [-2,-1,0,0,0,1], [-1,-1,0,0,0,3]]


def roll_dice():
    return randrange(0, DICE)


def process_race(horses_dict, turn_number, counter):
    random_number = roll_dice()
    for horse in horses_dict.values():
        current_speed, current_distance = get_speed(horse), get_distance(horse)
        next_speed = SPEED_LIST[current_speed][random_number]
        if check_speed(current_speed, next_speed, current_distance):
            current_speed += next_speed
            current_distance = DISTANCE * random_number
            horses_dict[HORSE_STR + str(counter+1)] = str(next_speed) + str(current_distance)


def check_speed(current_speed, next_speed, distance):
    if current_speed == 6 and next_speed == 3 or distance > MAX_LENGTH:
        return False
    return True


def get_distance(str_value):
    return int(str_value[:1])


def get_speed(str_value):
    return int(str_value[0][:1])


if __name__ == "__main__":
    game_over = False
    turn, race_distance = 0, 0
    horses = dict(zip([HORSE_STR + str(n + 1) for n in range(MAX_HORSES)], ['00' for _ in range(MAX_HORSES)]))

    game_mode_str = input("Quel mode de jeu desirez vous ?\n 1 - Tiercé | 2 - Quarté | 3 - Quinté\n")
    game_mode = int(game_mode_str) if game_mode_str.isdecimal() else 1
    game_mode += 2  # define correct loop mode


    count = 0
    while not game_over:
        process_race(horses, turn, count)

        if game_over:
            break

        count += 1
        print(horses)
        if count == MAX_HORSES:
            count = 0
            turn += 1
            if turn >= 50:
                game_over = True
                break



