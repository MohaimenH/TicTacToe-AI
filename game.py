import board

pos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
win = 0
numOfMoves = 0

print("This is a TicTacToe game.")
print("You can play against a player or a computer.")
print("The game will appear on the console.\n")

print("The TicTacToe board looks as follows, with each position being represented with a number: \n")
print(board.boardToStr(pos))

print("While playing, use the numbers to tell the program which position you want to mark.\n")

wCPU = input("Do you want to play with someone else? (Y/N): ")

playerOne = "Player One"
playerTwo = "Player Two"

if (wCPU == 'N'):
    playerTwo = "Computer"

else:
    playerOne = input("\nName of Player One: ")
    playerTwo = input("\nName of Player Two: ")

    print("\n")

    while (win == 0):
        print(f"{playerOne}'s Turn\n")
        print(board.boardToStr(pos))

        move = int(input(f"{playerOne}'s Move: "))
        print("\n")

        pos[move-1] = "X"
        numOfMoves = numOfMoves + 1

        if (win != 0 or numOfMoves >= 9): break

        print(f"{playerTwo}'s Turn\n")
        print(board.boardToStr(pos))

        move = int(input(f"{playerTwo}'s Move: "))
        print("\n")

        pos[move-1] = "O"
        numOfMoves = numOfMoves + 1

print(board.boardToStr(pos))

if (win == 1):
    print(f"{playerOne} Wins!")
else:
    print(f"{playerTwo} Wins!")

