"""
Tara (Star/Nakshatra) Analysis Module.
Source: Vedic Astrology: An Integrated Approach, Section 26.4, Table 64

The relationship between transit nakshatra and birth nakshatra determines
the "Tara Bala" (star strength) of a transit.

The 27 nakshatras are divided into 9 groups of 3 (cycles).
Each cycle position has a specific quality.
"""
from typing import Dict, Tuple, Optional

# Tara classifications with their qualities
# Format: { cycle_position: (tara_name, quality) }
TARA_DATA: Dict[int, Tuple[str, str]] = {
    1: ("Janma", "Mixed"),        # Birth star - Mixed results (body-related)
    2: ("Sampat", "Good"),        # Wealth star - Favorable
    3: ("Vipat", "Bad"),          # Danger star - Unfavorable
    4: ("Kshema", "Good"),        # Well-being star - Favorable
    5: ("Pratyak", "Bad"),        # Obstacles star - Unfavorable
    6: ("Saadhana", "Good"),      # Achievement star - Favorable
    7: ("Naidhana", "Bad"),       # Death/Transformation - Unfavorable
    8: ("Mitra", "Good"),         # Friend star - Favorable
    9: ("Parama Mitra", "Good"),  # Best friend star - Most Favorable
}

# Special Nakshatras relative to Janma Nakshatra
# These have additional significance beyond the basic Tara cycle
SPECIAL_NAKSHATRAS: Dict[int, Tuple[str, str]] = {
    1: ("Janma", "General well-being, body, physical health"),
    10: ("Karma", "Profession, workplace, career matters"),
    16: ("Sanghaatika", "Group/social activities, associations"),
    18: ("Saamudaayika", "Community activities, public life"),
    4: ("Jaati", "Community, class, caste, professional group"),
}

# Favorable and unfavorable Taras for quick lookup
FAVORABLE_TARAS = ["Sampat", "Kshema", "Saadhana", "Mitra", "Parama Mitra"]
UNFAVORABLE_TARAS = ["Vipat", "Pratyak", "Naidhana"]


def calculate_nakshatra_distance(birth_nakshatra: int, transit_nakshatra: int) -> int:
    """
    Calculate distance from birth nakshatra to transit nakshatra.
    Both values should be 1-27.
    
    Args:
        birth_nakshatra: Nakshatra of natal Moon (1-27)
        transit_nakshatra: Nakshatra of transiting planet (1-27)
    
    Returns:
        Distance (1-27)
    """
    if not (1 <= birth_nakshatra <= 27 and 1 <= transit_nakshatra <= 27):
        raise ValueError("Nakshatra indices must be between 1 and 27")
    
    distance = transit_nakshatra - birth_nakshatra + 1
    if distance <= 0:
        distance += 27
    return distance


def get_tara_cycle_position(distance: int) -> int:
    """
    Convert nakshatra distance (1-27) to Tara cycle position (1-9).
    
    The 27 nakshatras map to 3 cycles of 9:
    - 1-9: First cycle
    - 10-18: Second cycle  
    - 19-27: Third cycle
    
    Args:
        distance: Nakshatra distance (1-27)
    
    Returns:
        Cycle position (1-9)
    """
    cycle_pos = distance % 9
    return 9 if cycle_pos == 0 else cycle_pos


def calculate_tara(
    birth_nakshatra: int, 
    transit_nakshatra: int
) -> Dict[str, any]:
    """
    Calculate the Tara (star strength) for a transit.
    
    Args:
        birth_nakshatra: Nakshatra of natal Moon (1-27)
        transit_nakshatra: Nakshatra of transiting planet (1-27)
    
    Returns:
        Dict with tara_name, tara_quality, nakshatra_distance, special_nakshatra
    
    Example:
        If birth nakshatra is 26 (Uttarabhadrapada) and transit is 1 (Ashwini):
        Distance = 1 - 26 + 1 + 27 = 3
        Cycle position = 3
        Tara = Vipat (Danger) - Bad
    """
    distance = calculate_nakshatra_distance(birth_nakshatra, transit_nakshatra)
    cycle_pos = get_tara_cycle_position(distance)
    
    tara_name, tara_quality = TARA_DATA[cycle_pos]
    
    # Check for special nakshatras
    special = SPECIAL_NAKSHATRAS.get(distance)
    
    return {
        "tara_name": tara_name,
        "tara_quality": tara_quality,
        "nakshatra_distance": distance,
        "cycle_position": cycle_pos,
        "special_nakshatra": special[0] if special else None,
        "special_meaning": special[1] if special else None,
    }


def is_favorable_tara(tara_name: str) -> bool:
    """
    Check if a Tara is favorable for transit.
    
    Args:
        tara_name: Name of the Tara
    
    Returns:
        True if favorable, False otherwise
    """
    return tara_name in FAVORABLE_TARAS


def get_tara_strength_score(tara_name: str) -> int:
    """
    Get a numerical strength score for a Tara (for sorting/comparison).
    
    Returns:
        Score from -2 (worst) to +2 (best)
    """
    scores = {
        "Parama Mitra": 2,
        "Mitra": 1,
        "Sampat": 1,
        "Kshema": 1,
        "Saadhana": 1,
        "Janma": 0,
        "Vipat": -1,
        "Pratyak": -1,
        "Naidhana": -2,
    }
    return scores.get(tara_name, 0)
