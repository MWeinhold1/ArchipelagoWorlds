from . import World as WildfrostWorld

def set_all_rules(world: WildfrostWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: WildfrostWorld) -> None:
    # TODO
    return

def set_all_location_rules(world: WildfrostWorld) -> None:
    # TODO
    return

def set_completion_condition(world: WildfrostWorld) -> None:
    # TODO improve
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)