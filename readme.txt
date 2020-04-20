					Programming Assignment 4

Name: Shreyas Mohan

UTA ID: 1001669806

How to compile : python maxconnect4.py interactive [input_file] [computer-next/human-next] [depth]
		 or
python maxconnect4.py one-move [input_file] [output_file] [depth]
 
Language used : Python

Code Structure: Two files  - MaxConnect4Game.py and maxconnect4.py  

File1:   MaxConnect4Game.py

Function Name: printGameBoardtoFile 
Function Description: Writes the current state of the board to the appropriate file.

Function Name: playPiece 
Function Description: places the piece at the selected column.

Function Name: countScore 
Function Description: counts the total score of the board.


Function Name: checkPieceCount 
Function Description:  checks the number of pieces present in the current board.

Function Name: printGameBoard  
Function Description: Prints the current state of the board on the screen.



File2:   maxconnect4.py

Function Name: viable(board)
Function Description: Checks for all viable columns

Function Name: possible(Gold,attr)  
Function Description:  checks if any of the viable/available columns fetch the player a score, assigns a depth value and starts filling up the positions to check where it gets a point.

class minimax - implements the minimax algorithm

Function Name: decide(self) 
Function Description: Decidesat which position the AI will play the game.

Function Name: mini(self,gstate,alpha,beta)  
Function Description: minimiser function to select the minimum value in the successors.

Function Name: maximum(self,gstate,alpha,beta)
Function Description: maximiser function to select the maximum value in the successors

Function Name: evaluate(self,gstate)
Function Description: evaluation function of the program

Function Name: mover(GameC,nxt)
Function Description: After each move, it prints the board and writes the boards state to the file

Function Name: oneMoveGame(currentGame,depth)
Function Description:inputs the selected column and just makes a single move.

Function Name: interactiveGame(currentGame,depth)
Function Description: inputs the selected column in interactive mode, and if it is the computer's turn to play it uses the minimax class to select the move.

Function Name: declarewinner(currentGame)
Function Description: Prints the winner after the board is full.




