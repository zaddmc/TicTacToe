from termcolor import colored



def MakeTable():
    HASH_TABLE = {}
    secondCounter = 0
    for i in range(1, 10):
        for j in ["a", "b", "c", "d", "e", "f", "g", "h", "i"]:
            secondCounter += 1
            #HASH_TABLE[j + str(i)] = " "
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
        if boardsWon[SpotToSector(spot)] != ' ':
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

def BoardWin(board):

    return 

# execute the random code as pleased
#PrintBoard() # Depricated and old version
#HASH_TABLE = MakeTable() # It has been moved up in the stack to make the printboard function loadle and doable
boardsWon = []
for i in range(9):
    boardsWon.append(' ')

# GameLoop
PLAYER_TYPE = "X"
sectorToColor = -5
while True:
    #print(chr(27) + "[2J") # Clears terminal
    PrintBoardV2(sectorToColor)
    spot = GetAnswer(sectorToColor)
    sectorToColor = GetNextSector(spot)
    if boardsWon[sectorToColor] !=  ' ':
        sectorToColor = -5

    # Changes current player at end of turn to allow next player
    if PLAYER_TYPE == "X":
        PLAYER_TYPE = "O"
    else:
        PLAYER_TYPE = "X"

#print("kys")