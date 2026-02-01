"""
Chara Karaka (Variable Significators) Module

From Vedic Astrology: An Integrated Approach (P.V.R. Narasimha Rao)
Chapter 8.2 - Chara Karakas (Variable Significators)

Chara Karakas are computed based on planetary longitudes in the natal chart.
The planet with highest longitude becomes Atma Karaka (AK), and others follow.

The 8 Chara Karakas:
1. AK (Atma Karaka) - Soul significator - Self, soul's purpose
2. AmK (Amatya Karaka) - Minister - Career, profession
3. BK (Bhratri Karaka) - Siblings significator
4. MK (Matri Karaka) - Mother significator  
5. PiK (Pitri Karaka) - Father significator
6. PK (Putra Karaka) - Children significator
7. GK (Gnati Karaka) - Relatives/enemies significator
8. DK (Dara Karaka) - Spouse significator
"""
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class CharaKarakaType(str, Enum):
    """Types of Chara Karakas"""
    AK = "AK"   # Atma Karaka - Soul
    AMK = "AmK"  # Amatya Karaka - Minister/Career
    BK = "BK"   # Bhratri Karaka - Siblings
    MK = "MK"   # Matri Karaka - Mother
    PIK = "PiK"  # Pitri Karaka - Father
    PK = "PK"   # Putra Karaka - Children
    GK = "GK"   # Gnati Karaka - Relatives/Enemies
    DK = "DK"   # Dara Karaka - Spouse


@dataclass
class CharaKaraka:
    """Chara Karaka information"""
    karaka_type: CharaKarakaType
    planet: str
    longitude_in_sign: float  # Degree within sign (0-30)
    full_longitude: float
    significance: str
    areas_governed: List[str]


# Chara Karaka significations
KARAKA_SIGNIFICATIONS = {
    CharaKarakaType.AK: {
        "name": "Atma Karaka",
        "meaning": "Soul Significator",
        "significance": "Represents the soul, self, and life purpose. The most important karaka.",
        "areas": ["self", "soul purpose", "spiritual growth", "desires", "ego"],
    },
    CharaKarakaType.AMK: {
        "name": "Amatya Karaka", 
        "meaning": "Minister Significator",
        "significance": "Represents career, profession, and the person who advises/helps the native.",
        "areas": ["career", "profession", "advisors", "ministers", "mentors"],
    },
    CharaKarakaType.BK: {
        "name": "Bhratri Karaka",
        "meaning": "Siblings Significator",
        "significance": "Represents siblings, courage, and younger co-borns.",
        "areas": ["siblings", "courage", "initiative", "younger siblings"],
    },
    CharaKarakaType.MK: {
        "name": "Matri Karaka",
        "meaning": "Mother Significator",
        "significance": "Represents mother, nurturing, and maternal figures.",
        "areas": ["mother", "nurturing", "home", "property", "education"],
    },
    CharaKarakaType.PIK: {
        "name": "Pitri Karaka",
        "meaning": "Father Significator",
        "significance": "Represents father, fortune, and paternal figures.",
        "areas": ["father", "fortune", "dharma", "guru", "higher education"],
    },
    CharaKarakaType.PK: {
        "name": "Putra Karaka",
        "meaning": "Children Significator",
        "significance": "Represents children, intelligence, and creative expression.",
        "areas": ["children", "intelligence", "creativity", "romance", "speculation"],
    },
    CharaKarakaType.GK: {
        "name": "Gnati Karaka",
        "meaning": "Relatives/Enemies Significator",
        "significance": "Represents relatives, enemies, obstacles, and competition.",
        "areas": ["relatives", "enemies", "obstacles", "diseases", "competition"],
    },
    CharaKarakaType.DK: {
        "name": "Dara Karaka",
        "meaning": "Spouse Significator",
        "significance": "Represents spouse, partnerships, and marriage.",
        "areas": ["spouse", "marriage", "partnerships", "relationships", "business partners"],
    },
}

# Planets considered for Chara Karaka (7-planet scheme, excluding Rahu)
# Note: Some use 8-planet scheme including Rahu
KARAKA_PLANETS = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]

# Karaka order (by descending longitude in sign)
KARAKA_ORDER = [
    CharaKarakaType.AK,
    CharaKarakaType.AMK,
    CharaKarakaType.BK,
    CharaKarakaType.MK,
    CharaKarakaType.PIK,
    CharaKarakaType.PK,
    CharaKarakaType.GK,
    CharaKarakaType.DK,
]


def get_longitude_in_sign(longitude: float) -> float:
    """
    Get the degree within the sign (0-30).
    
    For Chara Karaka, we only consider the position within the sign,
    not the absolute longitude.
    """
    return longitude % 30


def calculate_chara_karakas(
    planet_longitudes: Dict[str, float],
    include_rahu: bool = False
) -> Dict[CharaKarakaType, CharaKaraka]:
    """
    Calculate Chara Karakas from planetary longitudes.
    
    Args:
        planet_longitudes: Dict of planet name to sidereal longitude (0-360)
        include_rahu: Whether to include Rahu (8-planet scheme)
    
    Returns:
        Dict of Karaka type to CharaKaraka object
    """
    # Get planets to consider
    planets = KARAKA_PLANETS.copy()
    if include_rahu and "Rahu" in planet_longitudes:
        planets.append("Rahu")
    
    # Calculate longitude within sign for each planet
    planet_degrees = []
    for planet in planets:
        if planet in planet_longitudes:
            full_long = planet_longitudes[planet]
            deg_in_sign = get_longitude_in_sign(full_long)
            planet_degrees.append((planet, deg_in_sign, full_long))
    
    # Sort by degree in sign (descending - highest degree = AK)
    planet_degrees.sort(key=lambda x: x[1], reverse=True)
    
    # Assign karakas
    karakas = {}
    karaka_types = KARAKA_ORDER[:len(planet_degrees)]
    
    for i, karaka_type in enumerate(karaka_types):
        if i < len(planet_degrees):
            planet, deg_in_sign, full_long = planet_degrees[i]
            signif = KARAKA_SIGNIFICATIONS[karaka_type]
            
            karakas[karaka_type] = CharaKaraka(
                karaka_type=karaka_type,
                planet=planet,
                longitude_in_sign=round(deg_in_sign, 2),
                full_longitude=round(full_long, 2),
                significance=signif["significance"],
                areas_governed=signif["areas"],
            )
    
    return karakas


def get_karaka_for_area(
    area: str,
    karakas: Dict[CharaKarakaType, CharaKaraka]
) -> Optional[CharaKaraka]:
    """
    Get the relevant Chara Karaka for a life area.
    
    Args:
        area: Life area (career, marriage, etc.)
        karakas: Calculated Chara Karakas
    
    Returns:
        The relevant CharaKaraka or None
    """
    area_lower = area.lower()
    
    # Area to karaka mapping
    area_karaka_map = {
        # Career related -> AmK
        "career": CharaKarakaType.AMK,
        "job": CharaKarakaType.AMK,
        "profession": CharaKarakaType.AMK,
        "work": CharaKarakaType.AMK,
        
        # Marriage related -> DK
        "marriage": CharaKarakaType.DK,
        "spouse": CharaKarakaType.DK,
        "partner": CharaKarakaType.DK,
        "relationships": CharaKarakaType.DK,
        
        # Children related -> PK
        "children": CharaKarakaType.PK,
        "child": CharaKarakaType.PK,
        "son": CharaKarakaType.PK,
        "daughter": CharaKarakaType.PK,
        
        # Mother related -> MK
        "mother": CharaKarakaType.MK,
        "home": CharaKarakaType.MK,
        "property": CharaKarakaType.MK,
        
        # Father related -> PiK
        "father": CharaKarakaType.PIK,
        "fortune": CharaKarakaType.PIK,
        "dharma": CharaKarakaType.PIK,
        "guru": CharaKarakaType.PIK,
        
        # Siblings related -> BK
        "siblings": CharaKarakaType.BK,
        "brother": CharaKarakaType.BK,
        "sister": CharaKarakaType.BK,
        "courage": CharaKarakaType.BK,
        
        # Enemies/obstacles -> GK
        "enemies": CharaKarakaType.GK,
        "obstacles": CharaKarakaType.GK,
        "health": CharaKarakaType.GK,
        "legal": CharaKarakaType.GK,
        
        # Self/soul -> AK
        "self": CharaKarakaType.AK,
        "soul": CharaKarakaType.AK,
        "spirituality": CharaKarakaType.AK,
    }
    
    karaka_type = area_karaka_map.get(area_lower)
    if karaka_type and karaka_type in karakas:
        return karakas[karaka_type]
    
    return None


def analyze_karaka_transit(
    karaka: CharaKaraka,
    transit_results: Dict[str, Dict],
) -> Dict:
    """
    Analyze how the transit affects a specific Chara Karaka.
    
    Args:
        karaka: The Chara Karaka to analyze
        transit_results: Transit analysis results
    
    Returns:
        Transit impact on the karaka's significations
    """
    karaka_planet = karaka.planet
    
    # Find the transit result for this planet
    planet_transit = transit_results.get(karaka_planet, {})
    
    transit_status = planet_transit.get("final_status", "Neutral")
    
    # Determine impact on karaka's areas
    impact = {
        "karaka": karaka.karaka_type.value,
        "karaka_planet": karaka_planet,
        "transit_status": transit_status,
        "areas_affected": karaka.areas_governed,
        "interpretation": "",
    }
    
    # Generate interpretation
    signif = KARAKA_SIGNIFICATIONS[karaka.karaka_type]
    
    if transit_status == "Good":
        impact["interpretation"] = (
            f"{karaka_planet} as {signif['name']} is well-placed in transit. "
            f"This supports matters related to: {', '.join(karaka.areas_governed[:3])}."
        )
        impact["outlook"] = "Favorable"
    elif transit_status == "Bad":
        impact["interpretation"] = (
            f"{karaka_planet} as {signif['name']} faces challenges in transit. "
            f"Be cautious with: {', '.join(karaka.areas_governed[:3])}."
        )
        impact["outlook"] = "Challenging"
    else:
        impact["interpretation"] = (
            f"{karaka_planet} as {signif['name']} has mixed transit influences. "
            f"Balanced approach needed for: {', '.join(karaka.areas_governed[:3])}."
        )
        impact["outlook"] = "Mixed"
    
    return impact


def get_all_karaka_transits(
    karakas: Dict[CharaKarakaType, CharaKaraka],
    transit_results: Dict[str, Dict],
) -> List[Dict]:
    """
    Analyze transits for all Chara Karakas.
    
    Args:
        karakas: All calculated Chara Karakas
        transit_results: Transit analysis results
    
    Returns:
        List of transit impacts for all karakas
    """
    impacts = []
    
    for karaka_type, karaka in karakas.items():
        impact = analyze_karaka_transit(karaka, transit_results)
        impacts.append(impact)
    
    return impacts


def format_karakas_for_display(
    karakas: Dict[CharaKarakaType, CharaKaraka]
) -> List[Dict]:
    """
    Format Chara Karakas for display/API response.
    
    Args:
        karakas: Calculated Chara Karakas
    
    Returns:
        List of formatted karaka info
    """
    result = []
    
    for karaka_type in KARAKA_ORDER:
        if karaka_type in karakas:
            karaka = karakas[karaka_type]
            signif = KARAKA_SIGNIFICATIONS[karaka_type]
            
            result.append({
                "type": karaka_type.value,
                "name": signif["name"],
                "meaning": signif["meaning"],
                "planet": karaka.planet,
                "degree_in_sign": karaka.longitude_in_sign,
                "significance": karaka.significance,
                "areas": karaka.areas_governed,
            })
    
    return result


# Naisargika (Natural) Karakas for reference
# These are fixed, not calculated
NAISARGIKA_KARAKAS = {
    "Sun": ["soul", "father", "authority", "government", "health"],
    "Moon": ["mind", "mother", "emotions", "public", "water"],
    "Mars": ["siblings", "courage", "land", "energy", "blood"],
    "Mercury": ["intellect", "communication", "business", "skin", "friends"],
    "Jupiter": ["wisdom", "children", "wealth", "husband (for females)", "guru"],
    "Venus": ["spouse", "marriage", "vehicles", "arts", "wife (for males)"],
    "Saturn": ["longevity", "grief", "servants", "delays", "discipline"],
    "Rahu": ["foreign", "paternal grandfather", "sudden events"],
    "Ketu": ["maternal grandfather", "moksha", "spiritual knowledge"],
}


# Sthira (Fixed) Karakas
STHIRA_KARAKAS = {
    1: {"planet": "Sun", "signification": "Self, health, vitality"},
    2: {"planet": "Jupiter", "signification": "Wealth, family"},
    3: {"planet": "Mars", "signification": "Siblings, courage"},
    4: {"planet": "Moon", "signification": "Mother, happiness"},
    5: {"planet": "Jupiter", "signification": "Children, intelligence"},
    6: {"planet": "Mars/Saturn", "signification": "Enemies, diseases"},
    7: {"planet": "Venus", "signification": "Spouse, marriage"},
    8: {"planet": "Saturn", "signification": "Longevity, obstacles"},
    9: {"planet": "Jupiter/Sun", "signification": "Father, fortune"},
    10: {"planet": "Mercury/Jupiter/Saturn", "signification": "Career, status"},
    11: {"planet": "Jupiter", "signification": "Gains, aspirations"},
    12: {"planet": "Saturn", "signification": "Losses, liberation"},
}
