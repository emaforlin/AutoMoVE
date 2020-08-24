import pyKey
import socket
from tkinter import ttk
from tkinter import *
from random import randint
from time import sleep

moves = ['w','a','s','d']

qty_moves = randint(3,10)


class Character:
    def __init__(self, window):
        self.wind = window
        self.wind.title('Stay AFK')
        frame = LabelFrame(self.wind, text='Anti(AntiAFK) Modes')
        frame.grid(row=0, column=0 ,columnspan=3, pady=20)

        # Mode Buttons
        #Label(frame, text='Anti(antiAFK) Modes:').grid(row=0,column=0, rowspan=1)
        ttk.Button(frame, text='Random', command=lambda: self.move(self.get_nextMove(moves, qty_moves))).grid(row=3, column=0, pady=5)
        ttk.Button(frame, text='Walk', command=lambda: self.walk()).grid(row=3, column=1, pady=5)

        # Stop Button
        ttk.Button(frame, text='Stop').grid(row=4, columnspan=2, pady=10 ,sticky=W+E)

        # Message Output
        log = self.message = Label(text='', fg='green')
        log.grid(row=3, column=0, columnspan=2, pady=20, sticky=W+E)


    def move(self, moves):
        sleep(15)
        while not stop():
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
        #print(next_move)
        return next_move

    def stop():
        return False
window = Tk()
app = Character(window)
window.mainloop()

'''
while True:
    move = person.get_nextMove(moves, qty_moves)
    person.move(move)
    sleep(30)
'''
