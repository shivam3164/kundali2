"""
Vedha (Obstruction) Analysis Module.
Source: Vedic Astrology: An Integrated Approach, Section 26.3, Table 63

When a planet transits in a favorable house from natal Moon, another planet
in the "Vedha Sthana" (obstruction house) can block its good effects.
"""
from typing import Dict, Optional, Tuple

# Vedha Rules: { Planet: { Favorable_House: Obstruction_House } }
# Only favorable houses have Vedha - unfavorable houses are not obstructed
VEDHA_RULES: Dict[str, Dict[int, int]] = {
    "Sun": {3: 9, 6: 12, 10: 4, 11: 5},
    "Moon": {1: 5, 3: 9, 6: 12, 7: 2, 10: 4, 11: 8},
    "Mars": {3: 12, 6: 9, 11: 5},
    "Mercury": {2: 5, 4: 3, 6: 9, 8: 1, 10: 8, 11: 12},
    "Jupiter": {2: 12, 5: 4, 7: 3, 9: 10, 11: 8},
    "Venus": {1: 8, 2: 7, 3: 1, 4: 10, 5: 9, 8: 5, 9: 11, 11: 6, 12: 3},
    "Saturn": {3: 12, 6: 9, 11: 5},
}

# Exception pairs that do NOT cause Vedha on each other
# Source: Section 26.3 - "Sun and Saturn do not cause vedha on each other"
VEDHA_EXCEPTIONS = [
    ("Sun", "Saturn"),      # Father-Son pair
    ("Moon", "Mercury"),    # Mind-Intellect pair
]


def get_vedha_house(planet: str, transit_house: int) -> Optional[int]:
    """
    Returns the Vedha (obstruction) house for a planet's favorable transit.
    Returns None if the transit house is not favorable or no Vedha applies.
    
    Args:
        planet: Planet name (Sun, Moon, Mars, etc.)
        transit_house: House (1-12) from natal Moon
    
    Returns:
        Vedha house number or None
    """
    if planet not in VEDHA_RULES:
        return None
    return VEDHA_RULES[planet].get(transit_house)


def is_exception_pair(planet1: str, planet2: str) -> bool:
    """
    Check if two planets are an exception pair (no mutual Vedha).
    
    Args:
        planet1: First planet name
        planet2: Second planet name
    
    Returns:
        True if they are an exception pair
    """
    for p1, p2 in VEDHA_EXCEPTIONS:
        if (planet1 == p1 and planet2 == p2) or (planet1 == p2 and planet2 == p1):
            return True
    return False


def check_vedha_obstruction(
    planet: str,
    transit_house_from_moon: int,
    all_transit_houses: Dict[str, int]
) -> Tuple[bool, Optional[str], Optional[int]]:
    """
    Checks if a planet's favorable transit is obstructed by Vedha.
    
    Example: Jupiter in 2nd house from Moon is favorable.
    But if any planet is in 12th house, Jupiter's good results are blocked.
    
    Args:
        planet: The transiting planet being analyzed
        transit_house_from_moon: House (1-12) the planet is transiting from natal Moon
        all_transit_houses: Dict of all planets and their current houses from natal Moon
    
    Returns:
        Tuple of (is_obstructed, obstructing_planet, vedha_house)
    """
    vedha_house = get_vedha_house(planet, transit_house_from_moon)
    
    if vedha_house is None:
        # No Vedha applies to this transit position (either not favorable or no rule)
        return (False, None, None)
    
    # Check if any planet occupies the Vedha house
    for other_planet, house in all_transit_houses.items():
        if other_planet == planet:
            continue
            
        if house == vedha_house:
            # Check exception pairs before declaring obstruction
            if is_exception_pair(planet, other_planet):
                continue
            
            return (True, other_planet, vedha_house)
    
    return (False, None, vedha_house)


def get_favorable_houses(planet: str) -> list:
    """
    Get list of favorable transit houses for a planet.
    
    Args:
        planet: Planet name
    
    Returns:
        List of favorable house numbers
    """
    if planet not in VEDHA_RULES:
        return []
    return list(VEDHA_RULES[planet].keys())
