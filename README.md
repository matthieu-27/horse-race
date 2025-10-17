# Course de Chevaux

Une simulation simple de course de chevaux.

## Description

Ce projet simule une course de chevaux où chaque cheval a une vitesse aléatoire et une distance parcourue. Le jeu se termine lorsque les chevaux ont parcouru une certaine distance.

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/matthieu-27/horse-race.git


2. Lancez le fichier :
   ```bash
   python horse_race.py

## Structure du programme

HORSE_STR = 'Horse '

SPEED_LIST = 
[[0, 1, 1, 1, 2, 2], [0, 0, 1, 1, 1, 2], [0, 0, 1, 1, 1, 2], [-1, 0, 0, 1, 1, 1], [-1, 0, 0, 0, 1, 1], [-2, -1, 0, 0, 0, 1], [-1, -1, 0, 0, 0, 3]]

````
def get_turn_distance(_speed):

Returns DISTANCE x _speed (horse turn distance)
````

````
def display_result(_horse_list):

Displays race result
````

````
def check_distance(_distance):

Returns True if parcoured distance is less than MAX_DISTANCE, False otherwise
````

````
def check_speed(current_speed, next_speed):

Returns True if not disqualified, False otherwise
````

````
def get_distance(_horses, x):

Returns horse parcoured distance
````

````
def get_speed(_horses, x):

Returns horse current speed
````

````
def gen_horses():

Generate and returns a new horse list
````