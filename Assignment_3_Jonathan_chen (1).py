#Assignment3.py
from random import randint
import time
import random 

#header for Project




print('''
+----------------------------------------------------+
|      Computer Science and Engineering              |
|     CSCE 1035.001 - Computer Programming I         |
|  Jonathan Chen  jec0412  joanthanchen3@my.unt.edu  |
+----------------------------------------------------+ 
''')


# Battleship game title 

print('''
+------------------------------------------------------------------+
|                                  )___(                           |
|                           _______/__/_                           |
|  ____       __   [\\\]___/____________|__[///]                    |
|  \   \_____[\\]__/___________________________\__[//]___           |
|   \ 40-A                                               |         |
|    \           WELCOME TO THE GAME BATTLESHIP          /         |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
+------------------------------------------------------------------+
''')

#Game instructions 
print('''
+-------------------------------------------------------------+ 
| This program will randomly choose two ships from your fleet | 
| made up of the following vessels: Carrier, Battleship, Sub- | 
| marine, and Destroyer. It will then randomly assign both of | 
| the vessels to the board that are oriented either vertical- | 
| ly or horizontally. As a player you will then have up to 20 | 
| tries to sink both of the computer's vessels                | 
+-------------------------------------------------------------+ 


''')
# Game information 
print(''' 
+----------------------------------------------------------------------------+
|                             *** Legend ***                                 |
|   1. "-" = water/ empty space                                              |
|   2. "O" = water that was shot with bullet, but did not hit meaning no hit |
|   3. "X" = part of ship that was hit with a bullet.                        |
|   4. "S" = a part of ship                                                    |
|                            *** Good Luck ***                               |
+----------------------------------------------------------------------------+
''')

#Code for the game 

#makes sure the randomization selection is based of the time the program is being ran so that
#it that it is less likey to repeat the same location 






random.seed(time.time())
length_of_ships = [2,3,3,4,5]


  



#this is the board that hold the location of the ship   
game_board = [['']* 9 for x in range (9)]
#this boards will used to allow the player to guess where the ships are
ship_board = [['']* 9 for x in range (9)]

letter_to_numbers = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8}

def print_board(board):
    print ("  A B C D E F G H I")
    print (" +------------------+")
    row_number = 1
    for row in board:
        print(str(row_number) + " | " + " | ".join(row) + "|")
        row_number += 1 
    
print_board(game_board)

def create_ships(board):
    pass


def place_ships(board):
    #loop through length of ships
    for ship_length in length_of_ships:
        #loop until ship fits and doesn't overlap
        while True:
            if board == game_board:
                orientation, row, column = random.choice(["H", "V"]), random.randint(0,7), random.randint(0,7)
                if check_ship_fit(ship_length, row, column, orientation):
                    #check if ship overlaps
                    if ship_overlaps(board, row, column, orientation, ship_length) == False:
                        #place ship
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "S"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "S"
                        break

#check if ship fits in board
def check_ship_fit(SHIP_LENGTH, row, column, orientation):
    if orientation == "H":
        if column + SHIP_LENGTH > 9:
            return False
        else:
            return True
    else:
        if row + SHIP_LENGTH > 9:
            return False
        else:
            return True
                    
#check each position for overlap
def ship_overlaps(board, row, column, orientation, ship_length):
    if orientation == "H":
        for i in range(column, column + ship_length):
            if board[row][i] == "X":
                return True
    else:
        for i in range(row, row + ship_length):
            if board[i][column] == "X":
                return True
    return False

def get_ship_location():
    row = input("Enter the row of the ship: ").upper()
    while row not in "12345678":
        print('Not an appropriate choice, please select a valid row')
        row = input("Enter the row of the ship: ").upper()
    column = input("Enter the column of the ship: ").upper()
    while column not in "ABCDEFGH":
        print('Not an appropriate choice, please select a valid column')
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, letter_to_numbers[column]

debug_mode = True


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count



if __name__ == "__main__":
    create_ships(game_board)
    turns = 20
    while turns > 0:
        print('Guess a battleship location')
        print_board(ship_board)
        row, column = get_ship_location()
        if ship_board[row][column] == "-":
            print("You guessed that one already.")
        elif ship_board[row][column] == "X":
            print("Hit")
            ship_board[row][column] = "X" 
            turns -= 1  
        else:
            print("MISS!")
            ship_board[row][column] = "O"   
            turns -= 1     
        if count_hit_ships(ship_board) == 2:
            print("You win!")
            break
        print("You have " + str(turns) + " turns left")
        if turns == 0:
            print("You ran out of turns")

