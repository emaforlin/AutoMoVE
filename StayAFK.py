import pyKey
import socket
from random import randint
from time import sleep

moves = ['w','a','s','d']

qty_moves = randint(3,10)


class Character():
    def move(self, moves):
        duration = randint(1,3)
        for l in moves:
            pyKey.press(key=l, sec=duration)

    def get_nextMove(self, moves, qty):
        next_move = []
        for l in range(0,qty):
            what_move = randint(0,len(moves)-1)
            #print("What move: " + str(what_move))
            print(len(next_move))

            if len(next_move) == 0:
                next_move.append(moves[what_move])
            elif moves[what_move] != next_move[len(next_move)-1]:
                next_move.append(moves[what_move])
        print(next_move)
        return next_move

person = Character()

while True:
    move = person.get_nextMove(moves, qty_moves)
    person.move(move)
    sleep(30)
