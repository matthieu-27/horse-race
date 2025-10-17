#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randrange

MIN_HORSES, MAX_HORSES, MAX_DISTANCE, DICE, DISTANCE = 10, 20, 2400, 6, 23
HORSE_STR = 'Horse '
SPEED_LIST = [[0,1,1,1,2,2], [0,0,1,1,1,2], [0,0,1,1,1,2], [-1,0,0,1,1,1], [-1,0,0,0,1,1], [-2,-1,0,0,0,1], [-1,-1,0,0,0,3]]


def get_turn_distance(_speed):
    """ Returns `DISTANCE` x `_speed` (horse turn distance)"""
    return DISTANCE * _speed


def display_result(_horse_list):
    """ Displays race result """
    count =  0
    winners = 0
    for horse in _horse_list:
        progress = horse[1] // 30
        progress_bar = '▓' * progress + '░' * (2500 // 30 - progress)
        if count < len(_horse_list):
            if horse[1] == "DQ":
                print(f"\033[91m{HORSE_STR + str(count)} - {horse[1]} : {progress_bar}\033[0m")
            elif horse[1] >= MAX_DISTANCE and winners < game_mode:
                print(f"\033[92m{HORSE_STR + str(count)} - {horse[1]} : {progress_bar}\033[0m")
                winners += 1
            else:
                print(f'{HORSE_STR + str(count)} - {horse[1]} : {progress_bar}')
            count += 1


def check_distance(_distance):
    """ Returns True if parcoured distance is less than `MAX_DISTANCE`, False otherwise """
    return True if _distance < MAX_DISTANCE else False


def check_speed(current_speed, next_speed):
    """ Returns True if not disqualified, False otherwise """
    if current_speed == 6 and next_speed == 3:
        return False
    return True


def get_distance(_horses, x):
    """ Returns horse parcoured distance """
    return int(_horses[x][1])


def get_speed(_horses, x):
    """ Returns horse current speed """
    return int(_horses[x][0])


def gen_horses():
    """ Generate and returns a new horse list """
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

    horses = gen_horses()  # generate horses list

    while not game_over:
        result = []
        for i in range(len(horses)):
            random_number = randrange(0, DICE)  # roll a number
            speed, distance = horses[i][0], horses[i][1]  # get speed and sitance
            turn_speed = SPEED_LIST[speed][random_number]  # find turn
            if check_speed(i, turn_speed) and horses[i][1] != "DQ":
                horses[i][0] = turn_speed
                horses[i][1] += get_turn_distance(turn_speed)
            else:
                horses[i][1] = -1

            if not check_distance(distance) and len(result) < game_mode:
                result.append(f"{len(result) + 1}: {HORSE_STR + str(i + 1)} (distance : {get_distance(horses, i)})")
                if len(result) == game_mode:
                    game_over = True
                    break

            # display_line(horses, i)

        if game_over:
            print(horses)
            print('-' * 30)
            display_result(horses)
            break