from __future__ import annotations
from typing import TYPE_CHECKING
from ..generic.Rules import add_rule, set_rule

if TYPE_CHECKING:
    from ...BaseClasses import CollectionState
    from .World import WildfrostWorld
    from .data import ItemData
    from .data.LocationData import building_challenges, hotspring_challenges, icebreaker_challenges, inventors_challenges, pethouse_challenges, tribehall_challenges
    from .data.LogicData import fight_enemies, fight_numbers

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
    vanilla_locked_battles: set[str] = {"The Bog Berries", "The Snow Lumps", "The Noxious Shrooms", "The Toothy Shades",\
                                        "The Ink Sacks", "The Gunk Bugs"}
    for region in world.get_regions():
        for location in region.locations:
            
            # Spent some time implementing this part then realized this is probably better done with regions (or maybe not idk)

            #rules = []

            #order_rule
            #add_order_rule = False
            #if location_name in building_challenges and not world.options.bypass_town_order:
            #    add_order_rule = True
            #    order = building_challenges[location_name]:
            #    order_rule = def accessible(state):
            #        return set(state.advancements) >= set(building_challenges[:order])
            #if not world.options.bypass_building_order:
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
            if location.name.startswith("Kill"):
                enemyName = location.name.removeprefix("Kill ")
                fights = []
                (fights.append(x) for x in fight_enemies.keys() if enemyName in fight_enemies[x])
                for fight in fights:
                    match world.options.fights_in_pool.value:
                        case 0:
                            if fight in vanilla_locked_battles:
                                add_rule(lambda state: state.can_access_region(fight_region, world.player)\
                                    and state.can_access_region("Shademancers", world.player)\
                                    and state.can_access_region("Clunkmasters",world.player))
                                    #TODO proper logic for this^
                            else:
                                (add_rule(lambda state: state.can_access_region(fight_region, world.player))\
                                    for fight_region in fight_numbers.keys() if fight in fight_numbers[fight_region])
                        case 1:
                            if fight in vanilla_locked_battles:
                                (add_rule(lambda state: state.can_access_region(fight_region, world.player)\
                                and state.has(fight, world.player)) \
                                for fight_region in fight_numbers.keys() if fight in fight_numbers[fight_region])
                            else:
                                (add_rule(lambda state: state.can_access_region(fight_region, world.player))\
                                    for fight_region in fight_numbers.keys() if fight in fight_numbers[fight_region])
                        case 2:
                            (add_rule(lambda state: state.can_access_region(fight_region, world.player)\
                                and state.has(fight, world.player)) \
                                for fight_region in fight_numbers.keys() if fight in fight_numbers[fight_region])
                         
            match location.name:
                case "Hot Spring Challenge - Equip 10 Charms":
                    rule = lambda state: state.has_any({name for name in world.item_names if name.endswith("Charm")}, world.player)
                case "Hot Spring Challenge - Kill 20 enemies with Smackback":
                    rule = lambda state: state.has_any({"Punchfist Charm", "Gojiber"}, world.player)
                    #in hard logic we can consider splinter/spoof/shade wisp + shademancers + any fight that has smackback enemies
                    #...or just account for the fact that leaders can have smackback
                case "Hot Spring Challenge - Summon 50 allies":
                    rule = lambda state: \
                        state.has("Shademancers Tribe", world.player) \
                        and (state.has_any({"Beepop Mask", "Fallow Mask", "Junjun Mask",\
                            "Leech Mask", "Pom Mask", "Sheepopper Mask", "Snuffer Mask", "Tigris Mask", "Egg", "Chikichi", "Spoof"}, world.player)\
                            or not world.options.random_inventory) \
                        #or (state.has_any({"Beepop Mask", "Fallow Mask", "Junjun Mask",\
                        #   "Leech Mask", "Pom Mask", "Sheepopper Mask", "Snuffer Mask", "Tigris Mask"}, world.player)\
                        #   and state.has("Gnome Traveller"))
                        #^ Commented out because its very RNG. Could be considered for some kind of "harder logic" setting if we want to do that
                        #Also technically possible without any cards because there are two shademancer leader types that summon (Summon Beepop & Summon Fallow When Deployed)
                case "Hot Spring Challenge - Add 10 Scrap to Clunkers":
                    rule = lambda state: state.has_all({"Scrap Pile", "Snowdwellers Tribe"}, world.player)\
                        or (state.has("Clunkmasters Tribe", world.player) and state.has_any({"Gigi's Cookie Box", "Gigi's Gizmo", "Alloy"}, world.player))
                        #I'm not sure if scrap charm counts for this achievement, im pretty sure they only track stuff that happens mid-battle
                        #Also there's a clunkmaster leader type that can add scrap. For hard logic if we add that
                case "Icebreaker Cabin Challenge - Kill 15 Enemies with Shroom":
                    rule = lambda state: state.has("Snowdwellers Tribe", world.player) \
                        and (state.has_any({"Shroom Charm", "Truffle Charm", "Hongo's Hammer", "Spore Pack", "Wort", "Fungun"}, world.player)\
                            or (state.has("Fulbert", world.player) \
                                and state.has_any({"Spice Charm", "Peppering", "Peppereaper", "Dragon Pepper", "Spice Stones", "Pyra", \
                                    "Shield Charm", "Shell Shield", "Nutshell Cake", "Shellbo", "Kernel", "Shelly"}, world.player)\
                            )\
                        )
                    # can once again account for leaders in hard logic OR account for splinter/spoof/shade wisp
                case "Icebreaker Cabin Challenge - Feed the Muncher 5 Times":
                    rule = lambda state: state.has("Muncher", world.player)
                #case "Inventors Hut Challenge - Add 3 Clunkers to your deck":
                    #TODO
                #case "Inventors Hut Challenge - Block 10 hits with Clunkers":
                    #TODO (impossible with random starting inventory / only shademancer access)
                case "Inventors Hut Challenge - Apply 60 Shell":
                    rule = lambda state: state.has("Snowdwellers Tribe", world.player) and state.has_any({"Shield Charm", "Shell Shield", "Nutshell Cake", "Shellbo", "Kernel", "Shelly"}, world.player)
                    #can also account for splinter/spoof/shade wisp & shell witch/pecan
                #case "Pet House Challenge - Recall 3 Companions":
                    #state = lambda state: state.has_any({})
                    #I still don't know how to access our ItemData tuples from here since it errors on accessibility check saying it doesn't exist
                case "Pet House Challenge - Kill 3 Demonized enemies":
                    rule = lambda state: state.has("Loki", world.player) \
                        or state.has_any({"Demonheart", "Totem of the Goat", "Goat Charm"}, world.player)
                case "Pet House Challenge - Kill 10 enemies with Teeth":
                    rule = lambda state: state.has("Spike", world.player) \
                        or (state.has("Shademancers Tribe", world.player) \
                            and state.has_any({"Bite Charm", "Tiger Charm", "Tiger Skull", "Tusk", "Taiga"}, world.player))
                #case "Beastmaster Idol":
                    #TODO: requires access to a boss fight
                case "Berry Good Idol":
                    rule = lambda state: state.has("Pinkberry Juice", world.player) \
                        or (state.has_all({"Snowdwellers Tribe", "Jewelberry Charm"}, world.player) \
                            and state.has_any({"Booshu", "Nourish Charm", "Berry Basket", "Demonheart", "Heartmist Station", "Bonnie"}, world.player)) \
                        or (state.has("Shademancers Tribe", world.player) \
                            and (state.has("Berry Sis", world.player)\
                                or (state.has_any({"Van Jun", "Monch"}, world.player) \
                                    and (state.has_any({"Beepop Mask", "Fallow Mask", "Junjun Mask",\
                                        "Leech Mask", "Pom Mask", "Sheepopper Mask", "Snuffer Mask", "Tigris Mask", "Egg", "Chikichi", "Spoof"}, world.player)\
                                    )\
                                )\
                                or state.has("Berry Bell", world.player)
                                or not world.options.random_inventory\
                            )) 
                        # Big berry also heals but his healing is limited to on-kill which means its not infinitely reusable. Could be considered for hard logic
                        # Same for cloudberry charm
                #TODO: also check if can win a run
                case "Best Friends Idol":
                    rule = lambda state: state.has_any({"Snoof", "Booshu", "Loki", "Sneezle", "Spike", "Binku", "Lil' Gazi"}, world.player)
                #case "Big Hitter Idol":
                #case "Bigger Hitter Idol":
                #case "Charmless Idol":
                #case "Clunkmaster Idol":
                case "Feed The Beast Idol":
                    rule = lambda state: state.has("Muncher", world.player)
                #case "Gnomebringer Idol":
                #case "High Roller Idol":
                #case "Hoarder Idol":
                case "Icemaster Idol":
                    rule = lambda state: state.has_any({"Blunky", "Ice Dice"}, world.player)
                #case "Long Live The King Idol":
                #case "Minimalist Idol":
                #case "One Punch":
                case "Rampage Idol":
                    rule = lambda state: state.has_all({"Snowdwellers Tribe", "Tiny Tyko"}, world.player) \
                        or state.has_all({"Clunkmasters Tribe", "Mini Mika"}, world.player)
                    # Can also account for spoof/splinter/shade wisp and Wild enemies. Can also account for krono + Lupa. Is also possible by omega buffing the numbers on blaze tea but that's very very rng.
                #case "Shademancer Idol":
                #case "Snowball Fight":
                #case "Snowdweller Idol":
                #case "Sunbringer Idol":
                case "Tough Nut Idol":
                    rule = lambda state: state.has("Snowdwellers Tribe", world.player) and state.has_any({"Shell Shield", "Shellbo"}, world.player)
                    #Can also account for kernel + healing/frost. Can also account for splinter/spoof/shade wisp
                case "Toxic Idol":
                    rule = lambda state: state.has("Snowdwellers Tribe", world.player) \
                        and (state.has_any({"Fungun"}, world.player)\
                            or (state.has("Fulbert", world.player) \
                                and state.has_any({"Dragon Pepper", "Spice Stones", \
                                    "Shellbo"}, world.player)\
                            )\
                        )
                    # Removed a lot of stuff compared to the other shroom achievement because they need high hp enemies to be in logic first and we dont have fight logic yet
                    # can once again account for leaders in hard logic OR account for splinter/spoof/shade wisp
                #case "Undefeated Idol":
                #case _ if location.name.count("Boss Reward") > 0:
                case _:
                    continue
            set_rule(location, rule)
    return

def set_completion_condition(world: WildfrostWorld) -> None:
    # TODO improve
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)

def can_access_fight(state: CollectionState, world: WildfrostWorld, fight: str, fight_region: str) -> bool:
    return state.can_access_region(fight_region, world.player) and state.has(fight, world.player)