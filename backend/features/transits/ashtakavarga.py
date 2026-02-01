"""
Ashtakavarga Transit Scoring Module

From Vedic Astrology: An Integrated Approach (P.V.R. Narasimha Rao)
Chapter 12 - Ashtakavarga

Ashtakavarga provides a point-based system for evaluating planetary transits.
Each planet's transit gains points based on the benefic dots (bindus) in that 
position from natal chart.

Key Concepts:
- BAV (Bhinnashtakavarga): Individual planet's points
- SAV (Sarvashtakavarga): Total of all 7 planets' contributions
- Sodhya Pinda: Weighted strength calculation
"""
from typing import Dict, List, Optional
from dataclasses import dataclass


# Default Ashtakavarga benefic positions for each planet
# These are positions (signs from planet) where each planet gives benefic points
# Format: planet -> list of positions where it gives bindus to transiting planet

ASHTAKAVARGA_BINDUS = {
    "Sun": {
        "Sun": [1, 2, 4, 7, 8, 9, 10, 11],
        "Moon": [3, 6, 10, 11],
        "Mars": [1, 2, 4, 7, 8, 9, 10, 11],
        "Mercury": [3, 5, 6, 9, 10, 11, 12],
        "Jupiter": [5, 6, 9, 11],
        "Venus": [6, 7, 12],
        "Saturn": [1, 2, 4, 7, 8, 9, 10, 11],
        "Lagna": [3, 4, 6, 10, 11, 12],
    },
    "Moon": {
        "Sun": [3, 6, 7, 8, 10, 11],
        "Moon": [1, 3, 6, 7, 10, 11],
        "Mars": [2, 3, 5, 6, 9, 10, 11],
        "Mercury": [1, 3, 4, 5, 7, 8, 10, 11],
        "Jupiter": [1, 4, 7, 8, 10, 11, 12],
        "Venus": [3, 4, 5, 7, 9, 10, 11],
        "Saturn": [3, 5, 6, 11],
        "Lagna": [3, 6, 10, 11],
    },
    "Mars": {
        "Sun": [3, 5, 6, 10, 11],
        "Moon": [3, 6, 11],
        "Mars": [1, 2, 4, 7, 8, 10, 11],
        "Mercury": [3, 5, 6, 11],
        "Jupiter": [6, 10, 11, 12],
        "Venus": [6, 8, 11, 12],
        "Saturn": [1, 4, 7, 8, 9, 10, 11],
        "Lagna": [1, 3, 6, 10, 11],
    },
    "Mercury": {
        "Sun": [5, 6, 9, 11, 12],
        "Moon": [2, 4, 6, 8, 10, 11],
        "Mars": [1, 2, 4, 7, 8, 9, 10, 11],
        "Mercury": [1, 3, 5, 6, 9, 10, 11, 12],
        "Jupiter": [6, 8, 11, 12],
        "Venus": [1, 2, 3, 4, 5, 8, 9, 11],
        "Saturn": [1, 2, 4, 7, 8, 9, 10, 11],
        "Lagna": [1, 2, 4, 6, 8, 10, 11],
    },
    "Jupiter": {
        "Sun": [1, 2, 3, 4, 7, 8, 9, 10, 11],
        "Moon": [2, 5, 7, 9, 11],
        "Mars": [1, 2, 4, 7, 8, 10, 11],
        "Mercury": [1, 2, 4, 5, 6, 9, 10, 11],
        "Jupiter": [1, 2, 3, 4, 7, 8, 10, 11],
        "Venus": [2, 5, 6, 9, 10, 11],
        "Saturn": [3, 5, 6, 12],
        "Lagna": [1, 2, 4, 5, 6, 7, 9, 10, 11],
    },
    "Venus": {
        "Sun": [8, 11, 12],
        "Moon": [1, 2, 3, 4, 5, 8, 9, 11, 12],
        "Mars": [3, 5, 6, 9, 11, 12],
        "Mercury": [3, 5, 6, 9, 11],
        "Jupiter": [5, 8, 9, 10, 11],
        "Venus": [1, 2, 3, 4, 5, 8, 9, 10, 11],
        "Saturn": [3, 4, 5, 8, 9, 10, 11],
        "Lagna": [1, 2, 3, 4, 5, 8, 9, 11],
    },
    "Saturn": {
        "Sun": [1, 2, 4, 7, 8, 10, 11],
        "Moon": [3, 6, 11],
        "Mars": [3, 5, 6, 10, 11, 12],
        "Mercury": [6, 8, 9, 10, 11, 12],
        "Jupiter": [5, 6, 11, 12],
        "Venus": [6, 11, 12],
        "Saturn": [3, 5, 6, 11],
        "Lagna": [1, 3, 4, 6, 10, 11],
    },
}

# Maximum possible bindus for each planet
MAX_BINDUS = {
    "Sun": 48, "Moon": 49, "Mars": 39, "Mercury": 54,
    "Jupiter": 56, "Venus": 52, "Saturn": 39
}


@dataclass
class AshtakavargaScore:
    """Ashtakavarga score for a planet's transit position"""
    planet: str
    transit_sign: int
    bav_score: int  # Bhinnashtakavarga score (0-8)
    sav_score: int  # Sarvashtakavarga score (0-56)
    quality: str  # Excellent, Good, Average, Poor, Very Poor
    interpretation: str


def calculate_bav(
    transiting_planet: str,
    transit_sign: int,
    natal_positions: Dict[str, int]
) -> int:
    """
    Calculate Bhinnashtakavarga (BAV) score for a planet's transit.
    
    Args:
        transiting_planet: The planet that is transiting
        transit_sign: The sign (1-12) where the planet is transiting
        natal_positions: Dict of planet/Lagna to their natal sign (1-12)
    
    Returns:
        BAV score (0-8)
    """
    if transiting_planet not in ASHTAKAVARGA_BINDUS:
        return 0
    
    bindu_rules = ASHTAKAVARGA_BINDUS[transiting_planet]
    score = 0
    
    for contributor, positions in bindu_rules.items():
        if contributor not in natal_positions:
            continue
        
        natal_sign = natal_positions[contributor]
        # Calculate position of transit sign from natal position
        position_from_natal = ((transit_sign - natal_sign) % 12) + 1
        
        if position_from_natal in positions:
            score += 1
    
    return score


def calculate_sav(
    transit_sign: int,
    natal_positions: Dict[str, int]
) -> int:
    """
    Calculate Sarvashtakavarga (SAV) score for a sign.
    
    Args:
        transit_sign: The sign (1-12) to evaluate
        natal_positions: Dict of planet/Lagna to their natal sign (1-12)
    
    Returns:
        SAV score (sum of all planets' BAV for this sign)
    """
    sav = 0
    for planet in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
        sav += calculate_bav(planet, transit_sign, natal_positions)
    return sav


def get_transit_quality(bav_score: int, planet: str = None) -> str:
    """
    Determine transit quality based on BAV score.
    
    Args:
        bav_score: The BAV score (0-8)
        planet: Optional planet name for context
    
    Returns:
        Quality assessment string
    """
    if bav_score >= 6:
        return "Excellent"
    elif bav_score >= 5:
        return "Good"
    elif bav_score >= 4:
        return "Average"
    elif bav_score >= 2:
        return "Poor"
    else:
        return "Very Poor"


def get_sav_quality(sav_score: int) -> str:
    """
    Determine quality based on SAV score.
    
    Args:
        sav_score: The SAV score (0-56)
    
    Returns:
        Quality assessment string
    """
    if sav_score >= 35:
        return "Highly Favorable"
    elif sav_score >= 30:
        return "Favorable"
    elif sav_score >= 25:
        return "Average"
    elif sav_score >= 20:
        return "Challenging"
    else:
        return "Difficult"


def analyze_transit_ashtakavarga(
    transiting_planet: str,
    transit_sign: int,
    natal_positions: Dict[str, int],
    transit_house: int = None
) -> AshtakavargaScore:
    """
    Comprehensive Ashtakavarga analysis for a transit.
    
    Args:
        transiting_planet: The planet that is transiting
        transit_sign: The sign (1-12) where the planet is transiting
        natal_positions: Dict of planet/Lagna to their natal sign
        transit_house: Optional house number for context
    
    Returns:
        Complete AshtakavargaScore analysis
    """
    bav = calculate_bav(transiting_planet, transit_sign, natal_positions)
    sav = calculate_sav(transit_sign, natal_positions)
    quality = get_transit_quality(bav, transiting_planet)
    
    # Generate interpretation
    interpretation_parts = []
    
    if bav >= 5:
        interpretation_parts.append(f"{transiting_planet}'s transit is well-supported with {bav} bindus.")
        interpretation_parts.append("This indicates favorable conditions for the planet's significations.")
    elif bav >= 4:
        interpretation_parts.append(f"{transiting_planet}'s transit has moderate support with {bav} bindus.")
        interpretation_parts.append("Results will be average - neither strongly positive nor negative.")
    elif bav >= 2:
        interpretation_parts.append(f"{transiting_planet}'s transit has weak support with only {bav} bindus.")
        interpretation_parts.append("The planet may struggle to deliver positive results.")
    else:
        interpretation_parts.append(f"{transiting_planet}'s transit is poorly supported with just {bav} bindus.")
        interpretation_parts.append("Expect challenges related to this planet's significations.")
    
    if transit_house:
        interpretation_parts.append(f"Transit through house {transit_house} with SAV of {sav}.")
    
    return AshtakavargaScore(
        planet=transiting_planet,
        transit_sign=transit_sign,
        bav_score=bav,
        sav_score=sav,
        quality=quality,
        interpretation=" ".join(interpretation_parts)
    )


def analyze_all_transit_ashtakavarga(
    planet_signs: Dict[str, int],
    natal_positions: Dict[str, int]
) -> Dict[str, AshtakavargaScore]:
    """
    Analyze Ashtakavarga for all transiting planets.
    
    Args:
        planet_signs: Dict of planet to their transit sign
        natal_positions: Dict of planet/Lagna to their natal sign
    
    Returns:
        Dict of planet to their AshtakavargaScore
    """
    results = {}
    
    for planet, transit_sign in planet_signs.items():
        if planet in ["Rahu", "Ketu"]:
            continue  # Rahu/Ketu don't have standard Ashtakavarga
        
        results[planet] = analyze_transit_ashtakavarga(
            planet, transit_sign, natal_positions
        )
    
    return results


def get_favorable_transit_days(
    planet: str,
    natal_positions: Dict[str, int]
) -> List[Dict]:
    """
    Get list of signs ranked by Ashtakavarga favorability for a planet.
    
    Args:
        planet: The planet to analyze
        natal_positions: Dict of planet/Lagna to their natal sign
    
    Returns:
        List of signs ranked by favorability
    """
    sign_scores = []
    
    for sign in range(1, 13):
        bav = calculate_bav(planet, sign, natal_positions)
        sav = calculate_sav(sign, natal_positions)
        
        sign_scores.append({
            "sign": sign,
            "sign_name": get_sign_name(sign),
            "bav": bav,
            "sav": sav,
            "quality": get_transit_quality(bav),
        })
    
    # Sort by BAV score descending
    sign_scores.sort(key=lambda x: x["bav"], reverse=True)
    
    return sign_scores


def get_sign_name(sign_num: int) -> str:
    """Get sign name from number (1-12)"""
    signs = [
        "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
        "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    ]
    if 1 <= sign_num <= 12:
        return signs[sign_num - 1]
    return "Unknown"


def calculate_transit_strength_summary(
    planet_signs: Dict[str, int],
    natal_positions: Dict[str, int]
) -> Dict:
    """
    Calculate overall transit strength summary using Ashtakavarga.
    
    Args:
        planet_signs: Dict of planet to their transit sign
        natal_positions: Dict of planet/Lagna to their natal sign
    
    Returns:
        Summary of transit strength
    """
    total_bav = 0
    planet_count = 0
    scores = {}
    
    for planet, transit_sign in planet_signs.items():
        if planet in ["Rahu", "Ketu"]:
            continue
        
        bav = calculate_bav(planet, transit_sign, natal_positions)
        scores[planet] = bav
        total_bav += bav
        planet_count += 1
    
    avg_bav = total_bav / planet_count if planet_count > 0 else 0
    
    # Categorize planets by strength
    strong_transits = [p for p, s in scores.items() if s >= 5]
    weak_transits = [p for p, s in scores.items() if s < 3]
    
    overall_quality = "Favorable" if avg_bav >= 4 else "Average" if avg_bav >= 3 else "Challenging"
    
    return {
        "total_bav": total_bav,
        "average_bav": round(avg_bav, 2),
        "planet_scores": scores,
        "strong_transits": strong_transits,
        "weak_transits": weak_transits,
        "overall_quality": overall_quality,
        "interpretation": f"Overall transit quality is {overall_quality.lower()} with average BAV of {avg_bav:.1f}. "
                         f"Strong planets: {', '.join(strong_transits) if strong_transits else 'None'}. "
                         f"Weak planets: {', '.join(weak_transits) if weak_transits else 'None'}."
    }


# House significations for Ashtakavarga transit interpretation
HOUSE_MATTERS = {
    1: "self, health, personality",
    2: "wealth, speech, family",
    3: "courage, siblings, communication",
    4: "mother, property, happiness",
    5: "children, intelligence, speculation",
    6: "enemies, diseases, service",
    7: "spouse, partnerships, travel",
    8: "longevity, obstacles, inheritance",
    9: "fortune, father, dharma",
    10: "career, status, authority",
    11: "gains, aspirations, friends",
    12: "losses, liberation, foreign lands",
}


def interpret_transit_by_house(
    planet: str,
    house: int,
    bav: int
) -> str:
    """Generate interpretation for planet transiting a house with given BAV"""
    matters = HOUSE_MATTERS.get(house, "")
    quality = get_transit_quality(bav)
    
    if quality in ["Excellent", "Good"]:
        return f"{planet} transiting house {house} ({matters}) with {bav} bindus brings favorable results."
    elif quality == "Average":
        return f"{planet} transiting house {house} ({matters}) with {bav} bindus gives mixed results."
    else:
        return f"{planet} transiting house {house} ({matters}) with only {bav} bindus may bring challenges."
