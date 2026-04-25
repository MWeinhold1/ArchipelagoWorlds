from worlds.AutoWorld import World
from . import Web_World, Regions, Locations, Items, Rules
from . import Options as WildfrostOptions
from .data.LocationData import LOCATION_NAME_TO_ID
from .data.ItemData import ITEM_NAME_TO_ID
from typing import Dict, Any

class WildfrostWorld(World):
    """Take on the elements in Wildfrost, a tactical roguelike deckbuilder!"""
    game: str = "Wildfrost"
    
    web = Web_World.WildfrostWeb()

    origin_region_name = "Snowdwell"

    item_name_to_id = ITEM_NAME_TO_ID
    location_name_to_id = LOCATION_NAME_TO_ID
    options_dataclass = WildfrostOptions.WildfrostOptions
    options: WildfrostOptions.WildfrostOptions

    

    #TODO - Override functions
    #def stage_assert_generate(cls, multiworld: "MultiWorld") -> None
    #def generate_early(self) -> None
    def create_regions(self) -> None:
        Regions.create_and_connect_regions(self)
        Locations.create_all_locations(self)
    def set_rules(self) -> None:
        Rules.set_all_rules(self)
    def create_items(self) -> None:
        Items.create_all_items(self)
    def create_item(self, name: str) -> Items.WildfrostItem:
        return Items.create_item(self, name)
    #def generate_basic(self) -> None
    #def generate_output(self, output_directory: str) -> None
    #def fill_slot_data(self) -> Mapping[str, Any]
    #def extend_hint_information(self, hint_data: Dict[int, Dict[int, str]])
    def get_filler_item_name(self) -> str:
        return Items.get_random_filler_item_name(self)
    #def collect_item(self, state: "CollectionState", item: "Item", remove: bool = False) -> Optional[str]
    def fill_slot_data(self) -> Dict[str, Any]:
        return {
            "goal": self.options.goal.value,
            "excluded_idols": self.options.idol_difficulty.value,
            "bypass_town_order": self.options.bypass_town_order.value,
            "bypass_building_order": self.options.bypass_building_order.value,
            "bell_sanity": self.options.bell_sanity.value,
            "fight_gating": self.options.fight_gating.value,
            "fight_rando": self.options.random_fights.value,
            "wave_rando": self.options.random_waves.value
        }