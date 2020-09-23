# dummy = ["X", 2, 3, 4, 5, 6, 7, "O", 9]

def boardToStr(pos):
    """This function prints a list into a TicTacToe Board"""
    line1 = f'{pos[0]} | {pos[1]} | {pos[2]}'
    line2 = f'{pos[3]} | {pos[4]} | {pos[5]}'
    line3 = f'{pos[6]} | {pos[7]} | {pos[8]}'

    seperator = '---------'

    return (line1 + "\n" + seperator + "\n" + line2 + "\n" + seperator + "\n" + line3 + "\n")

# print(boardToStr(dummy))