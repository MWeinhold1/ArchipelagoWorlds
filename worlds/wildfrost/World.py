from worlds.AutoWorld import World
from . import Web_World, Regions, Locations, Items

class WildfrostWorld(World):
    """Take on the elements in Wildfrost, a tactical roguelike deckbuilder!"""
    game: str = "Wildfrost"
    
    web = Web_World.WildfrostWeb()

    origin_region_name = Regions.startingRegion

    #TODO
    item_name_to_id = Items.item_name_to_id
    location_name_to_id = Locations.location_name_to_id
    #options_dataclass
    #options

    #TODO - Override functions
    #def stage_assert_generate(cls, multiworld: "MultiWorld") -> None
    #def generate_early(self) -> None
    def create_regions(self) -> None:
        Regions.create_and_connect_regions(self)
    #def set_rules(self) -> None
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