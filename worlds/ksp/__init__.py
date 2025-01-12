from __future__ import annotations

import logging
import itertools
from typing import List, Dict, Any, cast

from BaseClasses import Region, Entrance, Location, Item, Tutorial, ItemClassification
from worlds.AutoWorld import World, WebWorld
from . import items
from . import locations
from . import creatures
from . import options
from .items import item_table, group_items, items_by_type, ItemType
from .rules import set_rules

logger = logging.getLogger("KerbalSpaceProgram")

class KerbalSpaceProgramWeb(WebWorld):
    tutorials = []


all_locations = {data["name"]: loc_id for loc_id, data in locations.location_table.items()}
all_locations.update(creatures.creature_locations)


class KerbalSpaceProgramWorld(World):
    """
    KerbalSpaceProgram is a game.
    """
    game = "KerbalSpaceProgram"
    web = KerbalSpaceProgramWeb()

    item_name_to_id = {data.name: item_id for item_id, data in items.item_table.items()}
    location_name_to_id = all_locations
    option_definitions = options.option_definitions

    data_version = 10
    required_client_version = (0, 4, 1)

    creatures_to_scan: List[str]

    def generate_early(self) -> None:
        if self.options.early_seaglide:
            self.multiworld.local_early_items[self.player]["Seaglide Fragment"] = 2

        scan_option: options.AggressiveScanLogic = self.options.creature_scan_logic
        creature_pool = scan_option.get_pool()

        self.options.creature_scans.value = min(
            len(creature_pool),
            self.options.creature_scans.value
        )

        self.creatures_to_scan = self.random.sample(
            creature_pool, self.options.creature_scans.value)

    def create_regions(self):
        # Create Regions
        menu_region = Region("Menu", self.player, self.multiworld)
        planet_region = Region("Planet 4546B", self.player, self.multiworld)

        # Link regions together
        menu_region.connect(planet_region, "Lifepod 5")

        # Create regular locations
        location_names = itertools.chain((location["name"] for location in locations.location_table.values()),
                                         (creature + creatures.suffix for creature in self.creatures_to_scan))
        for location_name in location_names:
            loc_id = self.location_name_to_id[location_name]
            location = KerbalSpaceProgramLocation(self.player, location_name, loc_id, planet_region)
            planet_region.locations.append(location)

        # Create events
        goal_event_name = self.options.goal.get_event_name()

        for event in locations.events:
            location = KerbalSpaceProgramLocation(self.player, event, None, planet_region)
            planet_region.locations.append(location)
            location.place_locked_item(
                KerbalSpaceProgramItem(event, ItemClassification.progression, None, player=self.player))
            if event == goal_event_name:
                # make the goal event the victory "item"
                location.item.name = "Victory"

        # Register regions to multiworld
        self.multiworld.regions += [
            menu_region,
            planet_region
        ]

    # refer to Rules.py
    set_rules = set_rules

    def create_items(self):
        # Generate item pool
        pool: List[KerbalSpaceProgramItem] = []
        extras = self.options.creature_scans.value

        grouped = set(itertools.chain.from_iterable(group_items.values()))

        for item_id, item in item_table.items():
            if item_id in grouped:
                extras += item.count
            else:
                for i in range(item.count):
                    KerbalSpaceProgram_item = self.create_item(item.name)
                    if item.name == "Neptune Launch Platform":
                        self.get_location("Aurora - Captain Data Terminal").place_locked_item(
                            KerbalSpaceProgram_item)
                    else:
                        pool.append(KerbalSpaceProgram_item)

        group_amount: int = 2
        assert len(group_items) * group_amount <= extras
        for item_id in group_items:
            name = item_table[item_id].name
            for _ in range(group_amount):
                pool.append(self.create_item(name))
            extras -= group_amount

        for item_name in self.random.sample(
            # list of high-count important fragments as priority filler
                [
                    "Cyclops Engine Fragment",
                    "Cyclops Hull Fragment",
                    "Cyclops Bridge Fragment",
                    "Seamoth Fragment",
                    "Prawn Suit Fragment",
                    "Mobile Vehicle Bay Fragment",
                    "Modification Station Fragment",
                    "Moonpool Fragment",
                    "Laser Cutter Fragment",
                 ],
                k=min(extras, 9)):
            item = self.create_item(item_name)
            pool.append(item)
            extras -= 1

        # resource bundle filler
        for _ in range(extras):
            item = self.create_filler()
            item = cast(KerbalSpaceProgramItem, item)
            pool.append(item)

        self.multiworld.itempool += pool

    def fill_slot_data(self) -> Dict[str, Any]:
        vanilla_tech: List[str] = []

        slot_data: Dict[str, Any] = {
            "goal": self.options.goal.current_key,
            "swim_rule": self.options.swim_rule.current_key,
            "vanilla_tech": vanilla_tech,
            "creatures_to_scan": self.creatures_to_scan,
            "death_link": self.options.death_link.value,
            "free_samples": self.options.free_samples.value,
        }

        return slot_data

    def create_item(self, name: str) -> KerbalSpaceProgramItem:
        item_id: int = self.item_name_to_id[name]

        return KerbalSpaceProgramItem(name,
                              item_table[item_id].classification,
                              item_id, player=self.player)

    def get_filler_item_name(self) -> str:
        return item_table[self.multiworld.random.choice(items_by_type[ItemType.resource])].name


class KerbalSpaceProgramLocation(Location):
    game: str = "KerbalSpaceProgram"


class KerbalSpaceProgramItem(Item):
    game: str = "KerbalSpaceProgram"
