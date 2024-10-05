from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification
from worlds.AutoWorld import WebWorld, World

from .Options import WildfrostOptions, wildfrost_option_groups

class WildfrostWeb(WebWorld):
    theme = "ice"

    #TODO
    #setup_en = Tutorial()
    #location_descriptions
    #item_descriptions
    #bug_report_page

    option_groups = wildfrost_option_groups

class WildfrostWorld(World):
    """Take on the elements in Wildfrost, a tactical roguelike deckbuilder!"""
    game: str = "Wildfrost"
    
    #TODO
    #item_name_to_id
    #location_name_to_id
    #item_name_groups
    #location_name_groups

    web = WildfrostWeb()

    #TODO - Override functions
    #def stage_assert_generate(cls, multiworld: "MultiWorld") -> None
    #def generate_early(self) -> None
    #def create_regions(self) -> None
    #def create_items(self) -> None
    #def set_rules(self) -> None
    #def generate_basic(self) -> None
    #def generate_output(self, output_directory: str) -> None
    #def fill_slot_data(self) -> Mapping[str, Any]
    #def extend_hint_information(self, hint_data: Dict[int, Dict[int, str]])
    #def create_item(self, name: str) -> "Item"
    #def get_filler_item_name(self)
