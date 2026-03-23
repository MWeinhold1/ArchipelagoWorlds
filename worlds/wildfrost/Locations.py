from __future__ import annotations
from BaseClasses import Location
from . import Items
from typing import TYPE_CHECKING
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
    snowdwell.locations += [(WildfrostLocation(world.player, locationName, LOCATION_NAME_TO_ID[locationName], snowdwell)) for locationName in LOCATION_NAME_TO_ID]

def create_events(world: WildfrostWorld) -> None:
    #TODO: Improve
    snowdwell = world.get_region("Snowdwell")
    snowdwell.add_event(
        "Goal Completed", "Victory", location_type=WildfrostLocation, item_type=Items.WildfrostItem
    )