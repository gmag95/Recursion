#!/usr/bin/env python
# coding: utf-8

#this function checks whether the box selected is valid or not

def safe(board, x, y):
    
    if (x>=0 and y>=0 and x<n and y<n and board[x][y]==-1):
        return True
    else:
        return False

#this function prints the board with all the steps taken

def printer(board):
    
    for x in range(n):
        for y in range(n):
            print(board[x][y], end=" ")
        print()

#this is the recursive function used to solve the problem

def solvefunc(board, curr_x, curr_y, move):

    #if all the checkerboard boxes have been visited, the algorithm is stopped
    
    if move==n**2:
        return True
    
    for i in range(len(move_x)):

        #next step considered
        
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        
        if safe(board, new_x, new_y):

            #if the move was valid, update the path traced

            board[new_x][new_y]=move

            #the recursive function is called

            if solvefunc(board, new_x, new_y, move+1):
                return True
            else:
                
                #backtracking part of the algorithm

                board[new_x][new_y]=-1
    return False

#checherboard initialization

n=5

board=[[-1 for i in range(n)] for i in range(n)]

move_x=[2, 1, -1, -2, -2, -1, 1, 2]
move_y=[1, 2, 2, 1, -1, -2, -2, -1]

#data validation for the starting row

start_x=None

while isinstance(start_x, int)==False or start_x>=5 or start_x<0:
    try:
        start_x = int(input("Insert the row of the starting box (1-5): "))-1
    except:
        continue

#data validation for the starting column

start_y=None

while isinstance(start_y, int)==False or start_y>=5 or start_y<0:
    try:
        start_y = int(input("Insert the column of the starting box(1-5): "))-1
    except:
        continue

board[start_x][start_y]=0

move=1

#ending message

if solvefunc(board, start_x, start_y, move)==False:
    print("There is no solution for this starting point")
else:
    printer(board)