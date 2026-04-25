from BaseClasses import ItemClassification

# Item Types
# Building: 1
# Tribe: 2
# Pet: 3
# Map Event: 4
# Item Card: 5
# Unit: 6
# Charm: 7
# Bell: 8
# Filler/Trap: 9
# Progressive Items: 9 (counting backwards)
#
# Subtypes
# _0: Generic
# _1: Snowdweller
# _2: Shademancer
# _3: Clunkmaster

#   Name                    (Progression Level)
building_list = {
    "Pet House":            (ItemClassification.progression),
    "Inventor's Hut":       (ItemClassification.progression),
    "Icebreaker Cabin":     (ItemClassification.progression),
    "Hot Spring":           (ItemClassification.progression),
    "Frostoscope":          (ItemClassification.useful),
}

#   Name                    (Progression Level)
tribe_list = {
    "Snowdwellers Tribe":   (ItemClassification.progression | ItemClassification.useful),
    "Shademancers Tribe":   (ItemClassification.progression | ItemClassification.useful),
    "Clunkmasters Tribe":   (ItemClassification.progression | ItemClassification.useful)
}

pet_list = {
    "Snoof":                (ItemClassification.progression | ItemClassification.useful),
    "Booshu":               (ItemClassification.progression | ItemClassification.useful),
    "Loki":                 (ItemClassification.progression | ItemClassification.useful),
    "Sneezle":              (ItemClassification.progression | ItemClassification.useful),
    "Spike":                (ItemClassification.progression | ItemClassification.useful),
    "Binku":                (ItemClassification.progression | ItemClassification.useful),
    "Lil' Gazi":            (ItemClassification.progression | ItemClassification.useful),
}

#   Name                    (Progression Level)
map_event_list = {
    "Shade Sculptor":       (ItemClassification.useful),
    "Charm Merchant":       (ItemClassification.useful),
    "Gnome Traveller":      (ItemClassification.useful),
    "Injured Companion":    (ItemClassification.useful),
    "Muncher":              (ItemClassification.progression | ItemClassification.useful),
    "Blingsnail Cave":      (ItemClassification.useful)
}

#   Name                    (Progression Level)
general_item_card_list = {
    # Items
    "Berry Basket":         (ItemClassification.progression | ItemClassification.useful),
    "Berry Blade":          (ItemClassification.progression | ItemClassification.useful),
    "Blaze Tea":            (ItemClassification.progression | ItemClassification.useful),
    "Demonheart":           (ItemClassification.progression | ItemClassification.useful),
    "Frost Bell":           (ItemClassification.progression | ItemClassification.useful),
    "Frostbloom":           (ItemClassification.progression | ItemClassification.useful),
    "Grabber":              (ItemClassification.progression | ItemClassification.useful),
    "Ice Dice":             (ItemClassification.progression | ItemClassification.useful),
    "Molten Dip":           (ItemClassification.progression | ItemClassification.useful),
    "Noomlin Biscuit":      (ItemClassification.progression | ItemClassification.useful),
    "Pinkberry Juice":      (ItemClassification.progression | ItemClassification.useful),
    "Pombomb":              (ItemClassification.progression | ItemClassification.useful),
    "Slapcrackers":         (ItemClassification.progression | ItemClassification.useful),
    "Snowcake":             (ItemClassification.progression | ItemClassification.useful),
    "Storm Globe":          (ItemClassification.progression | ItemClassification.useful),
    "Sunlight Drum":        (ItemClassification.progression | ItemClassification.useful),
    "Zoomlin Wafers":       (ItemClassification.progression | ItemClassification.useful),
    # Clunkers
    "Bitebox":              (ItemClassification.progression | ItemClassification.useful),
    "Bling Bank":           (ItemClassification.progression | ItemClassification.useful),
    "Heartmist Station":    (ItemClassification.progression | ItemClassification.useful),
    "Krono":                (ItemClassification.progression | ItemClassification.useful),
    "Mega Mimik":           (ItemClassification.progression | ItemClassification.useful),
    "Mimik":                (ItemClassification.progression | ItemClassification.useful),
    "Totem of the Goat":    (ItemClassification.progression | ItemClassification.useful),
    "Zoomlin Nest":         (ItemClassification.progression | ItemClassification.useful),
    # Vase
    "Broken Vase":          (ItemClassification.progression),
    "Lumin Goop":           (ItemClassification.progression),
    "The Lumin Vase":       (ItemClassification.progression),
}

snowdweller_item_card_list = {
    # Items
    "Dragon Pepper":        (ItemClassification.progression | ItemClassification.useful),
    "FlameWater":           (ItemClassification.progression | ItemClassification.useful),
    "Hongo's Hammer":       (ItemClassification.progression | ItemClassification.useful),
    "Nutshell Cake":        (ItemClassification.progression | ItemClassification.useful),
    "Peppereaper":          (ItemClassification.progression | ItemClassification.useful),
    "Peppering":            (ItemClassification.progression | ItemClassification.useful),
    "Scrap Pile":           (ItemClassification.progression | ItemClassification.useful),
    "Shell Shield":         (ItemClassification.progression | ItemClassification.useful),
    "Shellbo":              (ItemClassification.progression | ItemClassification.useful),
    "Snow Stick":           (ItemClassification.progression | ItemClassification.useful),
    "Spice Stones":         (ItemClassification.progression | ItemClassification.useful),
    "Spore Pack":           (ItemClassification.progression | ItemClassification.useful),
    "Stormbear Spirit":     (ItemClassification.progression | ItemClassification.useful),
    "Sun Rod":              (ItemClassification.progression | ItemClassification.useful),
    # Clunkers
    "Fungo Blaster":        (ItemClassification.progression | ItemClassification.useful),
    "Heartforge":           (ItemClassification.progression | ItemClassification.useful),
    "Kobonker":             (ItemClassification.progression | ItemClassification.useful),
    "Mobile Campfire":      (ItemClassification.progression | ItemClassification.useful),
    "Moko Totem":           (ItemClassification.progression | ItemClassification.useful),
    "Pepper Flag":          (ItemClassification.progression | ItemClassification.useful),
    "Shroominator":         (ItemClassification.progression | ItemClassification.useful),
    "Shroomine":            (ItemClassification.progression | ItemClassification.useful),
    "Spice Sparklers":      (ItemClassification.progression | ItemClassification.useful),
    "Woodhead":             (ItemClassification.progression | ItemClassification.useful)
}

shademancer_item_card_list = {
    "Azul Battle Axe":      (ItemClassification.progression | ItemClassification.useful),
    "Azul Candle":          (ItemClassification.progression | ItemClassification.useful),
    "Azul Skull":           (ItemClassification.progression | ItemClassification.useful),
    "Beepop Mask":          (ItemClassification.progression | ItemClassification.useful),
    "Berry Bell":           (ItemClassification.progression | ItemClassification.useful),
    "Blank Mask":           (ItemClassification.progression | ItemClassification.useful),
    "Blizzard Bottle":      (ItemClassification.progression | ItemClassification.useful),
    "Bonescraper":          (ItemClassification.progression | ItemClassification.useful),
    "Fallow Mask":          (ItemClassification.progression | ItemClassification.useful),
    "Junjun Mask":          (ItemClassification.progression | ItemClassification.useful),
    "Leech Mask":           (ItemClassification.progression | ItemClassification.useful),
    "Pom Mask":             (ItemClassification.progression | ItemClassification.useful),
    "Shade Clay":           (ItemClassification.progression | ItemClassification.useful),
    "Shade Wisp":           (ItemClassification.progression | ItemClassification.useful),
    "Sheepopper Mask":      (ItemClassification.progression | ItemClassification.useful),
    "Skull Muffin":         (ItemClassification.progression | ItemClassification.useful),
    "Skullmist Tea":        (ItemClassification.progression | ItemClassification.useful),
    "Snuffer Mask":         (ItemClassification.progression | ItemClassification.useful),
    "Soulbound Skulls":     (ItemClassification.progression | ItemClassification.useful),
    "Sunburst Tootoo":      (ItemClassification.progression | ItemClassification.useful),
    "Tiger Skull":          (ItemClassification.progression | ItemClassification.useful),
    "Tigris Mask":          (ItemClassification.progression | ItemClassification.useful),
    "Yeti Skull":           (ItemClassification.progression | ItemClassification.useful),
}

clunkmaster_item_card_list = {
    # Items
    "B.I.N.K":              (ItemClassification.progression | ItemClassification.useful),
    "Blaze Bom":            (ItemClassification.progression | ItemClassification.useful),
    "Bom Barrel":           (ItemClassification.progression | ItemClassification.useful),
    "Clockwork Bom":        (ItemClassification.progression | ItemClassification.useful),
    "Flask of Ink":         (ItemClassification.progression | ItemClassification.useful),
    "Foggy Brew":           (ItemClassification.progression | ItemClassification.useful),
    "Forging Stove":        (ItemClassification.progression | ItemClassification.useful),
    "Frenzy Wrench":        (ItemClassification.progression | ItemClassification.useful),
    "Frostbite Shard":      (ItemClassification.progression | ItemClassification.useful),
    "Gigi's Cookie Box":    (ItemClassification.progression | ItemClassification.useful),
    "Gigi's Gizmo":         (ItemClassification.progression | ItemClassification.useful),
    "Haze Keg":             (ItemClassification.progression | ItemClassification.useful),
    "Lumin Lantern":        (ItemClassification.progression | ItemClassification.useful),
    "Magma Booster":        (ItemClassification.progression | ItemClassification.useful),
    "Mini Muncher":         (ItemClassification.progression | ItemClassification.useful),
    "Proto-Stomper":        (ItemClassification.progression | ItemClassification.useful),
    "Snowzooka":            (ItemClassification.progression | ItemClassification.useful),
    "Suncream":             (ItemClassification.progression | ItemClassification.useful),
    "Sunsong Box":          (ItemClassification.progression | ItemClassification.useful),
    "Supersnower":          (ItemClassification.progression | ItemClassification.useful),
    # Clunkers
    "Blundertank":          (ItemClassification.progression | ItemClassification.useful),
    "Bombarder":            (ItemClassification.progression | ItemClassification.useful),
    "Gachapomper":          (ItemClassification.progression | ItemClassification.useful),
    "Haze Balloon":         (ItemClassification.progression | ItemClassification.useful),
    "I.C.G.M":              (ItemClassification.progression | ItemClassification.useful),
    "Junkhead":             (ItemClassification.progression | ItemClassification.useful),
    "Plinker":              (ItemClassification.progression | ItemClassification.useful),
    "Portable Workbench":   (ItemClassification.progression | ItemClassification.useful),
    "Sunglass Chime":       (ItemClassification.progression | ItemClassification.useful),
    "Tootordion":           (ItemClassification.progression | ItemClassification.useful),
}

#   Name                    (Progression Level)
general_companion_list = {
    "Big Berry":            (ItemClassification.progression | ItemClassification.useful),
    "Blunky":               (ItemClassification.progression | ItemClassification.useful),
    "Bombom":               (ItemClassification.progression | ItemClassification.useful),
    "Bonnie":               (ItemClassification.progression | ItemClassification.useful),
    "Dimona":               (ItemClassification.progression | ItemClassification.useful),
    "Foxee":                (ItemClassification.progression | ItemClassification.useful),
    "Gojiber":              (ItemClassification.progression | ItemClassification.useful),
    "Jumbo":                (ItemClassification.progression | ItemClassification.useful),
    "Lupa":                 (ItemClassification.progression | ItemClassification.useful),
    "Naked Gnome":          (ItemClassification.progression | ItemClassification.useful),
    "Nova":                 (ItemClassification.progression | ItemClassification.useful),
    "Roibos":               (ItemClassification.progression | ItemClassification.useful),
    "Snobble":              (ItemClassification.progression | ItemClassification.useful),
    "Snoffel":              (ItemClassification.progression | ItemClassification.useful),
}

snowdweller_companion_list = {
    "Chompom":              (ItemClassification.progression | ItemClassification.useful),
    "Firefist":             (ItemClassification.progression | ItemClassification.useful),
    "Fulbert":              (ItemClassification.progression | ItemClassification.useful),
    "Fungun":               (ItemClassification.progression | ItemClassification.useful),
    "Kernel":               (ItemClassification.progression | ItemClassification.useful),
    "Lil' Berry":           (ItemClassification.progression | ItemClassification.useful),
    "Pimento":              (ItemClassification.progression | ItemClassification.useful),
    "Pootie":               (ItemClassification.progression | ItemClassification.useful),
    "Pyra":                 (ItemClassification.progression | ItemClassification.useful),
    "Shelly":               (ItemClassification.progression | ItemClassification.useful),
    "Tiny Tyko":            (ItemClassification.progression | ItemClassification.useful),
    "Wallop":               (ItemClassification.progression | ItemClassification.useful),
    "Wort":                 (ItemClassification.progression | ItemClassification.useful),
    "Yuki":                 (ItemClassification.progression | ItemClassification.useful),
}

shademancer_companion_list = {
    "Berry Sis":            (ItemClassification.progression | ItemClassification.useful),
    "Chikichi":             (ItemClassification.progression | ItemClassification.useful),
    "Devicro":              (ItemClassification.progression | ItemClassification.useful),
    "Egg":                  (ItemClassification.progression | ItemClassification.useful),
    "Groff":                (ItemClassification.progression | ItemClassification.useful),
    "Monch":                (ItemClassification.progression | ItemClassification.useful),
    "Shen":                 (ItemClassification.progression | ItemClassification.useful),
    "Splinter":             (ItemClassification.progression | ItemClassification.useful),
    "Spoof":                (ItemClassification.progression | ItemClassification.useful),
    "Taiga":                (ItemClassification.progression | ItemClassification.useful),
    "The Baker":            (ItemClassification.progression | ItemClassification.useful),
    "Tusk":                 (ItemClassification.progression | ItemClassification.useful),
    "Van Jun":              (ItemClassification.progression | ItemClassification.useful),
    "Vesta":                (ItemClassification.progression | ItemClassification.useful),
    "Zula":                 (ItemClassification.progression | ItemClassification.useful)
}

clunkmaster_companion_list = {
    "Alloy":                (ItemClassification.progression | ItemClassification.useful),
    "Biji":                 (ItemClassification.progression | ItemClassification.useful),
    "Fizzle":               (ItemClassification.progression | ItemClassification.useful),
    "Folby":                (ItemClassification.progression | ItemClassification.useful),
    "Hazeblazer":           (ItemClassification.progression | ItemClassification.useful),
    "Knuckles":             (ItemClassification.progression | ItemClassification.useful),
    "Kreggo":               (ItemClassification.progression | ItemClassification.useful),
    "Mama Tinkerson":       (ItemClassification.progression | ItemClassification.useful),
    "Mini Mika":            (ItemClassification.progression | ItemClassification.useful),
    "Needle":               (ItemClassification.progression | ItemClassification.useful),
    "Nom & Stompy":         (ItemClassification.progression | ItemClassification.useful),
    "Scaven":               (ItemClassification.progression | ItemClassification.useful),
    "Tinkerson Jr.":        (ItemClassification.progression | ItemClassification.useful),
    "Toaster":              (ItemClassification.progression | ItemClassification.useful),
}

#   Name                    (Progression Level)
general_charm_list = {
    "Balance Charm":        (ItemClassification.progression | ItemClassification.useful),
    "Battle Charm":         (ItemClassification.progression | ItemClassification.useful),
    "Beetle Charm":         (ItemClassification.progression | ItemClassification.useful),
    "Bling Charm":          (ItemClassification.progression | ItemClassification.useful),
    "Block Charm":          (ItemClassification.progression | ItemClassification.useful),
    "Bombskull Charm":      (ItemClassification.progression | ItemClassification.useful),
    "Cake Charm":           (ItemClassification.progression | ItemClassification.useful),
    "Chuckle Charm":        (ItemClassification.progression | ItemClassification.useful),
    "Cloudberry Charm":     (ItemClassification.progression | ItemClassification.useful),
    "Critical Charm":       (ItemClassification.progression | ItemClassification.useful),
    "Durian Charm":         (ItemClassification.progression | ItemClassification.useful),
    "Frenzy Charm":         (ItemClassification.progression | ItemClassification.useful),
    "Frog Charm":           (ItemClassification.progression | ItemClassification.useful),
    "Frosthand Charm":      (ItemClassification.progression | ItemClassification.useful),
    "Frozen Heart Charm":   (ItemClassification.progression | ItemClassification.useful),
    "Gnome Charm":          (ItemClassification.progression | ItemClassification.useful),
    "Goat Charm":           (ItemClassification.progression | ItemClassification.useful),
    "Greed Charm":          (ItemClassification.progression | ItemClassification.useful),
    "Heart Charm":          (ItemClassification.progression | ItemClassification.useful),
    "Hog Charm":            (ItemClassification.progression | ItemClassification.useful),
    "Hook Charm":           (ItemClassification.progression | ItemClassification.useful),
    "Jimbo Charm":          (ItemClassification.progression | ItemClassification.useful),
    "Lumin Ring":           (ItemClassification.progression | ItemClassification.useful),
    "Moko Charm":           (ItemClassification.progression | ItemClassification.useful),
    "Molten Egg Charm":     (ItemClassification.progression | ItemClassification.useful),
    "Moose Charm":          (ItemClassification.progression | ItemClassification.useful),
    "Muncher Charm":        (ItemClassification.progression | ItemClassification.useful),
    "Noomlin Charm":        (ItemClassification.progression | ItemClassification.useful),
    "Nourish Charm":        (ItemClassification.progression | ItemClassification.useful),
    "Pengu Charm":          (ItemClassification.progression | ItemClassification.useful),
    "Pinch Charm":          (ItemClassification.progression | ItemClassification.useful),
    "Pomegranate Charm":    (ItemClassification.progression | ItemClassification.useful),
    "Punchfist Charm":      (ItemClassification.progression | ItemClassification.useful),
    "Raspberry Charm":      (ItemClassification.progression | ItemClassification.useful),
    "Scorchberry Charm":    (ItemClassification.progression | ItemClassification.useful),
    "Scrap Charm":          (ItemClassification.progression | ItemClassification.useful), #Scrap charm is exclusive to both Snowdwellers and Clunkmasters, keeping it here for now
    "Shade Slug":           (ItemClassification.progression | ItemClassification.useful),
    "Snowball Charm":       (ItemClassification.progression | ItemClassification.useful),
    "Spark Charm":          (ItemClassification.progression | ItemClassification.useful),
    "Strawberry Charm":     (ItemClassification.progression | ItemClassification.useful),
    "Sun Charm":            (ItemClassification.progression | ItemClassification.useful),
    "Sunglass Charm":       (ItemClassification.progression | ItemClassification.useful),
    "Zoomlin Charm":        (ItemClassification.progression | ItemClassification.useful)
}

snowdweller_charm_list = {
    "Acorn Charm":          (ItemClassification.progression | ItemClassification.useful),
    "Jewelberry Charm":     (ItemClassification.progression | ItemClassification.useful),
    "Peppernut Charm":      (ItemClassification.progression | ItemClassification.useful),
    "Shield Charm":         (ItemClassification.progression | ItemClassification.useful),
    "Shroom Charm":         (ItemClassification.progression | ItemClassification.useful),
    "Spice Charm":          (ItemClassification.progression | ItemClassification.useful),
    "Truffle Charm":        (ItemClassification.progression | ItemClassification.useful),
}

shademancer_charm_list = {
    "Bite Charm":           (ItemClassification.progression | ItemClassification.useful),
    "Boonfire Charm":       (ItemClassification.progression | ItemClassification.useful),
    "Flameblade Charm":     (ItemClassification.progression | ItemClassification.useful),
    "Lamb Charm":           (ItemClassification.progression | ItemClassification.useful),
    "Mime Charm":           (ItemClassification.progression | ItemClassification.useful),
    "Tiger Charm":          (ItemClassification.progression | ItemClassification.useful),
}

clunkmaster_charm_list = {
    "Bom Charm":            (ItemClassification.progression | ItemClassification.useful),
    "Fidget Charm":         (ItemClassification.progression | ItemClassification.useful),
    "Gear Charm":           (ItemClassification.progression | ItemClassification.useful),
    "Recycle Charm":        (ItemClassification.progression | ItemClassification.useful),
    "Squid Charm":          (ItemClassification.progression | ItemClassification.useful),
}

#   Name                    (Progression Level)
sun_bell_list = {
    # Sun Bells
    "Sun Bell of Hands":    (ItemClassification.useful),
    "Sun Bell of Fellowship":(ItemClassification.useful),
    "Sun Bell of the Bell": (ItemClassification.useful),
    "Sun Bell of Health":   (ItemClassification.useful),
    "Sun Bell of Time":     (ItemClassification.useful),
    "Sun Bell of Recall":   (ItemClassification.useful),
    "Sun Bell of Charge":   (ItemClassification.useful),
    "Noomlin Sun Bell":     (ItemClassification.useful),
    "Sun Bell of Strength": (ItemClassification.useful),
    "Breakfast Sun Bell":   (ItemClassification.useful),
    "Infinity Sun Bell":    (ItemClassification.useful)
}

storm_bell_list = {
    # Storm Bells
    "Blingsnail Bell":      (ItemClassification.progression),
    "Bell of Death":        (ItemClassification.progression),
    "Titan Bell":           (ItemClassification.progression),
    "Frosthand Bell":       (ItemClassification.progression),
    "Gunk Bell":            (ItemClassification.progression),
    "Icebourne Bell":       (ItemClassification.progression),
    "Horde Bell":           (ItemClassification.progression),
    "Gloom Bell":           (ItemClassification.progression),
    "Frostbourne Bell":     (ItemClassification.progression),
    "Gobbler Bell":         (ItemClassification.progression),
    "Tyrant Bell":          (ItemClassification.progression),
    "Dread Bell":           (ItemClassification.progression),
    "Blood Bell":           (ItemClassification.progression)
}

voyage_bell_list = {
    # Voyage Bells
    "Battle Bell":          (ItemClassification.useful),
    "Blingsack Bell":       (ItemClassification.useful),
    "Bombskull Bell":       (ItemClassification.useful),
    "Broken Bell":          (ItemClassification.useful),
    "Fog Bell":             (ItemClassification.useful),
    "Frenzy Bell":          (ItemClassification.useful),
    "Frozen Heart Bell":    (ItemClassification.useful),
    "Goat Bell":            (ItemClassification.useful),
    "Gold Blade Bell":      (ItemClassification.useful),
    "Heart Bell":           (ItemClassification.useful),
    "Lumin Bell":           (ItemClassification.useful),
    "Party Bell":           (ItemClassification.useful)
}

bell_list = sun_bell_list | storm_bell_list | voyage_bell_list

#   Name                    (Progression Level)
filler_list = {
    "25 Bling":             (ItemClassification.filler),
    "Berry Basket Boon":    (ItemClassification.filler),
    "Spicy Boon":           (ItemClassification.filler),
    "Snowy Boon":           (ItemClassification.filler),
    "Speed Boon":           (ItemClassification.filler),
    "Bling Bling Boon":     (ItemClassification.filler),
    "Sun Smite Boon":       (ItemClassification.filler),
    "Bombard Trap":         (ItemClassification.trap),
    "Hoghead Trap":         (ItemClassification.trap),
    "Gunk Bomb Trap":       (ItemClassification.trap),
    "Ice Wall Trap":        (ItemClassification.trap),
    "Ink Blot Trap":        (ItemClassification.trap),
    "Goofy Gobbler Trap":   (ItemClassification.trap),
    "Minion Death Trap":    (ItemClassification.trap),
    "Throwing Shade Trap":  (ItemClassification.trap),
    "Cursed Crown Trap":    (ItemClassification.trap)
}

progressive_list = {
    "Progressive Act": (ItemClassification.progression),
    "Progressive Fight": (ItemClassification.progression)
}

buildings_map = {x: 10000 + i for i,x in enumerate(building_list)}
tribe_map = {x: 20000 + i for i,x in enumerate(tribe_list)}
pet_map = {x: 30000 + i for i,x in enumerate(pet_list)}
map_event_map = {x: 40000 + i for i,x in enumerate(map_event_list)}

general_item_cards = {x: 50000 + i for i,x in enumerate(general_item_card_list)}
snow_item_cards = {x: 51000 + i for i,x in enumerate(snowdweller_item_card_list)}
shade_item_cards = {x: 52000 + i for i,x in enumerate(shademancer_item_card_list)}
clunk_item_cards = {x: 53000 + i for i,x in enumerate(clunkmaster_item_card_list)}

item_card_map = general_item_cards | snow_item_cards | shade_item_cards | clunk_item_cards

general_companions = {x: 60000 + i for i,x in enumerate(general_companion_list)}
snow_companions = {x: 61000 + i for i,x in enumerate(snowdweller_companion_list)}
shade_companions = {x: 62000 + i for i,x in enumerate(shademancer_companion_list)}
clunk_companions = {x: 63000 + i for i,x in enumerate(clunkmaster_companion_list)}

companions_map = general_companions | snow_companions | shade_companions | clunk_companions

general_charms = {x: 70000 + i for i,x in enumerate(general_charm_list)}
snow_charms = {x: 71000 + i for i,x in enumerate(snowdweller_charm_list)}
shade_charms = {x: 72000 + i for i,x in enumerate(shademancer_charm_list)}
clunk_charms = {x: 73000 + i for i,x in enumerate(clunkmaster_charm_list)}

charm_map = general_charms | snow_charms | shade_charms | clunk_charms

sun_bell_map = {x: 80000 + i for i,x in enumerate(sun_bell_list)}
storm_bell_map = {x: 80000 + len(sun_bell_list) + i for i,x in enumerate(storm_bell_list)}
voyage_bell_map = {x: 80000 + len(sun_bell_list) + len(storm_bell_list) + i for i,x in enumerate(voyage_bell_list)}
bell_map = sun_bell_map | storm_bell_map | voyage_bell_map

filler_map = {x: 90000 + i for i,x in enumerate(filler_list)}
progressive_map = {x: 99999 - i for i,x in enumerate(progressive_list)}

# Full name to ID
ITEM_NAME_TO_ID = buildings_map | tribe_map | pet_map | map_event_map | item_card_map | companions_map | charm_map | bell_map | filler_map | progressive_map



ITEM_NAME_TO_CLASSIFICATION = building_list | tribe_list | pet_list | bell_list | filler_list | map_event_list |\
        general_item_card_list | snowdweller_item_card_list | shademancer_item_card_list | clunkmaster_item_card_list|\
        general_companion_list | snowdweller_companion_list | shademancer_companion_list | clunkmaster_companion_list|\
        general_charm_list | snowdweller_charm_list | shademancer_charm_list | clunkmaster_charm_list|\
        progressive_list
