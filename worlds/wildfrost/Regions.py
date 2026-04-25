from __future__ import annotations
from BaseClasses import Region
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .World import WildfrostWorld

startingRegion = "Snowdwell"
#snowdwellerRegion = "Snowdwellers"
#shademancerRegion = "Shademancers"
#clunkmasterRegion = "Clunkmasters"
pethouseRegion = "Pet House"
inventorsRegion = "Inventor's Hut"
icebreakerRegion = "Icebreaker's Cabin"
hotspringRegion = "Hot Springs"

fight1Region = "Fight 1"
fight2Region = "Fight 2"
fight3Region = "Fight 3"
fight4Region = "Fight 4"
fight5Region = "Fight 5"
fight6Region = "Fight 6"
fight7Region = "Fight 7"
eyeRegion = "Eye of the Storm"
heartRegion = "Heart of the storm"

def create_and_connect_regions(world: WildfrostWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: WildfrostWorld) -> None:
    # Define regions that can have multiple locations hidden behind them
    snowdwell = Region(startingRegion, world.player, world.multiworld)
    #snowdwellers = Region(snowdwellerRegion, world.player, world.multiworld)
    #shademancers = Region(shademancerRegion, world.player, world.multiworld)
    #clunkmasters = Region(clunkmasterRegion, world.player, world.multiworld)
    pethouse = Region(pethouseRegion, world.player, world.multiworld)
    inventors = Region(inventorsRegion, world.player, world.multiworld)
    icebreaker = Region(icebreakerRegion, world.player, world.multiworld)
    hotspring = Region(hotspringRegion, world.player, world.multiworld)

    fight1 = Region(fight1Region, world.player, world.multiworld)
    fight2 = Region(fight2Region, world.player, world.multiworld)
    fight3 = Region(fight3Region, world.player, world.multiworld)
    fight4 = Region(fight4Region, world.player, world.multiworld)
    fight5 = Region(fight5Region, world.player, world.multiworld)
    fight6 = Region(fight6Region, world.player, world.multiworld)
    fight7 = Region(fight7Region, world.player, world.multiworld)
    eye = Region(eyeRegion, world.player, world.multiworld)
    heart = Region(heartRegion, world.player, world.multiworld)

    regions = [snowdwell, pethouse, inventors, icebreaker, hotspring, fight1, fight2, fight3, fight4, fight5, fight6, fight7, eye, heart]
    # \regions = [snowdwell, snowdwellers, shademancers, clunkmasters, pethouse, inventors, icebreaker, hotspring]
    
    # TODO: Use options to determine if fights are also regions for monster kills

    world.multiworld.regions += regions

def connect_regions(world: WildfrostWorld) -> None:
    # Fetch regions, since we're out of scope from create_all_regions
    snowdwell = world.get_region(startingRegion)
    #snowdwellers = world.get_region(snowdwellerRegion)
    #shademancers = world.get_region(shademancerRegion)
    #clunkmasters = world.get_region(clunkmasterRegion)
    pethouse = world.get_region(pethouseRegion)
    inventors = world.get_region(inventorsRegion)
    icebreaker = world.get_region(icebreakerRegion)
    hotspring = world.get_region(hotspringRegion)
    
    fight1 = world.get_region(fight1Region)
    fight2 = world.get_region(fight2Region)
    fight3 = world.get_region(fight3Region)
    fight4 = world.get_region(fight4Region)
    fight5 = world.get_region(fight5Region)
    fight6 = world.get_region(fight6Region)
    fight7 = world.get_region(fight7Region)
    eye = world.get_region(eyeRegion)
    heart = world.get_region(heartRegion)

    #snowdwell.connect(snowdwellers, "Unlock Snowdwellers", lambda state: state.has("Snowdwellers Tribe", world.player))
    #snowdwell.connect(shademancers, "Unlock Shademancers", lambda state: state.has("Shademancers Tribe", world.player))
    #snowdwell.connect(clunkmasters, "Unlock Clunkmasters", lambda state: state.has("Clunkmasters Tribe", world.player))

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
    
    snowdwell.connect(fight1, "Unlock Fight 1")
    match(world.options.fight_gating.value):
        case 0:
            snowdwell.connect(fight2, "Unlock Fight 2")
            snowdwell.connect(fight3, "Unlock Fight 3")
            snowdwell.connect(fight4, "Unlock Fight 4")
            snowdwell.connect(fight5, "Unlock Fight 5")
            snowdwell.connect(fight6, "Unlock Fight 6")
            snowdwell.connect(fight7, "Unlock Fight 7")
            snowdwell.connect(eye, "Unlock Eye of the Storm")
            snowdwell.connect(heart, "Unlock Heart of the Storm")
        case 1:
            snowdwell.connect(fight2, "Unlock Fight 2", lambda state: state.count("Progressive Fight", world.player) > 0)
            snowdwell.connect(fight3, "Unlock Fight 3", lambda state: state.count("Progressive Fight", world.player) > 1)
            snowdwell.connect(fight4, "Unlock Fight 4", lambda state: state.count("Progressive Fight", world.player) > 2)
            snowdwell.connect(fight5, "Unlock Fight 5", lambda state: state.count("Progressive Fight", world.player) > 3)
            snowdwell.connect(fight6, "Unlock Fight 6", lambda state: state.count("Progressive Fight", world.player) > 4)
            snowdwell.connect(fight7, "Unlock Fight 7", lambda state: state.count("Progressive Fight", world.player) > 5)
            snowdwell.connect(eye, "Unlock Eye of the Storm", lambda state: state.count("Progressive Fight", world.player) > 6)
            snowdwell.connect(heart, "Unlock Heart of the Storm", lambda state: state.count("Progressive Fight", world.player) > 7\
            and state.has_all({"The Lumin Vase", "Lumin Goop", "Broken Vase"}, world.count))
        case 2:
            snowdwell.connect(fight2, "Unlock Fight 2")
            snowdwell.connect(fight3, "Unlock Fight 3")
            snowdwell.connect(fight4, "Unlock Fight 4", lambda state: state.count("Progressive Act", world.player) > 0)
            snowdwell.connect(fight5, "Unlock Fight 5", lambda state: state.count("Progressive Act", world.player) > 0)
            snowdwell.connect(fight6, "Unlock Fight 6", lambda state: state.count("Progressive Act", world.player) > 0)
            snowdwell.connect(fight7, "Unlock Fight 7", lambda state: state.count("Progressive Act", world.player) > 1)
            snowdwell.connect(eye, "Unlock Eye of the Storm", lambda state: state.count("Progressive Act", world.player) > 1)
            snowdwell.connect(heart, "Unlock Heart of the Storm", lambda state: state.count("Progressive Act", world.player) > 1\
            and state.has_all({"The Lumin Vase", "Lumin Goop", "Broken Vase"}, world.count))
        case 3:
            snowdwell.connect(fight2, "Unlock Fight 2", lambda state: state.count("Progressive Fight", world.player) > 0)
            snowdwell.connect(fight3, "Unlock Fight 3", lambda state: state.count("Progressive Fight", world.player) > 1)
            snowdwell.connect(fight4, "Unlock Fight 4", lambda state: state.count("Progressive Fight", world.player) > 2 and state.count("Progressive Act", world.player) > 0)
            snowdwell.connect(fight5, "Unlock Fight 5", lambda state: state.count("Progressive Fight", world.player) > 3 and state.count("Progressive Act", world.player) > 0)
            snowdwell.connect(fight6, "Unlock Fight 6", lambda state: state.count("Progressive Fight", world.player) > 4 and state.count("Progressive Act", world.player) > 0)
            snowdwell.connect(fight7, "Unlock Fight 7", lambda state: state.count("Progressive Fight", world.player) > 5 and state.count("Progressive Act", world.player) > 1)
            snowdwell.connect(eye, "Unlock Eye of the Storm", lambda state: state.count("Progressive Fight", world.player) > 6 and state.count("Progressive Act", world.player) > 1)
            snowdwell.connect(heart, "Unlock Heart of the Storm", lambda state: state.count("Progressive Fight", world.player) > 7\
            and state.count("Progressive Act", world.player) > 1\
            and state.has_all({"The Lumin Vase", "Lumin Goop", "Broken Vase"}, world.count))




    # TODO: Use options to define rules for monsters



    

