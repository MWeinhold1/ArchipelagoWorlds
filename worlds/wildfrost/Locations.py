from BaseClasses import Location
from . import WildfrostWorld as World

class WildfrostLocation(Location):
    game = World.game

# Location IDs are 5 digit numbers in the format of XYZZZ
# X = Location category
# Y = Location sub-category
# ZZZ = Incremented location number.
#
# Example: ID 51025
# X = 5 = Item Card
# Y = 1 = Shademancer Card Pool
# ZZZ = 25 = The 25th location in the card pool

LOCATION_CATEGORIES = {
    1: "Town",
    2: "Idol",
    3: "Enemy",
    4: "Boss",
    5: "Item",
    6: "Companion",
    7: "Charm",
    8: "Bell"
}

LOCATION_SUBCATEGORIES = {
    0: "General",
    1: "Snowdweller",
    2: "Shademancer",
    3: "Clunkmaster"
}

#   Name
reward_pools = {
    # "General Companion", # Sounds like we're not doing generic locations, only tribe-specific locations
    "Snowdweller Companion",
    "Shademancer Companion",
    "Clunkmaster Companion",
    # "General Item",
    "Snowdweller Item",
    "Shademancer Item",
    "Clunkmaster Item",
    # "General Charm",
    "Snowdweller Charm",
    "Shademancer Charm",
    "Clunkmaster Charm",
    "Boss Fight Reward" # Mainly for use with bells
}

buildings = {
    # "Build Frostoscope", # Should this be a location, if it's unlocked by beating EotS?
    "Build Hot Spring",
    "Build Icebreaker Cabin",
    "Build Inventor Hut",
    "Build Pet House",
    "Build Tribe Hall"
}

building_challenges = {
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
}

clunker_kills = {
    "Kill Bombarder",
    "Kill Ice Forge",
    "Kill Ice Lantern",
    "Kill Mega Mimik",
    "Kill Mimik",
    "Kill Octobom",
    "Kill Plinker",
    "Kill Spike Wall",
}

miniboss_kills = {
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
}

boss_kills = {
    "Kill Infernoko",
    "Kill Bamboozle",
    "Kill Truffle",
    "Kill Krunker",
    "Kill The Frost Guardian",
}