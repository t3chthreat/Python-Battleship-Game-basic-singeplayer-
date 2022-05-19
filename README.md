# Python-Battleship-Game-basic-singeplayer-
PROGRAM DESCRIPTION:
In this Python 3 program I designed  a simplified version of the
classic Battleship game. In this program, you will randomly assign two vessels from a
fleet consisting of an aircraft carrier, a battleship, a submarine, and a destroyer on an 8
by 8 game board implemented as a nested list. Game play will consist of 20 turns to try
and locate, and thus sink, the two vessels.
The board will visually appear like the classic Battleship game as follows, using the
number indexing 1 through 9 for rows and letter indexing A through I for columns:
A B C D E F G H I
1 - - - - - - - - -
2 - - - C C C C C -
3 - - - - - - - - -
4 - S - - - - - - -
5 - S - - - - - - -
6 - S - - - - - - -
7 - - - - - - - - -
8 - - - - - - - - -
9 - - - - - - - - -
In the game board, the 5 C’s represent a randomly generated aircraft carrier placed
horizontally having a total length of 5 units, while the 3 S’s represent a randomly
generated submarine placed vertically having a total length of 3 units. The aircraft
carrier, for example, in this case is located at elements B3, B4, B5, B6, and B7.
Each position on the game board may be displayed as one of the following values
according to the rules of the game:
– the initial value of each element on the game board indicating an empty
space where no vessel is present and no shot has been fired
O a shot has been fired, but no vessel is present, at this location
X a shot has been fired and a vessel is present at this location
C an aircraft carrier is present, but no shot has been fired at this location
B a battleship is present, but no shot has been fired at this location
S a submarine is present, but no shot has been fired at this location
D a destroyer is present, but no shot has been fired at this location


REQUIREMENTS:


• At a minimum, you will be required to define the following three functions:

- You will define a new function to print the game board that accepts at least two
arguments, the game board as a nested list and a Boolean value that is used to
indicate whether or not to “reveal” the solution with the ship positions visible.

-The function will print the current game board, showing empty values ('–'),
misses ('O'), hits ('X'), and possibly vessel data depending on whether or not
the reveal argument is set to True or False. If the reveal argument is set
False, you will display an empty value ('–') in place of any active, not hit,
vessels so as to not reveal the locations of the vessels on the game board. 
If the reveal argument is set to True, you will display the vessel location for
each position containing a vessel that has not been hit. 

You will call this function to display the updated board prior to the first shot
and then after every shot is fired by the user. During the game, the reveal
argument should be set to False. 

However, if the user loses the game, you will call this function with the reveal argument set to True to reveal the vessel
locations on the game board.

- You will define a new function to select and assign vessels on the game board
that accepts at least one argument, the game board as a nested list.

- You will use a nested dictionary to keep the data associated with each of two
vessels that will be selected and assigned to the game board. At a minimum,
the data for each vessel should include the 'name', 'length', and
'orientation'.

- For the ship selection, 'ship1' will be randomly chosen between a 5-unit
length aircraft carrier or a 4-unit length battleship. Similarly, 'ship2' will
be randomly chosen between a 3-unit length submarine or a 2-unit length
destroyer. For both ships, the orientation will be randomly chosen to be
either vertical or horizontal.

- For the ship assignment to its location on the game board, the starting
location row and column of each ship will be randomly chosen and will use
the orientation determined during the ship’s selection. Additionally, the
ships may not overlap and must not go beyond the length of the game
board.

- You will define a new function to determine the result of the latest torpedo shot
that accepts at least two arguments, the game board as a nested list and the
torpedo shot position, which may be sent separately or together in a string or
integer format.

- If a location where a ship is currently present is hit, you will mark its location
on the game board with an 'X' indicating that the ship has been hit. You will
need to keep a shot counter for each ship that records each time that ship
has been hit. 

A ship is sunk once all of its locations on the game board have
been hit and are marked with an 'X', which is the length of the ship.

 If an empty location (i.e., '–') is hit, you will mark its location on the game
board with an 'O' indicating that the shot missed.

 If a location that has been previously hit and currently already marked with
either an 'O' or an 'X', no action needs to be taken as this represents a
wasted shot.

You may add any number of supporting functions in addition to these three new
functions. You may also pass any additional arguments to the function or return any
data from the function.


- In the main part of your program, you will do the following:
 Print the game introduction, providing any necessary details about the game.


- Create and initialize the 9-by-9 game board using a nested list, assigning an
empty space to each position on the board.

;
- Call the function to select and assign the two ships to the game board and then
call the function to print the game board to start the game.


- Use a loop to play the game until either the player has sunk both ships and won
or has taken 20 turns and lost without sinking both ships. For each turn, the
player will enter a two character position for the row and column (e.g., 'B4')
corresponding to the position on the game board where the torpedo will be fired.

§ 

You will validate the player input by creating your own custom exception for
length, type, and range/value input errors. When one of these exceptions
occurs, you will print the exception and the associated string and simply
resume the player’s turn by prompting the player to enter the position again,
without losing a turn.

§ After the player has entered the torpedo position, you will call the function to
determine the outcome of the shot, which may include keeping track of how
many ships have been sunk or how many successful torpedoes have been
fired upon each of the two ships.

§ Before prompt the player to enter the next set of coordinates for the torpedo,
call the function to print the game board.

- Once the game has ended, print out the appropriate message whether the player
has won or lost. If the player has lost, you must print out the game board again
with the locations of the ships revealed.

- For each move, you will display a status message, such as as “hit” or “miss”, and
include when the player has sunk a ship as well as won or lost the game.

- code should be well documented in terms of comments. For example, good
comments in general consist of a header 

 comments for each variable, and commented blocks of code. This
means that in addition to the program printing your information to the terminal (see
SAMPLE OUTPUT), some of this information will also appear in the code in the
comments as well.


SAMPLE OUTPUT (input shown in bold):
$ python3 project3.py
+--------------------------------------------+
| Computer Science and Engineering |
| CSCE 1035 - Computer Programming I |
| Student Name EUID euid@my.unt.edu |
+--------------------------------------------+
+-------------------------------------------------------------+
| This program will randomly choose two ships from your fleet |
| made up of the following vessels: Carrier, Battleship, Sub- |
| marine, and Destroyer. It will then randomly assign both of |
| the vessels to the board that are oriented either vertical- |
| ly or horizontally. As a player you will then have up to 20 |
| tries to sink both of the computer's vessels |
+-------------------------------------------------------------+
 A B C D E F G H I
 +-------------------+
1 | - - - - - - - - - |
2 | - - - - - - - - - |
3 | - - - - - - - - - |
4 | - - - - - - - - - |
5 | - - - - - - - - - |
6 | - - - - - - - - - |
7 | - - - - - - - - - |
8 | - - - - - - - - - |
9 | - - - - - - - - - |
 +-------------------+
Enter position to fire torpedo #1 (e.g., B5): A14
PositionLengthError: Invalid position length: 3
Enter position to fire torpedo #1 (e.g., B5): K7
PositionColumnError: Invalid position column value: K
Enter position to fire torpedo #1 (e.g., B5): K10
PositionLengthError: Invalid position length: 3
Enter position to fire torpedo #1 (e.g., B5): 19
PositionColumnError: Invalid position column value: 1
Enter position to fire torpedo #1 (e.g., B5): AX
PositionRowError: Invalid position column value: X
Enter position to fire torpedo #1 (e.g., B5): B4
Hit... nice shot!
CSCE 1035: Project 3
Due: 11:59 PM on Monday, May 2, 2022
6
 A B C D E F G H I
 +-------------------+
1 | - - - - - - - - - |
2 | - - - - - - - - - |
3 | - - - - - - - - - |
4 | - X - - - - - - - |
5 | - - - - - - - - - |
6 | - - - - - - - - - |
7 | - - - - - - - - - |
8 | - - - - - - - - - |
9 | - - - - - - - - - |
 +-------------------+
Enter position to fire torpedo #2 (e.g., B5): B1
Miss...
 A B C D E F G H I
 +-------------------+
1 | - O - - - - - - - |
2 | - - - - - - - - - |
3 | - - - - - - - - - |
4 | - X - - - - - - - |
5 | - - - - - - - - - |
6 | - - - - - - - - - |
7 | - - - - - - - - - |
8 | - - - - - - - - - |
9 | - - - - - - - - - |
 +-------------------+
Enter position to fire torpedo #3 (e.g., B5): C1
Miss...
 A B C D E F G H I
 +-------------------+
1 | - O O - - - - - - |
2 | - - - - - - - - - |
3 | - - - - - - - - - |
4 | - X - - - - - - - |
5 | - - - - - - - - - |
6 | - - - - - - - - - |
7 | - - - - - - - - - |
8 | - - - - - - - - - |
9 | - - - - - - - - - |
 +-------------------+
CSCE 1035: Project 3
Due: 11:59 PM on Monday, May 2, 2022
7
Enter position to fire torpedo #4 (e.g., B5): E1
Miss...
 A B C D E F G H I
 +-------------------+
1 | - O O - O - - - - |
2 | - - - - - - - - - |
3 | - - - - - - - - - |
4 | - X - - - - - - - |
5 | - - - - - - - - - |
6 | - - - - - - - - - |
7 | - - - - - - - - - |
8 | - - - - - - - - - |
9 | - - - - - - - - - |
 +-------------------+
Enter position to fire torpedo #5 (e.g., B5): G3
Miss...
 A B C D E F G H I
 +-------------------+
1 | - O O - O - - - - |
2 | - - - - - - - - - |
3 | - - - - - - O - - |
4 | - X - - - - - - - |
5 | - - - - - - - - - |
6 | - - - - - - - - - |
7 | - - - - - - - - - |
8 | - - - - - - - - - |
9 | - - - - - - - - - |
 +-------------------+
Enter position to fire torpedo #6 (e.g., B5): G7
Miss...
 A B C D E F G H I
 +-------------------+
1 | - O O - O - - - - |
2 | - - - - - - - - - |
3 | - - - - - - O - - |
4 | - X - - - - - - - |
5 | - - - - - - - - - |
6 | - - - - - - - - - |
7 | - - - - - - O - - |
8 | - - - - - - - - - |
9 | - - - - - - - - - |
 +-------------------+
CSCE 1035: Project 3
Due: 11:59 PM on Monday, May 2, 2022
8
Enter position to fire torpedo #7 (e.g., B5): I4
Miss...
 A B C D E F G H I
 +-------------------+
1 | - O O - O - - - - |
2 | - - - - - - - - - |
3 | - - - - - - O - - |
4 | - X - - - - - - O |
5 | - - - - - - - - - |
6 | - - - - - - - - - |
7 | - - - - - - O - - |
8 | - - - - - - - - - |
9 | - - - - - - - - - |
 +-------------------+
Enter position to fire torpedo #8 (e.g., B5): B8
Miss...
 A B C D E F G H I
 +-------------------+
1 | - O O - O - - - - |
2 | - - - - - - - - - |
3 | - - - - - - O - - |
4 | - X - - - - - - O |
5 | - - - - - - - - - |
6 | - - - - - - - - - |
7 | - - - - - - O - - |
8 | - O - - - - - - - |
9 | - - - - - - - - - |
 +-------------------+
Enter position to fire torpedo #9 (e.g., B5): A9
Miss...
 A B C D E F G H I
 +-------------------+
1 | - O O - O - - - - |
2 | - - - - - - - - - |
3 | - - - - - - O - - |
4 | - X - - - - - - O |
5 | - - - - - - - - - |
6 | - - - - - - - - - |
7 | - - - - - - O - - |
8 | - O - - - - - - - |
9 | O - - - - - - - - |
 +-------------------+
CSCE 1035: Project 3
Due: 11:59 PM on Monday, May 2, 2022
9
Enter position to fire torpedo #10 (e.g., B5): I9
Miss...
 A B C D E F G H I
 +-------------------+
1 | - O O - O - - - - |
2 | - - - - - - - - - |
3 | - - - - - - O - - |
4 | - X - - - - - - O |
5 | - - - - - - - - - |
6 | - - - - - - - - - |
7 | - - - - - - O - - |
8 | - O - - - - - - - |
9 | O - - - - - - - O |
 +-------------------+
Enter position to fire torpedo #11 (e.g., B5): I8
Miss...
 A B C D E F G H I
 +-------------------+
1 | - O O - O - - - - |
2 | - - - - - - - - - |
3 | - - - - - - O - - |
4 | - X - - - - - - O |
5 | - - - - - - - - - |
6 | - - - - - - - - - |
7 | - - - - - - O - - |
8 | - O - - - - - - O |
9 | O - - - - - - - O |
 +-------------------+
Enter position to fire torpedo #12 (e.g., B5): E8
Miss...
 A B C D E F G H I
 +-------------------+
1 | - O O - O - - - - |
2 | - - - - - - - - - |
3 | - - - - - - O - - |
4 | - X - - - - - - O |
5 | - - - - - - - - - |
6 | - - - - - - - - - |
7 | - - - - - - O - - |
8 | - O - - O - - - O |
9 | O - - - - - - - O |
 +-------------------+
CSCE 1035: Project 3
Due: 11:59 PM on Monday, May 2, 2022
10
Enter position to fire torpedo #13 (e.g., B5): G8
Miss...
 A B C D E F G H I
 +-------------------+
1 | - O O - O - - - - |
2 | - - - - - - - - - |
3 | - - - - - - O - - |
4 | - X - - - - - - O |
5 | - - - - - - - - - |
6 | - - - - - - - - - |
7 | - - - - - - O - - |
8 | - O - - O - O - O |
9 | O - - - - - - - O |
 +-------------------+
Enter position to fire torpedo #14 (e.g., B5): D9
Miss...
 A B C D E F G H I
 +-------------------+
1 | - O O - O - - - - |
2 | - - - - - - - - - |
3 | - - - - - - O - - |
4 | - X - - - - - - O |
5 | - - - - - - - - - |
6 | - - - - - - - - - |
7 | - - - - - - O - - |
8 | - O - - O - O - O |
9 | O - - O - - - - O |
 +-------------------+
Enter position to fire torpedo #15 (e.g., B5): A5
Miss...
 A B C D E F G H I
 +-------------------+
1 | - O O - O - - - - |
2 | - - - - - - - - - |
3 | - - - - - - O - - |
4 | - X - - - - - - O |
5 | O - - - - - - - - |
6 | - - - - - - - - - |
7 | - - - - - - O - - |
8 | - O - - O - O - O |
9 | O - - O - - - - O |
 +-------------------+
CSCE 1035: Project 3
Due: 11:59 PM on Monday, May 2, 2022
11
Enter position to fire torpedo #16 (e.g., B5): A6
Miss...
 A B C D E F G H I
 +-------------------+
1 | - O O - O - - - - |
2 | - - - - - - - - - |
3 | - - - - - - O - - |
4 | - X - - - - - - O |
5 | O - - - - - - - - |
6 | O - - - - - - - - |
7 | - - - - - - O - - |
8 | - O - - O - O - O |
9 | O - - O - - - - O |
 +-------------------+
Enter position to fire torpedo #17 (e.g., B5): I1
Miss...
 A B C D E F G H I
 +-------------------+
1 | - O O - O - - - O |
2 | - - - - - - - - - |
3 | - - - - - - O - - |
4 | - X - - - - - - O |
5 | O - - - - - - - - |
6 | O - - - - - - - - |
7 | - - - - - - O - - |
8 | - O - - O - O - O |
9 | O - - O - - - - O |
 +-------------------+
Enter position to fire torpedo #18 (e.g., B5): B5
Miss...
 A B C D E F G H I
 +-------------------+
1 | - O O - O - - - O |
2 | - - - - - - - - - |
3 | - - - - - - O - - |
4 | - X - - - - - - O |
5 | O O - - - - - - - |
6 | O - - - - - - - - |
7 | - - - - - - O - - |
8 | - O - - O - O - O |
9 | O - - O - - - - O |
 +-------------------+
CSCE 1035: Project 3
Due: 11:59 PM on Monday, May 2, 2022
12
Enter position to fire torpedo #19 (e.g., B5): B3
Miss...
 A B C D E F G H I
 +-------------------+
1 | - O O - O - - - O |
2 | - - - - - - - - - |
3 | - O - - - - O - - |
4 | - X - - - - - - O |
5 | O O - - - - - - - |
6 | O - - - - - - - - |
7 | - - - - - - O - - |
8 | - O - - O - O - O |
9 | O - - O - - - - O |
 +-------------------+
Enter position to fire torpedo #20 (e.g., B5): A4
Miss...
 A B C D E F G H I
 +-------------------+
1 | - O O - O - - - O |
2 | - - - - - - - - - |
3 | - O - - - - O - - |
4 | O X - - - - - - O |
5 | O O - - - - - - - |
6 | O - - - - - - - - |
7 | - - - - - - O - - |
8 | - O - - O - O - O |
9 | O - - O - - - - O |
 +-------------------+
Sorry, but you were not able to sink my ships! Tough break...
 A B C D E F G H I
 +-------------------+
1 | - O O - O - - - O |
2 | - - - - - - - - - |
3 | - O - - - - O - - |
4 | O X B B B - - - O |
5 | O O - - D - - - - |
6 | O - - - D - - - - |
7 | - - - - - - O - - |
8 | - O - - O - O - O |
9 | O - - O - - - - O |
 +-------------------+
CSCE 1035: Project 3
Due: 11:59 PM on Monday, May 2, 2022
13
$ python3 project3.py
+--------------------------------------------+
| Computer Science and Engineering |
| CSCE 1035 - Computer Programming I |
| Student Name EUID euid@my.unt.edu |
+--------------------------------------------+
+-------------------------------------------------------------+
| This program will randomly choose two ships from your fleet |
| made up of the following vessels: Carrier, Battleship, Sub- |
| marine, and Destroyer. It will then randomly assign both of |
| the vessels to the board that are oriented either vertical- |
| ly or horizontally. As a player you will then have up to 20 |
| tries to sink both of the computer's vessels |
+-------------------------------------------------------------+
 A B C D E F G H I
 +-------------------+
1 | - - - - - - - - - |
2 | - - - - - - - - - |
3 | - - - - - - - - - |
4 | - - - - - - - - - |
5 | - - - - - - - - - |
6 | - - - - - - - - - |
7 | - - - - - - - - - |
8 | - - - - - - - - - |
9 | - - - - - - - - - |
 +-------------------+
Enter position to fire torpedo #1 (e.g., B5): A1
Miss...
 A B C D E F G H I
 +-------------------+
1 | O - - - - - - - - |
2 | - - - - - - - - - |
3 | - - - - - - - - - |
4 | - - - - - - - - - |
5 | - - - - - - - - - |
6 | - - - - - - - - - |
7 | - - - - - - - - - |
8 | - - - - - - - - - |
9 | - - - - - - - - - |
 +-------------------+
CSCE 1035: Project 3
Due: 11:59 PM on Monday, May 2, 2022
14
Enter position to fire torpedo #2 (e.g., B5): B1
Hit... nice shot!
 A B C D E F G H I
 +-------------------+
1 | O X - - - - - - - |
2 | - - - - - - - - - |
3 | - - - - - - - - - |
4 | - - - - - - - - - |
5 | - - - - - - - - - |
6 | - - - - - - - - - |
7 | - - - - - - - - - |
8 | - - - - - - - - - |
9 | - - - - - - - - - |
 +-------------------+
Enter position to fire torpedo #3 (e.g., B5): B2
Miss...
 A B C D E F G H I
 +-------------------+
1 | O X - - - - - - - |
2 | - O - - - - - - - |
3 | - - - - - - - - - |
4 | - - - - - - - - - |
5 | - - - - - - - - - |
6 | - - - - - - - - - |
7 | - - - - - - - - - |
8 | - - - - - - - - - |
9 | - - - - - - - - - |
 +-------------------+
CSCE 1035: Project 3
Due: 11:59 PM on Monday, May 2, 2022
15
Enter position to fire torpedo #4 (e.g., B5): C1
Hit... nice shot!
Congratulations! You sank my Destroyer!!
 A B C D E F G H I
 +-------------------+
1 | O X X - - - - - - |
2 | - O - - - - - - - |
3 | - - - - - - - - - |
4 | - - - - - - - - - |
5 | - - - - - - - - - |
6 | - - - - - - - - - |
7 | - - - - - - - - - |
8 | - - - - - - - - - |
9 | - - - - - - - - - |
 +-------------------+
Enter position to fire torpedo #5 (e.g., B5): D1
Miss...
 A B C D E F G H I
 +-------------------+
1 | O X X O - - - - - |
2 | - O - - - - - - - |
3 | - - - - - - - - - |
4 | - - - - - - - - - |
5 | - - - - - - - - - |
6 | - - - - - - - - - |
7 | - - - - - - - - - |
8 | - - - - - - - - - |
9 | - - - - - - - - - |
 +-------------------+
CSCE 1035: Project 3
Due: 11:59 PM on Monday, May 2, 2022
16
Enter position to fire torpedo #6 (e.g., B5): F3
Hit... nice shot!
 A B C D E F G H I
 +-------------------+
1 | O X X O - - - - - |
2 | - O - - - - - - - |
3 | - - - - - X - - - |
4 | - - - - - - - - - |
5 | - - - - - - - - - |
6 | - - - - - - - - - |
7 | - - - - - - - - - |
8 | - - - - - - - - - |
9 | - - - - - - - - - |
 +-------------------+
Enter position to fire torpedo #7 (e.g., B5): F4
Hit... nice shot!
 A B C D E F G H I
 +-------------------+
1 | O X X O - - - - - |
2 | - O - - - - - - - |
3 | - - - - - X - - - |
4 | - - - - - X - - - |
5 | - - - - - - - - - |
6 | - - - - - - - - - |
7 | - - - - - - - - - |
8 | - - - - - - - - - |
9 | - - - - - - - - - |
 +-------------------+
CSCE 1035: Project 3
Due: 11:59 PM on Monday, May 2, 2022
17
Enter position to fire torpedo #8 (e.g., B5): F5
Hit... nice shot!
 A B C D E F G H I
 +-------------------+
1 | O X X O - - - - - |
2 | - O - - - - - - - |
3 | - - - - - X - - - |
4 | - - - - - X - - - |
5 | - - - - - X - - - |
6 | - - - - - - - - - |
7 | - - - - - - - - - |
8 | - - - - - - - - - |
9 | - - - - - - - - - |
 +-------------------+
Enter position to fire torpedo #9 (e.g., B5): F6
Hit... nice shot!
Congratulations! You sank my Battleship!!
 A B C D E F G H I
 +-------------------+
1 | O X X O - - - - - |
2 | - O - - - - - - - |
3 | - - - - - X - - - |
4 | - - - - - X - - - |
5 | - - - - - X - - - |
6 | - - - - - X - - - |
7 | - - - - - - - - - |
8 | - - - - - - - - - |
9 | - - - - - - - - - |
 +-------------------+
You sank both of my ships in 9 tries
