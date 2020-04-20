					
# max-connect4

The task in this program is to implement an agent that plays the Max-Connect4 game using search. The game is played on a 6x7 grid, with six rows and seven columns. There are two players, player A (red) and player B (green). The two players take turns placing pieces on the board: the red player can only place red pieces, and the green player can only place green pieces.

It is best to think of the board as standing upright. We will assign a number to every row and column, as follows: columns are numbered from left to right, with numbers 1, 2, ..., 7. Rows are numbered from bottom to top, with numbers 1, 2, ..., 6. When a player makes a move, the move is completely determined by specifying the COLUMN where the piece will be placed. If all six positions in that column are occupied, then the move is invalid, and the program should reject it and force the player to make a valid move. In a valid move, once the column is specified, the piece is placed on that column and "falls down", until it reaches the lowest unoccupied position in that column.

The game is over when all positions are occupied. Obviously, every complete game consists of 42 moves, and each player makes 21 moves. The score, at the end of the game is determined as follows: consider each quadruple of four consecutive positions on board, either in the horizontal, vertical, or each of the two diagonal directions (from bottom left to top right and from bottom right to top left). The red player gets a point for each such quadruple where all four positions are occupied by red pieces. Similarly, the green player gets a point for each such quadruple where all four positions are occupied by green pieces. The player with the most points wins the game.

The program will run in two modes: an interactive mode, that is best suited for the program playing against a human player, and a one-move mode, where the program reads the current state of the game from an input file, makes a single move, and writes the resulting state to an output file. The one-move mode can be used to make programs play against each other.


### How to compile : 

python maxconnect4.py interactive [input_file] [computer-next/human-next] [depth]
		 or
python maxconnect4.py one-move [input_file] [output_file] [depth]
 
### Language used :

Python

### Code Structure:

Two files  - MaxConnect4Game.py and maxconnect4.py  

**File1:   MaxConnect4Game.py**

#### Function Name: printGameBoardtoFile 
Function Description: Writes the current state of the board to the appropriate file.

#### Function Name: playPiece 
Function Description: places the piece at the selected column.

#### Function Name: countScore 
Function Description: counts the total score of the board.


#### Function Name: checkPieceCount 
Function Description:  checks the number of pieces present in the current board.

#### Function Name: printGameBoard  
Function Description: Prints the current state of the board on the screen.



**File2:   maxconnect4.py**

#### Function Name: viable(board)
Function Description: Checks for all viable columns

##### Function Name: possible(Gold,attr)  
Function Description:  checks if any of the viable/available columns fetch the player a score, assigns a depth value and starts filling up the positions to check where it gets a point.

class minimax - implements the minimax algorithm

#### Function Name: decide(self) 
Function Description: Decidesat which position the AI will play the game.

#### Function Name: mini(self,gstate,alpha,beta)  
Function Description: minimiser function to select the minimum value in the successors.

#### Function Name: maximum(self,gstate,alpha,beta)
Function Description: maximiser function to select the maximum value in the successors

#### Function Name: evaluate(self,gstate)
Function Description: evaluation function of the program

#### Function Name: mover(GameC,nxt)
Function Description: After each move, it prints the board and writes the boards state to the file

#### Function Name: oneMoveGame(currentGame,depth)
Function Description:inputs the selected column and just makes a single move.

#### Function Name: interactiveGame(currentGame,depth)
Function Description: inputs the selected column in interactive mode, and if it is the computer's turn to play it uses the minimax class to select the move.

#### Function Name: declarewinner(currentGame)
Function Description: Prints the winner after the board is full.




