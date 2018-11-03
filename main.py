import numpy as np

Row = 6
Col = 6

def gen_board(row = 6 , col = 6):                         #generates board of 6 X 6 by default
    board = np.zeros((row,col))
    global Row 
    Row = row
    global Col 
    Col = col
    return board

def ins_piece(board , row , col , piece):
    board[row][col] = piece

def is_loc_valid(board , col):
    if (col <= Col-1):
        if(board[Row-1][col]) == 0:
            return True
    else:
        return False

def get_next_open_row(board , col):
    for r in range(Row-1):
        if board[r][col] == 0:
            return r
    return False        

def print_flipped_board(board):
    print(np.flip(board , 0))


board = gen_board()                     #generated a board

print(board)                            #printing the board

GameOver = False                        #Game Over variable

turn = 1                                #Turn Counter

while not GameOver:                     #Unless Game Over

    if( turn % 2 != 0):                 #Player One's Turn
        move1 = int(input("\n Turn No : " + str(turn) + "\tEnter your move Player One\t")) - 1
        print("\n Turn No : " + str(turn) + "\t Player One's move : column " + str(move1+1) + "\n")
        if is_loc_valid(board , move1):
            row = get_next_open_row(board , move1)
            ins_piece(board , row , move1 , 1)
        else:
            print("Invalid Move, Please Enter Again")
            # turn += 1
            continue
        print_flipped_board(board)

    else:                               #Playe Two's Turn
        move2 = int(input("\n Turn No : " + str(turn) + "\tEnter your move Player Two\t")) - 1
        print("\n Turn No : " + str(turn) + "\t Player Two's move : column " + str(move2+1) + "\n")
        if is_loc_valid(board , move2):
            row = get_next_open_row(board , move2)
            ins_piece(board , row , move2 , 2)
        else:
            print("Invalid Move, Please Enter Again")
            # turn += 1
            continue
        print_flipped_board(board)

    turn += 1