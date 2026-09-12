from wanderlight import Player , Item

def test_has_item():
    player = Player("TestPlayer", "TestMillbrook")
    assert player.has_item("Map") == False
    player.pick_up(Item("Map", "A hand-drawn map of the region."))
    assert player.has_item("Map") == True