from worlds.AutoWorld import WebWorld
from . import Options as WildfrostOptions
from . import World as WildfrostWorld

class WildfrostWeb(WebWorld):
    game = WildfrostWorld.game
    theme = "ice"

    #TODO
    #setup_en = Tutorial()
    #location_descriptions
    #item_descriptions
    #bug_report_page

    option_groups = WildfrostOptions.wildfrost_option_groups