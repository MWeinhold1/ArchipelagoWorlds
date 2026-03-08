from worlds.AutoWorld import WebWorld
from . import Options as WildfrostOptions

class WildfrostWeb(WebWorld):
    theme = "ice"

    #TODO
    #setup_en = Tutorial()
    #location_descriptions
    #item_descriptions
    #bug_report_page

    option_groups = WildfrostOptions.wildfrost_option_groups