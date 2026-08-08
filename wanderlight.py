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

    def __init__(self, starting_room_name):
        self.current_room = starting_room_name
        self.inventory = []  # list of Item objects

    def pick_up(self, item):
        self.inventory.append(item)

    def has_item(self, item_name):
        """Check if the player is carrying an item by name."""
        return any(item.name == item_name for item in self.inventory)
