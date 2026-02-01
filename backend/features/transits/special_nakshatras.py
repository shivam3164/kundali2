"""
Special Nakshatras Module - Transit Analysis Enhancement

From Vedic Astrology: An Integrated Approach (P.V.R. Narasimha Rao)
Section 26.4 - Special Nakshatras

These special nakshatras are counted from Janma Nakshatra (birth star) and
show different areas of life. Transits through these nakshatras activate
specific life areas.
"""
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class NakshatraQuality(str, Enum):
    """Quality of special nakshatra for predictions"""
    HIGHLY_SENSITIVE = "Highly Sensitive"  # Janma, Naidhana, Vainasika
    SENSITIVE = "Sensitive"  # Vipat, Pratyak
    FAVORABLE = "Favorable"  # Sampat, Kshema, Saadhana
    POWERFUL = "Powerful"  # Abhisheka, Karma
    NEUTRAL = "Neutral"


@dataclass
class SpecialNakshatraInfo:
    """Information about a special nakshatra"""
    name: str
    sanskrit_name: str
    offset: int  # Counted from janma nakshatra
    meaning: str
    life_area: str
    quality: NakshatraQuality
    benefic_transit: str  # Effect when benefic transits
    malefic_transit: str  # Effect when malefic transits


# Complete definition of special nakshatras from the textbook
SPECIAL_NAKSHATRAS: Dict[str, SpecialNakshatraInfo] = {
    "janma": SpecialNakshatraInfo(
        name="Janma",
        sanskrit_name="जन्म",
        offset=1,
        meaning="Birth",
        life_area="Self, body, physical constitution, overall well-being",
        quality=NakshatraQuality.HIGHLY_SENSITIVE,
        benefic_transit="Health improvement, vitality, self-confidence, new beginnings",
        malefic_transit="Health issues, physical discomfort, ego conflicts, identity crisis"
    ),
    
    "sampat": SpecialNakshatraInfo(
        name="Sampat",
        sanskrit_name="सम्पत्",
        offset=2,
        meaning="Wealth",
        life_area="Prosperity, financial matters, material gains",
        quality=NakshatraQuality.FAVORABLE,
        benefic_transit="Financial gains, prosperity, material comforts",
        malefic_transit="Financial concerns, but generally mitigated"
    ),
    
    "vipat": SpecialNakshatraInfo(
        name="Vipat",
        sanskrit_name="विपत्",
        offset=3,
        meaning="Danger",
        life_area="Risks, obstacles, challenges, dangers",
        quality=NakshatraQuality.SENSITIVE,
        benefic_transit="Challenges that lead to growth, manageable risks",
        malefic_transit="Dangers, accidents, obstacles, health risks"
    ),
    
    "kshema": SpecialNakshatraInfo(
        name="Kshema",
        sanskrit_name="क्षेम",
        offset=4,
        meaning="Well-being",
        life_area="Safety, security, comfort, peace of mind",
        quality=NakshatraQuality.FAVORABLE,
        benefic_transit="Safety, comfort, peaceful times, security",
        malefic_transit="Minor disturbances in peace, generally protected"
    ),
    
    "pratyak": SpecialNakshatraInfo(
        name="Pratyak",
        sanskrit_name="प्रत्यक्",
        offset=5,
        meaning="Obstacles",
        life_area="Opposition, hindrances, delays, blocks",
        quality=NakshatraQuality.SENSITIVE,
        benefic_transit="Delays that eventually benefit, patience rewarded",
        malefic_transit="Strong opposition, obstacles in path, delays"
    ),
    
    "saadhana": SpecialNakshatraInfo(
        name="Saadhana",
        sanskrit_name="साधना",
        offset=6,
        meaning="Achievement",
        life_area="Efforts, practices, accomplishments through work",
        quality=NakshatraQuality.FAVORABLE,
        benefic_transit="Success through efforts, achievements, fulfillment",
        malefic_transit="Hard work required, results may be delayed"
    ),
    
    "naidhana": SpecialNakshatraInfo(
        name="Naidhana",
        sanskrit_name="नैधन",
        offset=7,
        meaning="Death",
        life_area="Endings, death, suffering, transformation",
        quality=NakshatraQuality.HIGHLY_SENSITIVE,
        benefic_transit="Transformation, spiritual growth, endings that lead to new beginnings",
        malefic_transit="Danger to life, severe suffering, critical health issues"
    ),
    
    "mitra": SpecialNakshatraInfo(
        name="Mitra",
        sanskrit_name="मित्र",
        offset=8,
        meaning="Friend",
        life_area="Friends, allies, helpful people, support",
        quality=NakshatraQuality.FAVORABLE,
        benefic_transit="Support from friends, beneficial relationships, help arrives",
        malefic_transit="Issues with friends, but support available"
    ),
    
    "parama_mitra": SpecialNakshatraInfo(
        name="Parama Mitra",
        sanskrit_name="परम मित्र",
        offset=9,
        meaning="Best Friend",
        life_area="Close allies, strongest supporters, deep friendships",
        quality=NakshatraQuality.FAVORABLE,
        benefic_transit="Strong support, best friends help, deep connections",
        malefic_transit="Minor friction with close ones, but bond remains"
    ),
    
    # Extended special nakshatras from Section 26.4
    "jaati": SpecialNakshatraInfo(
        name="Jaati",
        sanskrit_name="जाति",
        offset=4,
        meaning="Community",
        life_area="One's community, social circle, caste/class relations",
        quality=NakshatraQuality.NEUTRAL,
        benefic_transit="Good relations with community, social harmony",
        malefic_transit="Alienation from community, social conflicts"
    ),
    
    "karma": SpecialNakshatraInfo(
        name="Karma",
        sanskrit_name="कर्म",
        offset=10,
        meaning="Profession",
        life_area="Career, work, professional achievements, duties",
        quality=NakshatraQuality.POWERFUL,
        benefic_transit="Career success, professional recognition, work achievements",
        malefic_transit="Career challenges, work-related tensions, professional setbacks"
    ),
    
    "desa": SpecialNakshatraInfo(
        name="Desa",
        sanskrit_name="देश",
        offset=12,
        meaning="Country",
        life_area="Homeland, country, place of residence, relocation",
        quality=NakshatraQuality.NEUTRAL,
        benefic_transit="Good relations with homeland, favorable for place matters",
        malefic_transit="May be driven away from country, issues with place of residence"
    ),
    
    "abhisheka": SpecialNakshatraInfo(
        name="Abhisheka",
        sanskrit_name="अभिषेक",
        offset=13,
        meaning="Coronation",
        life_area="Power, authority, leadership, recognition",
        quality=NakshatraQuality.POWERFUL,
        benefic_transit="Rise to power, authority gained, leadership roles, honors",
        malefic_transit="Power struggles, authority challenged, but potential for rise"
    ),
    
    "aadhaana": SpecialNakshatraInfo(
        name="Aadhaana",
        sanskrit_name="आधान",
        offset=19,
        meaning="Conception/Epoch",
        life_area="Family well-being, conception, family growth",
        quality=NakshatraQuality.NEUTRAL,
        benefic_transit="Family prosperity, conception possible, family harmony",
        malefic_transit="Family concerns, issues with family growth"
    ),
    
    "vainasika": SpecialNakshatraInfo(
        name="Vainasika",
        sanskrit_name="वैनासिक",
        offset=22,
        meaning="Destruction",
        life_area="One's destruction, severe losses, downfall",
        quality=NakshatraQuality.HIGHLY_SENSITIVE,
        benefic_transit="Transformation, destroying old patterns, rebirth",
        malefic_transit="Severe losses, destruction, major downfall"
    ),
    
    "maanasa": SpecialNakshatraInfo(
        name="Maanasa",
        sanskrit_name="मानस",
        offset=25,
        meaning="Mind",
        life_area="Mental state, psychology, thoughts, mental well-being",
        quality=NakshatraQuality.NEUTRAL,
        benefic_transit="Mental peace, clarity of thought, psychological well-being",
        malefic_transit="Mental disturbances, anxiety, psychological challenges"
    ),
}

# List of 27 nakshatras in order
NAKSHATRA_LIST = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
    "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
    "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha",
    "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishtha",
    "Shatabhisha", "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

# Natural benefics and malefics
NATURAL_BENEFICS = ["Jupiter", "Venus", "Mercury", "Moon"]
NATURAL_MALEFICS = ["Sun", "Mars", "Saturn", "Rahu", "Ketu"]


def get_nakshatra_index(nakshatra_name: str) -> int:
    """Get 1-based index of nakshatra from name"""
    try:
        return NAKSHATRA_LIST.index(nakshatra_name) + 1
    except ValueError:
        # Try partial match
        for i, nak in enumerate(NAKSHATRA_LIST):
            if nakshatra_name.lower() in nak.lower() or nak.lower() in nakshatra_name.lower():
                return i + 1
        return 0


def calculate_special_nakshatra(
    janma_nakshatra: int,
    special_type: str
) -> int:
    """
    Calculate which nakshatra is the special nakshatra for a given birth star.
    
    Args:
        janma_nakshatra: Birth nakshatra index (1-27)
        special_type: Type of special nakshatra (e.g., "karma", "naidhana")
    
    Returns:
        Nakshatra index (1-27) that is the special nakshatra
    """
    if special_type not in SPECIAL_NAKSHATRAS:
        return 0
    
    offset = SPECIAL_NAKSHATRAS[special_type].offset
    special_nak = ((janma_nakshatra - 1) + (offset - 1)) % 27 + 1
    return special_nak


def get_special_nakshatra_name(nakshatra_index: int) -> str:
    """Get nakshatra name from index (1-27)"""
    if 1 <= nakshatra_index <= 27:
        return NAKSHATRA_LIST[nakshatra_index - 1]
    return "Unknown"


def identify_special_nakshatra_for_transit(
    janma_nakshatra: int,
    transit_nakshatra: int
) -> Optional[Tuple[str, SpecialNakshatraInfo]]:
    """
    Identify if a transit nakshatra is a special nakshatra for the native.
    
    Args:
        janma_nakshatra: Birth nakshatra index (1-27)
        transit_nakshatra: Transit nakshatra index (1-27)
    
    Returns:
        Tuple of (special_type, info) if transit is in a special nakshatra, else None
    """
    for special_type, info in SPECIAL_NAKSHATRAS.items():
        special_nak = calculate_special_nakshatra(janma_nakshatra, special_type)
        if special_nak == transit_nakshatra:
            return (special_type, info)
    return None


def analyze_transit_in_special_nakshatra(
    janma_nakshatra: int,
    transit_nakshatra: int,
    planet: str
) -> Dict:
    """
    Analyze a planet's transit through special nakshatras.
    
    Args:
        janma_nakshatra: Birth nakshatra index (1-27)
        transit_nakshatra: Transit nakshatra index (1-27)
        planet: Planet name
    
    Returns:
        Analysis result with special nakshatra effects
    """
    result = {
        "is_special_nakshatra": False,
        "special_type": None,
        "special_name": None,
        "life_area": None,
        "quality": None,
        "transit_effect": None,
        "interpretation": None
    }
    
    special = identify_special_nakshatra_for_transit(janma_nakshatra, transit_nakshatra)
    
    if special:
        special_type, info = special
        is_benefic = planet in NATURAL_BENEFICS
        
        result["is_special_nakshatra"] = True
        result["special_type"] = special_type
        result["special_name"] = info.name
        result["life_area"] = info.life_area
        result["quality"] = info.quality.value
        result["transit_effect"] = info.benefic_transit if is_benefic else info.malefic_transit
        
        # Generate interpretation
        planet_nature = "benefic" if is_benefic else "malefic"
        result["interpretation"] = (
            f"{planet} (a natural {planet_nature}) is transiting through your "
            f"{info.name} nakshatra ({info.meaning}). This affects: {info.life_area}. "
            f"Effect: {result['transit_effect']}"
        )
    
    return result


def get_all_special_nakshatras_for_native(janma_nakshatra: int) -> Dict[str, Dict]:
    """
    Get all special nakshatras for a native based on their birth star.
    
    Args:
        janma_nakshatra: Birth nakshatra index (1-27)
    
    Returns:
        Dictionary of all special nakshatras with their positions
    """
    result = {}
    
    for special_type, info in SPECIAL_NAKSHATRAS.items():
        special_nak = calculate_special_nakshatra(janma_nakshatra, special_type)
        result[special_type] = {
            "name": info.name,
            "nakshatra_index": special_nak,
            "nakshatra_name": get_special_nakshatra_name(special_nak),
            "meaning": info.meaning,
            "life_area": info.life_area,
            "quality": info.quality.value
        }
    
    return result


def check_planets_in_special_nakshatras(
    janma_nakshatra: int,
    planet_nakshatras: Dict[str, int]
) -> List[Dict]:
    """
    Check which planets are in special nakshatras and their effects.
    
    Args:
        janma_nakshatra: Birth nakshatra index (1-27)
        planet_nakshatras: Dict of planet name to nakshatra index
    
    Returns:
        List of special nakshatra transits with effects
    """
    results = []
    
    for planet, transit_nak in planet_nakshatras.items():
        analysis = analyze_transit_in_special_nakshatra(
            janma_nakshatra, transit_nak, planet
        )
        if analysis["is_special_nakshatra"]:
            analysis["planet"] = planet
            analysis["transit_nakshatra"] = get_special_nakshatra_name(transit_nak)
            results.append(analysis)
    
    return results


# Key special nakshatras for specific life areas (for area-based queries)
AREA_TO_SPECIAL_NAKSHATRA = {
    "career": "karma",
    "job": "karma",
    "work": "karma",
    "profession": "karma",
    "power": "abhisheka",
    "authority": "abhisheka",
    "leadership": "abhisheka",
    "health": "janma",
    "body": "janma",
    "self": "janma",
    "wealth": "sampat",
    "money": "sampat",
    "finance": "sampat",
    "danger": "vipat",
    "risk": "vipat",
    "obstacles": "pratyak",
    "delays": "pratyak",
    "death": "naidhana",
    "ending": "naidhana",
    "transformation": "vainasika",
    "destruction": "vainasika",
    "family": "aadhaana",
    "children": "aadhaana",
    "mind": "maanasa",
    "mental": "maanasa",
    "psychology": "maanasa",
    "community": "jaati",
    "social": "jaati",
    "country": "desa",
    "relocation": "desa",
    "abroad": "desa",
    "friends": "mitra",
    "support": "parama_mitra",
    "safety": "kshema",
    "peace": "kshema",
    "achievement": "saadhana",
    "success": "saadhana",
}


def get_special_nakshatra_for_area(area: str) -> Optional[str]:
    """Get the relevant special nakshatra for a life area query"""
    area_lower = area.lower()
    return AREA_TO_SPECIAL_NAKSHATRA.get(area_lower)
