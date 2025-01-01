def main():
    difficulty = input("Difficult or casual? ").upper()
    #not equal we can write in words too
    if not (difficulty == "DIFFICULT" or difficulty == "CASUAL"):
        print("Enter a valid difficulty")
        return
    
    players = input("Multiplayer or Single-player? ").upper()
    if not (players == "MULTIPLAYER" or players == "SINGLE-PLAYER"):
         print("Enter a valid number of player")
         return
    if difficulty == "DIFFICULT"  and players == "MULTIPLAYER":
        recommend("Poker")
    elif difficulty == "DIFFICULT"  and players == "SINGLE-PLAYER":     
        recommend("Klondike")
    elif difficulty == "Casual"  and players == "MULTIPLAYER": 
        recommend("Hearts")
    else:
        recommend("Clock")
        
def recommend(game):
    print("You might like", game)

main()
        