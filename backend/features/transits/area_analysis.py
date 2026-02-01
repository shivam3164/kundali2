"""
Area Analysis System - Life Area Based Predictions

This module allows users to ask questions about specific life areas
(career, marriage, health, etc.) and get detailed analysis combining
house significations with transit data.

From Vedic Astrology: An Integrated Approach (P.V.R. Narasimha Rao)
Chapter 7 - Houses and Their Significations
"""
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class LifeArea(str, Enum):
    """Life areas that can be queried"""
    CAREER = "career"
    JOB = "job"
    BUSINESS = "business"
    FINANCE = "finance"
    WEALTH = "wealth"
    HEALTH = "health"
    MARRIAGE = "marriage"
    RELATIONSHIPS = "relationships"
    LOVE = "love"
    CHILDREN = "children"
    EDUCATION = "education"
    TRAVEL = "travel"
    SPIRITUALITY = "spirituality"
    FAMILY = "family"
    PROPERTY = "property"
    LEGAL = "legal"
    GOVERNMENT = "government"


@dataclass
class HouseSignification:
    """House signification details"""
    house: int
    name: str
    primary_significations: List[str]
    secondary_significations: List[str]
    body_parts: List[str]
    karaka: str  # Natural significator planet


# Complete house significations from Chapter 7
HOUSE_SIGNIFICATIONS: Dict[int, HouseSignification] = {
    1: HouseSignification(
        house=1,
        name="Lagna/Tanu Bhava",
        primary_significations=["self", "body", "personality", "health", "vitality"],
        secondary_significations=["appearance", "fame", "start of life", "physical constitution"],
        body_parts=["head", "brain"],
        karaka="Sun"
    ),
    2: HouseSignification(
        house=2,
        name="Dhana Bhava",
        primary_significations=["wealth", "family", "speech", "food", "early education"],
        secondary_significations=["face", "right eye", "accumulated wealth", "family values"],
        body_parts=["mouth", "face", "right eye", "teeth"],
        karaka="Jupiter"
    ),
    3: HouseSignification(
        house=3,
        name="Sahaja Bhava",
        primary_significations=["siblings", "courage", "communication", "short travels"],
        secondary_significations=["hobbies", "skills", "neighbors", "writing", "arms"],
        body_parts=["shoulders", "arms", "hands", "ears"],
        karaka="Mars"
    ),
    4: HouseSignification(
        house=4,
        name="Sukha Bhava",
        primary_significations=["mother", "home", "property", "vehicles", "happiness"],
        secondary_significations=["education", "peace of mind", "ancestral property", "comforts"],
        body_parts=["chest", "lungs", "heart"],
        karaka="Moon"
    ),
    5: HouseSignification(
        house=5,
        name="Putra Bhava",
        primary_significations=["children", "intelligence", "creativity", "romance"],
        secondary_significations=["speculation", "past life merits", "mantras", "stomach"],
        body_parts=["stomach", "upper abdomen"],
        karaka="Jupiter"
    ),
    6: HouseSignification(
        house=6,
        name="Shatru Bhava",
        primary_significations=["enemies", "diseases", "debts", "service", "daily work"],
        secondary_significations=["obstacles", "litigation", "maternal uncle", "pets"],
        body_parts=["intestines", "digestive system"],
        karaka="Mars/Saturn"
    ),
    7: HouseSignification(
        house=7,
        name="Kalatra Bhava",
        primary_significations=["spouse", "marriage", "partnerships", "business"],
        secondary_significations=["foreign travel", "death", "desires", "public dealings"],
        body_parts=["lower abdomen", "kidneys"],
        karaka="Venus"
    ),
    8: HouseSignification(
        house=8,
        name="Mrityu Bhava",
        primary_significations=["longevity", "obstacles", "sudden events", "inheritance"],
        secondary_significations=["occult", "research", "hidden matters", "transformation"],
        body_parts=["genitals", "excretory organs"],
        karaka="Saturn"
    ),
    9: HouseSignification(
        house=9,
        name="Dharma Bhava",
        primary_significations=["father", "fortune", "dharma", "higher education", "guru"],
        secondary_significations=["long journeys", "religion", "law", "philosophy"],
        body_parts=["thighs", "hips"],
        karaka="Jupiter"
    ),
    10: HouseSignification(
        house=10,
        name="Karma Bhava",
        primary_significations=["career", "profession", "status", "authority", "government"],
        secondary_significations=["fame", "honors", "father's status", "knees"],
        body_parts=["knees", "back"],
        karaka="Sun/Mercury/Jupiter/Saturn"
    ),
    11: HouseSignification(
        house=11,
        name="Labha Bhava",
        primary_significations=["gains", "income", "elder siblings", "friends", "aspirations"],
        secondary_significations=["fulfillment of desires", "networking", "social circles"],
        body_parts=["ankles", "left ear"],
        karaka="Jupiter"
    ),
    12: HouseSignification(
        house=12,
        name="Vyaya Bhava",
        primary_significations=["losses", "expenses", "foreign residence", "moksha"],
        secondary_significations=["hospitals", "prisons", "isolation", "bed pleasures"],
        body_parts=["feet", "left eye"],
        karaka="Saturn"
    ),
}


# Life area to house mapping with weights
AREA_HOUSE_MAPPING: Dict[str, List[Tuple[int, float]]] = {
    # Career related
    "career": [(10, 1.0), (6, 0.7), (2, 0.5), (11, 0.4)],
    "job": [(6, 1.0), (10, 0.8), (2, 0.5)],
    "business": [(7, 1.0), (10, 0.8), (11, 0.6), (2, 0.5)],
    
    # Finance related
    "finance": [(2, 1.0), (11, 0.9), (5, 0.6), (9, 0.5)],
    "wealth": [(2, 1.0), (11, 0.8), (5, 0.6), (9, 0.5)],
    "income": [(11, 1.0), (2, 0.8), (10, 0.5)],
    
    # Health related
    "health": [(1, 1.0), (6, 0.8), (8, 0.7)],
    "longevity": [(8, 1.0), (1, 0.8), (3, 0.5)],
    
    # Relationships
    "marriage": [(7, 1.0), (2, 0.6), (4, 0.4), (11, 0.3)],
    "relationships": [(7, 1.0), (5, 0.6), (11, 0.5)],
    "love": [(5, 1.0), (7, 0.8), (11, 0.4)],
    
    # Family
    "family": [(2, 1.0), (4, 0.8), (5, 0.6)],
    "children": [(5, 1.0), (9, 0.5), (11, 0.4)],
    "mother": [(4, 1.0), (1, 0.4)],
    "father": [(9, 1.0), (10, 0.5)],
    
    # Education
    "education": [(4, 1.0), (5, 0.8), (9, 0.7), (2, 0.4)],
    "higher_education": [(9, 1.0), (5, 0.6)],
    
    # Travel
    "travel": [(3, 0.8), (9, 1.0), (12, 0.7)],
    "foreign": [(12, 1.0), (9, 0.7), (7, 0.5)],
    
    # Spiritual
    "spirituality": [(9, 1.0), (12, 0.9), (5, 0.5)],
    "moksha": [(12, 1.0), (9, 0.6), (4, 0.4)],
    
    # Property
    "property": [(4, 1.0), (2, 0.6), (11, 0.5)],
    "vehicles": [(4, 1.0), (11, 0.5)],
    
    # Legal
    "legal": [(6, 1.0), (9, 0.7), (7, 0.5)],
    "litigation": [(6, 1.0), (12, 0.6)],
    
    # Government
    "government": [(10, 1.0), (9, 0.5), (1, 0.4)],
}


# Planet significations for area analysis
PLANET_AREA_SIGNIFICATIONS: Dict[str, List[str]] = {
    "Sun": ["career", "authority", "government", "health", "father"],
    "Moon": ["mind", "emotions", "mother", "public", "travel"],
    "Mars": ["courage", "property", "siblings", "legal", "health"],
    "Mercury": ["education", "business", "communication", "skills"],
    "Jupiter": ["finance", "children", "education", "spirituality", "fortune"],
    "Venus": ["marriage", "relationships", "love", "vehicles", "wealth"],
    "Saturn": ["career", "longevity", "service", "obstacles", "foreign"],
    "Rahu": ["foreign", "technology", "unconventional", "sudden gains"],
    "Ketu": ["spirituality", "moksha", "loss", "detachment"],
}


@dataclass
class AreaAnalysisResult:
    """Result of life area analysis"""
    area: str
    area_display_name: str
    overall_outlook: str  # Positive, Neutral, Challenging
    confidence: str  # High, Medium, Low
    score: float  # -100 to +100
    
    # House analysis
    relevant_houses: List[Dict]
    
    # Planet influences
    planet_influences: List[Dict]
    
    # Transit impacts
    transit_impacts: List[Dict]
    
    # Predictions
    short_term_prediction: str
    advice: str
    
    # Details
    strengths: List[str]
    challenges: List[str]


def normalize_area_query(query: str) -> Optional[str]:
    """
    Normalize user query to standard area name.
    
    Args:
        query: User's question or area name
    
    Returns:
        Normalized area name or None
    """
    query_lower = query.lower().strip()
    
    # Direct matches
    if query_lower in AREA_HOUSE_MAPPING:
        return query_lower
    
    # Keyword matching
    keyword_map = {
        # Career keywords
        "job": "job",
        "work": "job",
        "employment": "job",
        "profession": "career",
        "career": "career",
        "office": "job",
        "promotion": "career",
        "boss": "career",
        
        # Business keywords
        "business": "business",
        "trade": "business",
        "shop": "business",
        "enterprise": "business",
        "startup": "business",
        
        # Finance keywords
        "money": "finance",
        "finance": "finance",
        "wealth": "wealth",
        "income": "income",
        "savings": "finance",
        "investment": "finance",
        "profit": "business",
        
        # Health keywords
        "health": "health",
        "disease": "health",
        "illness": "health",
        "medical": "health",
        "body": "health",
        "life": "longevity",
        "longevity": "longevity",
        
        # Marriage keywords
        "marriage": "marriage",
        "wedding": "marriage",
        "spouse": "marriage",
        "wife": "marriage",
        "husband": "marriage",
        "partner": "marriage",
        
        # Relationship keywords
        "relationship": "relationships",
        "love": "love",
        "romance": "love",
        "dating": "love",
        "boyfriend": "love",
        "girlfriend": "love",
        
        # Family keywords
        "family": "family",
        "children": "children",
        "child": "children",
        "son": "children",
        "daughter": "children",
        "mother": "mother",
        "mom": "mother",
        "father": "father",
        "dad": "father",
        "parent": "family",
        
        # Education keywords
        "education": "education",
        "study": "education",
        "studies": "education",
        "exam": "education",
        "school": "education",
        "college": "higher_education",
        "university": "higher_education",
        "degree": "higher_education",
        
        # Travel keywords
        "travel": "travel",
        "journey": "travel",
        "trip": "travel",
        "abroad": "foreign",
        "foreign": "foreign",
        "overseas": "foreign",
        "immigration": "foreign",
        "visa": "foreign",
        
        # Property keywords
        "property": "property",
        "house": "property",
        "home": "property",
        "land": "property",
        "real estate": "property",
        "car": "vehicles",
        "vehicle": "vehicles",
        
        # Legal keywords
        "legal": "legal",
        "court": "litigation",
        "case": "litigation",
        "lawsuit": "litigation",
        "lawyer": "legal",
        
        # Spiritual keywords
        "spiritual": "spirituality",
        "meditation": "spirituality",
        "moksha": "moksha",
        "liberation": "moksha",
        "religion": "spirituality",
        
        # Government keywords
        "government": "government",
        "politics": "government",
        "civil service": "government",
    }
    
    for keyword, area in keyword_map.items():
        if keyword in query_lower:
            return area
    
    return None


def get_area_relevant_houses(area: str) -> List[Dict]:
    """Get houses relevant to an area with their significations."""
    if area not in AREA_HOUSE_MAPPING:
        return []
    
    houses_with_weights = AREA_HOUSE_MAPPING[area]
    result = []
    
    for house_num, weight in houses_with_weights:
        house_info = HOUSE_SIGNIFICATIONS[house_num]
        result.append({
            "house": house_num,
            "name": house_info.name,
            "weight": weight,
            "primary_significations": house_info.primary_significations,
            "karaka": house_info.karaka,
        })
    
    return result


def get_planet_area_relevance(planet: str, area: str) -> float:
    """Get how relevant a planet is for a specific area."""
    if planet not in PLANET_AREA_SIGNIFICATIONS:
        return 0.0
    
    planet_areas = PLANET_AREA_SIGNIFICATIONS[planet]
    
    # Direct match
    if area in planet_areas:
        return 1.0
    
    # Related area matches
    area_groups = {
        "career": ["job", "business", "government"],
        "finance": ["wealth", "income"],
        "health": ["longevity"],
        "marriage": ["relationships", "love"],
        "education": ["higher_education"],
        "travel": ["foreign"],
        "spirituality": ["moksha"],
        "family": ["children", "mother", "father"],
    }
    
    for main_area, related in area_groups.items():
        if area == main_area and any(r in planet_areas for r in [main_area] + related):
            return 0.7
        if area in related and main_area in planet_areas:
            return 0.5
    
    return 0.0


def analyze_area(
    area: str,
    transit_results: List[Dict],
    natal_house_lords: Dict[str, int] = None,
    natal_planet_houses: Dict[str, int] = None,
) -> AreaAnalysisResult:
    """
    Comprehensive analysis of a life area.
    
    Args:
        area: Life area to analyze
        transit_results: List of planet transit results
        natal_house_lords: Dict of planet to house it lords
        natal_planet_houses: Dict of planet to house it occupies
    
    Returns:
        Complete AreaAnalysisResult
    """
    area_normalized = normalize_area_query(area) or area.lower()
    
    # Get display name
    area_display = area_normalized.replace("_", " ").title()
    
    # Get relevant houses
    relevant_houses = get_area_relevant_houses(area_normalized)
    
    # Calculate score
    score = 0.0
    planet_influences = []
    transit_impacts = []
    strengths = []
    challenges = []
    
    # Process each transit
    for transit in transit_results:
        planet = transit.get("planet", "")
        house_from_moon = transit.get("house_from_moon", 0)
        house_from_lagna = transit.get("house_from_lagna", 0)
        status = transit.get("final_status", "Neutral")
        
        # Check if transit affects relevant houses
        house_weight = 0.0
        for house_info in relevant_houses:
            if house_info["house"] == house_from_moon or house_info["house"] == house_from_lagna:
                house_weight = max(house_weight, house_info["weight"])
        
        # Get planet relevance for area
        planet_relevance = get_planet_area_relevance(planet, area_normalized)
        
        # Calculate impact
        combined_relevance = max(house_weight, planet_relevance * 0.7)
        
        if combined_relevance > 0:
            if status == "Good":
                impact = combined_relevance * 20
                score += impact
                if impact >= 10:
                    strengths.append(f"{planet} transit supports {area_display}")
            elif status == "Bad":
                impact = combined_relevance * -20
                score += impact
                if impact <= -10:
                    challenges.append(f"{planet} transit challenges {area_display}")
            
            transit_impacts.append({
                "planet": planet,
                "status": status,
                "house_from_moon": house_from_moon,
                "relevance": round(combined_relevance, 2),
            })
        
        # Track planet influences
        if planet_relevance > 0:
            planet_influences.append({
                "planet": planet,
                "relevance": round(planet_relevance, 2),
                "current_status": status,
                "significations": PLANET_AREA_SIGNIFICATIONS.get(planet, []),
            })
    
    # Determine overall outlook
    if score >= 20:
        outlook = "Positive"
        confidence = "High" if score >= 35 else "Medium"
    elif score <= -20:
        outlook = "Challenging"
        confidence = "High" if score <= -35 else "Medium"
    else:
        outlook = "Neutral"
        confidence = "Low"
    
    # Generate predictions and advice
    prediction = _generate_area_prediction(area_display, outlook, score, strengths, challenges)
    advice = _generate_area_advice(area_display, outlook, strengths, challenges)
    
    return AreaAnalysisResult(
        area=area_normalized,
        area_display_name=area_display,
        overall_outlook=outlook,
        confidence=confidence,
        score=round(score, 2),
        relevant_houses=relevant_houses,
        planet_influences=planet_influences[:5],  # Top 5
        transit_impacts=transit_impacts,
        short_term_prediction=prediction,
        advice=advice,
        strengths=strengths[:3],
        challenges=challenges[:3],
    )


def _generate_area_prediction(
    area: str, outlook: str, score: float, strengths: List, challenges: List
) -> str:
    """Generate short-term prediction for area."""
    if outlook == "Positive":
        if score >= 35:
            return f"Excellent period for {area}. Strong planetary support indicates favorable outcomes."
        return f"Good period for {area}. Most influences are supportive of progress."
    elif outlook == "Challenging":
        if score <= -35:
            return f"Challenging period for {area}. Exercise caution and patience."
        return f"Some challenges expected in {area}. Careful planning recommended."
    else:
        return f"Mixed influences for {area}. Selective approach will yield best results."


def _generate_area_advice(
    area: str, outlook: str, strengths: List, challenges: List
) -> str:
    """Generate advice for area."""
    if outlook == "Positive":
        return f"Capitalize on favorable transits. Good time for initiatives in {area}."
    elif outlook == "Challenging":
        return f"Focus on maintenance rather than new ventures. Patience will help navigate {area} challenges."
    else:
        return f"Balance is key. Leverage strengths while being mindful of potential obstacles in {area}."


def get_all_area_analysis(
    transit_results: List[Dict],
) -> Dict[str, AreaAnalysisResult]:
    """
    Get analysis for all major life areas.
    
    Args:
        transit_results: List of planet transit results
    
    Returns:
        Dict of area name to AreaAnalysisResult
    """
    major_areas = [
        "career", "finance", "health", "marriage", 
        "education", "travel", "family", "spirituality"
    ]
    
    results = {}
    for area in major_areas:
        results[area] = analyze_area(area, transit_results)
    
    return results


# Quick reference for UI
AREA_ICONS = {
    "career": "💼",
    "job": "👔",
    "business": "🏢",
    "finance": "💰",
    "wealth": "💎",
    "health": "❤️",
    "marriage": "💍",
    "relationships": "💕",
    "love": "❤️‍🔥",
    "children": "👶",
    "education": "📚",
    "travel": "✈️",
    "spirituality": "🙏",
    "family": "👨‍👩‍👧‍👦",
    "property": "🏠",
    "legal": "⚖️",
    "government": "🏛️",
}


def get_area_display_info(area: str) -> Dict:
    """Get display info for an area."""
    normalized = normalize_area_query(area) or area.lower()
    return {
        "name": normalized.replace("_", " ").title(),
        "icon": AREA_ICONS.get(normalized, "🔮"),
        "key": normalized,
    }
