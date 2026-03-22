from __future__ import annotations
from BaseClasses import Item, ItemClassification
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .World import WildfrostWorld

class WildfrostItem(Item):
    game = "Wildfrost"


# Item Types
# Building = 1
# Charm = 2
# Unit = 3
# Item Card = 4
# Bell = 5
# Map Event = 6
# Tribe = 7
# Filler = 8

#   Name                    (ID,    Progression Level)
building_list = {
    "Pet House":            (10000, ItemClassification.progression),
    "Inventor's Hut":       (10001, ItemClassification.progression),
    "Icebreaker Cabin":     (10002, ItemClassification.progression),
    "Hot Spring":           (10003, ItemClassification.progression),
    "Frostoscope":          (10004, ItemClassification.useful),
}

#   Name                    (ID,    Progression Level)
charm_list = {
    "Acorn Charm":          (20000, ItemClassification.useful),
    "Balance Charm":        (20001, ItemClassification.useful),
    "Battle Charm":         (20002, ItemClassification.useful),
    "Beetle Charm":         (20003, ItemClassification.useful),
    "Bite Charm":           (20004, ItemClassification.useful),
    "Bling Charm":          (20005, ItemClassification.useful),
    "Block Charm":          (20006, ItemClassification.useful),
    "Bom Charm":            (20007, ItemClassification.useful),
    "Bombskull Charm":      (20008, ItemClassification.useful),
    "Boonfire Charm":       (20009, ItemClassification.useful),
    "Cake Charm":           (20010, ItemClassification.useful),
    "Chuckle Charm":        (20011, ItemClassification.useful),
    "Cloudberry Charm":     (20012, ItemClassification.useful),
    "Critical Charm":       (20013, ItemClassification.useful),
    "Durian Charm":         (20014, ItemClassification.useful),
    "Fidget Charm":         (20015, ItemClassification.useful),
    "Flameblade Charm":     (20016, ItemClassification.useful),
    "Frenzy Charm":         (20017, ItemClassification.useful),
    "Frog Charm":           (20018, ItemClassification.useful),
    "Frosthand Charm":      (20019, ItemClassification.useful),
    "Frozen Heart Charm":   (20020, ItemClassification.useful),
    "Gear Charm":           (20021, ItemClassification.useful),
    "Gnome Charm":          (20022, ItemClassification.useful),
    "Goat Charm":           (20023, ItemClassification.useful),
    "Greed Charm":          (20024, ItemClassification.useful),
    "Heart Charm":          (20025, ItemClassification.useful),
    "Hog Charm":            (20026, ItemClassification.useful),
    "Hook Charm":           (20027, ItemClassification.useful),
    "Jewelberry Charm":     (20028, ItemClassification.useful),
    "Jimbo Charm":          (20029, ItemClassification.useful),
    "Lamb Charm":           (20030, ItemClassification.useful),
    "Lumin Charm":          (20031, ItemClassification.useful),
    "Mime Charm":           (20032, ItemClassification.useful),
    "Moko Charm":           (20033, ItemClassification.useful),
    "Molten Egg Charm":     (20034, ItemClassification.useful),
    "Moose Charm":          (20035, ItemClassification.useful),
    "Muncher Charm":        (20036, ItemClassification.useful),
    "Noomlin Charm":        (20037, ItemClassification.useful),
    "Nourish Charm":        (20038, ItemClassification.useful),
    "Pengu Charm":          (20039, ItemClassification.useful),
    "Peppernut Charm":      (20040, ItemClassification.useful),
    "Pinch Charm":          (20041, ItemClassification.useful),
    "Pomegranate Charm":    (20042, ItemClassification.useful),
    "Punchfist Charm":      (20043, ItemClassification.useful),
    "Raspberry Charm":      (20044, ItemClassification.useful),
    "Recycle Charm":        (20045, ItemClassification.useful),
    "Scorchberry Charm":    (20046, ItemClassification.useful),
    "Scrap Charm":          (20047, ItemClassification.useful),
    "Shade Slug":           (20048, ItemClassification.useful),
    "Shield Charm":         (20049, ItemClassification.useful),
    "Shroom Charm":         (20050, ItemClassification.useful),
    "Snowball Charm":       (20051, ItemClassification.useful),
    "Spark Charm":          (20052, ItemClassification.useful),
    "Spice Charm":          (20053, ItemClassification.useful),
    "Squid Charm":          (20054, ItemClassification.useful),
    "Strawberry Charm":     (20055, ItemClassification.useful),
    "Sun Charm":            (20056, ItemClassification.useful),
    "Sunglass Charm":       (20057, ItemClassification.useful),
    "Tiger Charm":          (20058, ItemClassification.useful),
    "Truffle Charm":        (20059, ItemClassification.useful),
    "Zoomlin Charm":        (20060, ItemClassification.useful)
}

#   Name                    (ID,    Progression Level)
unit_list = {
    "Snoof":                (30000, ItemClassification.useful),
    "Booshu":               (30001, ItemClassification.useful),
    "Loki":                 (30002, ItemClassification.useful),
    "Sneezle":              (30003, ItemClassification.useful),
    "Spike":                (30004, ItemClassification.useful),
    "Binku":                (30005, ItemClassification.useful),
    "Lil' Gazi":            (30006, ItemClassification.useful),
    "Alloy":                (30007, ItemClassification.useful),
    "Berry Sis":            (30008, ItemClassification.useful),
    "Big Berry":            (30009, ItemClassification.useful),
    "Biji":                 (30010, ItemClassification.useful),
    "Blunky":               (30011, ItemClassification.useful),
    "Bombom":               (30012, ItemClassification.useful),
    "Bonnie":               (30013, ItemClassification.useful),
    "Chikichi":             (30014, ItemClassification.useful),
    "Chompom":              (30015, ItemClassification.useful),
    "Devicro":              (30016, ItemClassification.useful),
    "Dimona":               (30017, ItemClassification.useful),
    "Egg":                  (30018, ItemClassification.useful),
    "Firefist":             (30019, ItemClassification.useful),
    "Fizzle":               (30020, ItemClassification.useful),
    "Folby":                (30021, ItemClassification.useful),
    "Foxee":                (30022, ItemClassification.useful),
    "Fulbert":              (30023, ItemClassification.useful),
    "Fungun":               (30024, ItemClassification.useful),
    "Gojiber":              (30025, ItemClassification.useful),
    "Groff":                (30026, ItemClassification.useful),
    "Hazevlazer":           (30027, ItemClassification.useful),
    "Jumbo":                (30028, ItemClassification.useful),
    "Kernel":               (30029, ItemClassification.useful),
    "Knuckles":             (30030, ItemClassification.useful),
    "Kreggo":               (30031, ItemClassification.useful),
    "Lil' Berry":           (30032, ItemClassification.useful),
    "Lupa":                 (30033, ItemClassification.useful),
    "Mama Tinkerson":       (30034, ItemClassification.useful),
    "Mini Mika":            (30035, ItemClassification.useful),
    "Monch":                (30036, ItemClassification.useful),
    "Naked Gnome":          (30037, ItemClassification.useful),
    "Needle":               (30038, ItemClassification.useful),
    "Nom & Stompy":         (30039, ItemClassification.useful),
    "Nova":                 (30040, ItemClassification.useful),
    "Pimento":              (30041, ItemClassification.useful),
    "Pootie":               (30042, ItemClassification.useful),
    "Pyra":                 (30043, ItemClassification.useful),
    "Roibos":               (30044, ItemClassification.useful),
    "Scaven":               (30045, ItemClassification.useful),
    "Shelly":               (30046, ItemClassification.useful),
    "Shen":                 (30047, ItemClassification.useful),
    "Snobble":              (30048, ItemClassification.useful),
    "Snoffel":              (30049, ItemClassification.useful),
    "Splinter":             (30050, ItemClassification.useful),
    "Spoof":                (30051, ItemClassification.useful),
    "Taiga":                (30052, ItemClassification.useful),
    "The Baker":            (30053, ItemClassification.useful),
    "Tinkerson Jr.":        (30054, ItemClassification.useful),
    "Tiny Tyko":            (30055, ItemClassification.useful),
    "Toaster":              (30056, ItemClassification.useful),
    "Tusk":                 (30057, ItemClassification.useful),
    "Van Jun":              (30058, ItemClassification.useful),
    "Vesta":                (30059, ItemClassification.useful),
    "Wallop":               (30060, ItemClassification.useful),
    "Wort":                 (30061, ItemClassification.useful),
    "Yuki":                 (30062, ItemClassification.useful),
    "Zula":                 (30063, ItemClassification.useful)
}

#   Name                    (ID,    Progression Level)
item_card_list = {
    # Clunkers
    "Bitebox":              (40000, ItemClassification.useful),
    "Bling Bank":           (40001, ItemClassification.useful),
    "Blundertank":          (40002, ItemClassification.useful),
    "Bombarder":            (40003, ItemClassification.useful),
    "Fungo Blaster":        (40004, ItemClassification.useful),
    "Gachapomper":          (40005, ItemClassification.useful),
    "Haze Balloon":         (40006, ItemClassification.useful),
    "Heartforge":           (40007, ItemClassification.useful),
    "Heartmist Station":    (40008, ItemClassification.useful),
    "I.C.G.M":              (40009, ItemClassification.useful),
    "Junkhead":             (40010, ItemClassification.useful),
    "Kobonker":             (40011, ItemClassification.useful),
    "Krono":                (40012, ItemClassification.useful),
    "Mega Mimik":           (40013, ItemClassification.useful),
    "Mimik":                (40014, ItemClassification.useful),
    "Mobile Campfire":      (40015, ItemClassification.useful),
    "Moko Totem":           (40016, ItemClassification.useful),
    "Pepper Flag":          (40017, ItemClassification.useful),
    "Plinker":              (40018, ItemClassification.useful),
    "Portable Workbench":   (40019, ItemClassification.useful),
    "Shroominator":         (40020, ItemClassification.useful),
    "Shroomine":            (40021, ItemClassification.useful),
    "Spice Sparklers":      (40022, ItemClassification.useful),
    "Sunglass Chime":       (40023, ItemClassification.useful),
    "Tootordion":           (40024, ItemClassification.useful),
    "Totem of the Goat":    (40025, ItemClassification.useful),
    "Woodhead":             (40026, ItemClassification.useful),
    "Zoomlin Nest":         (40027, ItemClassification.useful),
    # Items
    "Azul Battle Axe":      (40028, ItemClassification.useful),
    "Azul Candle":          (40029, ItemClassification.useful),
    "Azul Skull":           (40030, ItemClassification.useful),
    "B.I.N.K":              (40031, ItemClassification.useful),
    "Beepop Mask":          (40032, ItemClassification.useful),
    "Berry Basket":         (40033, ItemClassification.useful),
    "Berry Bell":           (40034, ItemClassification.useful),
    "Berry Blade":          (40035, ItemClassification.useful),
    "Blank Mask":           (40036, ItemClassification.useful),
    "Blaze Bom":            (40037, ItemClassification.useful),
    "Blaze Tea":            (40038, ItemClassification.useful),
    "Blizzard Bottle":      (40039, ItemClassification.useful),
    "Bom Barrel":           (40040, ItemClassification.useful),
    "Bonescraper":          (40041, ItemClassification.useful),
    "Broken Vase":          (40042, ItemClassification.progression),
    "Clockwork Bom":        (40043, ItemClassification.useful),
    "Demonheart":           (40044, ItemClassification.useful),
    "Dragon Pepper":        (40045, ItemClassification.useful),
    "Fallow Mask":          (40046, ItemClassification.useful),
    "Flamewater":           (40047, ItemClassification.useful),
    "Flask of Ink":         (40048, ItemClassification.useful),
    "Foggy Brew":           (40049, ItemClassification.useful),
    "Forging Stove":        (40050, ItemClassification.useful),
    "Frenzy Wrench":        (40051, ItemClassification.useful),
    "Frost Bell":           (40052, ItemClassification.useful),
    "Frostbite Shard":      (40053, ItemClassification.useful),
    "Frostbloom":           (40054, ItemClassification.useful),
    "Gigi's Cookie Box":    (40055, ItemClassification.useful),
    "Gigi's Gizmo":         (40056, ItemClassification.useful),
    "Grabber":              (40057, ItemClassification.useful),
    "Haze Keg":             (40058, ItemClassification.useful),
    "Hongo's Hammer":       (40059, ItemClassification.useful),
    "Ice Dice":             (40060, ItemClassification.useful),
    "Junjun Mask":          (40061, ItemClassification.useful),
    "Leech Mask":           (40062, ItemClassification.useful),
    "Lumin Goop":           (40063, ItemClassification.progression),
    "Lumin Lantern":        (40064, ItemClassification.useful),
    "Magma Booster":        (40065, ItemClassification.useful),
    "Mini Muncher":         (40066, ItemClassification.useful),
    "Molten Dip":           (40067, ItemClassification.useful),
    "Noomlin Biscuit":      (40068, ItemClassification.useful),
    "Nutshell Cake":        (40069, ItemClassification.useful),
    "Peppereaper":          (40070, ItemClassification.useful),
    "Peppering":            (40071, ItemClassification.useful),
    "Pinkberry Juice":      (40072, ItemClassification.useful),
    "Pom Mask":             (40073, ItemClassification.useful),
    "Pombomb":              (40074, ItemClassification.useful),
    "Proto-Stomper":        (40075, ItemClassification.useful),
    "Scrap Pile":           (40076, ItemClassification.useful),
    "Shade Clay":           (40077, ItemClassification.useful),
    "Shade Wisp":           (40078, ItemClassification.useful),
    "Sheepopper Mask":      (40079, ItemClassification.useful),
    "Shell Shield":         (40080, ItemClassification.useful),
    "Shellbo":              (40081, ItemClassification.useful),
    "Skull Muffin":         (40082, ItemClassification.useful),
    "Skullmist Tea":        (40083, ItemClassification.useful),
    "Slapcrackers":         (40084, ItemClassification.useful),
    "Snow Stick":           (40085, ItemClassification.useful),
    "Snowcake":             (40086, ItemClassification.useful),
    "Snowzooka":            (40087, ItemClassification.useful),
    "Snuffer Mask":         (40088, ItemClassification.useful),
    "Soulbound Skulls":     (40089, ItemClassification.useful),
    "Spice Stones":         (40090, ItemClassification.useful),
    "Spore Pack":           (40091, ItemClassification.useful),
    "Storm Globe":          (40092, ItemClassification.useful),
    "Stormbear Spirit":     (40093, ItemClassification.useful),
    "Sun Rod":              (40094, ItemClassification.useful),
    "Sunburst Tootoo":      (40095, ItemClassification.useful),
    "Suncream":             (40096, ItemClassification.useful),
    "Sunlight Drum":        (40097, ItemClassification.useful),
    "Sunsong Box":          (40098, ItemClassification.useful),
    "Supersnower":          (40099, ItemClassification.useful),
    "The Lumin Vase":       (40100, ItemClassification.progression),
    "Tiger Skull":          (40101, ItemClassification.useful),
    "Tigris Mask":          (40102, ItemClassification.useful),
    "Yeti Skull":           (40103, ItemClassification.useful),
    "Zoomlin Wafers":       (40104, ItemClassification.useful)
}

#   Name                    (ID,    Progression Level)
bell_list = {
    # Sun Bells
    "Sun Bell of Hands":    (50000, ItemClassification.useful),
    "Sun Bell of Fellowship":(50001,ItemClassification.useful),
    "Sun Bell of the Bell": (50002, ItemClassification.useful),
    "Sun Bell of Health":   (50003, ItemClassification.useful),
    "Sun Bell of Time":     (50004, ItemClassification.useful),
    "Sun Bell of Recall":   (50005, ItemClassification.useful),
    "Sun Bell of Charge":   (50006, ItemClassification.useful),
    "Noomlin Sun Bell":     (50007, ItemClassification.useful),
    "Sun Bell of Strength": (50008, ItemClassification.useful),
    "Breakfast Sun Bell":   (50009, ItemClassification.useful),
    "Infinity Sun Bell":    (50010, ItemClassification.useful),
    # Storm Bells
    "Blingsnail Bell":      (50011, ItemClassification.progression),
    "Bell of Death":        (50012, ItemClassification.progression),
    "Titan Bell":           (50013, ItemClassification.progression),
    "Frosthand Bell":       (50014, ItemClassification.progression),
    "Gunk Bell":            (50015, ItemClassification.progression),
    "Icebourne Bell":       (50016, ItemClassification.progression),
    "Horde Bell":           (50017, ItemClassification.progression),
    "Gloom Bell":           (50018, ItemClassification.progression),
    "Frostbourne Bell":     (50019, ItemClassification.progression),
    "Gobbler Bell":         (50020, ItemClassification.progression),
    "Tyrant Bell":          (50021, ItemClassification.progression),
    "Dread Bell":           (50022, ItemClassification.progression),
    "Blood Bell":           (50023, ItemClassification.progression),
    # Voyage Bells
    "Battle Bell":          (50024, ItemClassification.useful),
    "Blingsack Bell":       (50025, ItemClassification.useful),
    "Bombskull Bell":       (50026, ItemClassification.useful),
    "Broken Bell":          (50027, ItemClassification.useful),
    "Fog Bell":             (50028, ItemClassification.useful),
    "Frenzy Bell":          (50029, ItemClassification.useful),
    "Frozen Heart Bell":    (50030, ItemClassification.useful),
    "Goat Bell":            (50031, ItemClassification.useful),
    "Gold Blade Bell":      (50032, ItemClassification.useful),
    "Heart Bell":           (50033, ItemClassification.useful),
    "Lumin Bell":           (50034, ItemClassification.useful),
    "Party Bell":           (50035, ItemClassification.useful)
}

#   Name                    (ID,    Progression Level)
map_event_list = {
    "Gnome Traveller":      (60000, ItemClassification.useful),
    "Shade Sculptor":       (60001, ItemClassification.useful),
    "Charm Merchant":       (60002, ItemClassification.useful),
    "Injured Companion":    (60003, ItemClassification.useful),
    "Muncher":              (60004, ItemClassification.useful),
    "Blingsnail Cave":      (60005, ItemClassification.useful)
}

#   Name                    (ID,    Progression Level)
tribe_list = {
    "Shademancers Tribe":   (70000, ItemClassification.progression | ItemClassification.useful),
    "Clunkmasters Tribe":   (70001, ItemClassification.progression | ItemClassification.useful)
}

#   Name                    (ID,    Progression Level)
filler_list = {
    "25 Bling":             (80000, ItemClassification.filler),
    "Berry Basket Boon":    (80001, ItemClassification.filler),
    "Spicy Boon":           (80002, ItemClassification.filler),
    "Snowy Boon":           (80003, ItemClassification.filler),
    "Speed Boon":           (80004, ItemClassification.filler),
    "Bling Bling Boon":     (80005, ItemClassification.filler),
    "Sun Smite Boon":       (80006, ItemClassification.filler),
    "Bombard Trap":         (80007, ItemClassification.trap),
    "Hoghead Trap":         (80008, ItemClassification.trap),
    "Gunk Bomb Trap":       (80009, ItemClassification.trap),
    "Ice Wall Trap":        (80010, ItemClassification.trap),
    "Ink Blot Trap":        (80012, ItemClassification.trap),
    "Goofy Gobbler Trap":   (80013, ItemClassification.trap),
    "Minion Death Trap":    (80014, ItemClassification.trap),
    "Throwing Shade Trap":  (80015, ItemClassification.trap),
    "Cursed Crown Trap":    (80016, ItemClassification.trap)
}

# Full name to ID *and* classificaiton dictionary
full_item_list = building_list | charm_list | unit_list | item_card_list | bell_list | map_event_list | tribe_list | filler_list

# Full name to ID dictionary
item_name_to_id = {x: full_item_list[x][0] for x in full_item_list}

def get_random_filler_item_name(world: WildfrostWorld) -> str:
    # TODO use random filler chance based on options
    # return world.random.choice(filler_list.keys)
    return filler_list.keys[0]

def create_item(world: WildfrostWorld, name: str) -> WildfrostItem:
    item = full_item_list[name]
    return WildfrostItem(name, item[1], item[0], world.player)

def create_all_items(world: WildfrostWorld) -> None:
    # Start with items that are always put into the item pool
    itempool: list[Item] = []
    itempool += [(world.create_item(x)) for x in building_list.keys()]
    itempool += [(world.create_item(x)) for x in charm_list.keys()]
    itempool += [(world.create_item(x)) for x in unit_list.keys()]
    itempool += [(world.create_item(x)) for x in item_card_list.keys()]
    itempool += [(world.create_item(x)) for x in bell_list.keys()]
    itempool += [(world.create_item(x)) for x in tribe_list.keys()]

    # TODO: Add optional items
    itempool += [(world.create_item(x)) for x in map_event_list.keys()]

    # Determine number of filler items needed
    num_of_items = len(itempool)
    num_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    num_filler_items = num_unfilled_locations - num_of_items
    
    print("Number of items: " + str(num_of_items))
    print("Number of empty locations: " + str(num_unfilled_locations))
    print("Number of filler items: " + str(num_filler_items))

    # Use helper function to add filler items
    itempool += [world.create_filler() for _ in range(num_filler_items)]

    # Commit item pool
    world.multiworld.itempool += itempool