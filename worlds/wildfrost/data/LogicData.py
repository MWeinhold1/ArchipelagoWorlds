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