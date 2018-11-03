import numpy as np

Row = 6
Col = 6

def gen_board(row = 6 , col = 6):                         #generates board of 6 X 6 by default
    board = np.zeros((row,col))
    global Row 
    Row = row-1
    global Col 
    Col = col-1
    return board

def ins_piece(board , row , col , piece):
    board[row][col] = piece

def is_loc_valid(board , col):
    if(board[Row][col]) == 0:
        return True

def get_next_open_row(board , col):
    for r in range(Row):
        if board[r][col] == 0:
            return r


board = gen_board()                     #generated a board

print(board)                            #printing the board

GameOver = False                        #Game Over variable

turn = 1                                #Turn Counter

while not GameOver:                     #Unless Game Over

    if( turn % 2 != 0):                 #Player One's Turn
        move1 = int(input("Enter your move Player One\t")) - 1
        print("\n Player One's move : " + str(move1) + "\n\n")
        if is_loc_valid(board , move1):
            row = get_next_open_row(board , move1)
            ins_piece(board , row , move1 , 1)
        print(board)

    else:                               #Playe Two's Turn
        move2 = int(input("Enter your move Player Two\t")) - 1
        print(" Player Two's move : " + str(move2) + "\n\n")
        if is_loc_valid(board , move2):
            row = get_next_open_row(board , move2)
            ins_piece(board , row , move2 , 2)
        print(board)

    turn += 1