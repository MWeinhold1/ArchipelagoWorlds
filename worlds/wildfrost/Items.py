from enum import Enum

from BaseClasses import Item, ItemClassification

class WildfrostItem(Item): #TODO
    game: str = "Wildfrost"


class ItemType(Enum):
    Unknown = 0, # Fallback value, should not be used
    Building = 1,
    Charm = 2,
    Unit = 3,
    Item = 4,
    Bell = 5,
    MapEvent = 6,
    Tribe = 7,
    TrapBoon = 8

class Importance(Enum):
    Useless = 0,
    Generic = 1,
    Useful = 2,
    UnlockChecks = 3,
    HotSBlocker = 4

#   Name                    (Item Type,         Progression Level,              LocalID )
building_list = {
    "Pet House":            (ItemType.Building, ItemClassification.progression, 0  ),
    "Inventor's Hut":       (ItemType.Building, ItemClassification.progression, 1  ),
    "Icebreaker Cabin":     (ItemType.Building, ItemClassification.progression, 2  ),
    "Hot Spring":           (ItemType.Building, ItemClassification.progression, 3  ),
    "Frostoscope":          (ItemType.Building, ItemClassification.useful,      4  ),
}

#   Name                    (Item Type,         Progression Level,              LocalID )
charm_list = {
    "Acorn Charm":          (ItemType.Charm,    ItemClassification.useful,      0  ),
    "Balance Charm":        (ItemType.Charm,    ItemClassification.useful,      1  ),
    "Battle Charm":         (ItemType.Charm,    ItemClassification.useful,      2  ),
    "Beetle Charm":         (ItemType.Charm,    ItemClassification.useful,      3  ),
    "Bite Charm":           (ItemType.Charm,    ItemClassification.useful,      4  ),
    "Bling Charm":          (ItemType.Charm,    ItemClassification.useful,      5  ),
    "Block Charm":          (ItemType.Charm,    ItemClassification.useful,      6  ),
    "Bom Charm":            (ItemType.Charm,    ItemClassification.useful,      7  ),
    "Bombskull Charm":      (ItemType.Charm,    ItemClassification.useful,      8  ),
    "Boonfire Charm":       (ItemType.Charm,    ItemClassification.useful,      9  ),
    "Cake Charm":           (ItemType.Charm,    ItemClassification.useful,      10 ),
    "Chuckle Charm":        (ItemType.Charm,    ItemClassification.useful,      11 ),
    "Cloudberry Charm":     (ItemType.Charm,    ItemClassification.useful,      12 ),
    "Critical Charm":       (ItemType.Charm,    ItemClassification.useful,      13 ),
    "Durian Charm":         (ItemType.Charm,    ItemClassification.useful,      14 ),
    "Fidget Charm":         (ItemType.Charm,    ItemClassification.useful,      15 ),
    "Flameblade Charm":     (ItemType.Charm,    ItemClassification.useful,      16 ),
    "Frenzy Charm":         (ItemType.Charm,    ItemClassification.useful,      17 ),
    "Frog Charm":           (ItemType.Charm,    ItemClassification.useful,      18 ),
    "Frosthand Charm":      (ItemType.Charm,    ItemClassification.useful,      19 ),
    "Frozen Heart Charm":   (ItemType.Charm,    ItemClassification.useful,      20 ),
    "Gear Charm":           (ItemType.Charm,    ItemClassification.useful,      21 ),
    "Gnome Charm":          (ItemType.Charm,    ItemClassification.useful,      22 ),
    "Goat Charm":           (ItemType.Charm,    ItemClassification.useful,      23 ),
    "Greed Charm":          (ItemType.Charm,    ItemClassification.useful,      24 ),
    "Heart Charm":          (ItemType.Charm,    ItemClassification.useful,      25 ),
    "Hog Charm":            (ItemType.Charm,    ItemClassification.useful,      26 ),
    "Hook Charm":           (ItemType.Charm,    ItemClassification.useful,      27 ),
    "Jewelberry Charm":     (ItemType.Charm,    ItemClassification.useful,      28 ),
    "Jimbo Charm":          (ItemType.Charm,    ItemClassification.useful,      29 ),
    "Lamb Charm":           (ItemType.Charm,    ItemClassification.useful,      30 ),
    "Lumin Charm":          (ItemType.Charm,    ItemClassification.useful,      31 ),
    "Mime Charm":           (ItemType.Charm,    ItemClassification.useful,      32 ),
    "Moko Charm":           (ItemType.Charm,    ItemClassification.useful,      33 ),
    "Molten Egg Charm":     (ItemType.Charm,    ItemClassification.useful,      34 ),
    "Moose Charm":          (ItemType.Charm,    ItemClassification.useful,      35 ),
    "Muncher Charm":        (ItemType.Charm,    ItemClassification.useful,      36 ),
    "Noomlin Charm":        (ItemType.Charm,    ItemClassification.useful,      37 ),
    "Nourish Charm":        (ItemType.Charm,    ItemClassification.useful,      38 ),
    "Pengu Charm":          (ItemType.Charm,    ItemClassification.useful,      39 ),
    "Peppernut Charm":      (ItemType.Charm,    ItemClassification.useful,      40 ),
    "Pinch Charm":          (ItemType.Charm,    ItemClassification.useful,      41 ),
    "Pomegranate Charm":    (ItemType.Charm,    ItemClassification.useful,      42 ),
    "Punchfist Charm":      (ItemType.Charm,    ItemClassification.useful,      43 ),
    "Raspberry Charm":      (ItemType.Charm,    ItemClassification.useful,      44 ),
    "Recycle Charm":        (ItemType.Charm,    ItemClassification.useful,      45 ),
    "Scorchberry Charm":    (ItemType.Charm,    ItemClassification.useful,      46 ),
    "Scrap Charm":          (ItemType.Charm,    ItemClassification.useful,      47 ),
    "Shade Slug":           (ItemType.Charm,    ItemClassification.useful,      48 ),
    "Shield Charm":         (ItemType.Charm,    ItemClassification.useful,      49 ),
    "Shroom Charm":         (ItemType.Charm,    ItemClassification.useful,      50 ),
    "Snowball Charm":       (ItemType.Charm,    ItemClassification.useful,      51 ),
    "Spark Charm":          (ItemType.Charm,    ItemClassification.useful,      52 ),
    "Spice Charm":          (ItemType.Charm,    ItemClassification.useful,      53 ),
    "Squid Charm":          (ItemType.Charm,    ItemClassification.useful,      54 ),
    "Strawberry Charm":     (ItemType.Charm,    ItemClassification.useful,      55 ),
    "Sun Charm":            (ItemType.Charm,    ItemClassification.useful,      56 ),
    "Sunglass Charm":       (ItemType.Charm,    ItemClassification.useful,      57 ),
    "Tiger Charm":          (ItemType.Charm,    ItemClassification.useful,      58 ),
    "Truffle Charm":        (ItemType.Charm,    ItemClassification.useful,      59 ),
    "Zoomlin Charm":        (ItemType.Charm,    ItemClassification.useful,      60 ),
}

#   Name                    (Item Type,         Progression Level,              LocalID )
unit_list = {
    "Snoof":                (ItemType.Unit,     ItemClassification.useful,      0  ),
    "Booshu":               (ItemType.Unit,     ItemClassification.useful,      1  ),
    "Loki":                 (ItemType.Unit,     ItemClassification.useful,      2  ),
    "Sneezle":              (ItemType.Unit,     ItemClassification.useful,      3  ),
    "Spike":                (ItemType.Unit,     ItemClassification.useful,      4  ),
    "Binku":                (ItemType.Unit,     ItemClassification.useful,      5  ),
    "Lil' Gazi":            (ItemType.Unit,     ItemClassification.useful,      6  ),
    "Alloy":                (ItemType.Unit,     ItemClassification.useful,      7  ),
    "Berry Sis":            (ItemType.Unit,     ItemClassification.useful,      8  ),
    "Big Berry":            (ItemType.Unit,     ItemClassification.useful,      9  ),
    "Biji":                 (ItemType.Unit,     ItemClassification.useful,      10 ),
    "Blunky":               (ItemType.Unit,     ItemClassification.useful,      11 ),
    "Bombom":               (ItemType.Unit,     ItemClassification.useful,      12 ),
    "Bonnie":               (ItemType.Unit,     ItemClassification.useful,      13 ),
    "Chikichi":             (ItemType.Unit,     ItemClassification.useful,      14 ),
    "Chompom":              (ItemType.Unit,     ItemClassification.useful,      15 ),
    "Devicro":              (ItemType.Unit,     ItemClassification.useful,      16 ),
    "Dimona":               (ItemType.Unit,     ItemClassification.useful,      17 ),
    "Egg":                  (ItemType.Unit,     ItemClassification.useful,      18 ),
    "Firefist":             (ItemType.Unit,     ItemClassification.useful,      19 ),
    "Fizzle":               (ItemType.Unit,     ItemClassification.useful,      20 ),
    "Folby":                (ItemType.Unit,     ItemClassification.useful,      21 ),
    "Foxee":                (ItemType.Unit,     ItemClassification.useful,      22 ),
    "Fulbert":              (ItemType.Unit,     ItemClassification.useful,      23 ),
    "Fungun":               (ItemType.Unit,     ItemClassification.useful,      24 ),
    "Gojiber":              (ItemType.Unit,     ItemClassification.useful,      25 ),
    "Groff":                (ItemType.Unit,     ItemClassification.useful,      26 ),
    "Hazevlazer":           (ItemType.Unit,     ItemClassification.useful,      27 ),
    "Jumbo":                (ItemType.Unit,     ItemClassification.useful,      28 ),
    "Kernel":               (ItemType.Unit,     ItemClassification.useful,      29 ),
    "Knuckles":             (ItemType.Unit,     ItemClassification.useful,      30 ),
    "Kreggo":               (ItemType.Unit,     ItemClassification.useful,      31 ),
    "Lil' Berry":           (ItemType.Unit,     ItemClassification.useful,      32 ),
    "Lupa":                 (ItemType.Unit,     ItemClassification.useful,      33 ),
    "Mama Tinkerson":       (ItemType.Unit,     ItemClassification.useful,      34 ),
    "Mini Mika":            (ItemType.Unit,     ItemClassification.useful,      35 ),
    "Monch":                (ItemType.Unit,     ItemClassification.useful,      36 ),
    "Naked Gnome":          (ItemType.Unit,     ItemClassification.useful,      37 ),
    "Needle":               (ItemType.Unit,     ItemClassification.useful,      38 ),
    "Nom & Stompy":         (ItemType.Unit,     ItemClassification.useful,      39 ),
    "Nova":                 (ItemType.Unit,     ItemClassification.useful,      40 ),
    "Pimento":              (ItemType.Unit,     ItemClassification.useful,      41 ),
    "Pootie":               (ItemType.Unit,     ItemClassification.useful,      42 ),
    "Pyra":                 (ItemType.Unit,     ItemClassification.useful,      43 ),
    "Roibos":               (ItemType.Unit,     ItemClassification.useful,      44 ),
    "Scaven":               (ItemType.Unit,     ItemClassification.useful,      45 ),
    "Shelly":               (ItemType.Unit,     ItemClassification.useful,      46 ),
    "Shen":                 (ItemType.Unit,     ItemClassification.useful,      47 ),
    "Snobble":              (ItemType.Unit,     ItemClassification.useful,      48 ),
    "Snoffel":              (ItemType.Unit,     ItemClassification.useful,      49 ),
    "Splinter":             (ItemType.Unit,     ItemClassification.useful,      50 ),
    "Spoof":                (ItemType.Unit,     ItemClassification.useful,      51 ),
    "Taiga":                (ItemType.Unit,     ItemClassification.useful,      52 ),
    "The Baker":            (ItemType.Unit,     ItemClassification.useful,      53 ),
    "Tinkerson Jr.":        (ItemType.Unit,     ItemClassification.useful,      54 ),
    "Tiny Tyko":            (ItemType.Unit,     ItemClassification.useful,      55 ),
    "Toaster":              (ItemType.Unit,     ItemClassification.useful,      56 ),
    "Tusk":                 (ItemType.Unit,     ItemClassification.useful,      57 ),
    "Van Jun":              (ItemType.Unit,     ItemClassification.useful,      58 ),
    "Vesta":                (ItemType.Unit,     ItemClassification.useful,      59 ),
    "Wallop":               (ItemType.Unit,     ItemClassification.useful,      60 ),
    "Wort":                 (ItemType.Unit,     ItemClassification.useful,      61 ),
    "Yuki":                 (ItemType.Unit,     ItemClassification.useful,      62 ),
    "Zula":                 (ItemType.Unit,     ItemClassification.useful,      63 ),
}

#   Name                    (Item Type,         Progression Level,              LocalID )
clunker_list = {
    "Bitebox":              (ItemType.Item,     ItemClassification.useful,      0  ),
    "Bling Bank":           (ItemType.Item,     ItemClassification.useful,      1  ),
    "Blundertank":          (ItemType.Item,     ItemClassification.useful,      2  ),
    "Bombarder":            (ItemType.Item,     ItemClassification.useful,      3  ),
    "Fungo Blaster":        (ItemType.Item,     ItemClassification.useful,      4  ),
    "Gachapomper":          (ItemType.Item,     ItemClassification.useful,      5  ),
    "Haze Balloon":         (ItemType.Item,     ItemClassification.useful,      6  ),
    "Heartforge":           (ItemType.Item,     ItemClassification.useful,      7  ),
    "Heartmist Station":    (ItemType.Item,     ItemClassification.useful,      8  ),
    "I.C.G.M":              (ItemType.Item,     ItemClassification.useful,      9  ),
    "Junkhead":             (ItemType.Item,     ItemClassification.useful,      10 ),
    "Kobonker":             (ItemType.Item,     ItemClassification.useful,      11 ),
    "Krono":                (ItemType.Item,     ItemClassification.useful,      12 ),
    "Mega Mimik":           (ItemType.Item,     ItemClassification.useful,      13 ),
    "Mimik":                (ItemType.Item,     ItemClassification.useful,      14 ),
    "Mobile Campfire":      (ItemType.Item,     ItemClassification.useful,      15 ),
    "Moko Totem":           (ItemType.Item,     ItemClassification.useful,      16 ),
    "Pepper Flag":          (ItemType.Item,     ItemClassification.useful,      17 ),
    "Plinker":              (ItemType.Item,     ItemClassification.useful,      18 ),
    "Portable Workbench":   (ItemType.Item,     ItemClassification.useful,      19 ),
    "Shroominator":         (ItemType.Item,     ItemClassification.useful,      20 ),
    "Shroomine":            (ItemType.Item,     ItemClassification.useful,      21 ),
    "Spice Sparklers":      (ItemType.Item,     ItemClassification.useful,      22 ),
    "Sunglass Chime":       (ItemType.Item,     ItemClassification.useful,      23 ),
    "Tootordion":           (ItemType.Item,     ItemClassification.useful,      24 ),
    "Totem of the Goat":    (ItemType.Item,     ItemClassification.useful,      25 ),
    "Woodhead":             (ItemType.Item,     ItemClassification.useful,      26 ),
    "Zoomlin Nest":         (ItemType.Item,     ItemClassification.useful,      27 ),
}

#   Name                    (Item Type,         Progression Level,              LocalID )
cards_list = {
    "Azul Battle Axe":      (ItemType.Item,     ItemClassification.useful,      28 ),
    "Azul Candle":          (ItemType.Item,     ItemClassification.useful,      29 ),
    "Azul Skull":           (ItemType.Item,     ItemClassification.useful,      30 ),
    "B.I.N.K":              (ItemType.Item,     ItemClassification.useful,      31 ),
    "Beepop Mask":          (ItemType.Item,     ItemClassification.useful,      32 ),
    "Berry Basket":         (ItemType.Item,     ItemClassification.useful,      33 ),
    "Berry Bell":           (ItemType.Item,     ItemClassification.useful,      34 ),
    "Berry Blade":          (ItemType.Item,     ItemClassification.useful,      35 ),
    "Blank Mask":           (ItemType.Item,     ItemClassification.useful,      36 ),
    "Blaze Bom":            (ItemType.Item,     ItemClassification.useful,      37 ),
    "Blaze Tea":            (ItemType.Item,     ItemClassification.useful,      38 ),
    "Blizzard Bottle":      (ItemType.Item,     ItemClassification.useful,      39 ),
    "Bom Barrel":           (ItemType.Item,     ItemClassification.useful,      40 ),
    "Bonescraper":          (ItemType.Item,     ItemClassification.useful,      41 ),
    "Broken Vase":          (ItemType.Item,     ItemClassification.progression, 42 ),
    "Clockwork Bom":        (ItemType.Item,     ItemClassification.useful,      43 ),
    "Demonheart":           (ItemType.Item,     ItemClassification.useful,      44 ),
    "Dragon Pepper":        (ItemType.Item,     ItemClassification.useful,      45 ),
    "Fallow Mask":          (ItemType.Item,     ItemClassification.useful,      46 ),
    "Flamewater":           (ItemType.Item,     ItemClassification.useful,      47 ),
    "Flask of Ink":         (ItemType.Item,     ItemClassification.useful,      48 ),
    "Foggy Brew":           (ItemType.Item,     ItemClassification.useful,      49 ),
    "Forging Stove":        (ItemType.Item,     ItemClassification.useful,      50 ),
    "Frenzy Wrench":        (ItemType.Item,     ItemClassification.useful,      51 ),
    "Frost Bell":           (ItemType.Item,     ItemClassification.useful,      52 ),
    "Frostbite Shard":      (ItemType.Item,     ItemClassification.useful,      53 ),
    "Frostbloom":           (ItemType.Item,     ItemClassification.useful,      54 ),
    "Gigi's Cookie Box":    (ItemType.Item,     ItemClassification.useful,      55 ),
    "Gigi's Gizmo":         (ItemType.Item,     ItemClassification.useful,      56 ),
    "Grabber":              (ItemType.Item,     ItemClassification.useful,      57 ),
    "Haze Keg":             (ItemType.Item,     ItemClassification.useful,      58 ),
    "Hongo's Hammer":       (ItemType.Item,     ItemClassification.useful,      59 ),
    "Ice Dice":             (ItemType.Item,     ItemClassification.useful,      60 ),
    "Junjun Mask":          (ItemType.Item,     ItemClassification.useful,      61 ),
    "Leech Mask":           (ItemType.Item,     ItemClassification.useful,      62 ),
    "Lumin Goop":           (ItemType.Item,     ItemClassification.progression, 63 ),
    "Lumin Lantern":        (ItemType.Item,     ItemClassification.useful,      64 ),
    "Magma Booster":        (ItemType.Item,     ItemClassification.useful,      65 ),
    "Mini Muncher":         (ItemType.Item,     ItemClassification.useful,      66 ),
    "Molten Dip":           (ItemType.Item,     ItemClassification.useful,      67 ),
    "Noomlin Biscuit":      (ItemType.Item,     ItemClassification.useful,      68 ),
    "Nutshell Cake":        (ItemType.Item,     ItemClassification.useful,      69 ), # nice
    "Peppereaper":          (ItemType.Item,     ItemClassification.useful,      70 ),
    "Peppering":            (ItemType.Item,     ItemClassification.useful,      71 ),
    "Pinkberry Juice":      (ItemType.Item,     ItemClassification.useful,      72 ),
    "Pom Mask":             (ItemType.Item,     ItemClassification.useful,      73 ),
    "Pombomb":              (ItemType.Item,     ItemClassification.useful,      74 ),
    "Proto-Stomper":        (ItemType.Item,     ItemClassification.useful,      75 ),
    "Scrap Pile":           (ItemType.Item,     ItemClassification.useful,      76 ),
    "Shade Clay":           (ItemType.Item,     ItemClassification.useful,      77 ),
    "Shade Wisp":           (ItemType.Item,     ItemClassification.useful,      78 ),
    "Sheepopper Mask":      (ItemType.Item,     ItemClassification.useful,      79 ),
    "Shell Shield":         (ItemType.Item,     ItemClassification.useful,      80 ),
    "Shellbo":              (ItemType.Item,     ItemClassification.useful,      81 ),
    "Skull Muffin":         (ItemType.Item,     ItemClassification.useful,      82 ),
    "Skullmist Tea":        (ItemType.Item,     ItemClassification.useful,      83 ),
    "Slapcrackers":         (ItemType.Item,     ItemClassification.useful,      84 ),
    "Snow Stick":           (ItemType.Item,     ItemClassification.useful,      85 ),
    "Snowcake":             (ItemType.Item,     ItemClassification.useful,      86 ),
    "Snowzooka":            (ItemType.Item,     ItemClassification.useful,      87 ),
    "Snuffer Mask":         (ItemType.Item,     ItemClassification.useful,      88 ),
    "Soulbound Skulls":     (ItemType.Item,     ItemClassification.useful,      89 ),
    "Spice Stones":         (ItemType.Item,     ItemClassification.useful,      90 ),
    "Spore Pack":           (ItemType.Item,     ItemClassification.useful,      91 ),
    "Storm Globe":          (ItemType.Item,     ItemClassification.useful,      92 ),
    "Stormbear Spirit":     (ItemType.Item,     ItemClassification.useful,      93 ),
    "Sun Rod":              (ItemType.Item,     ItemClassification.useful,      94 ),
    "Sunburst Tootoo":      (ItemType.Item,     ItemClassification.useful,      95 ),
    "Suncream":             (ItemType.Item,     ItemClassification.useful,      96 ),
    "Sunlight Drum":        (ItemType.Item,     ItemClassification.useful,      97 ),
    "Sunsong Box":          (ItemType.Item,     ItemClassification.useful,      98 ),
    "Supersnower":          (ItemType.Item,     ItemClassification.useful,      99 ),
    "The Lumin Vase":       (ItemType.Item,     ItemClassification.progression, 100),
    "Tiger Skull":          (ItemType.Item,     ItemClassification.useful,      101),
    "Tigris Mask":          (ItemType.Item,     ItemClassification.useful,      102),
    "Yeti Skull":           (ItemType.Item,     ItemClassification.useful,      103),
    "Zoomlin Wafers":       (ItemType.Item,     ItemClassification.useful,      104),
}

#   Name                    (Item Type,         Progression Level,              LocalID )
sun_bell_list = {
    "Sun Bell of Hands":    (ItemType.Bell,     ItemClassification.useful,      0  ),
    "Sun Bell of Fellowship":(ItemType.Bell,    ItemClassification.useful,      1  ),
    "Sun Bell of the Bell": (ItemType.Bell,     ItemClassification.useful,      2  ),
    "Sun Bell of Health":   (ItemType.Bell,     ItemClassification.useful,      3  ),
    "Sun Bell of Time":     (ItemType.Bell,     ItemClassification.useful,      4  ),
    "Sun Bell of Recall":   (ItemType.Bell,     ItemClassification.useful,      5  ),
    "Sun Bell of Charge":   (ItemType.Bell,     ItemClassification.useful,      6  ),
    "Noomlin Sun Bell":     (ItemType.Bell,     ItemClassification.useful,      7  ),
    "Sun Bell of Strength": (ItemType.Bell,     ItemClassification.useful,      8  ),
    "Breakfast Sun Bell":   (ItemType.Bell,     ItemClassification.useful,      9  ),
    "Infinity Sun Bell":    (ItemType.Bell,     ItemClassification.useful,      10 ),
}

#   Name                    (Item Type,         Progression Level,              LocalID )
storm_bell_list = {
    "Blingsnail Bell":      (ItemType.Bell,     ItemClassification.progression, 11 ),
    "Bell of Death":        (ItemType.Bell,     ItemClassification.progression, 12 ),
    "Titan Bell":           (ItemType.Bell,     ItemClassification.progression, 13 ),
    "Frosthand Bell":       (ItemType.Bell,     ItemClassification.progression, 14 ),
    "Gunk Bell":            (ItemType.Bell,     ItemClassification.progression, 15 ),
    "Icebourne Bell":       (ItemType.Bell,     ItemClassification.progression, 16 ),
    "Horde Bell":           (ItemType.Bell,     ItemClassification.progression, 17 ),
    "Gloom Bell":           (ItemType.Bell,     ItemClassification.progression, 18 ),
    "Frostbourne Bell":     (ItemType.Bell,     ItemClassification.progression, 19 ),
    "Gobbler Bell":         (ItemType.Bell,     ItemClassification.progression, 20 ),
    "Tyrant Bell":          (ItemType.Bell,     ItemClassification.progression, 21 ),
    "Dread Bell":           (ItemType.Bell,     ItemClassification.progression, 22 ),
    "Blood Bell":           (ItemType.Bell,     ItemClassification.progression, 23 ),
}

#   Name                    (Item Type,         Progression Level,              LocalID )
voyage_bell_list = {
    "Battle Bell":          (ItemType.Bell,     ItemClassification.useful,      24 ),
    "Blingsack Bell":       (ItemType.Bell,     ItemClassification.useful,      25 ),
    "Bombskull Bell":       (ItemType.Bell,     ItemClassification.useful,      26 ),
    "Broken Bell":          (ItemType.Bell,     ItemClassification.useful,      27 ),
    "Fog Bell":             (ItemType.Bell,     ItemClassification.useful,      28 ),
    "Frenzy Bell":          (ItemType.Bell,     ItemClassification.useful,      29 ),
    "Frozen Heart Bell":    (ItemType.Bell,     ItemClassification.useful,      30 ),
    "Goat Bell":            (ItemType.Bell,     ItemClassification.useful,      31 ),
    "Gold Blade Bell":      (ItemType.Bell,     ItemClassification.useful,      32 ),
    "Heart Bell":           (ItemType.Bell,     ItemClassification.useful,      33 ),
    "Lumin Bell":           (ItemType.Bell,     ItemClassification.useful,      34 ),
    "Party Bell":           (ItemType.Bell,     ItemClassification.useful,      35 ),
}

#   Name                    (Item Type,         Progression Level,              LocalID )
map_event_list = {
    "Gnome Traveller":      (ItemType.MapEvent, ItemClassification.useful,      0  ),
    "Shade Sculptor":       (ItemType.MapEvent, ItemClassification.useful,      1  ),
    "Charm Merchant":       (ItemType.MapEvent, ItemClassification.useful,      2  ),
    "Injured Companion":    (ItemType.MapEvent, ItemClassification.useful,      3  ),
    "Muncher":              (ItemType.MapEvent, ItemClassification.useful,      4  ),
    "Blingsnail Cave":      (ItemType.MapEvent, ItemClassification.useful,      5  ),
}

#   Name                    (Item Type,         Progression Level,              LocalID )
tribe_list = {
    "Shademancers Tribe":   (ItemType.Tribe,    ItemClassification.progression, 0  ),
    "Clunkmasters Tribe":   (ItemType.Tribe,    ItemClassification.progression, 0  ),
}

#   Name                    (Item Type,         Progression Level,              LocalID )
trap_boon_list = {
    "Berry Basket Boon":    (ItemType.TrapBoon, ItemClassification.filler,      0  ),
    "Spicy Boon":           (ItemType.TrapBoon, ItemClassification.filler,      1  ),
    "Snowy Boon":           (ItemType.TrapBoon, ItemClassification.filler,      2  ),
    "Speed Boon":           (ItemType.TrapBoon, ItemClassification.filler,      3  ),
    "Bling Bling Boon":     (ItemType.TrapBoon, ItemClassification.filler,      4  ),
    "Sun Smite Boon":       (ItemType.TrapBoon, ItemClassification.filler,      5  ),

    "Bombard Trap":         (ItemType.TrapBoon, ItemClassification.filler,      6  ),
    "Hoghead Trap":         (ItemType.TrapBoon, ItemClassification.filler,      7  ),
    "Gunk Bomb Trap":       (ItemType.TrapBoon, ItemClassification.filler,      8  ),
    "Ice Wall Trap":        (ItemType.TrapBoon, ItemClassification.filler,      9  ),
    "Ink Blot Trap":        (ItemType.TrapBoon, ItemClassification.filler,      10 ),
    "Goofy Gobbler Trap":   (ItemType.TrapBoon, ItemClassification.filler,      12 ),

    "Support Death Event":  (ItemType.TrapBoon, ItemClassification.filler,      13 ),
    "Throwing Shade Event": (ItemType.TrapBoon, ItemClassification.filler,      14 ),
    "Cursed Crown Event":   (ItemType.TrapBoon, ItemClassification.filler,      14 ),
}

full_item_list = {
    **building_list,
    **charm_list,
    **unit_list,
    **clunker_list,
    **cards_list,
    **sun_bell_list,
    **storm_bell_list,
    **voyage_bell_list,
    **map_event_list,
    **tribe_list,
    **trap_boon_list
}