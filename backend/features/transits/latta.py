"""
Latta (Planetary Kicks) Module - Transit Analysis Enhancement

From Vedic Astrology: An Integrated Approach (P.V.R. Narasimha Rao)
Section 26.7 - Latta (Kick)

Latta is a nakshatra-based planetary kick. Each planet has latta (kick) on a
constellation based on its transit position. If a transit planet has latta on 
the constellation occupied by Moon (or lagna) in natal chart, then we may expect 
some unfavorable results related to the signification of the planet in natal chart.
"""
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class LattaDirection(str, Enum):
    """Direction of planetary kick"""
    FORWARD = "forward"   # Purolatta - forward kick
    BACKWARD = "backward"  # Prishtha latta - backward kick


@dataclass
class LattaRule:
    """Rule for planetary kick calculation"""
    planet: str
    offset: int
    direction: LattaDirection
    description: str


# Latta rules from Section 26.7
LATTA_RULES: Dict[str, LattaRule] = {
    # Forward kicks (Purolatta)
    "Sun": LattaRule(
        planet="Sun",
        offset=12,
        direction=LattaDirection.FORWARD,
        description="Sun has latta on the 12th nakshatra forward from him"
    ),
    "Mars": LattaRule(
        planet="Mars",
        offset=3,
        direction=LattaDirection.FORWARD,
        description="Mars has latta on the 3rd nakshatra forward from him"
    ),
    "Jupiter": LattaRule(
        planet="Jupiter",
        offset=6,
        direction=LattaDirection.FORWARD,
        description="Jupiter has latta on the 6th nakshatra forward from him"
    ),
    "Saturn": LattaRule(
        planet="Saturn",
        offset=8,
        direction=LattaDirection.FORWARD,
        description="Saturn has latta on the 8th nakshatra forward from him"
    ),
    
    # Backward kicks (Prishtha Latta)
    "Moon": LattaRule(
        planet="Moon",
        offset=22,
        direction=LattaDirection.BACKWARD,
        description="Moon has latta on the 22nd nakshatra backward from her"
    ),
    "Mercury": LattaRule(
        planet="Mercury",
        offset=7,
        direction=LattaDirection.BACKWARD,
        description="Mercury has latta on the 7th nakshatra backward from him"
    ),
    "Venus": LattaRule(
        planet="Venus",
        offset=5,
        direction=LattaDirection.BACKWARD,
        description="Venus has latta on the 5th nakshatra backward from him"
    ),
    "Rahu": LattaRule(
        planet="Rahu",
        offset=9,
        direction=LattaDirection.BACKWARD,
        description="Rahu has latta on the 9th nakshatra backward from him"
    ),
}

# Nakshatra list for reference
NAKSHATRA_LIST = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
    "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
    "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha",
    "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishtha",
    "Shatabhisha", "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]


def get_nakshatra_name(index: int) -> str:
    """Get nakshatra name from 1-based index"""
    if 1 <= index <= 27:
        return NAKSHATRA_LIST[index - 1]
    return "Unknown"


def get_nakshatra_index(name: str) -> int:
    """Get 1-based index from nakshatra name"""
    try:
        return NAKSHATRA_LIST.index(name) + 1
    except ValueError:
        for i, nak in enumerate(NAKSHATRA_LIST):
            if name.lower() in nak.lower() or nak.lower() in name.lower():
                return i + 1
        return 0


def calculate_latta_nakshatra(planet: str, transit_nakshatra: int) -> Optional[int]:
    """
    Calculate which nakshatra a planet has latta (kick) on.
    
    Args:
        planet: Planet name
        transit_nakshatra: Current nakshatra of the planet (1-27)
    
    Returns:
        Nakshatra index (1-27) that has latta from this planet, or None if no rule
    """
    if planet not in LATTA_RULES:
        return None
    
    rule = LATTA_RULES[planet]
    
    if rule.direction == LattaDirection.FORWARD:
        # Forward kick: count forward from transit position
        latta_nak = ((transit_nakshatra - 1) + (rule.offset - 1)) % 27 + 1
    else:
        # Backward kick: count backward from transit position
        latta_nak = ((transit_nakshatra - 1) - (rule.offset - 1)) % 27 + 1
    
    return latta_nak


def check_latta_on_nakshatra(
    target_nakshatra: int,
    planet_nakshatras: Dict[str, int]
) -> List[Dict]:
    """
    Check which planets have latta (kick) on a target nakshatra.
    
    Args:
        target_nakshatra: The nakshatra to check for latta (e.g., janma nakshatra)
        planet_nakshatras: Dict of planet name to their current nakshatra
    
    Returns:
        List of planets having latta on the target nakshatra
    """
    latta_results = []
    
    for planet, transit_nak in planet_nakshatras.items():
        if planet == "Ketu":
            continue  # Ketu doesn't have latta rule
        
        latta_nak = calculate_latta_nakshatra(planet, transit_nak)
        
        if latta_nak == target_nakshatra:
            rule = LATTA_RULES.get(planet)
            latta_results.append({
                "planet": planet,
                "transit_nakshatra": get_nakshatra_name(transit_nak),
                "transit_nakshatra_index": transit_nak,
                "latta_on": get_nakshatra_name(target_nakshatra),
                "direction": rule.direction.value if rule else None,
                "offset": rule.offset if rule else None,
            })
    
    return latta_results


def analyze_latta_effects(
    janma_nakshatra: int,
    lagna_nakshatra: int,
    planet_nakshatras: Dict[str, int],
    natal_house_lords: Dict[str, int] = None
) -> Dict:
    """
    Comprehensive latta analysis for a native.
    
    Args:
        janma_nakshatra: Birth star nakshatra (1-27)
        lagna_nakshatra: Lagna nakshatra (1-27)
        planet_nakshatras: Dict of planet name to their current transit nakshatra
        natal_house_lords: Dict of planet to house they lord in natal chart
    
    Returns:
        Complete latta analysis with effects
    """
    result = {
        "latta_on_janma": [],
        "latta_on_lagna": [],
        "overall_latta_count": 0,
        "severity": "None",
        "affected_areas": [],
        "interpretation": ""
    }
    
    # Check latta on janma nakshatra (more important)
    janma_lattas = check_latta_on_nakshatra(janma_nakshatra, planet_nakshatras)
    result["latta_on_janma"] = janma_lattas
    
    # Check latta on lagna nakshatra
    lagna_lattas = check_latta_on_nakshatra(lagna_nakshatra, planet_nakshatras)
    result["latta_on_lagna"] = lagna_lattas
    
    total_lattas = len(janma_lattas) + len(lagna_lattas)
    result["overall_latta_count"] = total_lattas
    
    # Determine severity
    if total_lattas == 0:
        result["severity"] = "None"
        result["interpretation"] = "No planetary kicks active. Period is relatively smooth."
    elif total_lattas == 1:
        result["severity"] = "Mild"
        result["interpretation"] = "One planetary kick active. Minor challenges possible."
    elif total_lattas == 2:
        result["severity"] = "Moderate"
        result["interpretation"] = "Multiple planetary kicks active. Exercise caution."
    else:
        result["severity"] = "Significant"
        result["interpretation"] = "Several planetary kicks active. Period requires careful handling."
    
    # Identify affected areas based on planets
    affected_areas = set()
    
    planet_significations = {
        "Sun": ["authority", "father", "career", "health", "government"],
        "Moon": ["mind", "mother", "emotions", "public image"],
        "Mars": ["siblings", "courage", "property", "accidents", "litigation"],
        "Mercury": ["communication", "business", "education", "skin"],
        "Jupiter": ["wisdom", "children", "fortune", "teachers", "legal matters"],
        "Venus": ["marriage", "relationships", "vehicles", "arts", "luxury"],
        "Saturn": ["longevity", "career", "delays", "chronic issues", "servants"],
        "Rahu": ["foreign matters", "unconventional", "sudden events", "technology"],
    }
    
    for latta in janma_lattas + lagna_lattas:
        planet = latta["planet"]
        if planet in planet_significations:
            affected_areas.update(planet_significations[planet])
    
    result["affected_areas"] = list(affected_areas)
    
    # Add detailed interpretation for each latta
    for latta in janma_lattas:
        planet = latta["planet"]
        latta["effect"] = f"{planet}'s kick on birth star may cause setbacks in {planet}'s significations"
        latta["importance"] = "High (on Janma Nakshatra)"
        
        if natal_house_lords and planet in natal_house_lords:
            house = natal_house_lords[planet]
            latta["house_effect"] = f"As lord of house {house}, may affect that house's matters"
    
    for latta in lagna_lattas:
        planet = latta["planet"]
        latta["effect"] = f"{planet}'s kick on lagna star may cause challenges in {planet}'s significations"
        latta["importance"] = "Medium (on Lagna Nakshatra)"
    
    return result


def get_latta_for_all_planets(planet_nakshatras: Dict[str, int]) -> Dict[str, Dict]:
    """
    Get the latta (kick) target for all planets.
    
    Args:
        planet_nakshatras: Dict of planet name to their current nakshatra
    
    Returns:
        Dict of planet to their latta target
    """
    result = {}
    
    for planet, transit_nak in planet_nakshatras.items():
        if planet == "Ketu":
            continue
        
        latta_nak = calculate_latta_nakshatra(planet, transit_nak)
        
        if latta_nak:
            rule = LATTA_RULES.get(planet)
            result[planet] = {
                "transit_nakshatra": get_nakshatra_name(transit_nak),
                "latta_on_nakshatra": get_nakshatra_name(latta_nak),
                "latta_nakshatra_index": latta_nak,
                "direction": rule.direction.value if rule else None,
                "description": rule.description if rule else None,
            }
    
    return result


# House significations for latta effect interpretation
HOUSE_SIGNIFICATIONS = {
    1: "self, body, personality, health",
    2: "wealth, family, speech, food",
    3: "siblings, courage, communication, short travels",
    4: "mother, home, vehicles, education, peace of mind",
    5: "children, intelligence, creativity, romance, speculation",
    6: "enemies, diseases, debts, service, litigation",
    7: "spouse, partnerships, business, foreign travel",
    8: "longevity, obstacles, inheritance, occult, transformation",
    9: "father, fortune, dharma, higher education, long journeys",
    10: "career, profession, status, authority, government",
    11: "gains, income, elder siblings, friends, aspirations",
    12: "losses, expenses, foreign residence, moksha, hospitals",
}


def interpret_latta_by_house_lord(planet: str, house: int) -> str:
    """Generate interpretation when a house lord has latta on natal nakshatra"""
    signif = HOUSE_SIGNIFICATIONS.get(house, "")
    return (
        f"{planet} (lord of house {house}) has latta on your birth star. "
        f"This may cause challenges related to: {signif}. "
        f"Be cautious in these areas during this transit."
    )
