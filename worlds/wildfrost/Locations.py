from __future__ import annotations
from BaseClasses import Location
from . import Items
from typing import TYPE_CHECKING
from .data import LocationData
from .data.LocationData import LOCATION_NAME_TO_ID, building_challenges_map, idols_map, enemy_kills_map, boss_kills_map, item_card_map, companions_map, charm_map, boss_reward_map

if TYPE_CHECKING:
    from .World import WildfrostWorld

class WildfrostLocation(Location):
    game = "Wildfrost"

def create_all_locations(world: WildfrostWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: WildfrostWorld) -> None:
    # TODO: Place items in correct regions, and in correct amounts
    snowdwell = world.get_region("Snowdwell")
    locations_to_use = LOCATION_NAME_TO_ID
    locations_to_remove = []
    
    extra_enemies = (
        "Grizzle",
        "Plum",
        "Willow",
        "Bombarder",
        "Mega Mimik",
        "Plinker"
    )
    
    remove_bosses_flag = False
    remove_minibosses_flag = False
    remove_enemies_flag = False
    remove_extra_enemies_flag = False
    if not ("Bosses" in world.options.kill_checks.value):
        remove_bosses_flag = True
    if not ("Mini Bosses" in world.options.kill_checks.value):
        remove_minibosses_flag = True
    if not ("Enemy" in world.options.kill_checks.value):
        remove_enemies_flag = True
    if not ("Extra" in world.options.kill_checks.value):
        remove_extra_enemies_flag = True

    for key in locations_to_use.keys():
        if key in LocationData.boss_kills and remove_bosses_flag:
            locations_to_remove.append(key)
        if key in LocationData.miniboss_kills and remove_minibosses_flag:
            locations_to_remove.append(key)
        if key in LocationData.enemy_kills and not key[5::] in extra_enemies and remove_enemies_flag:
            locations_to_remove.append(key)
        if key[5::] in extra_enemies and remove_extra_enemies_flag:
            locations_to_remove.append(key)
            
    for key in locations_to_remove:
        locations_to_use.pop(key, 0)
                
    snowdwell.locations += [(WildfrostLocation(world.player, locationName, LOCATION_NAME_TO_ID[locationName], snowdwell)) for locationName in locations_to_use]

def create_events(world: WildfrostWorld) -> None:
    #TODO: Improve
    snowdwell = world.get_region("Snowdwell")
    snowdwell.add_event(
        "Goal Completed", "Victory", location_type=WildfrostLocation, item_type=Items.WildfrostItem
    )