"""
Eduardo Saldana Suarez
6612626
Python
Done in Visual Studio Code

To test this program just run it normally and input the number of column you wish to play
"""

import math
import random
import time
from copy import deepcopy

# This number determines how many moves ahead the program will plan ahead
# Increase it for a more difficult AI or decrease it for an easier one
# Increasing the DEPTH variable beyond 6 makes the program extremly slow
DEPTH = 5
difficulty = None

# Creates a board with 6 Rows ans 7 Columns
def make_board():
    board = []
    for x in range (6):
        board.append([" "," "," "," "," "," "," "])
    return board

def display(board):
    for x in range (6):
        print()
        if x==0:
            print(" 1 2 3 4 5 6 7")
        print("|",end="")
        for y in range (7):
            print(board[x][y]+"|", end="")

def move(board, col, letter):
    # Inputs the player symbol into the first available space in the column
    for x in range(6):
        if board[5-x][col-1] ==" ":
            board[5-x][col-1] = letter
            return board
            break
    

def check_winner(board, end):
    #Horizontal check
    for y in range(6):
        for x in range(7):
            if x<4 and board[y][x]!=" ":
                if board[y][x]==board[y][x+1]==board[y][x+2]==board[y][x+3]:
                    #print("Winner is "+board[y][x])
                    if end:
                        return True
                    else:
                        return board[y][x]

    #Vertical check
    for y in range(6):
        for x in range(7):
            if y<3 and board[y][x]!=" ":
                if board[y][x]==board[y+1][x]==board[y+2][x]==board[y+3][x]:
                    #print("Winner is "+board[y][x])
                    if end:
                        return True
                    else:
                        return board[y][x]

    #Diagonal from Left-Top to Right-Bottom
    for y in range(6):
        for x in range(7):
            if x<4 and y<3 and board[y][x]!=" ":
                if board[y][x]==board[y+1][x+1]==board[y+2][x+2]==board[y+3][x+3]:
                    #print("Winner is "+board[y][x])
                    if end:
                        return True
                    else:
                        return board[y][x]
    
    #Diagonal from Left-Bottom to Right-Top
    for y in range(6):
        for x in range(7):
            if x<4 and y>2 and board[y][x]!=" ":
                if board[y][x]==board[y-1][x+1]==board[y-2][x+2]==board[y-3][x+3]:
                    #print("Winner is "+board[y][x])
                    if end:
                        return True
                    else:
                        return board[y][x]
                
# Returns true if all the columns are filled to the top
def is_full(board):
    for x in range(7):
        if board[0][x]==" ":
            return False
    return True


# Returns possible moves
def possible_moves(board):
    possibilities = []
    for x in range(6):
        if board[5-x][0]==" ":
            possibilities.append(0)
            break
    for x in range(6):
        if board[5-x][1]==" ":
            possibilities.append(1)
            break
    for x in range(6):
        if board[5-x][2]==" ":
            possibilities.append(2)
            break
    for x in range(6):
        if board[5-x][3]==" ":
            possibilities.append(3)
            break
    for x in range(6):
        if board[5-x][4]==" ":
            possibilities.append(4)
            break
    for x in range(6):
        if board[5-x][5]==" ":
            possibilities.append(5)
            break
    for x in range(6):
        if board[5-x][6]==" ":
            possibilities.append(6)
            break
    return possibilities

# Heuristic function
def heuristic(board):

    points = 0

    '''
    Explanation on Heuristic:

    The program checks on all possible directions for current locations where either the player or the AI have placed their chips and could possibly extend their line.
    It gives more points for chains of chips that are already placed which means it gives a lot of positive or negative points in an scenario where 4 chips are already aligned
    and gives way less points for places where chips COULD be aligned but currently arent

    '''

    #Horizontal check
    # The horizontal check has extra conditonals to check for empty spaces of both sides unlike the vertical directon
    for y in range(6):
        for x in range(7):
            if x<4:
                if board[y][x]==board[y][x+1]==board[y][x+2]==board[y][x+3]:
                    if board[y][x]=="X":
                        points = points-300
                    elif board[y][x]=="O":
                        points = points+301
                elif (board[y][x]==board[y][x+1]==board[y][x+2] and board[y][x+3]==" ") or (board[y][x+3]==board[y][x+1]==board[y][x+2] and board[y][x]==" "):
                    if board[y][x]=="X" or board[y][x+3]=="X":
                        points = points-25
                    elif board[y][x]=="O" or board[y][x+3]=="O":
                        points = points+26
                elif (board[y][x]==board[y][x+1] and board[y][x+2]==board[y][x+3]==" ") or (board[y][x]==board[y][x+1]==" " and board[y][x+2]==board[y][x+3]):
                    if board[y][x]=="X" or board[y][x+3]=="X":
                        points = points-10
                    elif board[y][x]=="O"  or board[y][x+3]=="O":
                        points = points+11

    #Vertical check
    for y in range(6):
        for x in range(7):
            if y<3 and board[y][x]!=" ":
                if board[y][x]==board[y+1][x]==board[y+2][x]==board[y+3][x]:
                    if board[y][x]=="X":
                        points = points-300
                    elif board[y][x]=="O":
                        points = points+301
                elif board[y][x]==board[y+1][x]==board[y+2][x] and board[y+3][x]==" ":
                    if board[y][x]=="X":
                        points = points-25
                    elif board[y][x]=="O":
                        points = points+26
                elif board[y][x]==board[y+1][x] and board[y+2][x]==board[y+3][x]==" ":
                    if board[y][x]=="X":
                        points = points-10
                    elif board[y][x]=="O":
                        points = points+11

    #Diagonal from Left-Top to Right-Bottom
    for y in range(6):
        for x in range(7):
            if x<4 and y<3: 
                if board[y][x]==board[y+1][x+1]==board[y+2][x+2]==board[y+3][x+3]:
                    if board[y][x]=="X":
                        points = points-300
                    elif board[y][x]=="O":
                        points = points+301
                elif (board[y][x]==board[y+1][x+1]==board[y+2][x+2] and board[y+3][x+3]==" ") or (board[y+3][x+3]==board[y+1][x+1]==board[y+2][x+2] and board[y][x]==" "):
                    if board[y][x]=="X" or board[y+3][x+3]=="X":
                        points = points-25
                    elif board[y][x]=="O"  or board[y+3][x+3]=="O":
                        points = points+26
                elif (board[y][x]==board[y+1][x+1] and board[y+2][x+2]==board[y+3][x+3]==" ") or (board[y][x]==board[y+1][x+1]==" " and board[y+2][x+2]==board[y+3][x+3]):
                    if board[y][x]=="X" or board[y+3][x+3]=="X":
                        points = points-10
                    elif board[y][x]=="O"  or board[y+3][x+3]=="O":
                        points = points+11

    #Diagonal from Left-Bottom to Right-Top
    for y in range(6):
        for x in range(7):
            if x<4 and y>2: 
                if board[y][x]==board[y-1][x+1]==board[y-2][x+2]==board[y-3][x+3]:
                    if board[y][x]=="X":
                        points = points-300
                    elif board[y][x]=="O":
                        points = points+301
                elif (board[y][x]==board[y-1][x+1]==board[y-2][x+2] and board[y-3][x+3]==" ") or (board[y-3][x+3]==board[y-1][x+1]==board[y-2][x+2] and board[y][x]==" "):
                    if board[y][x]=="X" or board[y-3][x+3]=="X":
                        points = points-25
                    elif board[y][x]=="O" or board[y-3][x+3]=="O":
                        points = points+26
                elif (board[y][x]==board[y-1][x+1] and board[y-2][x+2]==board[y-3][x+3]==" ") or (board[y][x]==board[y-1][x+1]==" " and board[y-2][x+2]==board[y-3][x+3]):
                    if board[y][x]=="X" or board[y-3][x+3]=="X":
                        points = points-10
                    elif board[y][x]=="O" or board[y-3][x+3]=="O":
                        points = points+11
                
    return points
 


# AI MOVE MINMAX

def minimax(depth, board, maximizing, alpha, beta):
    moves = possible_moves(board)

    if depth==0 or len(moves)==0:
        return heuristic(board), None

    #Maximizing player
    if maximizing:
        max_value = -99999999999999
        pick = random.choice(moves)
        for x in moves:
            fake_board = deepcopy(board)
            move(fake_board,x+1,"O")
            # We obtain the boards heuristic value
            new_number = minimax(depth-1,fake_board,False, alpha, beta)[0]
            
            if (new_number>max_value):
                max_value = new_number
                pick = x
            alpha = max(alpha,max_value)
            if alpha>=beta:
                break
        return max_value, pick

    # Minimizing player
    else:
        min_value = 99999999999999
        pick = random.choice(moves)
        for x in moves:
            fake_board = deepcopy(board)
            move(fake_board,x+1,"X")
            # We obtain the boards heuristic value
            new_number = minimax(depth-1,fake_board,True, alpha, beta)[0]
            if (new_number<min_value):
                min_value = new_number
                pick = x
            beta = min(beta, min_value)
            if alpha>=beta:
                break
        return min_value, pick
        
            


main_board = make_board()


# HUMAN PLAYER WILL BE "X" AND AI WILL "O"
# HUMAN PLAYER WILL ALWAYS GO FIRST
while True:
        try:
            difficulty = int(input("Enter Difficulty (1-Easy 2-Medium 3-Hard): "))
            if difficulty>3 or difficulty<1:
                raise Exception
            break
        except:
            pass

if difficulty==1:
    DEPTH=2
elif difficulty==2:
    DEPTH=4
else:
    DEPTH=6


display(main_board)
print()
while True:
    # Validating user input
    while True:
        try:
            col = int(input("Enter Column (1-7): "))
            if col>7 or col<1:
                raise Exception
            break
        except:
            pass
    move (main_board, col, "X")
    display(main_board)
    print()
    end = check_winner(main_board, True)
    if end:
        print("\nThanks for playing, X wins")
        time.sleep(2)
        break
    # Creates a copy of the board for the AI to plan its moves so it does not affect the real board
    fake = main_board.copy()
    # Calls the AI to play its turn
    pick = minimax(DEPTH,fake,True, -math.inf, math.inf)[1]
    move (main_board, pick+1, "O")
    print("AI chose column: "+str(pick+1))
    display(main_board)
    print()
    end = check_winner(main_board, True)
    if end:
        print("\n Thanks for playing, O wins")
        time.sleep(2)
        break
   
    

