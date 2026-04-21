from __future__ import annotations
from BaseClasses import Region
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .World import WildfrostWorld

startingRegion = "Snowdwell"
snowdwellerRegion = "Snowdwellers"
shademancerRegion = "Shademancers"
clunkmasterRegion = "Clunkmasters"
pethouseRegion = "Pet House"
inventorsRegion = "Inventor's Hut"
icebreakerRegion = "Icebreaker's Cabin"
hotspringRegion = "Hot Springs"

def create_and_connect_regions(world: WildfrostWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: WildfrostWorld) -> None:
    # Define regions that can have multiple locations hidden behind them
    snowdwell = Region(startingRegion, world.player, world.multiworld)
    snowdwellers = Region(snowdwellerRegion, world.player, world.multiworld)
    shademancers = Region(shademancerRegion, world.player, world.multiworld)
    clunkmasters = Region(clunkmasterRegion, world.player, world.multiworld)
    pethouse = Region(pethouseRegion, world.player, world.multiworld)
    inventors = Region(inventorsRegion, world.player, world.multiworld)
    icebreaker = Region(icebreakerRegion, world.player, world.multiworld)
    hotspring = Region(hotspringRegion, world.player, world.multiworld)

    regions = [snowdwell, snowdwellers, shademancers, clunkmasters, pethouse, inventors, icebreaker, hotspring]
    
    # TODO: Use options to determine if fights are also regions for monster kills

    world.multiworld.regions += regions

def connect_regions(world: WildfrostWorld) -> None:
    # Fetch regions, since we're out of scope from create_all_regions
    snowdwell = world.get_region(startingRegion)
    snowdwellers = world.get_region(snowdwellerRegion)
    shademancers = world.get_region(shademancerRegion)
    clunkmasters = world.get_region(clunkmasterRegion)
    pethouse = world.get_region(pethouseRegion)
    inventors = world.get_region(inventorsRegion)
    icebreaker = world.get_region(icebreakerRegion)
    hotspring = world.get_region(hotspringRegion)

    snowdwell.connect(snowdwellers, "Unlock Snowdwellers", lambda state: state.has("Snowdwellers Tribe", world.player))
    snowdwell.connect(shademancers, "Unlock Shademancers", lambda state: state.has("Shademancers Tribe", world.player))
    snowdwell.connect(clunkmasters, "Unlock Clunkmasters", lambda state: state.has("Clunkmasters Tribe", world.player))

    if world.options.town_buildings:
        if world.options.bypass_town_order:
            snowdwell.connect(pethouse, "Build Pet House", lambda state: state.has("Pet House", world.player))
            snowdwell.connect(inventors, "Build Inventor's Hut", lambda state: state.has("Inventor's Hut", world.player))
            snowdwell.connect(icebreaker, "Build Icebreaker Cabin", lambda state: state.has("Icebreaker Cabin", world.player))
            snowdwell.connect(hotspring, "Build Hot Spring", lambda state: state.has("Hot Spring", world.player))
        else:
            snowdwell.connect(pethouse, "Build Pet House", lambda state: state.has("Pet House", world.player))
            pethouse.connect(inventors, "Build Inventor's Hut", lambda state: state.has("Inventor's Hut", world.player))
            inventors.connect(icebreaker, "Build Icebreaker Cabin", lambda state: state.has("Icebreaker Cabin", world.player))
            icebreaker.connect(hotspring, "Build Hot Spring", lambda state: state.has("Hot Spring", world.player))
    else:
        snowdwell.connect(pethouse, "Build Pet House")
        snowdwell.connect(inventors, "Build Inventor's Hut")
        snowdwell.connect(icebreaker, "Build Icebreaker Cabin")
        snowdwell.connect(hotspring, "Build Hot Spring")

    # TODO: Use options to define rules for monsters



    

