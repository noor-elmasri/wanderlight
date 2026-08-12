def store(player):
    print("Shopkeeper: \"Hello, welcome to Millbrook. Are you new in town?\"")
    print("Shopkeeper: \"Hello, welcome to Millbrook. Are you new in town?\"")
    print("Shopkeeper: \"You'll need a map if you want to find your way out of town.\"")

    while not player.has_item("Map"):
        print("Would you like to buy a map for 5 coins? Y/N")
        player_input = input("> ").lower()
        if player_input == "y":
            player.pick_up(Item("Map", "A hand-drawn map of the region."))
            print("Shopkeeper: \"Here you go, safe travels!\"")
        else:
            print("Shopkeeper: \"You won't get far without one...\"")


def run_intro():
    player_input = ""
    player_name = input("Enter player name: ")
    print(f"Hello {player_name}, you are a traveling messenger who has lost their way home")
    print("You are currently at a quiet village called 'Millbrook'. You see a store in the village.")
    print("Would you like to enter the store to start the game? Y/N")
    player_input = (input("> ")).lower()
    if player_input == "y":
        store()
    else:
        print(f"Very well, thank you {player_name} for playing. Goodbye")


run_intro()
