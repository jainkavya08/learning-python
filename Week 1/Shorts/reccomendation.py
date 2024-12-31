def main():
    difficulty = input("Difficult or Casual? ")
    if not (difficulty == "Difficult" or difficulty=="Casual") :
        print ("Enter a valid difficulty")
        return
    
    players = input("Multiplayer or Single-player? ")
    if not (players =="Multiplayer" or players =="Single-player"):
        print("Enter a valid number of players")

    if difficulty == "Difficult":
        if players =="Multiplayer":
            reccomend("Poker")
        elif players =="Single-player":
            reccomend("Klondike")
    elif difficulty =="Casual":
        if players =="Multiplayer":
            reccomend("Hearts")
        else:
            reccomend("Clock")


def reccomend(game):
    print("You might like " , game)


main()