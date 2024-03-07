board = {1:" ",2:" ",3:" ",
         4:" ",5:" ",6:" ",
         7:" ",8:" ",9:" "}

def printboard(board):
    print(board[1]+"|"+board[2]+"|"+board[3])
    print("-+-+-")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("-+-+-")
    print(board[7]+"|"+board[8]+"|"+board[9])
    print("-+-+-")

printboard(board)

def isSPACEFree(position):
    if board[position] == " ":
        return True
    else :
        return False

def checkDraw():
    for key in board:
        if board[key] == " ":
            return False

    return True

def checkWin(letter):
    if board[1] == board[2] and board[1] == board[3] and board[1] == letter:
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] == letter:
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] == letter:
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] == letter:
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3] == letter:
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] == letter:
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] == letter:
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] == letter:
        return True
    else:
        return False

def insertLetter(letter,position):
    if isSPACEFree(position):
        board[position] = letter
        printboard(board)
        if checkDraw():
            print("Draw")
            quit()
        if checkWin(letter):
            print(letter,"Wins the Game")
            quit()
    else:
        print("Can't insert here")
        position = int(input("Enter a position : "))
        insertLetter(letter,position)

def playerMove(letter):
    position = int(input(f"Enter a position {letter} : "))
    insertLetter(letter,position)

def minimax(board,letter):
    if checkWin("X"):
        return -1
    if checkWin("0"):
        return 1
    if checkDraw():
        return 0
    if letter == "0":
        bestScore = -10
        for key in board:
            if board[key] == " ":
                board[key] = letter
                score = minimax(board,"X")
                board[key] = " "
                if score > bestScore:
                    bestScore = score
        return bestScore
    if letter == "X":
        bestScore = 10
        for key in board:
            if board[key] == " ":
                board[key] = letter
                score = minimax(board,"0")
                board[key] = ' '
                if score<bestScore:
                    bestScore = score
        return bestScore

def computerMove(letter):
    bestScore = -10
    bestPosition = 0
    for key in board:
        if board[key] == " ":
            board[key] = letter
            score = minimax(board,"X")
            board[key] =  " "
            if score > bestScore:
                bestScore = score
                bestPosition = key
    insertLetter(letter,bestPosition)

comp = "0"
user = "X"

while checkWin(comp) == False and checkWin(user) == False:
    playerMove(user)
    computerMove(comp)
