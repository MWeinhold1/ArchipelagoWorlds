# Static Location Names
building_challenges = {
    "Build Hot Spring",
    "Build Icebreaker Cabin",
    "Build Inventor Hut",
    "Build Pet House",
    #"Build Tribe Hall",
    "Tribe Hall Challenge - Kill 100 Enemies",
    "Tribe Hall Challenge - Deal 1000 Damage",
    "Pet House Challenge - Recall 3 Companions",
    "Pet House Challenge - Kill 3 Demonized enemies",
    "Pet House Challenge - Buy 5 discounted Items",
    "Pet House Challenge - Kill 10 enemies with Teeth",
    "Pet House Challenge - Hit the Enemy Wave Bell 5 times",
    "Pet House Challenge - Achieve a 6x kill combo",
    "Inventors Hut Challenge - Achieve a 3x kill combo",
    "Inventors Hut Challenge - Add 3 Clunkers to your deck",
    "Inventors Hut Challenge - Kill 20 enemies with Items",
    "Inventors Hut Challenge - Block 10 hits with Clunkers",
    "Inventors Hut Challenge - Apply 60 Shell",
    "Inventors Hut Challenge - Buy 10 Crown",
    "Icebreaker Cabin Challenge - Gain 50 Bling from a Single battle",
    "Icebreaker Cabin Challenge - Kill 15 Enemies with Shroom",
    "Icebreaker Cabin Challenge - Feed the Muncher 5 Times",
    "Hot Spring Challenge - Equip 10 Charms",
    "Hot Spring Challenge - Deal 10 damage to your own team",
    "Hot Spring Challenge - Achieve a 4x kill combo",
    "Hot Spring Challenge - Kill 20 enemies with Smackback",
    "Hot Spring Challenge - Summon 50 allies",
    "Hot Spring Challenge - Add 10 Scrap to Clunkers"
}
idols = {
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
}
enemy_kills = {
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
    "Kill Grizzle",
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
    "Kill Naked Gnome",
    "Kill Octako",
    "Kill Ooba Bear",
    "Kill Paw Paw",
    "Kill Pecan",
    "Kill Pengoon",
    "Kill Pepper Witch",
    "Kill Plum",
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
    "Kill Willow",
    "Kill Winter Worm",
    "Kill Woolly Drek",
    # Clunkers
    "Kill Bombarder",
    "Kill Ice Forge",
    "Kill Ice Lantern",
    "Kill Mega Mimik",
    "Kill Mimik",
    "Kill Octobom",
    "Kill Plinker",
    "Kill Spike Wall",
}
boss_kills = {
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
    # Bosses
    "Kill Infernoko",
    "Kill Bamboozle",
    "Kill Truffle",
    "Kill Krunker",
    "Kill The Frost Guardian",
}

# Dynamic Sized Location Name Parts
snow_name = "Snowdweller"
shade_name = "Shademancer"
clunk_name = "Clunkmaster"
item_card_name = " Item Card "
companion_name = " Companion "
charm_name = " Charm "
boss_reward_name = "Boss Reward "

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
idols_map = {x: 20000 + i for i,x in enumerate(idols)}
enemy_kills_map = {x: 30000 + i for i,x in enumerate(enemy_kills)}
boss_kills_map = {x: 40000 + i for i,x in enumerate(boss_kills)}

# Dynamic Sized Location Maps (currently limited to 99 per type)
snow_cards = {snow_name + item_card_name + str(i): 51000 + i for i in range(1,99)}
shade_cards = {shade_name + item_card_name + str(i): 52000 + i for i in range(1,99)}
clunk_cards = {clunk_name + item_card_name + str(i): 53000 + i for i in range(1,99)}
item_card_map = snow_cards | shade_cards | clunk_cards

snow_companions = {snow_name + companion_name + str(i): 61000 + i for i in range(1,99)}
shade_companions = {shade_name + companion_name + str(i): 62000 + i for i in range(1,99)}
clunk_companions = {clunk_name + companion_name + str(i): 63000 + i for i in range(1,99)}
companions_map = snow_companions | shade_companions | clunk_companions

snow_charms = {snow_name + charm_name + str(i): 71000 + i for i in range(1,99)}
shade_charms = {shade_name + charm_name + str(i): 72000 + i for i in range(1,99)}
clunk_charms = {clunk_name + charm_name + str(i): 73000 + i for i in range(1,99)}
charm_map = snow_charms | shade_charms | clunk_charms

boss_reward_map = {boss_reward_name + str(i): 80000 + i for i in range(1,99)}

# Full name to ID dictionary
LOCATION_NAME_TO_ID = building_challenges_map | idols_map | enemy_kills_map | boss_kills_map | item_card_map | companions_map | charm_map | boss_reward_map