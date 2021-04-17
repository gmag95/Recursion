#!/usr/bin/env python
# coding: utf-8

#this function checks whether the adjacent cell is valid or not

def safe(x, y):
    
    if x>=0 and y>=0 and x<len_x and y<len_y and board[x][y]==0 and path[x][y]==0:
        print(f"Coordinates {x}, {y} are ok")
        return True
    else:
        print(f"Coordinates {x}, {y} are not ok")
        return False

#this function prints the maze and the path traced so far

def printer(table):

    for x in range(len_x):
        for y in range(len_y):
            print(table[x][y], end=" ")
        print()

#this function executes the recursive algorithm used to find the path to the end of the maze

def myfunc(curr_x, curr_y):
    
    print(f"I'm currently in {curr_x}, {curr_y}")
    
    print("---")
    printer(path)
    print("---")
    
    #if the exit is reached, stop the algorithm

    if curr_x==end_x and curr_y==end_y:
        return True
    
    for i in range(4):
        
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        
        print(f"I'm trying coordinates {new_x}, {new_y}")
        
        if safe(new_x, new_y):

            #if the cell examined is valid use a recursive function to find the next step
            
            path[new_x][new_y]="*"
            
            if myfunc(new_x, new_y):
                return True
            
            else: 
                
                #if there is a roadblock backtrack to the previous step

                print("Roadblock")
                path[new_x][new_y]=0
    
    return False

#board initialization

board=[[0,"X","X","X"],[0,0,0,0],["X",0,"X",0],[0,0,0,0]]

len_x=len(board)
len_y=len(board[0])

printer(board)

path=board

move_x=[0,1,0,-1]
move_y=[-1,0,1,0]

#data validation for the starting point

start_x=10
start_y=10
start_list=[]

while isinstance(start_x, int)==False or isinstance(start_y, int)==False or len(start_list)!=3 or start_x<0 or start_x>3 or start_y<0 or start_y>3 or board[start_x][start_y]=="X":
    try:
        start_list=input("Insert the start coordinates (1-4) separated by a space: ")
        start_x, start_y = start_list.split()
        start_x=int(start_x)-1
        start_y=int(start_y)-1
    except:
        continue

#data validation for the ending point

end_x=10
end_y=10
end_list=[]

while isinstance(end_x, int)==False or isinstance(end_y, int)==False or len(start_list)!=3 or end_x<0 or end_x>3 or end_y<0 or end_y>3 or board[end_x][end_y]=="X":
    try:
        end_list=input("Insert the end coordinates (1-4) separated by a space: ")
        end_x, end_y = end_list.split()
        end_x=int(end_x)-1
        end_y=int(end_y)-1

    except:
        continue

path[start_x][start_y]="*"

#ending message

if myfunc(start_x, start_y):
    print("Path found")
else:
    print("There is no solution")