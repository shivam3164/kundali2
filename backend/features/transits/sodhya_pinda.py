"""
Sodhya Pinda Transit Timing

From Vedic Astrology: An Integrated Approach
Chapter 25.6: Timing with Sodhya Pindas

Parasara taught techniques of timing events based on sodhya pindas.
The sodhya pinda multiplied by rekhas gives nakshatra/rasi triggers.

Key uses (from Table 61):
- Sun 9th house: Father
- Moon 4th house: Mother
- Mars 3rd house: Siblings
- Mercury 10th house: Profession
- Jupiter 5th house: Children
- Venus 7th house: Marriage
- Saturn 8th house: Longevity
"""
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass


@dataclass
class SodhyaTiming:
    """Timing result from Sodhya Pinda calculation"""
    planet: str
    house: int
    matter: str
    triggered_nakshatra: int
    triggered_nakshatra_name: str
    triggered_rasi: int
    triggered_rasi_name: str
    interpretation: str


# Nakshatra names (1-27)
NAKSHATRA_NAMES = [
    "", "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
    "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
    "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha",
    "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishtha",
    "Shatabhisha", "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

# Rasi names (1-12)
RASI_NAMES = [
    "", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

# Default sodhya pindas (can be calculated from actual BAV if available)
DEFAULT_SODHYA_PINDAS = {
    "Sun": 86,
    "Moon": 122,
    "Mars": 78,
    "Mercury": 152,
    "Jupiter": 112,
    "Venus": 125,
    "Saturn": 145,
}

# Timing matters from Table 61
SODHYA_MATTERS = {
    "Sun": {"house": 9, "matter": "Father"},
    "Moon": {"house": 4, "matter": "Mother"},
    "Mars": {"house": 3, "matter": "Siblings"},
    "Mercury": {"house": 10, "matter": "Profession"},
    "Jupiter": {"house": 5, "matter": "Children"},
    "Venus": {"house": 7, "matter": "Marriage"},
    "Saturn": {"house": 8, "matter": "Longevity"},
}

# Planet significations for area interpretation
PLANET_SIGNIFICATIONS = {
    "Sun": "soul, authority, government, health, father, willpower",
    "Moon": "mind, emotions, mother, peace, happiness, wisdom",
    "Mars": "siblings, land, strength, courage, accidents",
    "Mercury": "business, profession, friends, intelligence, commerce",
    "Jupiter": "body, learning, children, wealth, fortune",
    "Venus": "marriage, comforts, luxuries, vehicles, pleasures",
    "Saturn": "longevity, livelihood, fears, sadness, dangers",
}


def calculate_sodhya_timing(
    planet: str,
    natal_planet_sign: int,
    bav_rekhas: int,
    sodhya_pinda: Optional[int] = None,
) -> SodhyaTiming:
    """
    Calculate Sodhya Pinda timing for a planet.
    
    From Ch. 25.6:
    1. Take rekhas in house from planet in that planet's BAV
    2. Multiply by sodhya pinda
    3. Divide by 27 for nakshatra, by 12 for rasi
    4. Saturn transit in result = bad, Jupiter = good
    
    Args:
        planet: Planet name
        natal_planet_sign: Sign (1-12) where planet is placed in natal chart
        bav_rekhas: Number of rekhas in the relevant house from planet's BAV
        sodhya_pinda: Sodhya pinda value (uses default if not provided)
    
    Returns:
        SodhyaTiming with triggered nakshatra and rasi
    """
    if planet not in SODHYA_MATTERS:
        raise ValueError(f"No sodhya timing defined for {planet}")
    
    matter_info = SODHYA_MATTERS[planet]
    house = matter_info["house"]
    matter = matter_info["matter"]
    
    # Use default if not provided
    if sodhya_pinda is None:
        sodhya_pinda = DEFAULT_SODHYA_PINDAS.get(planet, 100)
    
    # Calculate product
    product = bav_rekhas * sodhya_pinda
    
    # Calculate nakshatra (divide by 27)
    if product == 0:
        nakshatra_num = 27  # 0 remainder = 27th nakshatra (Revati)
    else:
        nakshatra_num = product % 27
        if nakshatra_num == 0:
            nakshatra_num = 27
    
    # Calculate rasi (divide by 12)
    if product == 0:
        rasi_num = 12  # 0 remainder = 12th rasi (Pisces)
    else:
        rasi_num = product % 12
        if rasi_num == 0:
            rasi_num = 12
    
    nakshatra_name = NAKSHATRA_NAMES[nakshatra_num]
    rasi_name = RASI_NAMES[rasi_num]
    
    # Generate interpretation
    interpretation = (
        f"For {matter} matters, watch when Saturn transits {nakshatra_name} nakshatra "
        f"({rasi_name} rasi) - may bring challenges. "
        f"Jupiter transiting here brings benefits for {matter}."
    )
    
    return SodhyaTiming(
        planet=planet,
        house=house,
        matter=matter,
        triggered_nakshatra=nakshatra_num,
        triggered_nakshatra_name=nakshatra_name,
        triggered_rasi=rasi_num,
        triggered_rasi_name=rasi_name,
        interpretation=interpretation,
    )


def get_sodhya_timing_for_area(
    area: str,
    natal_positions: Dict[str, int],
    bav_data: Optional[Dict[str, List[int]]] = None,
) -> List[SodhyaTiming]:
    """
    Get sodhya timing relevant to a life area.
    
    Args:
        area: Life area (career, marriage, etc.)
        natal_positions: Dict of planet -> natal sign
        bav_data: Optional BAV data (uses defaults if not provided)
    
    Returns:
        List of relevant SodhyaTiming results
    """
    # Map areas to relevant planets
    area_planets = {
        "career": ["Mercury", "Sun", "Saturn"],
        "finance": ["Jupiter", "Venus", "Mercury"],
        "health": ["Sun", "Moon", "Mars"],
        "marriage": ["Venus", "Jupiter", "Moon"],
        "education": ["Jupiter", "Mercury", "Moon"],
        "children": ["Jupiter", "Venus", "Moon"],
        "family": ["Moon", "Jupiter", "Venus"],
        "travel": ["Moon", "Mercury", "Jupiter"],
        "property": ["Mars", "Venus", "Jupiter"],
        "spirituality": ["Jupiter", "Saturn", "Moon"],
    }
    
    relevant_planets = area_planets.get(area, ["Jupiter", "Saturn"])
    results = []
    
    for planet in relevant_planets:
        if planet not in SODHYA_MATTERS:
            continue
        
        natal_sign = natal_positions.get(planet, 1)
        
        # Get relevant house for this planet
        house_info = SODHYA_MATTERS[planet]
        relevant_house = house_info["house"]
        
        # Calculate which sign is the relevant house from natal position
        target_sign = ((natal_sign - 1 + relevant_house - 1) % 12) + 1
        
        # Get rekhas (use default of 4 if no BAV data)
        if bav_data and planet in bav_data:
            rekhas = bav_data[planet][target_sign - 1]  # 0-indexed
        else:
            rekhas = 4  # Default average
        
        timing = calculate_sodhya_timing(planet, natal_sign, rekhas)
        results.append(timing)
    
    return results


def check_current_sodhya_triggers(
    natal_positions: Dict[str, int],
    transit_saturn_nakshatra: int,
    transit_jupiter_nakshatra: int,
) -> Dict[str, List[str]]:
    """
    Check if any sodhya pinda nakshatras are currently triggered.
    
    Returns dict with:
    - "saturn_triggers": Matters where Saturn is in trigger nakshatra
    - "jupiter_triggers": Matters where Jupiter is in trigger nakshatra
    """
    triggers = {"saturn_triggers": [], "jupiter_triggers": []}
    
    for planet, info in SODHYA_MATTERS.items():
        natal_sign = natal_positions.get(planet, 1)
        
        # Use default calculation with average rekhas
        timing = calculate_sodhya_timing(planet, natal_sign, 4)
        
        # Check if Saturn is in the trigger nakshatra (or 10th/19th from it)
        # As per textbook: same planet owns 1st, 10th, 19th nakshatras
        trigger_nakshatras = [
            timing.triggered_nakshatra,
            ((timing.triggered_nakshatra - 1 + 9) % 27) + 1,  # 10th
            ((timing.triggered_nakshatra - 1 + 18) % 27) + 1,  # 19th
        ]
        
        if transit_saturn_nakshatra in trigger_nakshatras:
            triggers["saturn_triggers"].append(
                f"{info['matter']} (Saturn in {NAKSHATRA_NAMES[transit_saturn_nakshatra]})"
            )
        
        if transit_jupiter_nakshatra in trigger_nakshatras:
            triggers["jupiter_triggers"].append(
                f"{info['matter']} (Jupiter in {NAKSHATRA_NAMES[transit_jupiter_nakshatra]})"
            )
    
    return triggers


def get_timing_advice(area: str, natal_positions: Dict[str, int]) -> str:
    """
    Get timing advice for a life area based on Sodhya Pinda.
    
    Args:
        area: Life area
        natal_positions: Planet positions
    
    Returns:
        Advice string
    """
    timings = get_sodhya_timing_for_area(area, natal_positions)
    
    if not timings:
        return "No specific timing triggers found for this area."
    
    advice_parts = [f"Timing considerations for {area}:"]
    
    for timing in timings[:2]:  # Limit to 2 main factors
        advice_parts.append(
            f"• {timing.matter}: Watch Saturn's transit through {timing.triggered_nakshatra_name}. "
            f"Jupiter here brings opportunities."
        )
    
    return " ".join(advice_parts)
