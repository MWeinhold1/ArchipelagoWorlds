from __future__ import annotations
from BaseClasses import Location
from . import Items
from typing import TYPE_CHECKING
from .data import LocationData
from .data.LocationData import LOCATION_NAME_TO_ID, building_challenges_map, idols_map, enemy_kills_map, miniboss_kills_map, boss_kills_map, extra_enemy_kills_map, item_card_map, companions_map, charm_map, boss_reward_map

if TYPE_CHECKING:
    from .World import WildfrostWorld

class WildfrostLocation(Location):
    game = "Wildfrost"

def create_all_locations(world: WildfrostWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def add_location_to_pool(world: WildfrostWorld, region: Region, location_name: str) -> WildfrostLocation: # type: ignore
    "A basic function for adding a specific location to the location pool for the create_regular_locations function."
    return (WildfrostLocation(world.player, location_name, LOCATION_NAME_TO_ID[location_name], region))

def create_regular_locations(world: WildfrostWorld) -> None:
    # TODO: Place items in correct regions, and in correct amounts
    # TODO: Remove locations based on options, like tribe challenges.
    locationpool: list[Location] = []

    #Regions (I hope using string names works)
    snowdwell    = world.get_region("Snowdwell")
    shademancers = world.get_region("Shademancers")
    clunkmasters = world.get_region("Clunkmasters")
    # pethouse     = world.get_region("Pethouse")       #These dont work
    # inventors    = world.get_region("Inventors")
    # icebreaker   = world.get_region("Icebreaker")
    # hotspring    = world.get_region("HotSpring")


    #Add building challenge locations, if enabled:
    #TODO: Seperate building challenges into regions
    if world.options.town_buildings:
        locationpool += [add_location_to_pool(world, snowdwell, locationName) for locationName in building_challenges_map]
    
    #Add locations for idols, if enabled:
    if True: #Always enabled (for now)
        locationpool += [add_location_to_pool(world, snowdwell, locationName) for locationName in idols_map if locationName not in world.options.idol_difficulty] #Remove the idols disabled by the option
    
    #Add locations for enemy kills:
    if "Enemies" in world.options.kill_checks.value:
        locationpool += [add_location_to_pool(world, snowdwell, locationName) for locationName in enemy_kills_map]

    #Add locations for miniboss kills:
    if "Mini Bosses" in world.options.kill_checks.value: #Always enabled (for now)
        locationpool += [add_location_to_pool(world, snowdwell, locationName) for locationName in miniboss_kills_map]

    #Add locations for boss kills:
    if "Bosses" in world.options.kill_checks.value: #Always enabled (for now)
        locationpool += [add_location_to_pool(world, snowdwell, locationName) for locationName in boss_kills_map]

    #Add locations for eye of the storm kills:
    if "Storm Only" in world.options.kill_checks.value: #Always enabled (for now)
        locationpool += [add_location_to_pool(world, snowdwell, locationName) for locationName in extra_enemy_kills_map]
    
    #Add random location checks for item cards:
    if True: #Always enabled (for now)
        locationpool += [add_location_to_pool(world, snowdwell, locationName) for locationName in item_card_map]
    
    #Add random location checks for companions:
    if True: #Always enabled (for now)
        locationpool += [add_location_to_pool(world, snowdwell, locationName) for locationName in companions_map]
    
    #Add random locations checks for gaining charms:
    if world.options.shuffle_charms: #Toggle
        locationpool += [add_location_to_pool(world, snowdwell, locationName) for locationName in charm_map]
    
    #Add locations for boss rewards:
    if True: #Always enabled (for now)
        locationpool += [add_location_to_pool(world, snowdwell, locationName) for locationName in boss_reward_map]

    snowdwell.locations += locationpool

    # snowdwell = world.get_region("Snowdwell")
    # locations_to_use = LOCATION_NAME_TO_ID
    # locations_to_remove = []
    
    # extra_enemies = (
    #     "Grizzle",
    #     "Plum",
    #     "Willow",
    #     "Bombarder",
    #     "Mega Mimik",
    #     "Plinker"
    # )

    # remove_bosses_flag        = not ("Bosses" in world.options.kill_checks.value)
    # remove_minibosses_flag    = not ("Mini Bosses" in world.options.kill_checks.value)
    # remove_enemies_flag       = not ("Enemy" in world.options.kill_checks.value)
    # remove_extra_enemies_flag = not ("Extra" in world.options.kill_checks.value)

    # for key in locations_to_use.keys():
    #     if key in LocationData.boss_kills and remove_bosses_flag:
    #         locations_to_remove.append(key)
    #     if key in LocationData.miniboss_kills and remove_minibosses_flag:
    #         locations_to_remove.append(key)
    #     if key in LocationData.enemy_kills and not key[5::] in extra_enemies and remove_enemies_flag:
    #         locations_to_remove.append(key)
    #     if key[5::] in extra_enemies and remove_extra_enemies_flag:
    #         locations_to_remove.append(key)
            
    # for key in locations_to_remove:
    #     locations_to_use.pop(key, 0)
                
    # snowdwell.locations += [(WildfrostLocation(world.player, locationName, LOCATION_NAME_TO_ID[locationName], snowdwell)) for locationName in locations_to_use]

def create_events(world: WildfrostWorld) -> None:
    #TODO: Improve
    snowdwell = world.get_region("Snowdwell")
    snowdwell.add_event(
        "Goal Completed", "Victory", location_type=WildfrostLocation, item_type=Items.WildfrostItem
    )