#!/usr/bin/env python
# coding: utf-8

# # TIC TAC TOE GAME

# In[1]:


import random


# In[2]:


#CREATE A BOARD
board=["-","-","-",
      "-","-","-",
      "-","-","-"]


# In[3]:


currentPlayer="X"
winner=None
gameRunning=True


# In[4]:


def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# In[5]:


# TAKE PLAYER INPUT
def playerInput(board):
    inp = int(input("Select a spot from 1-9: "))
    if board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops player is already at that spot.")


# In[6]:


# check for win or tie
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


# In[7]:


def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True


# In[8]:


def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True


# In[9]:


def checkIfWin(board):
    global gameRunning
    if checkHorizontle(board):
        printBoard(board)
        print(f" winner is {winner}!")
        gameRunning = False

    elif checkRow(board):
        printBoard(board)
        print(f" winner is {winner}!")
        gameRunning = False

    elif checkDiag(board):
        printBoard(board)
        print(f" winner is {winner}!")
        gameRunning = False


# In[10]:


def checkIfTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False


# In[11]:


# SWITCH PLAYER
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


# In[12]:


def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


# In[13]:


while gameRunning:
    printBoard(board)
    playerInput(board)
    checkIfWin(board)
    checkIfTie(board)
    switchPlayer()
    computer(board)
    checkIfWin(board)
    checkIfTie(board)
     


# In[ ]:




