import pyKey
from random import randint
from time import sleep

moves = ['w','a','s','d']

qty_moves = randint(3,10)


class Character:
    def move(self, moves):
        duration = randint(1,3)
        for l in moves:
            pyKey.press(key=l, sec=duration)

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
            excpt()

    def controlled_walk(self, time):
        show_msg()
        try:
            while True:
                pyKey.press(key='w', sec=time)
                pyKey.press(key='s', sec=time)
        except KeyboardInterrupt:
            excpt()



def excpt():
    print('Exiting...')
    sleep(2)
    ui()

def show_msg():
    print('''
    --> The program init in 10 seconds, remember maximize the window.

    --> Ctrl + C to exit.
    ''')
    sleep(10)

def ui():
    print('''
# Modes #
0)  Random           --> This mode makes random moves on the character (every 30s).
1)  Walk             --> This mode makes the character walk fordward indefinitely.
2)  Controlled walk  --> This mode makes a walk for a time defined for you and get back the same time.
99) Exit the program
''')
    person = Character()
    choose = int(input("$~> "))
    if choose == 0:
        try:
            show_msg()
            while True:
                move = person.get_nextMove(moves, qty_moves)
                person.move(move)
                sleep(30)
        except KeyboardInterrupt:
            print('Exiting...')
            excpt()
    elif choose == 1:
        person.walk()
    elif choose == 2:
        time = int(input('Enter the time (seconds): '))
        person.controlled_walk(time)
    elif choose == 99:
        exit()


ui()
