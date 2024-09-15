"""
If it does not compile, it is most likely due to "termcolor" which can be installed with pip:

pip install termcolor

If it doesnt recognize the pip command, you need to modify your installation to put python on the PATH, search the google if unsure
If the ultimate version looks like a hot mess it is likely because it is not run in an bash terminal, to fix this run it in vscode's terminal
"""


from termcolor import colored
import random

def MakeTable():
    HASH_TABLE = {}
    secondCounter = 0
    for i in range(1, 10):
        for j in ["a", "b", "c", "d", "e", "f", "g", "h", "i"]:
            secondCounter += 1
            HASH_TABLE[str(i) + j] = " "
        secondCounter = 0
    return HASH_TABLE

# it needs to be here or else the new board function dont work
HASH_TABLE = MakeTable()

def StrText(text:str, color:str, sector:int, i:int, offset:int = 0, exception:bool = False):
    if not exception:
        return colored(text, color if sector == i + offset else "white")
    else: 
        return colored(text, color if sector == i + offset or sector == i + offset - 3 else "white")

def StrSquare(color:str, sector:int, i:int, offset:int = 0, exception:bool = False):
    if not exception:
        return colored("▯", color if sector == i + offset or sector == i + 1 + offset else "white")
    else:
        return colored("▯", color if sector == i + offset or sector == i + 1 + offset or sector == i + offset - 3 or sector == i + 1 + offset - 3 else "white")


def StrLine(lineType:str, color:str, sector:int, i:int):
    result = ''
    text = ["□ ▯ □ □ □ □ □ "," □ □ □ □ □ ", " □ □ □ □ □ ▯"] if lineType == 'square' else ["  ▯ --+---+---", " --+---+---", " --+---+---▯"]
    for x in range(3):
            result += StrText(text[x], color, sector, i, x, True if lineType == 'square' else False) 
            if x != 2:
                result += StrSquare(color, sector, i, x, True if lineType == 'square' else False)
    return result
    

def PrintBoardV2(sector):
    COLOR = "red" if PLAYER_TYPE == "X" else "blue"
    LETTER_LIST = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    
    text = [" a   b   c "," d   e   f ", " g   h   i "] 
    for x in range(3):
        if x == 0:
            print(StrText("  ▯", COLOR, sector, 0), end='')
        print(colored(text[x], COLOR if sector == x or sector == 3 + x  or sector == 6 + x else "white"),end='')
        if x != 2:
            print(StrSquare(COLOR, sector, 0, x),end='')
        else:
            print(StrText("▯", COLOR, sector, 2))
    
    for i in range(0, 9, 3):
        print(StrLine('square', COLOR, sector, i))
        for j in range(3):
            for k in range(3):
                # Writes the leading  number of a row, with color if one in the row is selected
                if k == 0:  
                    print(colored(f'{str(i + j +1)} ', COLOR if sector == i or sector == i+1 or sector == i+2  else 'white'), end='')
                    print(StrText('▯', COLOR, sector, i), end='')
                else: 
                    print(StrSquare(COLOR, sector, i, k-1), end='')
                
                for l in range(3):
                    print(StrText(f' {HASH_TABLE[str(i+j+1)+LETTER_LIST[k*3+l]]} ', COLOR, sector, i, k), end='')
                    if l != 2:
                        print(StrText('|', COLOR, sector, i, k), end='')

            print(StrText('▯', COLOR, sector, i, 2))
            if j != 2: 
                print(StrLine('dash', COLOR, sector, i))
    print(StrLine('square', COLOR, sector, 9))
    return

def MarkSpot(spot:str, sector):
    """
    Input is the spot to check
    return is if it did something or not
    """
    if HASH_TABLE[spot] == " ":
        if SpotToSector(spot) != sector and sector != -5:
            return False
        HASH_TABLE[spot] = PLAYER_TYPE

        return True
    return False

def GetAnswer(sector):
    print("It is now ", end='')
    while True:
        result = False
        print(f"{PLAYER_TYPE} to move")
        giveninput = ''
        try:
            giveninput = input()
            result = MarkSpot(giveninput, sector)
        except:
            if len(giveninput) == 2:
                newInput = giveninput[1] + giveninput[0]
                try:
                    result = MarkSpot(newInput, sector)
                except:
                    result = result
                if result:
                    giveninput = newInput
                    break

            print("Invalid input, it is still ", end='')
            continue
        if result:
            break
        else:
            print("Spot already taken, it is still ", end='')
    return giveninput

def SpotToSector(input:str):
    LETTER_LIST = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    letterValue = int(LETTER_LIST.index(input[1])/3)
    numbValue = int((int(input[0])-1)/3)

    sector = numbValue*3+letterValue
    #print(sector)
    return sector

def GetNextSector(input:str):
    LETTER_LIST = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    letterValue = int(LETTER_LIST.index(input[1])%3)
    numbValue = int((int(input[0])-1)%3)

    sector = numbValue*3+letterValue
    return sector

def SectorToSpots(sector:int, spot=False):
    LETTER_LIST = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    m2 = LETTER_LIST[sector%3*3:sector%3*3+3]
    m1 = [f'{i+1}'for i in range(int(sector/3)*3,int(sector/3)*3+3)]
    if spot:
        return [f'{m1[i] + m2[j]}' for i in range(3) for j in range(3)]
    else:
        return [f'{HASH_TABLE[m1[i] + m2[j]]}' for i in range(3) for j in range(3)]

def CheckSectorWin(sector):
    return CheckBoardWin(SectorToSpots(sector))

def CheckBoardWin(board):
    for i in range(3):
         result = CheckRowWin(board[3*i:3*i+3]) or CheckRowWin(board[i::3]) or CheckRowWin(board[::4]) or CheckRowWin(board[2:7:2])
         if result:
             return result
    return False

def CheckRowWin(row):
    if row[0] == ' ':
        return False
    if row[0] == row[1] and row[0] == row[2]:
        return True, row[0]
    else:
        return False

def IsSectorMaxed(sector):
    for a in SectorToSpots(sector):
        if a == ' ':
            return False
    return True

def IsBoardMaxed():
    for i in range(9):
        if not IsSectorMaxed(i):
            return False
    return True

def StartUltimateTicTacToe(playerCount:int, gameDifficulty='r', humanPlayer='X'):
    # GameLoop
    boardsWon = [' ' for _ in range(9)]
    global PLAYER_TYPE 
    PLAYER_TYPE = "X"
    sectorToColor = -5
    winner = ' '

    global HUMAN_PLAYER
    global COMPUTER_PLAYER
    PLAYER_TYPE = 'X'
    HUMAN_PLAYER = humanPlayer
    if humanPlayer == 'X':
        COMPUTER_PLAYER = 'O'
    else: 
        COMPUTER_PLAYER = 'X' 


    while True:
        #print(chr(27) + "[2J") # Clears terminal
        if playerCount == 2 or PLAYER_TYPE == humanPlayer:
            PrintBoardV2(sectorToColor)

        spot = ''
        if playerCount == 2:
            spot = GetAnswer(sectorToColor)
        elif PLAYER_TYPE == HUMAN_PLAYER:
            spot = GetAnswer(sectorToColor)
        else:
            print("Bot picks... ", end='')
            if gameDifficulty == 'r':
                if sectorToColor == -5:
                    avalSpotList = []
                    for i in range(9):
                        avalSpotList.extend(SectorToSpots(i, True))
                else:
                    avalSpotList = SectorToSpots(sectorToColor, True)
                for s in avalSpotList:
                    if HASH_TABLE[s] != ' ':
                        avalSpotList.remove(s)
                isrunning = False
                while not isrunning:
                    spot = random.choice(avalSpotList)
                    isrunning = MarkSpot(spot, sectorToColor)
                print(spot)
            elif gameDifficulty == 'i':
                    bestScore = -800
                    bestMove = 0
                    for key in HASH_TABLE.keys():
                        if HASH_TABLE[key] == ' ':
                            HASH_TABLE[key] = COMPUTER_PLAYER
                            score = minimax(HASH_TABLE, False)
                            HASH_TABLE[key] = ' '
                            if score > bestScore:
                                bestScore = score 
                                bestMove = key
                    print(bestMove)
                    HASH_TABLE[bestMove] = COMPUTER_PLAYER

        sectorToColor = GetNextSector(spot)

        # Checking small board for win
        curSector = SpotToSector(spot)
        scanResult = CheckSectorWin(curSector)
        if scanResult:
            boardsWon[curSector] = scanResult[1]
            newScanResult = CheckBoardWin(boardsWon)
            if newScanResult:
                winner = newScanResult[1]
                break
        
        if IsSectorMaxed(sectorToColor):
            sectorToColor = -5

        if IsBoardMaxed():
            print("The game is a draw")
            return winner

        # Changes current player at end of turn to allow next player
        if PLAYER_TYPE == "X":
            PLAYER_TYPE = "O"
        else:
            PLAYER_TYPE = "X"

    print(f"Player {winner} has won")

    print("now kys")
    return winner

def StartDefaultTicTacToe(playerCount:int, gameDifficulty='r', humanPlayer='X'):
    # Variables
    gameState = {}
    for i in range(9):
        gameState[str(i+1)] = ' '
    #gameState = [f'{i+1}' for i in range(9)]
    global HUMAN_PLAYER
    global COMPUTER_PLAYER
    PLAYER_TYPE = 'X'
    HUMAN_PLAYER = humanPlayer
    if humanPlayer == 'X':
        COMPUTER_PLAYER = 'O'
    else: 
        COMPUTER_PLAYER = 'X' 

    while True:
        # Board printing
        #if playerCount == 2 or PLAYER_TYPE == humanPlayer:
        print('-'*13)
        print(f'| {gameState['1']} | {gameState['2']} | {gameState['3']} ', end='|\n')
        print('-'*13)
        print(f'| {gameState['4']} | {gameState['5']} | {gameState['6']} ', end='|\n')
        print('-'*13)
        print(f'| {gameState['7']} | {gameState['8']} | {gameState['9']} ', end='|\n')
        print('-'*13)

        # Determine if there is a winner
        tempList = []
        for i in gameState.keys():
            tempList.append(gameState[i])
        result = CheckBoardWin(tempList)
        if result:
            print(f"Player {result[1]} won")
            return result[1]

        # Check if draw
        if CheckDraw(gameState):
            print("The game is a draw")        
            return ' '

        # Player input with sanitation
        if playerCount == 2 or PLAYER_TYPE == humanPlayer:
            while True:
                print(f"It is player {PLAYER_TYPE} to move")
                playerInput = input()
                try:
                    if gameState[playerInput] == 'X' or gameState[playerInput] == 'O':
                        print("Spot already taken, choose another")
                        continue
                    else:
                        gameState[playerInput] = PLAYER_TYPE
                        break
                except:
                    print(f"Invalid input: {playerInput} \nTry again")
        else:
            print("Bot picks... ", end='')
            if gameDifficulty == 'r':
                avalTiles = [f'{i}' for i in range(1,10)]
                for s in avalTiles:
                    if gameState[s] == 'X' or gameState[s] == 'O':
                        avalTiles.remove(s)
                while True:
                    spot = random.choice(avalTiles)
                    if gameState[spot] != 'X' and gameState[spot] != 'O':
                        print(f"{spot}")
                        gameState[spot] = PLAYER_TYPE
                        break
            elif gameDifficulty == 'i':
                    bestScore = -800
                    bestMove = 0
                    for key in gameState.keys():
                        if gameState[key] == ' ':
                            gameState[key] = COMPUTER_PLAYER
                            score = minimax(gameState, False)
                            gameState[key] = ' '
                            if score > bestScore:
                                bestScore = score 
                                bestMove = key
                    print(f"{bestMove}")
                    gameState[bestMove] = COMPUTER_PLAYER

        

        # Change player after turn
        if PLAYER_TYPE == "X":
            PLAYER_TYPE = "O"
        else:
            PLAYER_TYPE = "X"

def CheckDraw(board):
    for s in board.keys():
        if board[s] == ' ':
            return False
    return True



def minimax(board, isMaximizing):
    tempList = []
    for i in board.keys():
        tempList.append(board[i])
    checkWinResult = CheckBoardWin(tempList)

    if checkWinResult:
        if checkWinResult[1] == COMPUTER_PLAYER:
            return 1
        elif checkWinResult[1] == HUMAN_PLAYER:
            return -1
        else: 
            print("what, this should never be called")
    elif CheckDraw(board):
        return 0
        
    if isMaximizing:
        bestScore = -800 
        for key in board.keys():
            if board[key] == ' ':
                board[key] = COMPUTER_PLAYER 
                score = minimax(board, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore 
    else:
        bestScore = 800 
        for key in board.keys():
            if board[key] == ' ':
                board[key] = HUMAN_PLAYER
                score = minimax(board, True)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score 
        return bestScore

# Game starter
print("Play Ultimate Tic Tac Toe or default (ult/def)")
while True:
    gameType = (input()).lower()
    if gameType == 'u' or gameType == 'ult' or gameType == 'd' or gameType == 'def':
        break
    else:
        print(f"invalid input: '{gameType}' is not recognized\n Try again")

print("1 Player or 2 Player (1/2)")
while True:
    playerCount = input()
    try: 
        playerCount_int = int(playerCount)
    except:
        print(f"'{playerCount}' is nan\n Try again")
    
    if playerCount_int == 1 or playerCount_int == 2:
        break
    else:
        print(f"'{playerCount_int}' is out of bounds \n Try again")

gameDifficulty = 'r'
if playerCount_int == 1:
    print("What difficulty do you want to play against")
    if gameType == 'u' or gameType == 'ult':
        print("WARNING, the impossible mode takes forever to take actions")
    print("Random: r")
    print("Impossible: i")
    while True:
        gameDifficulty = input()
        if gameDifficulty == 'r' or gameDifficulty == 'i':
            break
        else:
            print(f"Invalid input: '{gameDifficulty}'\n try again")

# Game Master
score = {
    'Player 1' : 0,
    'Draw' : 0,
    'Player 2' : 0
}
player1_type = 'X'
while True:
    
    if gameType == 'u' or gameType == 'ult':
        print("To make a move lineup a letter and number like: '5e' or 'e5', which are equivalent")
        result = StartUltimateTicTacToe(playerCount_int, gameDifficulty, player1_type)
    elif gameType == 'd' or gameType == 'def':
        result = StartDefaultTicTacToe(playerCount_int, gameDifficulty, player1_type)

    if result == ' ':
        score['Draw'] += 1
    elif result == player1_type:
        score['Player 1'] += 1
    else:
        score['Player 2'] += 1
        
    print()
    print(score)
    print("Player roles have now switched")

    if player1_type == "X":
        player1_type = "O"
    else:
        player1_type = "X"