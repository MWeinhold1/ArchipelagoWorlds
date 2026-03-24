from __future__ import annotations
from BaseClasses import Item
from typing import TYPE_CHECKING
from .data.ItemData import ITEM_NAME_TO_ID, ITEM_NAME_TO_CLASSIFICATION, building_list, charm_map, companions_map, item_card_map, bell_list, map_event_list, tribe_list, filler_list

if TYPE_CHECKING:
    from .World import WildfrostWorld

class WildfrostItem(Item):
    game = "Wildfrost"

def get_random_filler_item_name(world: WildfrostWorld) -> str:
    # TODO use random filler chance based on options
    # return world.random.choice(filler_list.keys)
    return list(filler_list.keys())[0]

def create_item(world: WildfrostWorld, name: str) -> WildfrostItem:
    id = ITEM_NAME_TO_ID[name]
    classification = ITEM_NAME_TO_CLASSIFICATION[name]
    return WildfrostItem(name, classification, id, world.player)

def create_all_items(world: WildfrostWorld) -> None:
    # Start with items that are always put into the item pool
    itempool: list[Item] = []
    itempool += [(world.create_item(x)) for x in building_list.keys()]
    itempool += [(world.create_item(x)) for x in charm_map.keys()]
    itempool += [(world.create_item(x)) for x in companions_map.keys()]
    itempool += [(world.create_item(x)) for x in item_card_map.keys()]
    itempool += [(world.create_item(x)) for x in bell_list.keys()]
    itempool += [(world.create_item(x)) for x in tribe_list.keys()]

    # TODO: Add optional items
    itempool += [(world.create_item(x)) for x in map_event_list.keys()]

    # Determine number of filler items needed
    num_of_items = len(itempool)
    num_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    num_filler_items = num_unfilled_locations - num_of_items
    
    print("Number of items: " + str(num_of_items))
    print("Number of empty locations: " + str(num_unfilled_locations))
    print("Number of filler items: " + str(num_filler_items))

    # Use helper function to add filler items
    itempool += [world.create_filler() for _ in range(num_filler_items)]

    # Commit item pool
    world.multiworld.itempool += itempool