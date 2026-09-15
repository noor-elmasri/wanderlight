from wanderlight import Player , Item , Room

def test_has_item():
    player = Player("TestPlayer", "TestMillbrook")
    assert player.has_item("Map") == False
    player.pick_up(Item("Map", "A hand-drawn map of the region."))
    assert player.has_item("Map") == True


def test_describe_lists_exits():
    room = Room("Millbrook", "A quiet village with a general store.", {"north": "Bramblegate"})
    assert room.describe() == "Millbrook\nA quiet village with a general store.\nExits: north"
    