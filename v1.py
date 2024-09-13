def PrintBoard():
    print("  ▯ a   b   c ▯ d   e   f ▯ g   h   i ▯")
    print("□ ▯ □ □ □ □ □ ▯ □ □ □ □ □ ▯ □ □ □ □ □ ▯")
    print("1 ▯   |   |   ▯   |   |   ▯   |   |   ▯")
    print("  ▯---+---+---▯---+---+---▯---+---+---▯")
    print("2 ▯   |   |   ▯   |   |   ▯   |   |   ▯")
    print("  ▯---+---+---▯---+---+---▯---+---+---▯")
    print("3 ▯   |   |   ▯   |   |   ▯   |   |   ▯")
    print("□ ▯ □ □ □ □ □ ▯ □ □ □ □ □ ▯ □ □ □ □ □ ▯")
    print("4 ▯   |   |   ▯   |   |   ▯   |   |   ▯")
    print("  ▯---+---+---▯---+---+---▯---+---+---▯")
    print("5 ▯   |   |   ▯   |   |   ▯   |   |   ▯")
    print("  ▯---+---+---▯---+---+---▯---+---+---▯")
    print("6 ▯   |   |   ▯   |   |   ▯   |   |   ▯")
    print("□ ▯ □ □ □ □ □ ▯ □ □ □ □ □ ▯ □ □ □ □ □ ▯")
    print("7 ▯   |   |   ▯   |   |   ▯   |   |   ▯")
    print("  ▯---+---+---▯---+---+---▯---+---+---▯")
    print("8 ▯   |   |   ▯   |   |   ▯   |   |   ▯")
    print("  ▯---+---+---▯---+---+---▯---+---+---▯")
    print("9 ▯   |   |   ▯   |   |   ▯   |   |   ▯")
    print("□ ▯ □ □ □ □ □ ▯ □ □ □ □ □ ▯ □ □ □ □ □ ▯")
    return

def MakeTable():
    HASH_TABLE = {}
    secondCounter = 0
    for i in range(1, 10):
        for j in ["a", "b", "c", "d", "e", "f", "g", "h", "i"]:
            secondCounter += 1
            HASH_TABLE[str(i)+j or j+str(i)] = ["blank", i*2+2, secondCounter*4+1]
        secondCounter = 0
    return HASH_TABLE

def MarkSpot(spot:str):
    """
    Input is the spot to check
    return is if it did something or not
    """
    tile = HASH_TABLE[spot]
    if tile[0] == "blank":
        tile[0] = PLAYER_TYPE
        print(f"\033[{tile[1]};{tile[2]}H{tile[0]}", end= "")

        return True
    return False




# execute the random code as pleased
PrintBoard()
HASH_TABLE = MakeTable()


# GameLoop
PLAYER_TYPE = "X"
while True:
    print(f"It is now {PLAYER_TYPE} to move")
    MarkSpot(input())
    print("\033[22;0H", end= "")

    # Changes current player at end of turn to allow next player
    if PLAYER_TYPE == "X":
        PLAYER_TYPE = "O"
    else:
        PLAYER_TYPE = "X"

print("kys")