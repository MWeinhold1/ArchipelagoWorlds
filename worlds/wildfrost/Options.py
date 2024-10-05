from dataclasses import dataclass
import typing

from Options import Option, Choice, Range, Toggle, DeathLink, OptionGroup, PerGameCommonOptions
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
    default = 0

class TownBuildings(Choice):
    """Buildings are added to the item pool. The building process provides an Archipelago check instead"""
    display_name = "Town Buildings - WIP"

class BuildingChallenges(Toggle):
    """In-building challenge rewards are added to the item pool. Challenges provide an Archipelago check instead"""
    display_name = "Building Challenges - WIP"

class TownSequence(Choice):
    """Determines the progression of town challenges.

    Vanilla: Buildings/Challenges must be completed before the next building/challenge progression starts.

    All Buildings: All buildings can be built at the same time.

    All Challenges: Once a building is built, all challenges in that building can be progressed at the same time.

    All At Once: Combines the All Buildings and All Challenges options.
    Buildings must still be unlocked before their challenges can be started."""
    display_name = "Town Unlock Sequence - WIP"
    vanilla = 0
    all_buildings = 1
    all_challenges = 2
    all_at_once = 3

class RandomTribes(Toggle):
    """Adds the Shademancers and Clunkmasters to the item pool.
    Tribe Hall challenges become Archipelago checks."""
    display_name = "Randomize Tribes - WIP"

class LockMoreEvents(Toggle):
    """Adds the Injured Companion, Muncher, and Blingsnail map events to the item pool."""
    display_name = "Lock More Map Events - WIP"

class IdolDifficulty(Choice):
    """Chooses which tedious idols are removed from the Archipelago checks.
    Daily Voyage is not enabled while randomized, meaning that idol will always be removed.
    Removed idols will not be required for the \"Complete Snowdwell\" goal

    Sunbringer: Disables the idol for defeating the Heart of the Storm.
    
    Undefeated: Disables the idol for a 3 Win Streak.
    
    Gnomebringer: Disables the idol for winning with the Naked Gnome.
    """
    display_name = "Idol Difficulty - WIP"
    none = 0
    sunbringer = 1
    undefeated = 2
    gnomebringer = 3
    sunbringer_undefeated = 4
    sunbringer_gnomebringer = 5
    undefeated_gnomebringer = 6
    all_three = 7

class RandomInventory(Toggle):
    """Add items from the starting inventory to the item pool.

    Excludes Scrappy Sword, Tar Blade, Gearhammer, and Junk."""
    display_name = "Randomize Starting Inventory - WIP"

class RandomLuminVase(Choice):
    """Option to add the Lumin Vase to the item pool.
    
    Off: Lumin Vase is not randomized.
    
    Single: The Lumin Vase is added to the item pool. Lumin parts will not appear until the Vase is found.
    
    Parts: The Broken Vase, Lumin Goop, and The Lumin Vase are added to the item pool as separate items."""
    display_name = "Randomize Lumin Vase - WIP"
    off = 0
    single = 1
    parts = 2

class RandomSnoof(Toggle):
    """If enabled, Snoof is added to the list of randomized companions.
    Otherwise, Snoof is unlocked as soon as the Pet House is built."""
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
    standard = 0
    selection = 1
    bellsanity = 2

class ArchipelaGnome(Toggle):
    """Replaces the Naked Gnome with the Archipela-Gnome. Gives a free hint when spared.
    Naked Gnome will instead appear in Frozen Travelers."""
    display_name = "Archipela-Gnome - WIP"

class KillChecks(Choice):
    """Adds extra checks for unique kills on enemies.
    NOTE: Excludes the Gnome and Heart of the Storm Bosses. Bosses only count when all phases/splits are defeated.
    
    Off: Unique kills do not give checks.
    
    Bosses: Bosses give extra checks.
    
    Mini-Bosses: Bosses and Mini-Bosses give extra checks.
    
    Enemies: All enemies give extra checks, as well as Bosses and Mini-Bosses.
    
    Enemies+: Same as the Enemies option, but includes certain enemies that can
    only appear in the Eye of the Storm, based on previous team compositions"""
    display_name = "Add Unique Boss Kill Checks - WIP"
    off = 0
    bosses = 1
    mini_bosses = 2
    enemies = 3
    enemies_plus = 4

class RandomFights(Choice):
    """Changes the order of where fights will appear. Eye/Heart of the Storm will never be randomized.
    
    Off: No fight randomization.
    
    Zone: Fights within a zone can appear in any order, including bosses.
    
    Chaos: All fights can appear in any order, including bosses."""
    display_name = "Randomize Fight Appearance - WIP"
    off = 0
    zone = 1
    chaos = 2

class FightBalance(Choice):
    """Randomizes what enemy waves can appear within a fight.
    
    Off: Normal waves appear in each fight.
    
    Mild: New waves with reasonable wave changes can appear.
    
    Wild: New waves with bizarre wave changes can appear."""
    display_name = "Randomize Fight Waves - WIP"
    off = 0
    mild = 1
    wild = 2


class TrapsBoons(Choice):
    """Add traps and boons to the item pool. For each trap/boon added to the item pool, an
    additional check will be added to the companions, items, charms, or bells checks,
    keeping the relative ratio of checks between each.
    
    Off: No traps and boons.
    
    Exact: Each range adds the exact number of that trap or boon to the item pool.
    
    Weight: Traps and Boons are randomly added to the pool, using the weight to determine
    how likely each trap/boon will appear."""
    display_name = "Use Traps and Boons - WIP"
    off = 0
    exact = 1
    weight = 2

class TBWeightCount(Range):
    """If the \"Use Traps and Boons\" setting is set to \"Weight\", this determines how many total
    traps/boons will be added. If the setting is \"Exact\" or \"Off\", this does nothing."""
    display_name = "Weight Count - WIP"
    range_start = 1
    range_end = 100

class TBInkBlot(Range):
    """Apply 5 ink to all active companions."""
    display_name = "Ink Blot - WIP"
    range_start = 0
    range_end = 25

class TBHoghead(Range):
    """Apply hogheaded to all active companions."""
    display_name = "Hoghead - WIP"
    range_start = 0
    range_end = 25

class TBSupportDeath(Range):
    """All Shades and Clunkers on both sides are killed."""
    display_name = "Support Death - WIP"
    range_start = 0
    range_end = 25

class TBBombard(Range):
    """Prepares a Phase 2 Krunker Bombard for the next turn."""
    display_name = "Bombard - WIP"
    range_start = 0
    range_end = 25

class TBIceWall(Range):
    """All active enemies get 1 ice block."""
    display_name = "Ice Wall - WIP"
    range_start = 0
    range_end = 25

class TBThrowShade(Range):
    """Does one of the following:\n
    - Fill all empty enemy spaces with Beepop.
    - Spawn a Tigris on the enemy side.
    - Spawn a Leech, Pom, or Sheepopper on your side, with either Frontline or Backline."""
    display_name = "Throwing Shade - WIP"
    range_start = 0
    range_end = 25

class TBSpeedBoost(Range):
    """Adds a Zoomlin Consume Sun Rod to your hand."""
    display_name = "Speed Boost - WIP"
    range_start = 0
    range_end = 25

class TBSnowDay(Range):
    """Adds 2 snow to all enemies."""
    display_name = "Snow Day - WIP"
    range_start = 0
    range_end = 25

class TBSpicy(Range):
    """Adds a Zoomlin Consume Peppering to your hand."""
    display_name = "Spicy - WIP"
    range_start = 0
    range_end = 25

class TBSunSmite(Range):
    """Gain a 50 attack Consume card to your hand."""
    display_name = "Bombard - WIP"
    range_start = 0
    range_end = 25

class TBBerryPicking(Range):
    """Adds a Zoomlin Consume Berry Basket to your hand."""
    display_name = "Bombard - WIP"
    range_start = 0
    range_end = 25

class TBPayday(Range):
    """Gain 100 bling"""
    display_name = "Payday - WIP"
    range_start = 0
    range_end = 25

class TBGunk(Range):
    """Adds 5 Gunk Fruits to your deck."""
    display_name = "Gunk - WIP"
    range_start = 0
    range_end = 25

class TBCurseCrown(Range):
    """Adds a cursed crown to a random companion."""
    display_name = "Cursed Crown - WIP"
    range_start = 0
    range_end = 25

wildfrost_option_groups = [
    OptionGroup("Town Options", [
        TownBuildings,
        BuildingChallenges,
        TownSequence,
        RandomTribes,
        LockMoreEvents
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
        TBBerryPicking,
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
        TBThrowShade
    ])
]

@dataclass
class WildfrostOptions(PerGameCommonOptions):
    goal: Goal
    deathlink: DeathLink

    town_buildings: TownBuildings
    building_challenges: BuildingChallenges
    town_sequence: TownSequence
    random_tribes: RandomTribes
    lock_more_events: LockMoreEvents
    
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
    tb_berry_picking: TBBerryPicking
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