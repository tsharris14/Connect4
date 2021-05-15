# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 00:24:06 2019

@author: TaCoya Harris & Lucas Yeend
"""
"""The AI blocks vertical and horizontal moves"""
"--------------------Functions----------------------------------"

import random

def displayBoard(board):
    #board is a 2d list 
    #display the board in a matrix format
    
    for i in range(6): #rows
        
        print("|",end="")
        for j in range(7): #cols
            print(board[i][j],end='|')
        print("")
    print("---------------")
    
def checkRow(board):
    validColumn = False #column is full
    while(True): #while validColumn is false
        col = int(input("X: Enter col#:"))#player input col
        for i in range(5,-1,-1):#for each row, start at the last row and check the entire row
            if (board[i][col] == ' '): #available spot
                board[i][col] = 'X' #mark spot
                validColumn=True #raise the flag 
                break
        if (validColumn):#True
            displayBoard(board)
            break
        else:#False
           print("Full")
           
               
def checkWin(board):#checks win for player turn
    
    #horizontal 
    for j in range(4): #for each set of 4 columns
        for i in range(6): #for all 6 rows
            if (board[i][j]=='X' and board[i][j+1]=='X' and board[i][j+2]=='X' and board[i][j+3]=='X'):
                return True#win
    
    #vertical
    for i in range(3): #for each set of 4 rows
        for j in range(7):#for all 7 columns
            if (board[i][j]=='X' and board[i+1][j]=='X' and board[i+2][j]=='X' and board[i+3][j]=='X'):
                return True#win

    #Diagonals downwards
    for j in range(4): #for each set of 4 columns
        for i in range(3):#for rows 0,1,3 add one row, add one col
            if (board[i][j]=='X' and board[i+1][j+1] == 'X' and board[i+2][j+2]=='X'and board[i+3][j+3]=='X'):
                return True#win
            
    #Diagnonals upwards
    for j in range(4): #for each set of 4 columns
        for i in range(3,6):#for rows 3,4,5 subtract one row, add a col 
            if (board[i][j]=='X' and board[i-1][j+1] == 'X' and board[i-2][j+2]=='X'and board[i-3][j+3]=='X'):#move down and to the right
                return True#win
        
       
    
def Ai(board):
    validColumn = False #Flag to get out of a loop
    
    #Horizontal Competiveness
    for j in range(4): #for each set of 4 columns
        for i in range(6): #for all 6 rows
            if (board[i][j]==' ' and board[i][j+1]=='X' and board[i][j+2]=='X' and board[i][j+3]=='X' and board[i-1][j] != ' '):
                board[i][j] = 'O'
                validColumn = True
                break
            if (board[i][j]=='X' and board[i][j+1]==' ' and board[i][j+2]=='X' and board[i][j+3]=='X'and board[i-1][j+1] != ' '):
                board[i][j+1] = 'O'
                validColumn = True
                break
            if(board[i][j]=='X' and board[i][j+1]=='X' and board[i][j+2]==' ' and board[i][j+3]=='X' and board[i-1][j+2] != ' '):
                board[i][j+2] = 'O'
                validColumn = True
                break
            if(board[i][j]=='X' and board[i][j+1]=='X' and board[i][j+2]=='X' and board[i][j+3]==' ' and board[i-1][j+3] != ' ' ):
                board[i][j+3] = 'O'
                validColumn = True
                break
        if(validColumn):#True
            displayBoard(board)
            break
        
            
    #vertical
    for i in range(5,-1,-1): #for rows 5 to 0 (going up each column)
        for j in range(7):#for all 7 columns
            if (board[i][j]=='X' and board[i-1][j]=='X' and board[i-2][j]=='X' and board[i-3][j]==' '):
                board[i-3][j] = 'O'
                validColumn = True
                break
        if(validColumn):#True
            displayBoard(board)
            break
    
        
    if(validColumn == False): #if there are no places to block X, make random move
        while(True):
            col = random.randint(0,6)#any random column
            for k in range(5,-1,-1):#for rows 5 to 0 (going up each column)
                if (board[k][col] == ' '): #available spot
                    board[k][col] = 'O' #mark spot
                    validColumn=True #raise the flag 
                    break
            if (validColumn):#True
                displayBoard(board)
                break
       
        
        
    
def aiWin(board):
    #horizontal 
    for j in range(4): #for each set of 4 columns
        for i in range(6): #for all 6 rows
            if (board[i][j]=='O' and board[i][j+1]=='O' and board[i][j+2]=='O' and board[i][j+3]=='O'):
                return True
    
    #vertical
    for i in range(3): #for each set of 4 rows
        for j in range(7):#for all 7 columns
            if (board[i][j]=='O' and board[i+1][j]=='O' and board[i+2][j]=='O' and board[i+3][j]=='O'):
                return True

    #Diagonals downwards
    for j in range(4): #for each set of 4 columns
        for i in range(3):#for rows 0,1,2, add one row, add one col
            if (board[i][j]=='O' and board[i+1][j+1] == 'O' and board[i+2][j+2]=='O'and board[i+3][j+3]=='O'):
                return True
            
    #Diagnonals upwards
    for j in range(4): #for each set of 4 columns
        for i in range(3,6):#for rows 3,4,5 subtract one row, add a col 
            if (board[i][j]=='O' and board[i-1][j+1] == 'O' and board[i-2][j+2]=='O'and board[i-3][j+3]=='O'):
                return True
    
    

"---------------------Main----------------------------------------"

gameBoard = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], 
             [' ', ' ', ' ', ' ', ' ', ' ', ' '], 
             [' ', ' ', ' ', ' ', ' ', ' ', ' '], 
             [' ', ' ', ' ', ' ', ' ', ' ', ' '], 
             [' ', ' ', ' ', ' ', ' ', ' ', ' '], 
             [' ', ' ', ' ', ' ', ' ', ' ', ' ']]

displayBoard(gameBoard)#displays board

turns = 0
while(True):  
    
    if (checkRow(gameBoard)): #if space was available
            turns = turns + 1
            
    if (checkWin(gameBoard)):
        print ("You win!")
        break
    
    if(Ai(gameBoard)):
        turns = turns + 1

    if(aiWin(gameBoard)):
        print("Ai Wins!")
        break   
    
    if (turns == 42):
        print ("Tie!")
        break
