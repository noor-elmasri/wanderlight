"""
Wanderlight - core game classes.

This file defines the basic building blocks of the game: Room, Item, and
Player. No game data or game loop yet - that comes in a later PR. This
first version just defines the *shape* of things.
"""


class Room:
    """A single location in the game world."""

    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits  # dict, e.g. {"north": "Bramblegate"}

    def describe(self):
        """Return the text shown to the player when they enter this room."""
        return f"{self.name}\n{self.description}"


class Item:
    """A single object the player can pick up and carry."""

    def __init__(self, name, description):
        self.name = name
        self.description = description


class Player:
    """The player character - tracks location and inventory."""

    def __init__(self, name, starting_room_name):
        self.name = name
        self.current_room = starting_room_name
        self.inventory = []  # list of Item objects

    def pick_up(self, item):
        self.inventory.append(item)

    def has_item(self, item_name):
        """Check if the player is carrying an item by name."""
        return any(item.name == item_name for item in self.inventory)
    
def store(player):
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
    player = Player(player_name, "Millbrook")
    print(f"Hello {player_name}, you are a traveling messenger who has lost their way home")
    print("You are currently at a quiet village called 'Millbrook'. You see a store in the village.")
    print("Would you like to enter the store to start the game? Y/N")
    player_input = (input("> ")).lower()
    if player_input == "y":
        store(player)
    else:
        print(f"Very well, thank you {player_name} for playing. Goodbye")


if __name__ == "__main__":
    run_intro()
