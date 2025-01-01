def main():
    difficulty = input("Difficult or casual? ").upper()
    players = input("Multiplayer or Single-player? ").upper()
    
    if difficulty == "DIFFICULT":
        #nested if
        if players == "MULTIPLAYER":
            print("Poker")
        elif players == "SINGLE-PLAYER":
            print("Klondike")
        else:
            print("Enter a valid number of platers")
    elif difficulty == "CASUAL":
        if players == "MULTIPLAYER":
            print("Hearts")
        elif players == "SINLGE_PLAYER":
            print("Clock")
        else:
            print("Enter a valid number of players")
    else:
        print("Enter a valid difficulty")

main()
        