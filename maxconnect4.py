#!/usr/bin/env python

# Written by Chris Conly based on C++
# code provided by Dr. Vassilis Athitsos
# Written to be Python 2.4 compatible for omega
#Name:Shreyas Mohan
#Student Id:1001669806
#AI Assignment-4
import sys
from MaxConnect4Game import *
import copy

def viable(board):                                      ## checks for all the viable/available columns available to player 2 after player 1 has played his/her move
    viable = []
    for att, attV in enumerate(board[0]):           
        if attV == 0:
            viable.append(att)                          ##puts the location of all the available columns to the list.
    return viable
    
        
def possible(GOld, attr):                               ## checks if any of the viable/available columns get the player a score 
    GNew = maxConnect4Game()
    try:
        GNew.nodeD = GOld.nodeD + 1
    except:
        GNew.nodeD = 1                                       ## assign a depth value to the game
    GNew.pieceCount = GOld.pieceCount
    GNew.gameBoard = copy.deepcopy(GOld.gameBoard)
    if not (GNew.gameBoard[0][attr]):                    ##if column not full
        for flag in range(5, -1, -1):
            if not (GNew.gameBoard[flag][attr]):          ##if position not full
                GNew.gameBoard[flag][attr] = GOld.currentTurn           ## starts filling up the positions to check where it gets a point
                GNew.pieceCount = GNew.pieceCount + 1
                break
    if GOld.currentTurn == 1:
        GNew.currentTurn = 2
    elif GOld.currentTurn == 2:
        GNew.currentTurn = 1
    GNew.checkPieceCount()
    GNew.countScore()
    return GNew

class minimax:
    def __init__(self, game, depth):
        self.currentTurn = game.currentTurn
        self.game = game
        self.maxD = int(depth)
        self.evaltable = [[3,4,5,7,5,4,3],
             [4,6,8,10,8,6,4],
             [5,8,11,13,11,8,5],
             [5,8,11,13,11,8,5],
             [4,6,8,10,8,6,4],
             [3,4,5,7,5,4,3]]

    def decide(self):
        mini = []
        via = viable(self.game.gameBoard)                   ## the gameboard from MaxConnect4Game is passed to check for viable places
        for nxt in via:                                     ## iterating through the available plays in viable
            poss = possible(self.game,nxt)                  
            mini.append( self.mini(poss,99999,-99999) )    ## the new game state is passed to the minimiser function in minimax and the evaluate value returned is appended in mini
        select = via[mini.index( max( mini ) )]             ## select the best possible move in mini list.
        return select

    def mini(self, gstate, alpha, beta):
        if gstate.pieceCount == 42 or gstate.nodeD == self.maxD:
            return self.evaluate(gstate)
        val = 99999
        for nxt in viable(gstate.gameBoard):
            nS = possible(gstate,nxt)                       ## creates the possible successors for the nS game state
            val = min(val,self.maximum( nS,alpha,beta ))       ## selects the minimum value in the successors
            if val <= alpha:
                return val
            beta = min(beta, val)   
        return val
        
    def maximum(self, gstate, alpha, beta):
        if gstate.pieceCount == 42 or gstate.nodeD == self.maxD:
            return self.evaluate(gstate)
        val = -99999
        for nxt in viable(gstate.gameBoard):
            nS = possible(gstate,nxt)                       ## creates the possible successors for the nS game state
            val = max(val,self.mini( nS,alpha,beta ))      ## selects the max value in the
            if val >= beta:
                return val
            alpha = max(alpha, val)
        return val

    def evaluate(self,gstate):
        sum=0
        utility=138
        for i in range(0,6):
            for j in range (0,7):
                if(gstate.gameBoard[i][j]==1):
                    sum-=self.evaltable[i][j]
                elif(gstate.gameBoard[i][j]==2):
                    sum+=self.evaltable[i][j]
        evaluate = utility+sum
        gstate.countScore()
        if self.currentTurn == 1:
            final = (gstate.player1Score * 2) - (gstate.player2Score)
        elif self.currentTurn == 2:
            final = (gstate.player2Score * 2 - gstate.player1Score)
        return (evaluate+final)

def oneMoveGame(currentGame,depth):
    if currentGame.pieceCount == 42:   
        print '\n\nGame Over!\n'
        sys.exit(0)
    mM = minimax(currentGame,depth)
    nxt = mM.decide()
    currentGame.playPiece(nxt)
    mover(currentGame,nxt)
    currentGame.gameFile.close()


def mover(GameC,nxt):
    print('Player no %d, played column %d\n' % (GameC.currentTurn, nxt+1))
    if GameC.currentTurn == 1:
        GameC.currentTurn = 2
    elif GameC.currentTurn == 2:
        GameC.currentTurn = 1
    GameC.printGameBoard()
    GameC.countScore()
    print('Player 1 = %d, Player 2 = %d\n' % (GameC.player1Score, GameC.player2Score))
    GameC.printGameBoardToFile()


def interactiveGame(currentGame,depth):
    while currentGame.pieceCount != 42:                                     ## runs till the entire board fills up
        if currentGame.currentTurn == 1:                                    
            player = input("Enter the column number(1-7) : ")
            if (player <= 0 or player >= 8):                             ## checking for illegal column inputs
                print "Illegal column number!! Try again!!"
                continue
            if  not (currentGame.playPiece(player-1)):                   
                print "The selected column is full"
                continue
            try:
                currentGame.gameFile = open("player1.txt", 'w')             ## put the move played into the file
            except:
                sys.exit('Output file error')
            mover(currentGame,player-1)
        elif currentGame.pieceCount != 42:                                  ## the computer's turn to play
            mM = minimax(currentGame,depth)                                 ## the minimax algorithm runs
            nxt = mM.decide()                                                 ## the best possible play is returned from decide function.
            currentGame.playPiece(nxt)                       
            try:
                currentGame.gameFile = open("player2.txt", 'w')
            except:
                sys.exit('Output file error')
            mover(currentGame,nxt)

    currentGame.gameFile.close()
    declarewinner(currentGame)

def declarewinner(currentGame):                         ## prints the winner
    if currentGame.player1Score > currentGame.player2Score:
        print "Player 1 is the winner"
    elif currentGame.player1Score < currentGame.player2Score:
        print "Player 2 is the winner"
    else:print "The game ended in a draw"    

def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) != 5:
        print 'Four command-line arguments are needed:'
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile = argv[1:3]

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game() # Create a game

    # Try to open the input file
    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")

    # Read the initial game state from the file and save in a 2D list
    file_lines = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    currentGame.currentTurn = int(file_lines[-1][0])
    currentGame.gameFile.close()

    print '\nMaxConnect-4 game\n'
    print 'Game state before move:'
    currentGame.printGameBoard()

    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if game_mode == 'interactive':
        if argv[3] == 'computer-next': 
            currentGame.currentTurn = 2
        else: 
            currentGame.currentTurn = 1
        interactiveGame(currentGame,argv[4]) # argv[4] is the depth being passed to the function
    else: 
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame,argv[4]) 


if __name__ == '__main__':
    main(sys.argv)
