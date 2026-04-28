#WIP
#TODO: Actually read item data
stormstrength_values = {
    # Values for all the storm bell strengths
    "Blingsnail Bell":  1,
    "Bell of Death":    1,
    "Titan Bell":       2,
    "Frosthand Bell":   1,
    "Gunk Bell":        1,
    "Icebourne Bell":   2,
    "Horde Bell":       2,
    "Gloom Bell":       1,
    "Frostbourne Bell": 2,
    "Gobbler Bell":     2,
    "Tyrant Bell":      2,
    "Dread Bell":       3,
    "Blood Bell":       2,
}

#Naked Gnome appears in every fight 1. Gobling appears in every non-boss fight. Gobbler appears in every boss fight except heart of the storm if gobbler bell is enabled.
fight_enemies = {
  "The Pengoons": {"Chungoon", "Gogong", "Pengoon", "Waddlegoons", "Wild Snoolf", "Big Peng"},
  "The Snowbo Squad": {"Baby Snowbo", "Grouchy", "Gogong", "Snowbo", "Wild Snoolf", "Winter Worm", "The Snow Knight"},  
  "The Bog Berries": {"Beeberry", "Wild Snoolf", "Baby Snowbo", "Gogong", "Berry Witch", "Bogberry"},
  "The Snow Lumps": {"Lump", "Wild Snoolf", "Gogong", "Porkypine", "Nimbus"},

  "The Globerries": {"Berry Witch", "Earth Berry", "Porkypine", "Snowbirb", "Queen Globerry"},
  "The Frost Shades": {"Frostinger", "Ice Lantern", "Mimik", "Porkypine", "Snowbirb", "The Ringer"},
  "The Noxious Shrooms": {"Bulbhead", "Popshroom", "Puffball", "Shroom Gobbler", "Shrootles", "Veiled Lady"},
  "The Snowland Bears": {"Frostinger", "Porkypine", "Ooba Bear", "Snow Gobbler", "Bumbo"},

  "Infernoko": {"Frostinger", "Minimoko", "Porkypine", "Infernoko"},
  "Bamboozle": {"Baby Snowbo", "Grouchy", "Snowbo", "Wild Snoolf", "Winter Worm", "Bamboozle"},

  "The Demonhorn Goats": {"Gok", "Jab Joat", "Porkypine", "Pygmy", "Muttonhead"},
  "The Shelled Husks": {"Conker", "Pecan", "Prickle", "Shell Witch", "Bolgo"},
  "The Spice Mokos": {"Grog", "Grumps", "Makoko", "Moko Head", "Pepper Witch", "King Moko"},
  
  "The Wooly Drek": {"Bigfoot", "Gromble", "Paw Paw", "Woolly Drek", "Bigloo"},
  "The Toothy Shades": {"Gromble", "Paw Paw", "Smog", "Marrow", "Maw Jaw"},
  "The Ink Sacks": {"Octako", "Tentickle", "Kraken", "Ooba Bear", "Octobom", "Lumako"},
  
  "Krunker": {"Grink", "Ice Forge", "Spike Wall", "Spuncher", "Krunker"},
  "Truffle": {"Popshroom", "Puffball", "Shroom Gobbler", "Shrootles", "Truffle"},
  
  "The Ice Krabs": {"Burster", "Krab", "Krawler", "Numskull"},
  "The Wild Hogs": {"Hog", "Rockhog", "Warthog", "Razor"},
  "The Gunk Bugs": {"Dungrok", "Gunkback", "Gunk Gobbler", "Blaze Beetles", "Weevil"},

  "Eye of the Storm": {"Frost Guardian", "Bigfoot", "Grink", "Grizzle", "Ice Forge", "Mega Mimik", "Plum", "Rockhog", "Spike Wall", "Ooba Bear", "Porkypine", "Winter Worm"},
  
  "Heart of the Storm": {"Frost Jailer", "Frost Lancer", "Frost Junker", "Frost Crusher", "Frost Bomber", "Frost Muncher"},
}

fight_numbers = {
  "Fight 1": {"The Pengoons", "The Snowbo Squad", "The Bog Berries", "The Snow Lumps"},
  "Fight 2": {"The Globerries", "The Frost Shades", "The Noxious Shrooms", "The Snowland Bears"},
  "Fight 3": {"Infernoko", "Bamboozle"},
  "Fight 4": {"The Demonhorn Goats", "The Shelled Husks", "The Spice Mokos"},
  "Fight 5": {"The Wooly Drek", "The Toothy Shades", "The Ink Sacks"},
  "Fight 6": {"Krunker", "Truffle"},
  "Fight 7": {"The Ice Krabs", "The Wild Hogs", "The Gunk Bugs"},
  "Eye of the Storm": {"Eye of the Storm"},
  "Heart of the Storm": {"Heart of the Storm"}
}

def get_stormstrength_values(available_bells: list[str]) -> list[int]:
    """
    Get the values of available stormstrength bells.
    """
    return [
        stormstrength_values[i] for i in available_bells
    ]
    
    
def get_stormstrength_reachable_step(available_point_amounts: list[int], target: int) -> bool:  
    if sum(available_point_amounts) < target:
        return False
    elif available_point_amounts.count(1) >= target:
        return True
    elif 3 in available_point_amounts and target >= 3:
        new_available_point_amounts = available_point_amounts.copy()
        new_available_point_amounts.remove(3)
        return get_stormstrength_reachable_step(new_available_point_amounts, target - 3)
    elif 2 in available_point_amounts and target >= 2:
        new_available_point_amounts = available_point_amounts.copy()
        new_available_point_amounts.remove(2)
        return get_stormstrength_reachable_step(new_available_point_amounts, target - 2)
    else:
        return False
    

def get_stormstrength_reachable(available_bells: list[str], target: int) -> bool:
    "Determine if it is possible to reach the target with the available storm bells."
    available_point_amounts = get_stormstrength_values(available_bells)
    return get_stormstrength_reachable_step(available_point_amounts, target)


def main():
    "Test the logic"
    assert get_stormstrength_reachable(
      [], 0  
    ) == True, 1
    assert get_stormstrength_reachable(
      ["Blingsnail Bell", "Bell of Death", "Titan Bell", "Frosthand Bell"], 5
    ) == True, 2
    assert get_stormstrength_reachable(
      ["Blingsnail Bell", "Bell of Death", "Titan Bell", "Frosthand Bell"], 6
    ) == False, 3
    assert get_stormstrength_reachable(
      ["Blingsnail Bell", "Bell of Death", "Titan Bell", "Frosthand Bell"], 4
    ) == True, 4
    assert get_stormstrength_reachable(
      ["Tyrant Bell", "Dread Bell", "Blood Bell"], 5  
    ) == True, 5
    assert get_stormstrength_reachable(
      ["Tyrant Bell", "Dread Bell", "Blood Bell"], 7  
    ) == True, 6
    assert get_stormstrength_reachable(
      ["Tyrant Bell", "Dread Bell", "Blood Bell"], 6  
    ) == False, 7
    assert get_stormstrength_reachable(
      ["Tyrant Bell", "Dread Bell", "Blood Bell"], 1  
    ) == False, 8
    assert get_stormstrength_reachable(
      ["Tyrant Bell", "Dread Bell", "Blood Bell"], 4  
    ) == False, 9

    print("Passed without a hitch!")


if __name__ == "__main__":
    main()