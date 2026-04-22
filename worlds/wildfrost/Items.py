from __future__ import annotations
from BaseClasses import Item
from typing import TYPE_CHECKING
from .data.ItemData import ITEM_NAME_TO_ID, ITEM_NAME_TO_CLASSIFICATION, pet_list, building_list, charm_map, companions_map, item_card_map, sun_bell_list, storm_bell_list, voyage_bell_list, map_event_list, tribe_list, filler_list

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
    # Start with items that are always put into the item pool ## Really? These are not always included
    itempool: list[Item] = []
    starting_cards: set[str] = {"Snow Stick", "Sun Rod", "FlameWater", "Woodhead", \
                                "Blizzard Bottle", "Junjun Mask", "Berry Bell", "Sunburst Tootoo",\
                                "Snowzooka", "Sunsong Box", "Junkhead"}

    #Item Cards, Companions and Pets: Always shuffle
    if True:
        itempool += [(world.create_item(x)) for x in companions_map.keys()]
        itempool += [(world.create_item(x)) for x in item_card_map.keys() if x not in starting_cards or world.options.random_inventory]
        if not world.options.random_inventory:
            (world.multiworld.push_precollected((world.create_item(x))) for x in starting_cards)
        itempool += [(world.create_item(x)) for x in pet_list.keys() if x != "Snoof" or world.options.random_snoof]
        if not world.options.random_snoof:
            world.multiworld.push_precollected((world.create_item("Snoof")))

    #Tribes: These will be added if Choice ShuffleTribes is postive.
    if world.options.shuffle_tribes:
        itempool += [(world.create_item(x)) for x in tribe_list.keys() if x + " Tribe" not in world.options.starting_tribes.value]
        for tribe in world.options.starting_tribes.value:
            world.multiworld.push_precollected(world.create_item(tribe + " Tribe"))
    else:
        world.multiworld.push_precollected(world.create_item("Snowdwellers Tribe"))
        world.multiworld.push_precollected(world.create_item("Shademancers Tribe"))
        world.multiworld.push_precollected(world.create_item("Clunkmasters Tribe"))

    #Buildings: These will be added if Toggle TownBuildings is enabled.
    if world.options.town_buildings:
        itempool += [(world.create_item(x)) for x in building_list.keys()]
    else:
        world.multiworld.push_precollected((world.create_item(x)) for x in building_list.keys())


    #Charms: These will be added if Toggle ShuffleCharms is enabled.
    if world.options.shuffle_charms:
        itempool += [(world.create_item(x)) for x in charm_map.keys()]
    else:
        (world.multiworld.push_precollected((world.create_item(x))) for x in charm_map.keys())

    #Bells: Shuffle if the requested bells should be shuffled.
    if world.options.sun_bells:
        itempool += [(world.create_item(x)) for x in sun_bell_list.keys()]
    else:
        (world.multiworld.push_precollected((world.create_item(x))) for x in sun_bell_list.keys())
    if world.options.storm_bells:
        itempool += [(world.create_item(x)) for x in storm_bell_list.keys()]
    else:
        (world.multiworld.push_precollected((world.create_item(x))) for x in storm_bell_list.keys())
    if world.options.voyage_bells:
        itempool += [(world.create_item(x)) for x in voyage_bell_list.keys()]
    else:
        (world.multiworld.push_precollected((world.create_item(x))) for x in voyage_bell_list.keys())

    # TODO: Add optional items
    itempool += [(world.create_item(x)) for x in map_event_list.keys()]

    # Determine number of filler items needed
    num_of_items = len(itempool)
    num_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    num_filler_items = num_unfilled_locations - num_of_items
    
    print(f"Number of items: {num_of_items}")
    print(f"Number of empty locations: {num_unfilled_locations}")
    print(f"Number of filler items: {num_filler_items}")

    # Use helper function to add filler items
    itempool += [world.create_filler() for _ in range(num_filler_items)]

    # Commit item pool
    world.multiworld.itempool += itempool