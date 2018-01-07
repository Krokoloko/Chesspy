import sys

from board import board
from piece import piece

ChessBoard = board.Board()

def HelpMe():
    for i in funcList:
        print("\n" + funcList[i][2] + " : " + funcList[i][1])

def NewGame():
    return

def About():
    print("This is a chess game I am building so I can improve making AI's.\n\nMade by Daan Joachim Ruting")

def CloseApp():
    print("closing...")
    sys.exit(0)

def Main():
    About()
    while True:
        command = input()
        try:
            for i in funcList:
                if funcList[i][2] == command:
                    funcList[i][0]()

        except KeyError:
            print("No such command exists. \nBe sure to type \'helpMe\' to look for appropiate commands.")

"""index: [function,description,functionString,object,group] """


funcList = {0:[HelpMe,"Shows all the functions and descriptions.","helpMe",None,"app"],
            1:[About,"About this application","about",None,"app"],
            2:[CloseApp,"Closes the application.","closeApp",None,"app"],
            3:[ChessBoard.PrintBoard,"Prints the current board layout.","printBoard",ChessBoard,"visual"]}

if(__name__ == __main__):
    Main()
