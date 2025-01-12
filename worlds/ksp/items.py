from BaseClasses import ItemClassification as IC
from typing import NamedTuple, Dict, Set, List
from enum import IntEnum

APP_ID = 220200
ITEM_ID = APP_ID * 10000 + 1000


class ItemType(IntEnum):
    technology = 1


class ItemData(NamedTuple):
    classification: IC
    count: int
    name: str
    tech_type: str
    type: ItemType = ItemType.technology


item_table: Dict[int, ItemData] = {
    # The first item is the start node and is always unlocked
    ITEM_ID+0: ItemData(IC.progression, 0, "Start", "start"),
    ITEM_ID+1: ItemData(IC.progression, 1, "Basic Rocketry", "basicRocketry"),
    ITEM_ID+2: ItemData(IC.progression, 1, "Engineering 101", "engineering101"),
    ITEM_ID+3: ItemData(IC.progression, 1, "Survivability", "survivability"),
    ITEM_ID+4: ItemData(IC.progression, 1, "Stability", "stability"),
    ITEM_ID+5: ItemData(IC.progression, 1, "General Rocketry", "generalRocketry"),
    ITEM_ID+6: ItemData(IC.progression, 1, "Aviation", "aviation"),
    ITEM_ID+7: ItemData(IC.progression, 1, "Basic Science", "basicScience"),
    ITEM_ID+8: ItemData(IC.progression, 1, "Flight Control", "flightControl"),
    ITEM_ID+9: ItemData(IC.progression, 1, "Advanced Rocketry", "advRocketry"),
    ITEM_ID+10: ItemData(IC.progression, 1, "General Construction", "generalConstruction"),
    ITEM_ID+11: ItemData(IC.useful, 1, "Propulsion Systems", "propulsionSystems"),
    ITEM_ID+12: ItemData(IC.filler, 1, "Space Exploration", "spaceExploration"),
    ITEM_ID+13: ItemData(IC.progression, 1, "Advanced Flight Control", "advFlightControl"),
    ITEM_ID+14: ItemData(IC.progression, 1, "Landing", "landing"),
    ITEM_ID+15: ItemData(IC.useful, 1, "Aerodynamics", "aerodynamicSystems"),
    ITEM_ID+16: ItemData(IC.progression, 1, "Electrics", "electrics"),
    ITEM_ID+17: ItemData(IC.progression, 1, "Heavy Rocketry", "heavyRocketry"),
    ITEM_ID+18: ItemData(IC.progression, 1, "Fuel Systems", "fuelSystems"),
    ITEM_ID+19: ItemData(IC.progression, 1, "Advanced Construction", "advConstruction"),
    ITEM_ID+20: ItemData(IC.progression, 1, "Miniaturization", "miniaturization"),
    ITEM_ID+21: ItemData(IC.useful, 1, "Actuators", "actuators"),
    ITEM_ID+22: ItemData(IC.progression, 1, "Command Modules", "commandModules"),
    ITEM_ID+23: ItemData(IC.progression, 1, "Heavier Rocketry", "heavierRocketry"),
    ITEM_ID+24: ItemData(IC.useful, 1, "Precision Engineering", "precisionEngineering"),
    ITEM_ID+25: ItemData(IC.progression, 1, "Advanced Exploration", "advExploration"),
    ITEM_ID+26: ItemData(IC.progression, 1, "Specialized Control", "specializedControl"),
    ITEM_ID+27: ItemData(IC.progression, 1, "Advanced Landing", "advLanding"),
    ITEM_ID+28: ItemData(IC.filler, 1, "Supersonic Flight", "supersonicFlight"),
    ITEM_ID+29: ItemData(IC.progression, 1, "Adv. Fuel Systems", "advFuelSystems"),
    ITEM_ID+30: ItemData(IC.progression, 1, "Advanced Electrics", "advElectrics"),
    ITEM_ID+31: ItemData(IC.progression, 1, "Specialized Construction", "specializedConstruction"),
    ITEM_ID+32: ItemData(IC.useful, 1, "Precision Propulsion", "precisionPropulsion"),
    ITEM_ID+33: ItemData(IC.filler, 1, "Advanced Aerodynamics", "advAerodynamics"),
    ITEM_ID+34: ItemData(IC.filler, 1, "Heavy Landing", "heavyLanding"),
    ITEM_ID+35: ItemData(IC.progression, 1, "Scanning Tech", "scienceTech"),
    ITEM_ID+36: ItemData(IC.useful, 1, "Unmanned Tech", "unmannedTech"),
    ITEM_ID+37: ItemData(IC.progression, 1, "Nuclear Propulsion", "nuclearPropulsion"),
    ITEM_ID+38: ItemData(IC.filler, 1, "Advanced MetalWorks", "advMetalworks"),
    ITEM_ID+39: ItemData(IC.filler, 1, "Field Science", "fieldScience"),
    ITEM_ID+40: ItemData(IC.filler, 1, "High Altitude Flight", "highAltitudeFlight"),
    ITEM_ID+41: ItemData(IC.progression, 1, "Large Volume Containment", "largeVolumeContainment"),
    ITEM_ID+42: ItemData(IC.filler, 1, "Composites", "composites"),
    ITEM_ID+43: ItemData(IC.progression, 1, "Electronics", "electronics"),
    ITEM_ID+44: ItemData(IC.progression, 1, "High-Power Electrics", "largeElectrics"),
    ITEM_ID+45: ItemData(IC.filler, 1, "Heavy Aerodynamics", "heavyAerodynamics"),
    ITEM_ID+46: ItemData(IC.useful, 1, "Ion Propulsion", "ionPropulsion"),
    ITEM_ID+47: ItemData(IC.filler, 1, "Hypersonic Flight", "hypersonicFlight"),
    # This node has nothing in it and is therefore hidden
    ITEM_ID+48: ItemData(IC.filler, 0, "Nanolathing", "nanolathing"),
    ITEM_ID+49: ItemData(IC.useful, 1, "Advanced Unmanned Tech", "advUnmanned"),
    ITEM_ID+50: ItemData(IC.useful, 1, "Meta-Materials", "metaMaterials"),
    ITEM_ID+51: ItemData(IC.progression, 1, "Very Heavy Rocketry", "veryHeavyRocketry"),
    ITEM_ID+52: ItemData(IC.progression, 1, "Advanced Science Tech", "advScienceTech"),
    ITEM_ID+53: ItemData(IC.filler, 1, "Advanced Motors", "advancedMotors"),
    ITEM_ID+54: ItemData(IC.useful, 1, "Specialized Electrics", "specializedElectrics"),
    ITEM_ID+55: ItemData(IC.progression, 1, "High-Performance Fuel Systems", "highPerformanceFuelSystems"),
    ITEM_ID+56: ItemData(IC.filler, 1, "Experimental Aerodynamics", "experimentalAerodynamics"),
    ITEM_ID+57: ItemData(IC.useful, 1, "Automation", "automation"),
    ITEM_ID+58: ItemData(IC.filler, 1, "Aerospace Tech", "aerospaceTech"),
    ITEM_ID+59: ItemData(IC.filler, 1, "Large Probes", "largeUnmanned"),
    ITEM_ID+60: ItemData(IC.filler, 1, "Experimental Science", "experimentalScience"),
    # This node has nothing in it and is therefore hidden
    ITEM_ID+61: ItemData(IC.filler, 0, "Experimental Motors", "experimentalMotors"),
    ITEM_ID+62: ItemData(IC.useful, 1, "Experimental Electrics", "experimentalElectrics"),
}

items_by_type: Dict[ItemType, List[int]] = {
    item_type: [] for item_type in ItemType}
for item_id, item_data in item_table.items():
    items_by_type[item_data.type].append(item_id)

group_items: Dict[int, Set[int]] = {
    35100: {35025, 35047, 35048, 35056, 35057, 35058, 35059, 35060, 35061, 35062, 35063, 35064, 35065, 35067, 35068,
            35069, 35070, 35073, 35074},
    35101: {35049, 35050, 35051, 35071, 35072, 35074},
    35102: set(items_by_type[ItemType.resource]),
}
