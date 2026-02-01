"""
Murthi (Form/Idol) Analysis Module.
Source: Vedic Astrology: An Integrated Approach, Section 26.2, Table 62

The Moon's position at the moment a planet enters a new sign determines
the "Murthi" (form) quality of that transit for an individual.

This is an advanced technique that modifies the intensity of transit results.
"""
from typing import Dict, Tuple

# Murthi classifications based on Moon's house from natal Moon at rasi entry
# Format: { murthi_name: (house_list, quality_description) }
MURTHI_DATA: Dict[str, Tuple[list, str]] = {
    "Swarna": ([1, 6, 11], "Highly Favorable"),   # Golden form - Full results
    "Rajata": ([2, 5, 9], "Favorable"),           # Silver form - 3/4 results
    "Taamra": ([3, 7, 10], "Unfavorable"),        # Copper form - 1/2 results
    "Loha": ([4, 8, 12], "Highly Unfavorable"),   # Iron form - 1/4 results
}

# Reverse lookup: house -> murthi
HOUSE_TO_MURTHI: Dict[int, str] = {}
for murthi, (houses, _) in MURTHI_DATA.items():
    for house in houses:
        HOUSE_TO_MURTHI[house] = murthi

# Result modifiers for each Murthi type
MURTHI_MODIFIERS: Dict[str, float] = {
    "Swarna": 1.0,   # Full results (100%)
    "Rajata": 0.75,  # Three-quarters results (75%)
    "Taamra": 0.5,   # Half results (50%) - can also mean unfavorable
    "Loha": 0.25,    # Quarter results (25%) - highly unfavorable
}


def calculate_house_from_moon(natal_moon_sign: int, transit_moon_sign: int) -> int:
    """
    Calculate house position of transit Moon from natal Moon's sign.
    Signs are 1-12.
    
    Args:
        natal_moon_sign: Sign of natal Moon (1-12)
        transit_moon_sign: Sign of transit Moon (1-12)
    
    Returns:
        House number (1-12)
    """
    house = transit_moon_sign - natal_moon_sign + 1
    if house <= 0:
        house += 12
    return house


def get_murthi_for_transit(
    natal_moon_sign: int,
    moon_sign_at_planet_entry: int
) -> Dict[str, any]:
    """
    Determine the Murthi (form) of a planet's transit through a sign.
    
    This technique requires knowing where Moon was when the planet
    entered its current sign. The Moon's position relative to natal Moon
    determines the quality of the entire transit through that sign.
    
    Args:
        natal_moon_sign: Sign of natal Moon (1-12)
        moon_sign_at_planet_entry: Sign of Moon when planet entered current sign (1-12)
    
    Returns:
        Dict with murthi_type, moon_house_at_entry, result_quality
    
    Example:
        If natal Moon is in Pisces (12) and Moon was in Aquarius (11) when
        Jupiter entered Aries:
        House = 11 - 12 + 1 + 12 = 12 (Loha/Iron - Highly Unfavorable)
    """
    house = calculate_house_from_moon(natal_moon_sign, moon_sign_at_planet_entry)
    murthi_type = HOUSE_TO_MURTHI.get(house, "Unknown")
    
    result_quality = "Unknown"
    for murthi, (houses, quality) in MURTHI_DATA.items():
        if murthi == murthi_type:
            result_quality = quality
            break
    
    return {
        "murthi_type": murthi_type,
        "moon_house_at_entry": house,
        "result_quality": result_quality,
    }


def get_murthi_modifier(murthi_type: str) -> float:
    """
    Returns a modifier (0.0 to 1.0) for transit results based on Murthi.
    
    This modifier can be used to scale the intensity of predictions:
    - Swarna (1.0): Planet gives full results
    - Rajata (0.75): Planet gives 3/4 results
    - Taamra (0.5): Planet gives half results or mixed
    - Loha (0.25): Planet gives 1/4 results or negative
    
    Args:
        murthi_type: Type of Murthi
    
    Returns:
        Modifier value (0.25 to 1.0)
    """
    return MURTHI_MODIFIERS.get(murthi_type, 0.5)


def get_murthi_description(murthi_type: str) -> str:
    """
    Get a human-readable description of a Murthi type.
    
    Args:
        murthi_type: Type of Murthi
    
    Returns:
        Description string
    """
    descriptions = {
        "Swarna": "Golden Form (Swarna Murthi) - The planet bestows its full positive results. "
                  "This is the most auspicious form for transit.",
        "Rajata": "Silver Form (Rajata Murthi) - The planet gives good results, "
                  "approximately 3/4 of its potential.",
        "Taamra": "Copper Form (Taamra Murthi) - The planet's results are mixed or reduced. "
                  "Only about half the expected results manifest.",
        "Loha": "Iron Form (Loha Murthi) - The planet's positive results are severely restricted. "
                "Even favorable transits may not yield expected benefits.",
    }
    return descriptions.get(murthi_type, "Unknown Murthi type")
