#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randrange

MIN_HORSES, MAX_HORSES, MAX_DISTANCE, DICE, DISTANCE = 10, 12, 2400, 6, 23
HORSE_STR = 'Horse '
SPEED_LIST = [[0,1,1,1,2,2], [0,0,1,1,1,2], [0,0,1,1,1,2], [-1,0,0,1,1,1], [-1,0,0,0,1,1], [-2,-1,0,0,0,1], [-1,-1,0,0,0,3]]


def get_turn_distance(_speed):
    return DISTANCE * _speed


def display_race(_horses, _i):
    print(f"Horse {_i} -- Speed: {_horses[_i][0]} | Distance : {_horses[_i][1]}")


def display_result(_result):
    print(_result)


def check_distance(_distance):
    return True if _distance < MAX_DISTANCE else False


def check_speed(current_speed, next_speed):
    if current_speed == 6 and next_speed == 3:
        return False
    return True


def get_distance(_horses, x):
    return int(_horses[x][1])


def get_speed(_horses, x):
    return int(_horses[x][0])


def gen_horses():
    _result = []
    for _ in range(MAX_HORSES):
        _result.append([0,0])
    return list(_result)


if __name__ == "__main__":
    game_over = False
    turn = 0


    game_mode_str = input("Quel mode de jeu desirez vous ?\n 1 - Tiercé | 2 - Quarté | 3 - Quinté\n")
    game_mode = int(game_mode_str) if game_mode_str.isdecimal() else 1
    game_mode += 2  # define correct loop mode

    horses = gen_horses()

    while not game_over:
        result = []
        for i in range(len(horses)):
            random_number = randrange(0, DICE)
            speed, distance = horses[i][0], horses[i][1]
            turn_speed = SPEED_LIST[speed][random_number]
            if check_speed(i, turn_speed):
                horses[i][0] = turn_speed
                horses[i][1] += get_turn_distance(turn_speed)
            else:
                horses[i][1] = -1

            if not check_distance(distance) and len(result) < game_mode:
                result.append(f"Position {len(result) + 1}: {HORSE_STR + str(i)} (distance : {get_distance(horses, i)})")
                if len(result) == game_mode:
                    game_over = True
                    break

            display_race(horses, i)

        if game_over:
            print(horses)
            print(result)
            break


