# Static Location Names
# TODO: Sperate these for proper regioning
building_challenges = (
    "Build Hot Spring",
    "Build Icebreaker Cabin",
    "Build Inventor Hut",
    "Build Pet House",
)
hotspring_challenges = (
    "Hot Spring Challenge - Equip 10 Charms",
    "Hot Spring Challenge - Deal 10 damage to your own team",
    "Hot Spring Challenge - Achieve a 4x kill combo",
    "Hot Spring Challenge - Kill 20 enemies with Smackback",
    "Hot Spring Challenge - Summon 50 allies",
    "Hot Spring Challenge - Add 10 Scrap to Clunkers",
)
icebreaker_challenges = (
    "Icebreaker Cabin Challenge - Gain 50 Bling from a Single battle",
    "Icebreaker Cabin Challenge - Kill 15 Enemies with Shroom",
    "Icebreaker Cabin Challenge - Feed the Muncher 5 Times",
)
inventors_challenges = (
    "Inventors Hut Challenge - Achieve a 3x kill combo",
    "Inventors Hut Challenge - Add 3 Clunkers to your deck",
    "Inventors Hut Challenge - Kill 20 enemies with Items",
    "Inventors Hut Challenge - Block 10 hits with Clunkers",
    "Inventors Hut Challenge - Apply 60 Shell",
    "Inventors Hut Challenge - Buy 10 Crown",
)
pethouse_challenges = (
    "Pet House Challenge - Recall 3 Companions",
    "Pet House Challenge - Kill 3 Demonized enemies",
    "Pet House Challenge - Buy 5 discounted Items",
    "Pet House Challenge - Kill 10 enemies with Teeth",
    "Pet House Challenge - Hit the Enemy Wave Bell 5 times",
    "Pet House Challenge - Achieve a 6x kill combo",
)
tribehall_challenges = (
    "Tribe Hall Challenge - Kill 100 Enemies",
    "Tribe Hall Challenge - Deal 1000 Damage",
)

idols = (
    "Balloonist Idol",
    "Beastmaster Idol",
    "Berry Good Idol",
    "Best Friends Idol",
    "Big Hitter Idol",
    "Bigger Hitter Idol",
    "Charmless Idol",
    "Clunkmaster Idol",
    "Feed The Beast Idol",
    "Gnome Friend Idol",
    "Gnomebringer Idol",
    "High Roller Idol",
    "Hoarder Idol",
    "Icemaster Idol",
    "Lone Survivor Idol",
    "Long Live The King Idol",
    "Minimalist Idol",
    "One Punch Idol",
    "Rampage Idol",
    "Ritual Idol",
    "Shademancer Idol",
    "Snowball Fight Idol",
    "Snowdweller Idol",
    "Sunbringer Idol",
    "Tough Nut Idol",
    "Toxic Idol",
    "Undefeated Idol",
)

enemy_kills = (
    "Kill Baby Snowbo",
    "Kill Beeberry",
    "Kill Berry Witch",
    "Kill Bigfoot",
    "Kill Blaze Beetles",
    "Kill Bulbhead",
    "Kill Burster",
    "Kill Chungoon",
    "Kill Conker",
    "Kill Dungrok",
    "Kill Earth Berry",
    "Kill Frostinger",
    "Kill Gobbler",
    "Kill Gobling",
    "Kill Gogong",
    "Kill Gok",
    "Kill Grink",
    "Kill Grog",
    "Kill Gromble",
    "Kill Grouchy",
    "Kill Grumps",
    "Kill Gunk Gobbler",
    "Kill Gunkback",
    "Kill Hog",
    "Kill Jab Joat",
    "Kill Krab",
    "Kill Kraken",
    "Kill Krawler",
    "Kill Lump",
    "Kill Makoko",
    "Kill Marrow",
    "Kill Minimoko",
    "Kill Octako",
    "Kill Ooba Bear",
    "Kill Paw Paw",
    "Kill Pecan",
    "Kill Pengoon",
    "Kill Pepper Witch",
    "Kill Popshroom",
    "Kill Porkypine",
    "Kill Prickle",
    "Kill Puffball",
    "Kill Pygmy",
    "Kill Rockhog",
    "Kill Shell Witch",
    "Kill Shroom Gobbler",
    "Kill Shrootles",
    "Kill Smog",
    "Kill Snow Gobbler",
    "Kill Snowbirb",
    "Kill Snowbo",
    "Kill Spuncher",
    "Kill Tentickle",
    "Kill Waddlegoons",
    "Kill Warthog",
    "Kill Wild Snoolf",
    "Kill Winter Worm",
    "Kill Woolly Drek",
    "Kill Naked Gnome",
    "Kill ArchipelaGnome",
    # Clunkers
    "Kill Ice Forge",
    "Kill Ice Lantern",
    "Kill Mimik",
    "Kill Octobom",
    "Kill Spike Wall",
)

extra_enemy_kills = (
    "Kill Grizzle",
    "Kill Plum",
    "Kill Willow",
    "Kill Bombarder",
    "Kill Mega Mimik",
    "Kill Plinker"
)

miniboss_kills = (
    # Minibosses
    "Kill Big Peng",
    "Kill Bigloo",
    "Kill Bogberry",
    "Kill Bolgo",
    "Kill Bumbo",
    "Kill King Moko",
    "Kill Lumako",
    "Kill Maw Jaw",
    "Kill Muttonhead",
    "Kill Nimbus",
    "Kill Numskull",
    "Kill Queen Globerry",
    "Kill Razor",
    "Kill The Ringer",
    "Kill The Snow Knight",
    "Kill Veiled Lady",
    "Kill Weevil",
)

boss_kills = (
    # Bosses
    "Kill Bamboozle",
    "Kill Infernoko",
    "Kill Krunker",
    "Kill Truffle",
    "Kill The Frost Guardian",
    "Kill Frost Bomber",
    "Kill Frost Crusher",
    "Kill Frost Jailer",
    "Kill Frost Junker",
    "Kill Frost Muncher",
    "Kill Frost Lancer",
)

# Dynamic Sized Location Name Parts
snow_name = "Snowdweller"
shade_name = "Shademancer"
clunk_name = "Clunkmaster"
item_card_name = "Item Card"
companion_name = "Companion"
charm_name = "Charm"
boss_reward_name = "Boss Reward"

#Number of repeatable locations per location
num_repeatable_locations = 99

# Location IDs are 5 digit numbers in the format of XYZZZ
# X = Location category
# Y = Location sub-category
# ZZZ = Incremented location number.
#
# Example: ID 51025
# X = 5 = Item Card
# Y = 1 = Shademancer Card Pool
# ZZZ = 25 = The 25th location in the item card pool

# Location Categories
# 1: Town
# 2: Idol
# 3: Enemy
# 4: Boss
# 5: Item
# 6: Companion
# 7: Charm
# 8: Boss rewards (AKA Bells)
# 
# _0: Generic
# _1: Snowdweller
# _2: Shademancer
# _3: Clunkmaster

# Static Location Maps
building_challenges_map = {x: 10000 + i for i,x in enumerate(building_challenges)}
total_category_ids = len(building_challenges)

hotspring_challenges_map = {x: 10000 + total_category_ids + i for i,x in enumerate(hotspring_challenges)}
total_category_ids += len(hotspring_challenges_map)

icebreaker_challenges_map = {x: 10000 + total_category_ids + i for i,x in enumerate(icebreaker_challenges)}
total_category_ids += len(icebreaker_challenges_map)

inventors_challenges_map = {x: 10000 + total_category_ids + i for i,x in enumerate(inventors_challenges)}
total_category_ids += len(inventors_challenges_map)

pethouse_challenges_map = {x: 10000 + total_category_ids + i for i,x in enumerate(pethouse_challenges)}
total_category_ids += len(pethouse_challenges_map)

tribehall_challenges_map = {x: 10000 + total_category_ids + i for i,x in enumerate(tribehall_challenges)}


idols_map               = {x: 20000 + i for i,x in enumerate(idols)}
enemy_kills_map         = {x: 30000 + i for i,x in enumerate(enemy_kills)}
extra_enemy_kills_map   = {x: 30000 + len(enemy_kills) + i for i,x in enumerate(extra_enemy_kills)}
miniboss_kills_map      = {x: 40000 + i for i,x in enumerate(miniboss_kills)}
boss_kills_map          = {x: 40000 + len(miniboss_kills) + i for i,x in enumerate(boss_kills)}

# Dynamic Sized Location Maps (currently limited to 99 per type)
snow_cards       = {f"{snow_name } {item_card_name} {i}": 51000 + i for i in range(1, num_repeatable_locations)}
shade_cards      = {f"{shade_name} {item_card_name} {i}": 52000 + i for i in range(1, num_repeatable_locations)}
clunk_cards      = {f"{clunk_name} {item_card_name} {i}": 53000 + i for i in range(1, num_repeatable_locations)}
item_card_map    = snow_cards | shade_cards | clunk_cards

snow_companions  = {f"{snow_name } {companion_name} {i}": 61000 + i for i in range(1, num_repeatable_locations)}
shade_companions = {f"{shade_name} {companion_name} {i}": 62000 + i for i in range(1, num_repeatable_locations)}
clunk_companions = {f"{clunk_name} {companion_name} {i}": 63000 + i for i in range(1, num_repeatable_locations)}
companions_map   = snow_companions | shade_companions | clunk_companions

snow_charms      = {f"{snow_name } {charm_name} {i}":     71000 + i for i in range(1, num_repeatable_locations)}
shade_charms     = {f"{shade_name} {charm_name} {i}":     72000 + i for i in range(1, num_repeatable_locations)}
clunk_charms     = {f"{clunk_name} {charm_name} {i}":     73000 + i for i in range(1, num_repeatable_locations)}
charm_map        = snow_charms | shade_charms | clunk_charms

boss_reward_map  = {f"{boss_reward_name} {i}":            80000 + i for i in range(1, num_repeatable_locations)}

# Full name to ID dictionary
LOCATION_NAME_TO_ID = building_challenges_map | idols_map | enemy_kills_map | extra_enemy_kills_map | miniboss_kills_map | boss_kills_map | item_card_map | companions_map | charm_map | boss_reward_map