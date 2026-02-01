"""
Body Parts Transit Module - Nakshatra to Body Parts Mapping

From Vedic Astrology: An Integrated Approach (P.V.R. Narasimha Rao)
Section 26.8 - Tables 65-69

This module maps nakshatras to body parts for transit analysis.
When malefic planets transit certain nakshatras, they may affect
the corresponding body parts, especially during illness periods.
"""
from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class BodyPartMapping:
    """Mapping of nakshatra to body parts"""
    nakshatra: str
    nakshatra_index: int
    body_part: str
    region: str  # Head, Upper body, Middle body, Lower body
    significance: str


# Table 65-69: Nakshatra to Body Parts mapping
# Based on the textbook's comprehensive nakshatra-body mapping
NAKSHATRA_BODY_PARTS: Dict[int, BodyPartMapping] = {
    1: BodyPartMapping(
        nakshatra="Ashwini",
        nakshatra_index=1,
        body_part="Head (top)",
        region="Head",
        significance="Crown of the head, brain"
    ),
    2: BodyPartMapping(
        nakshatra="Bharani",
        nakshatra_index=2,
        body_part="Head (forehead)",
        region="Head",
        significance="Forehead, cerebrum"
    ),
    3: BodyPartMapping(
        nakshatra="Krittika",
        nakshatra_index=3,
        body_part="Head (crown), Eyebrows, Eyes",
        region="Head",
        significance="Eyes, vision, face"
    ),
    4: BodyPartMapping(
        nakshatra="Rohini",
        nakshatra_index=4,
        body_part="Forehead, Eyes",
        region="Head",
        significance="Forehead, face beauty"
    ),
    5: BodyPartMapping(
        nakshatra="Mrigashira",
        nakshatra_index=5,
        body_part="Eyes, Face",
        region="Head",
        significance="Eyes, nose, face"
    ),
    6: BodyPartMapping(
        nakshatra="Ardra",
        nakshatra_index=6,
        body_part="Eyes, Head",
        region="Head",
        significance="Back of the head, ears"
    ),
    7: BodyPartMapping(
        nakshatra="Punarvasu",
        nakshatra_index=7,
        body_part="Ears, Nose, Throat",
        region="Head",
        significance="Ears, nose, fingers"
    ),
    8: BodyPartMapping(
        nakshatra="Pushya",
        nakshatra_index=8,
        body_part="Face, Mouth",
        region="Head",
        significance="Face, mouth, lips"
    ),
    9: BodyPartMapping(
        nakshatra="Ashlesha",
        nakshatra_index=9,
        body_part="Ears, Chin, Nails",
        region="Head",
        significance="Chin, nails, joints"
    ),
    10: BodyPartMapping(
        nakshatra="Magha",
        nakshatra_index=10,
        body_part="Chin, Lips, Nose",
        region="Head",
        significance="Nose tip, upper lip"
    ),
    11: BodyPartMapping(
        nakshatra="Purva Phalguni",
        nakshatra_index=11,
        body_part="Right Hand",
        region="Upper Body",
        significance="Right arm, hand"
    ),
    12: BodyPartMapping(
        nakshatra="Uttara Phalguni",
        nakshatra_index=12,
        body_part="Left Hand",
        region="Upper Body",
        significance="Left arm, hand"
    ),
    13: BodyPartMapping(
        nakshatra="Hasta",
        nakshatra_index=13,
        body_part="Fingers, Hands",
        region="Upper Body",
        significance="All fingers, palm"
    ),
    14: BodyPartMapping(
        nakshatra="Chitra",
        nakshatra_index=14,
        body_part="Neck, Throat",
        region="Upper Body",
        significance="Neck, throat, voice"
    ),
    15: BodyPartMapping(
        nakshatra="Swati",
        nakshatra_index=15,
        body_part="Chest, Breast",
        region="Upper Body",
        significance="Chest, lungs, heart region"
    ),
    16: BodyPartMapping(
        nakshatra="Vishakha",
        nakshatra_index=16,
        body_part="Chest, Heart, Breasts",
        region="Upper Body",
        significance="Heart, upper chest"
    ),
    17: BodyPartMapping(
        nakshatra="Anuradha",
        nakshatra_index=17,
        body_part="Breasts, Stomach",
        region="Middle Body",
        significance="Stomach, lower chest"
    ),
    18: BodyPartMapping(
        nakshatra="Jyeshtha",
        nakshatra_index=18,
        body_part="Right Side, Neck",
        region="Middle Body",
        significance="Right side of body"
    ),
    19: BodyPartMapping(
        nakshatra="Mula",
        nakshatra_index=19,
        body_part="Left Side, Feet",
        region="Middle Body",
        significance="Left side, lower spine"
    ),
    20: BodyPartMapping(
        nakshatra="Purva Ashadha",
        nakshatra_index=20,
        body_part="Back, Thighs",
        region="Middle Body",
        significance="Back, lower back, thighs"
    ),
    21: BodyPartMapping(
        nakshatra="Uttara Ashadha",
        nakshatra_index=21,
        body_part="Thighs, Waist",
        region="Middle Body",
        significance="Waist, thighs"
    ),
    22: BodyPartMapping(
        nakshatra="Shravana",
        nakshatra_index=22,
        body_part="Belly, Genitals",
        region="Lower Body",
        significance="Abdomen, reproductive organs"
    ),
    23: BodyPartMapping(
        nakshatra="Dhanishtha",
        nakshatra_index=23,
        body_part="Back, Anus",
        region="Lower Body",
        significance="Lower back, excretory organs"
    ),
    24: BodyPartMapping(
        nakshatra="Shatabhisha",
        nakshatra_index=24,
        body_part="Right Thigh",
        region="Lower Body",
        significance="Right thigh, knee"
    ),
    25: BodyPartMapping(
        nakshatra="Purva Bhadrapada",
        nakshatra_index=25,
        body_part="Left Thigh, Sides",
        region="Lower Body",
        significance="Left thigh, ribs"
    ),
    26: BodyPartMapping(
        nakshatra="Uttara Bhadrapada",
        nakshatra_index=26,
        body_part="Shins, Ankles",
        region="Lower Body",
        significance="Legs, ankles, heels"
    ),
    27: BodyPartMapping(
        nakshatra="Revati",
        nakshatra_index=27,
        body_part="Feet, Ankles",
        region="Lower Body",
        significance="Feet, toes"
    ),
}


# Malefic planets that may cause health issues during transit
NATURAL_MALEFICS = ["Sun", "Mars", "Saturn", "Rahu", "Ketu"]


def get_body_part_for_nakshatra(nakshatra_index: int) -> Optional[BodyPartMapping]:
    """
    Get the body part mapping for a nakshatra.
    
    Args:
        nakshatra_index: 1-based nakshatra index (1-27)
    
    Returns:
        BodyPartMapping or None
    """
    return NAKSHATRA_BODY_PARTS.get(nakshatra_index)


def analyze_body_part_transits(
    planet_nakshatras: Dict[str, int],
    check_malefics_only: bool = True
) -> Dict[str, Dict]:
    """
    Analyze which body parts are affected by current planetary transits.
    
    Args:
        planet_nakshatras: Dict of planet name to their current nakshatra
        check_malefics_only: If True, only check natural malefics
    
    Returns:
        Dict of body parts that may be affected
    """
    affected_parts = {}
    
    for planet, nakshatra_index in planet_nakshatras.items():
        if check_malefics_only and planet not in NATURAL_MALEFICS:
            continue
        
        mapping = NAKSHATRA_BODY_PARTS.get(nakshatra_index)
        if not mapping:
            continue
        
        body_part = mapping.body_part
        if body_part not in affected_parts:
            affected_parts[body_part] = {
                "body_part": body_part,
                "region": mapping.region,
                "nakshatra": mapping.nakshatra,
                "affecting_planets": [],
                "significance": mapping.significance,
            }
        
        affected_parts[body_part]["affecting_planets"].append({
            "planet": planet,
            "nakshatra": mapping.nakshatra,
            "nakshatra_index": nakshatra_index,
            "is_malefic": planet in NATURAL_MALEFICS,
        })
    
    return affected_parts


def get_health_sensitive_transits(
    janma_nakshatra: int,
    planet_nakshatras: Dict[str, int],
    include_trikona: bool = True
) -> Dict:
    """
    Analyze health-sensitive transits based on janma nakshatra.
    
    When malefics transit janma nakshatra or specific nakshatras from it,
    health of the native may be affected.
    
    Args:
        janma_nakshatra: Birth star nakshatra (1-27)
        planet_nakshatras: Dict of planet to their current nakshatra
        include_trikona: Include 5th and 9th nakshatras (trikona)
    
    Returns:
        Health sensitivity analysis
    """
    sensitive_nakshatras = [janma_nakshatra]
    
    # Vipat (3rd), Pratyak (5th), Naidhana (7th) are unfavorable
    # From special nakshatra theory
    sensitive_nakshatras.append(((janma_nakshatra - 1) + 2) % 27 + 1)  # 3rd
    sensitive_nakshatras.append(((janma_nakshatra - 1) + 4) % 27 + 1)  # 5th  
    sensitive_nakshatras.append(((janma_nakshatra - 1) + 6) % 27 + 1)  # 7th
    
    if include_trikona:
        # Include trikona nakshatras (10th and 19th)
        sensitive_nakshatras.append(((janma_nakshatra - 1) + 9) % 27 + 1)
        sensitive_nakshatras.append(((janma_nakshatra - 1) + 18) % 27 + 1)
    
    result = {
        "janma_nakshatra": NAKSHATRA_BODY_PARTS[janma_nakshatra].nakshatra,
        "sensitive_nakshatras": [],
        "malefic_transits_in_sensitive": [],
        "health_risk_level": "Low",
        "body_parts_to_watch": [],
        "recommendations": []
    }
    
    # Map sensitive nakshatras
    for nak in sensitive_nakshatras:
        mapping = NAKSHATRA_BODY_PARTS.get(nak)
        if mapping:
            result["sensitive_nakshatras"].append({
                "nakshatra": mapping.nakshatra,
                "index": nak,
                "body_part": mapping.body_part
            })
    
    # Check malefic transits in sensitive nakshatras
    risk_count = 0
    body_parts_affected = set()
    
    for planet, nak_index in planet_nakshatras.items():
        if planet not in NATURAL_MALEFICS:
            continue
        
        if nak_index in sensitive_nakshatras:
            mapping = NAKSHATRA_BODY_PARTS.get(nak_index)
            result["malefic_transits_in_sensitive"].append({
                "planet": planet,
                "nakshatra": mapping.nakshatra if mapping else "Unknown",
                "body_part": mapping.body_part if mapping else "Unknown",
            })
            risk_count += 1
            if mapping:
                body_parts_affected.add(mapping.body_part)
    
    # Determine health risk level
    if risk_count == 0:
        result["health_risk_level"] = "Low"
        result["recommendations"].append("General health appears favorable. Maintain regular routines.")
    elif risk_count == 1:
        result["health_risk_level"] = "Moderate"
        result["recommendations"].append("One malefic in sensitive position. Take preventive care.")
    elif risk_count == 2:
        result["health_risk_level"] = "Elevated"
        result["recommendations"].append("Multiple malefics in sensitive positions. Focus on health maintenance.")
    else:
        result["health_risk_level"] = "High"
        result["recommendations"].append("Several malefics affecting health zones. Prioritize health and rest.")
    
    result["body_parts_to_watch"] = list(body_parts_affected)
    
    return result


def get_all_nakshatra_body_mappings() -> List[Dict]:
    """
    Get complete list of nakshatra to body part mappings.
    
    Returns:
        List of all mappings
    """
    return [
        {
            "index": mapping.nakshatra_index,
            "nakshatra": mapping.nakshatra,
            "body_part": mapping.body_part,
            "region": mapping.region,
            "significance": mapping.significance,
        }
        for mapping in NAKSHATRA_BODY_PARTS.values()
    ]


# Region-wise body part groupings for analysis
BODY_REGIONS = {
    "Head": {
        "nakshatras": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "health_areas": ["headaches", "eye problems", "ear issues", "dental", "mental health"],
    },
    "Upper Body": {
        "nakshatras": [11, 12, 13, 14, 15, 16],
        "health_areas": ["arm injuries", "throat problems", "respiratory", "heart", "chest"],
    },
    "Middle Body": {
        "nakshatras": [17, 18, 19, 20, 21],
        "health_areas": ["digestive issues", "back pain", "liver", "kidney", "spine"],
    },
    "Lower Body": {
        "nakshatras": [22, 23, 24, 25, 26, 27],
        "health_areas": ["leg issues", "reproductive", "urinary", "knee", "foot problems"],
    },
}


def analyze_regional_health(planet_nakshatras: Dict[str, int]) -> Dict:
    """
    Analyze health by body regions based on planetary transits.
    
    Args:
        planet_nakshatras: Dict of planet to their current nakshatra
    
    Returns:
        Regional health analysis
    """
    result = {}
    
    for region, info in BODY_REGIONS.items():
        malefics_in_region = []
        benefics_in_region = []
        
        for planet, nak_index in planet_nakshatras.items():
            if nak_index in info["nakshatras"]:
                if planet in NATURAL_MALEFICS:
                    malefics_in_region.append(planet)
                else:
                    benefics_in_region.append(planet)
        
        status = "Neutral"
        if len(malefics_in_region) > len(benefics_in_region):
            status = "Challenged"
        elif len(benefics_in_region) > len(malefics_in_region):
            status = "Supported"
        
        result[region] = {
            "status": status,
            "malefics": malefics_in_region,
            "benefics": benefics_in_region,
            "health_areas": info["health_areas"],
            "advice": f"{'Take care of' if status == 'Challenged' else 'Favorable for'} {', '.join(info['health_areas'][:3])}"
        }
    
    return result
