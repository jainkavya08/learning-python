def main():
    difficulty = input("Difficult or Casual? ")
    players = input("Multiplayer or Single-player? ")

    if difficulty == "Difficult":
        if players == "Multiplayer":
            reccomend("Poker")
        elif players == "Single-player":
            reccomend("Klondike")
        else:
            print("Enter a valid number of players ")
    else : 
        if players =="Multiplayer":
            reccomend("Heearts")
        elif players =="Single-player":
            reccomend("Clock")
        else:
            print("Enter a valid number of players ")

def reccomend(game):
    print("You might like " , game)


main()