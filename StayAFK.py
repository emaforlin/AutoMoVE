import pyKey
import socket
from random import randint
from time import sleep

moves = ['w','a','s','d']

qty_moves = randint(3,10)


def next_move(moves, qty):
    next_move = []

    for l in range(0,qty):
        what_move = randint(0,len(moves)-1)
        #print("What move: " + str(what_move))
        print(len(next_move))

        if len(next_move) == 0:
            next_move.append(moves[what_move])
        elif moves[what_move] != next_move[len(next_move)-1]:
            next_move.append(moves[what_move])
        

    #print("Qty: " + str(qty))
    print(next_move)
    return next_move

def move_character(moves):
    duration = randint(1,3)

    for l in moves:
        pyKey.press(key=l, sec=duration)

while True:
    try:
#    next_move(moves, qty_moves)
        move_character(next_move(moves, qty_moves))
        sleep(30)
    except:
        print("Ha ocurrido un error.")
