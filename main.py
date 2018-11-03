import numpy as np

def gen_board(row = 6 , col = 6):                         #generates board of 6 X 6 by default
    board = np.zeros((row,col))
    return board

def drop_piece():
    pass

def is_loc_valid():
    pass

def get_next_open_row():
    pass


board = gen_board()                     #generated a board

GameOver = False                        #Game Over variable

turn = 1                                #Turn Counter

while not GameOver:                     #Unless Game Over

    if( turn % 2 != 0):                 #Player One's Turn
        move1 = int(input("Enter your move Player One"))
        print(" Player One's move : " + str(move1))

    else:                               #Playe Two's Turn
        move2 = int(input("Enter your move Player Two"))
        print(" Player Two's move : " + str(move2))

    turn += 1