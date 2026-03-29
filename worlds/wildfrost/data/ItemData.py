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
    "Snoof":                (ItemClassification.useful),
    "Booshu":               (ItemClassification.useful),
    "Loki":                 (ItemClassification.useful),
    "Sneezle":              (ItemClassification.useful),
    "Spike":                (ItemClassification.useful),
    "Binku":                (ItemClassification.useful),
    "Lil' Gazi":            (ItemClassification.useful),
}

#   Name                    (Progression Level)
map_event_list = {
    "Shade Sculptor":       (ItemClassification.useful),
    "Charm Merchant":       (ItemClassification.useful),
    "Gnome Traveller":      (ItemClassification.useful),
    "Injured Companion":    (ItemClassification.useful),
    "Muncher":              (ItemClassification.useful),
    "Blingsnail Cave":      (ItemClassification.useful)
}

#   Name                    (Progression Level)
general_item_card_list = {
    # Items
    "Berry Basket":         (ItemClassification.useful),
    "Berry Blade":          (ItemClassification.useful),
    "Blaze Tea":            (ItemClassification.useful),
    "Demonheart":           (ItemClassification.useful),
    "Frost Bell":           (ItemClassification.useful),
    "Frostbloom":           (ItemClassification.useful),
    "Grabber":              (ItemClassification.useful),
    "Ice Dice":             (ItemClassification.useful),
    "Molten Dip":           (ItemClassification.useful),
    "Noomlin Biscuit":      (ItemClassification.useful),
    "Pinkberry Juice":      (ItemClassification.useful),
    "Pombomb":              (ItemClassification.useful),
    "Slapcrackers":         (ItemClassification.useful),
    "Snowcake":             (ItemClassification.useful),
    "Storm Globe":          (ItemClassification.useful),
    "Sunlight Drum":        (ItemClassification.useful),
    "Zoomlin Wafers":       (ItemClassification.useful),
    # Clunkers
    "Bitebox":              (ItemClassification.useful),
    "Bling Bank":           (ItemClassification.useful),
    "Heartmist Station":    (ItemClassification.useful),
    "Krono":                (ItemClassification.useful),
    "Mega Mimik":           (ItemClassification.useful),
    "Mimik":                (ItemClassification.useful),
    "Totem of the Goat":    (ItemClassification.useful),
    "Zoomlin Nest":         (ItemClassification.useful),
    # Vase
    "Broken Vase":          (ItemClassification.progression),
    "Lumin Goop":           (ItemClassification.progression),
    "The Lumin Vase":       (ItemClassification.progression),
}

snowdweller_item_card_list = {
    # Items
    "Dragon Pepper":        (ItemClassification.useful),
    "FlameWater":           (ItemClassification.useful),
    "Hongo's Hammer":       (ItemClassification.useful),
    "Nutshell Cake":        (ItemClassification.useful),
    "Peppereaper":          (ItemClassification.useful),
    "Peppering":            (ItemClassification.useful),
    "Scrap Pile":           (ItemClassification.useful),
    "Shell Shield":         (ItemClassification.useful),
    "Shellbo":              (ItemClassification.useful),
    "Snow Stick":           (ItemClassification.useful),
    "Spice Stones":         (ItemClassification.useful),
    "Spore Pack":           (ItemClassification.useful),
    "Stormbear Spirit":     (ItemClassification.useful),
    "Sun Rod":              (ItemClassification.useful),
    # Clunkers
    "Fungo Blaster":        (ItemClassification.useful),
    "Heartforge":           (ItemClassification.useful),
    "Kobonker":             (ItemClassification.useful),
    "Mobile Campfire":      (ItemClassification.useful),
    "Moko Totem":           (ItemClassification.useful),
    "Pepper Flag":          (ItemClassification.useful),
    "Shroominator":         (ItemClassification.useful),
    "Shroomine":            (ItemClassification.useful),
    "Spice Sparklers":      (ItemClassification.useful),
    "Woodhead":             (ItemClassification.useful)
}

shademancer_item_card_list = {
    "Azul Battle Axe":      (ItemClassification.useful),
    "Azul Candle":          (ItemClassification.useful),
    "Azul Skull":           (ItemClassification.useful),
    "Beepop Mask":          (ItemClassification.useful),
    "Berry Bell":           (ItemClassification.useful),
    "Blank Mask":           (ItemClassification.useful),
    "Blizzard Bottle":      (ItemClassification.useful),
    "Bonescraper":          (ItemClassification.useful),
    "Fallow Mask":          (ItemClassification.useful),
    "Junjun Mask":          (ItemClassification.useful),
    "Leech Mask":           (ItemClassification.useful),
    "Pom Mask":             (ItemClassification.useful),
    "Shade Clay":           (ItemClassification.useful),
    "Shade Wisp":           (ItemClassification.useful),
    "Sheepopper Mask":      (ItemClassification.useful),
    "Skull Muffin":         (ItemClassification.useful),
    "Skullmist Tea":        (ItemClassification.useful),
    "Snuffer Mask":         (ItemClassification.useful),
    "Soulbound Skulls":     (ItemClassification.useful),
    "Sunburst Tootoo":      (ItemClassification.useful),
    "Tiger Skull":          (ItemClassification.useful),
    "Tigris Mask":          (ItemClassification.useful),
    "Yeti Skull":           (ItemClassification.useful),
}

clunkmaster_item_card_list = {
    # Items
    "B.I.N.K":              (ItemClassification.useful),
    "Blaze Bom":            (ItemClassification.useful),
    "Bom Barrel":           (ItemClassification.useful),
    "Clockwork Bom":        (ItemClassification.useful),
    "Flask of Ink":         (ItemClassification.useful),
    "Foggy Brew":           (ItemClassification.useful),
    "Forging Stove":        (ItemClassification.useful),
    "Frenzy Wrench":        (ItemClassification.useful),
    "Frostbite Shard":      (ItemClassification.useful),
    "Gigi's Cookie Box":    (ItemClassification.useful),
    "Gigi's Gizmo":         (ItemClassification.useful),
    "Haze Keg":             (ItemClassification.useful),
    "Lumin Lantern":        (ItemClassification.useful),
    "Magma Booster":        (ItemClassification.useful),
    "Mini Muncher":         (ItemClassification.useful),
    "Proto-Stomper":        (ItemClassification.useful),
    "Snowzooka":            (ItemClassification.useful),
    "Suncream":             (ItemClassification.useful),
    "Sunsong Box":          (ItemClassification.useful),
    "Supersnower":          (ItemClassification.useful),
    # Clunkers
    "Blundertank":          (ItemClassification.useful),
    "Bombarder":            (ItemClassification.useful),
    "Gachapomper":          (ItemClassification.useful),
    "Haze Balloon":         (ItemClassification.useful),
    "I.C.G.M":              (ItemClassification.useful),
    "Junkhead":             (ItemClassification.useful),
    "Plinker":              (ItemClassification.useful),
    "Portable Workbench":   (ItemClassification.useful),
    "Sunglass Chime":       (ItemClassification.useful),
    "Tootordion":           (ItemClassification.useful),
}

#   Name                    (Progression Level)
general_companion_list = {
    "Big Berry":            (ItemClassification.useful),
    "Blunky":               (ItemClassification.useful),
    "Bombom":               (ItemClassification.useful),
    "Bonnie":               (ItemClassification.useful),
    "Dimona":               (ItemClassification.useful),
    "Foxee":                (ItemClassification.useful),
    "Gojiber":              (ItemClassification.useful),
    "Jumbo":                (ItemClassification.useful),
    "Lupa":                 (ItemClassification.useful),
    "Naked Gnome":          (ItemClassification.useful),
    "Nova":                 (ItemClassification.useful),
    "Roibos":               (ItemClassification.useful),
    "Snobble":              (ItemClassification.useful),
    "Snoffel":              (ItemClassification.useful),
}

snowdweller_companion_list = {
    "Chompom":              (ItemClassification.useful),
    "Firefist":             (ItemClassification.useful),
    "Fulbert":              (ItemClassification.useful),
    "Fungun":               (ItemClassification.useful),
    "Kernel":               (ItemClassification.useful),
    "Lil' Berry":           (ItemClassification.useful),
    "Pimento":              (ItemClassification.useful),
    "Pootie":               (ItemClassification.useful),
    "Pyra":                 (ItemClassification.useful),
    "Shelly":               (ItemClassification.useful),
    "Tiny Tyko":            (ItemClassification.useful),
    "Wallop":               (ItemClassification.useful),
    "Wort":                 (ItemClassification.useful),
    "Yuki":                 (ItemClassification.useful),
}

shademancer_companion_list = {
    "Berry Sis":            (ItemClassification.useful),
    "Chikichi":             (ItemClassification.useful),
    "Devicro":              (ItemClassification.useful),
    "Egg":                  (ItemClassification.useful),
    "Groff":                (ItemClassification.useful),
    "Monch":                (ItemClassification.useful),
    "Shen":                 (ItemClassification.useful),
    "Splinter":             (ItemClassification.useful),
    "Spoof":                (ItemClassification.useful),
    "Taiga":                (ItemClassification.useful),
    "The Baker":            (ItemClassification.useful),
    "Tusk":                 (ItemClassification.useful),
    "Van Jun":              (ItemClassification.useful),
    "Vesta":                (ItemClassification.useful),
    "Zula":                 (ItemClassification.useful)
}

clunkmaster_companion_list = {
    "Alloy":                (ItemClassification.useful),
    "Biji":                 (ItemClassification.useful),
    "Fizzle":               (ItemClassification.useful),
    "Folby":                (ItemClassification.useful),
    "Hazeblazer":           (ItemClassification.useful),
    "Knuckles":             (ItemClassification.useful),
    "Kreggo":               (ItemClassification.useful),
    "Mama Tinkerson":       (ItemClassification.useful),
    "Mini Mika":            (ItemClassification.useful),
    "Needle":               (ItemClassification.useful),
    "Nom & Stompy":         (ItemClassification.useful),
    "Scaven":               (ItemClassification.useful),
    "Tinkerson Jr.":        (ItemClassification.useful),
    "Toaster":              (ItemClassification.useful),
}

#   Name                    (Progression Level)
general_charm_list = {
    "Balance Charm":        (ItemClassification.useful),
    "Battle Charm":         (ItemClassification.useful),
    "Beetle Charm":         (ItemClassification.useful),
    "Bling Charm":          (ItemClassification.useful),
    "Block Charm":          (ItemClassification.useful),
    "Bombskull Charm":      (ItemClassification.useful),
    "Cake Charm":           (ItemClassification.useful),
    "Chuckle Charm":        (ItemClassification.useful),
    "Cloudberry Charm":     (ItemClassification.useful),
    "Critical Charm":       (ItemClassification.useful),
    "Durian Charm":         (ItemClassification.useful),
    "Frenzy Charm":         (ItemClassification.useful),
    "Frog Charm":           (ItemClassification.useful),
    "Frosthand Charm":      (ItemClassification.useful),
    "Frozen Heart Charm":   (ItemClassification.useful),
    "Gnome Charm":          (ItemClassification.useful),
    "Goat Charm":           (ItemClassification.useful),
    "Greed Charm":          (ItemClassification.useful),
    "Heart Charm":          (ItemClassification.useful),
    "Hog Charm":            (ItemClassification.useful),
    "Hook Charm":           (ItemClassification.useful),
    "Jimbo Charm":          (ItemClassification.useful),
    "Lumin Ring":          (ItemClassification.useful),
    "Moko Charm":           (ItemClassification.useful),
    "Molten Egg Charm":     (ItemClassification.useful),
    "Moose Charm":          (ItemClassification.useful),
    "Muncher Charm":        (ItemClassification.useful),
    "Noomlin Charm":        (ItemClassification.useful),
    "Nourish Charm":        (ItemClassification.useful),
    "Pengu Charm":          (ItemClassification.useful),
    "Pinch Charm":          (ItemClassification.useful),
    "Pomegranate Charm":    (ItemClassification.useful),
    "Punchfist Charm":      (ItemClassification.useful),
    "Raspberry Charm":      (ItemClassification.useful),
    "Scorchberry Charm":    (ItemClassification.useful),
    "Scrap Charm":          (ItemClassification.useful), #Scrap charm is exclusive to both Snowdwellers and Clunkmasters, keeping it here for now
    "Shade Slug":           (ItemClassification.useful),
    "Snowball Charm":       (ItemClassification.useful),
    "Spark Charm":          (ItemClassification.useful),
    "Strawberry Charm":     (ItemClassification.useful),
    "Sun Charm":            (ItemClassification.useful),
    "Sunglass Charm":       (ItemClassification.useful),
    "Zoomlin Charm":        (ItemClassification.useful)
}

snowdweller_charm_list = {
    "Acorn Charm":          (ItemClassification.useful),
    "Jewelberry Charm":     (ItemClassification.useful),
    "Peppernut Charm":      (ItemClassification.useful),
    "Shield Charm":         (ItemClassification.useful),
    "Shroom Charm":         (ItemClassification.useful),
    "Spice Charm":          (ItemClassification.useful),
    "Truffle Charm":        (ItemClassification.useful),
}

shademancer_charm_list = {
    "Bite Charm":           (ItemClassification.useful),
    "Boonfire Charm":       (ItemClassification.useful),
    "Flameblade Charm":     (ItemClassification.useful),
    "Lamb Charm":           (ItemClassification.useful),
    "Mime Charm":           (ItemClassification.useful),
    "Tiger Charm":          (ItemClassification.useful),
}

clunkmaster_charm_list = {
    "Bom Charm":            (ItemClassification.useful),
    "Fidget Charm":         (ItemClassification.useful),
    "Gear Charm":           (ItemClassification.useful),
    "Recycle Charm":        (ItemClassification.useful),
    "Squid Charm":          (ItemClassification.useful),
}

#   Name                    (Progression Level)
bell_list = {
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
    "Infinity Sun Bell":    (ItemClassification.useful),
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
    "Blood Bell":           (ItemClassification.progression),
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

bell_map = {x: 80000 + i for i,x in enumerate(bell_list)}
filler_map = {x: 90000 + i for i,x in enumerate(filler_list)}

# Full name to ID
ITEM_NAME_TO_ID = buildings_map | tribe_map | pet_map | map_event_map | item_card_map | companions_map | charm_map | bell_map | filler_map

# There's a lot of dicts to combine, using intermediate dicts to not have a massive single line
classification_a = building_list | tribe_list | pet_list | bell_list | filler_list | map_event_list
classification_b = general_item_card_list | snowdweller_item_card_list | shademancer_item_card_list | clunkmaster_item_card_list
classification_c = general_companion_list | snowdweller_companion_list | shademancer_companion_list | clunkmaster_companion_list
classification_d = general_charm_list | snowdweller_charm_list | shademancer_charm_list | clunkmaster_charm_list
# Full name to classification
ITEM_NAME_TO_CLASSIFICATION = classification_a | classification_b | classification_c | classification_d