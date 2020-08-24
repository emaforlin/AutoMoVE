import pyKey
from random import randint
from time import sleep

moves = ['w','a','s','d']

qty_moves = randint(3,10)


class Character:
    def move(self, moves):
        try:
            duration = randint(1,3)
            for l in moves:
                pyKey.press(key=l, sec=duration)
        except KeyboardInterrupt:
            print('Exiting...')

    def get_nextMove(self, moves, qty):
        next_move = []
        for l in range(0,qty):
            what_move = randint(0,len(moves)-1)
            #print("What move: " + str(what_move))
            #print(len(next_move))

            if len(next_move) == 0:
                next_move.append(moves[what_move])
            elif moves[what_move] != next_move[len(next_move)-1]:
                next_move.append(moves[what_move])
        #print(next_move)
        return next_move

    def walk(self):
        show_msg()
        try:
            while True:
                sleep(1)
                pyKey.press(key='w', sec=10)
        except KeyboardInterrupt:
            print('Exiting...')

    def controlled_walk(self, time):
        show_msg()
        try:
            while True:
                pyKey.press(key='w', sec=time)
                pyKey.press(key='s', sec=time)
        except KeyboardInterrupt:
            print('Exiting...')
