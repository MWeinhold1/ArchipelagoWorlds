from dataclasses import dataclass
import typing

from Options import Option, Choice, Range, Toggle, DeathLink, OptionGroup, PerGameCommonOptions, OptionSet
from worlds.ladx.LADXR.mapgen.wfc import Cell

class Goal(Choice):
    """Determines the goal of the run.

    Frost Guardian: Reach the Eye of the Storm and defeat the Frost Guardian.

    Heart of the Storm: Get 10 storm bell power, fix the Lumin Vase, and defeat the Heart of the Storm.

    Complete Snowdwell: Complete every challenge in Snowdwell.
    This includes building the town, per-building challenges, and all idols."""
    display_name = "Goal"
    option_frost_guardian = 0
    option_heart_of_the_storm = 1
    option_complete_snowdwell = 2
    default = option_frost_guardian

class TownBuildings(Toggle):
    """Buildings are added to the item pool. The building challenge provides an Archipelago check instead"""
    display_name = "Town Buildings - WIP"

class BuildingChallenges(Toggle):
    """In-building challenge rewards are added to the item pool. Challenges provide an Archipelago check instead"""
    display_name = "Building Challenges - WIP"

class BypassBuildingOrder(Toggle):
    """If enabled, you can progress towards any build challenge from the start.
    Otherwise, you can only progress towards a build challenge if the previous one has been completed (like in vanilla).
    """
    display_name = "Bypass Building Order - (WIP)"
    default = 1
    
class BypassQuestOrder(Toggle):
    """If enabled, you can progress towards any building quest as soon as the related building is built.
    Otherwise, you can only progress towards a building quest if the previous one within the same building has been completed (like in vanilla).
    """
    display_name = "Bypass Quest Order - (WIP)"
    default = 1

class ShuffleTribes(Toggle):
    """Whether to randomize the three tribes.
    Tribe Hall challenges become Archipelago checks if shuffled.
    """
    display_name = "Shuffle Tribes - WIP"

class StartingTribes(OptionSet):
    """Determines which tribes start unlocked.
    Does nothing if "Shuffle Tribes" is disabled.
    
    Valid keys: Snowdwellers, Shademancers, Clunkmasters.
    """
    display_name = "Starting Tribes - WIP"
    valid_keys = {"Snowdwellers", "Shademancers", "Clunkmasters"}
    default = valid_keys

class LockMoreEvents(Toggle):
    """Adds the Injured Companion, Muncher, and Blingsnail Cave map events to the item pool."""
    display_name = "Lock More Map Events - WIP"

class IdolDifficulty(OptionSet):
    """Chooses which tedious idols are removed from the Archipelago checks.
    Daily Voyage is not enabled while randomized, meaning that idol will always be removed.
    Removed idols will not be required for the \"Complete Snowdwell\" goal

    Sunbringer: Disables the idol for defeating the Heart of the Storm. Auto-disabled for both victory conditions.
    
    Undefeated: Disables the idol for a 3 Win Streak. Auto-disabled for Frost Guardian victory condition.
    
    Gnomebringer: Disables the idol for winning with the Naked Gnome. Auto-disabled for Frost Guardian victory condition.
    """
    display_name = "Idol Difficulty - WIP"
    valid_keys = {"Sunbringer", "Undefeated", "Gnomebringer"}
    default = valid_keys

class RandomInventory(Toggle):
    """Add items from the starting inventory to the item pool.

    Excludes Scrappy Sword, Tar Blade, Gearhammer, and Junk."""
    display_name = "Randomize Starting Inventory - WIP"

class ShuffleCharms(Toggle):
    """Option to add charms to the item pool.

    When enabled, every charm will be locked at the start as items.
    Adds a random location for every charm.
    """
    display_name = "Shuffle Charms"
    default = 1

class RandomLuminVase(Choice):
    """Option to add the Lumin Vase to the item pool.
    
    Off: Lumin Vase is not randomized.
    
    Single: The Lumin Vase is added to the item pool. Lumin parts will not appear until the Vase is found.
    
    Parts: The Broken Vase, Lumin Goop, and The Lumin Vase are added to the item pool as separate items."""
    display_name = "Randomize Lumin Vase - WIP"
    option_off = 0
    option_single = 1
    option_parts = 2
    default = option_off

class RandomSnoof(Toggle):
    """If enabled, Snoof is added to the list of randomized companions.
    Otherwise, Snoof is unlocked from the start."""
    display_name = "Randomize Snoof - WIP"

class SunBells(Toggle):
    """Adds Sun Bells to the item pool."""
    display_name = "Sun Bells - WIP"

class StormBells(Toggle):
    """Adds Storm Bells to the item pool."""
    display_name = "Storm Bells - WIP"

class VoyageBells(Toggle):
    """Adds Bells unique to the Daily Voyage to the item pool."""
    display_name = "Voyage Bells - WIP"

class BellSanity(Choice):
    """Changes how bell selection works.

    Standard: Storm Bells can be selected before a run.
    Sun Bells are applied when selected after boss fights.
    Voyage Bells are disabled.
    
    Selection: Unlocked Bells do not appear in boss rewards.
    Before each run, all types of bells can be enabled/disabled.
    
    Bellsanity: Unlocked Bells are automatically enabled for every run.
    Bells cannot be disabled."""
    display_name = "Bell-Sanity - WIP"
    option_standard = 0
    option_selection = 1
    option_bellsanity = 2
    default = option_standard

class ArchipelaGnome(Toggle):
    """Replaces the Naked Gnome with the Archipela-Gnome. Gives a free hint when spared.
    Naked Gnome will instead appear in Frozen Travelers."""
    display_name = "Archipela-Gnome - WIP"

class KillChecks(OptionSet):
    """Adds extra checks for unique kills on enemies.
    NOTE: Boss kills only count as completed when the fight is won.
    
    Bosses: Bosses give extra checks.
    
    Mini Bosses: Mini-Bosses give extra checks.
    
    Enemies: All enemies give extra checks

    ***NOT RECOMMENDED***
    Storm Only: Certain enemies that can only appear in the Eye of the Storm, 
    based on previous team compositions, give extra checks"""

    display_name = "Add Unique Boss Kill Checks - WIP"
    valid_keys = {"Bosses", "Mini Bosses", "Enemies", "Storm Only"}
    default = ["Bosses", "Mini Bosses"]

class RandomFights(Choice):
    """Changes the order of where fights will appear. Eye/Heart of the Storm will never be randomized.
    
    Off: No fight randomization.
    
    Zone: Fights within a zone can appear in any order, including bosses.
    
    Chaos: All fights can appear in any order, including bosses."""
    display_name = "Randomize Fight Appearance - WIP"
    option_off = 0
    option_zone = 1
    option_chaos = 2
    default = option_off

class FightBalance(Choice):
    """Randomizes what enemy waves can appear within a fight.
    
    Off: Normal waves appear in each fight.
    
    Mild: New waves with reasonable wave changes can appear.
    
    Wild: New waves with bizarre wave changes can appear."""
    display_name = "Randomize Fight Waves - WIP"
    option_off = 0
    option_mild = 1
    option_wild = 2
    default = option_off


class TrapsBoons(Choice):
    """Add traps and boons to the item pool. For each trap/boon added to the item pool, an
    additional check will be added to the companions, items, charms, or bells checks,
    keeping the relative ratio of checks between each.
    
    Off: No traps and boons.
    
    Exact: Each range adds the exact number of that trap or boon to the item pool.
    
    Weight: Traps and Boons are randomly added to the pool, using the weight to determine
    how likely each trap/boon will appear."""
    display_name = "Use Traps and Boons - WIP"
    option_off = 0
    option_exact = 1
    option_weight = 2
    default = option_off

class TBWeightCount(Range):
    """If the \"Use Traps and Boons\" setting is set to \"Weight\", this determines how many total
    traps/boons will be added. If the setting is \"Exact\" or \"Off\", this does nothing."""
    display_name = "Weight Count - WIP"
    range_start = 1
    range_end = 100
    default = 1

class TBInkBlot(Range):
    """Apply 5 ink to all active companions."""
    display_name = "Ink Blot Trap - WIP"
    range_start = 0
    range_end = 25

class TBHoghead(Range):
    """Apply hogheaded to all active companions."""
    display_name = "Hoghead Trap - WIP"
    range_start = 0
    range_end = 25

class TBSupportDeath(Range):
    """All Shades and Clunkers on both sides are killed."""
    display_name = "Minion Death Trap - WIP"
    range_start = 0
    range_end = 25

class TBBombard(Range):
    """Prepares a Phase 2 Krunker Bombard for the next turn."""
    display_name = "Bombard Trap - WIP"
    range_start = 0
    range_end = 25

class TBIceWall(Range):
    """All active enemies get 1 ice block."""
    display_name = "Ice Wall Trap - WIP"
    range_start = 0
    range_end = 25

class TBThrowShade(Range):
    """Spawns shade(s) on either side of the map. Shades might be helpful or harmful.\n"""
    # Helpful:
    # Summon Chikani
    # Summon a copy of your leader
    # Fill enemy spaces with Sheepoppers
    # Summon a copy of a random enemy
    #
    # Harmful:
    # Spawn a Tigris on the enemy side
    # Spawn a Backline Leech on your side 
    # Spawn a Frontline Sheepopper on your side 
    # Spawn Chikagoru on emey side
    #
    # Either:
    # Fill all empty spaces with Beepop (both sides)
    # Summon a Shade Monch
    display_name = "Throwing Shade Event - WIP"
    range_start = 0
    range_end = 25

class TBSpeedBoost(Range):
    """Adds a Zoomlin Consume Sun Rod to your hand."""
    display_name = "Speed Boon - WIP"
    range_start = 0
    range_end = 25

class TBSnowDay(Range):
    """Adds 2 snow to all enemies."""
    display_name = "Snowy Boon - WIP"
    range_start = 0
    range_end = 25

class TBSpicy(Range):
    """Adds a Zoomlin Consume Peppering to your hand."""
    display_name = "Spicy Boon - WIP"
    range_start = 0
    range_end = 25

class TBSunSmite(Range):
    """Gain a 20 attack Consume card to your hand."""
    display_name = "Sun Smite Boon - WIP"
    range_start = 0
    range_end = 25

class TBBerryBoon(Range):
    """Adds a Zoomlin Consume Berry Basket to your hand."""
    display_name = "Berry Basket Boon - WIP"
    range_start = 0
    range_end = 25

class TBPayday(Range):
    """Gain 100 bling"""
    display_name = "Bling Bling Boon - WIP"
    range_start = 0
    range_end = 25

class TBGunk(Range):
    """Adds 5 Gunk Fruits to your deck."""
    display_name = "Gunk Bomb Trap - WIP"
    range_start = 0
    range_end = 25

class TBCurseCrown(Range):
    """Adds a cursed crown to a random companion."""
    display_name = "Cursed Crown - WIP"
    range_start = 0
    range_end = 25

class TBGoofyGobbler(Range):
    """Fills the enemy side with Gobblers. Can be any combination of Gunk/Shroom/Snow/Standard Gobblers."""
    display_name = "Goofy Gobbler Trap - WIP"
    range_start = 0
    range_end = 25

wildfrost_option_groups = [
    OptionGroup("Town Options", [
        TownBuildings,
        BuildingChallenges,
        BypassBuildingOrder,
        BypassQuestOrder,
        ShuffleTribes,
        StartingTribes,
        LockMoreEvents,
        IdolDifficulty,
        ShuffleCharms
    ]),
    OptionGroup("Inventory Options", [
        RandomInventory,
        RandomLuminVase,
        RandomSnoof
    ]),
    OptionGroup("Bell Options", [
        SunBells,
        StormBells,
        VoyageBells,
        BellSanity,
    ]),
    OptionGroup("Fight Options", [
        ArchipelaGnome,
        KillChecks,
        RandomFights,
        FightBalance
    ]),
    OptionGroup("Traps and Boons", [
        TrapsBoons,
        TBWeightCount,
        TBBerryBoon,
        TBBombard,
        TBCurseCrown,
        TBGunk,
        TBHoghead,
        TBIceWall,
        TBInkBlot,
        TBPayday,
        TBSnowDay,
        TBSpeedBoost,
        TBSpicy,
        TBSupportDeath,
        TBThrowShade,
        TBGoofyGobbler
    ])
]

@dataclass
class WildfrostOptions(PerGameCommonOptions):
    goal: Goal
    deathlink: DeathLink

    town_buildings: TownBuildings
    building_challenges: BuildingChallenges
    bypass_building_order: BypassBuildingOrder
    bypass_quest_order: BypassQuestOrder
    shuffle_tribes: ShuffleTribes
    starting_tribes: StartingTribes
    shuffle_charms: ShuffleCharms
    lock_more_events: LockMoreEvents
    idol_difficulty: IdolDifficulty
    
    random_inventory: RandomInventory
    random_lumin_vase: RandomLuminVase
    random_snoof: RandomSnoof

    sun_bells: SunBells
    storm_bells: StormBells
    voyage_bells: VoyageBells
    bell_sanity: BellSanity

    archipelagnome: ArchipelaGnome
    kill_checks: KillChecks
    random_fights: RandomFights
    fight_balance: FightBalance
    
    traps_boons: TrapsBoons
    tb_weight_count: TBWeightCount
    tb_berry_picking: TBBerryBoon
    tb_bombard: TBBombard
    tb_curse_crown: TBCurseCrown
    tb_gunk: TBGunk
    tb_hoghead: TBHoghead
    tb_ice_wall: TBIceWall
    tb_ink_blot: TBInkBlot
    tb_payday: TBPayday
    tb_snow_day: TBSnowDay
    tb_speed_boost: TBSpeedBoost
    tb_spicy: TBSpicy
    tb_support_death: TBSupportDeath
    tb_throw_shade: TBThrowShade