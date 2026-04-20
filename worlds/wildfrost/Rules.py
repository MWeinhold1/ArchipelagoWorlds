from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .World import WildfrostWorld
    from .data.ItemData import charm_map
    from .data.LocationData import building_challenges, hotspring_challenges, icebreaker_challenges, inventors_challenges, pethouse_challenges, tribehall_challenges

def set_all_rules(world: WildfrostWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: WildfrostWorld) -> None:
    # TODO
    return

def set_all_location_rules(world: WildfrostWorld) -> None:
    # TODO
    # I have no idea if any of this works
    for region in world.regions:
        for location_name in region.locations:
            # Spent some time implementing this part then realized this is probably better done with regions (or maybe not idk)

            #rules = []

            #order_rule
            #add_order_rule = False
            #if location_name in building_challenges and not world.options.bypass_building_order:
            #    add_order_rule = True
            #    order = building_challenges[location_name]:
            #    order_rule = def accessible(state):
            #        return set(state.advancements) >= set(building_challenges[:order])
            #if not world.options.bypass_quest_order:
            #    if location_name in hotspring_challenges:
            #        add_order_rule = True
            #        order = hotspring_challenges[location_name]:
            #        order_rule = def accessible(state):
            #            return set(state.advancements) >= set(hotspring_challenges[:order])
            #    if location_name in icebreaker_challenges:
            #        add_order_rule = True
            #        order = icebreaker_challenges[location_name]:
            #        order_rule = def accessible(state):
            #            return set(state.advancements) >= set(icebreaker_challenges[:order])
            #    if location_name in inventors_challenges:
            #        add_order_rule = True
            #        order = inventors_challenges[location_name]:
            #        order_rule = def accessible(state):
            #            return set(state.advancements) >= set(inventors_challenges[:order])
            #    if location_name in pethouse_challenges:
            #        add_order_rule = True
            #        order = pethouse_challenges[location_name]:
            #        order_rule = def accessible(state):
            #            return set(state.advancements) >= set(pethouse_challenges[:order])
            #    if location_name in tribehall_challenges:
            #        add_order_rule = True
            #        order = tribehall_challenges[location_name]:
            #        order_rule = def accessible(state):
            #            return set(state.advancements) >= set(tribehall_challenges[:order])
            #if add_order_rule:
            #    rules.append(order_rule)

            rule
            add_rule = True
            match (location_name):
                case "Hot Spring Challenge - Equip 10 Charms":
                    rule = def accessible(state):
                        return state.has_any(*charm_map.keys())
                case "Hot Spring Challenge - Summon 50 allies":
                    rule = def accessible(state):
                        shademancer_access = (state.has("Shademancers Tribe") or not world.options.shuffle_tribes)
                        summoning_item_access = state.has_any("Beepop Mask", "Fallow Mask", "Junjun Mask",\
                            "Leech Mask", "Pom Mask", "Sheepopper Mask", "Snuffer Mask", "Tigris Mask")
                        summoning_companion_access = state.has_any("Egg", "Chikichi", "Spoof")
                        return  (summoning_item_access or summoning_companion_access or not world.options.random_inventory) and shademancer_access \
                        #   or (summoning_item_access and state.has("Gnome Traveller"))
                        #^ Commented out because its very RNG. Could be considered for some kind of "harder logic" setting if we want to do that
                        #Also technically possible without any cards because there are two shademancer leader types that summon (Summon Beepop & Summon Fallow When Deployed)
                case _:
                    add_rule = False

            #v this is remains of the big commented out code block above v

            #rules.append(rule)
            #overall_rule = def accessible(state):
            #    for rule in rules:
            #        if not rule(state):
            #            return False
            #    return True
            if add_rule:
                set_rule(location_name, rule)
    return

def set_completion_condition(world: WildfrostWorld) -> None:
    # TODO improve
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)