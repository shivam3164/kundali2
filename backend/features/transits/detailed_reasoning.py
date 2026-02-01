"""
Detailed Reasoning Engine for Transit Analysis

This module provides comprehensive explanations for transit predictions,
including the astrological reasoning behind each conclusion.

Based on:
- BPHS (Brihat Parashara Hora Shastra)
- Vedic Astrology: An Integrated Approach (P.V.R. Narasimha Rao)
  - Chapter 25: Transits and Natal References
  - Chapter 26: Transits: Miscellaneous Topics
"""
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass


@dataclass
class DetailedExplanation:
    """Complete explanation for a transit prediction"""
    summary: str
    conclusion_steps: List[str]  # Step-by-step reasoning
    why_this_conclusion: str  # Explanation of the why
    supporting_factors: List[Dict]
    challenging_factors: List[Dict]
    textbook_references: List[str]
    confidence_breakdown: Dict[str, float]


# Transit quality descriptions from textbook Tables 53-59
TRANSIT_RESULTS_DESCRIPTIONS = {
    "Sun": {
        1: {"quality": "Bad", "result": "Financial loss, many travels, discomfort"},
        2: {"quality": "Bad", "result": "Unhappiness, eye troubles, fear"},
        3: {"quality": "Good", "result": "Wealth, good health, victory"},
        4: {"quality": "Bad", "result": "Marital disharmony, loss of name"},
        5: {"quality": "Bad", "result": "Bad health, fear from enemies"},
        6: {"quality": "Good", "result": "Success over enemies, good health"},
        7: {"quality": "Bad", "result": "Travels, physical pain"},
        8: {"quality": "Bad", "result": "Disease, setbacks in marriage"},
        9: {"quality": "Bad", "result": "Mental worries, obstacles"},
        10: {"quality": "Good", "result": "Success, honors, gains"},
        11: {"quality": "Good", "result": "Good health, prosperity, honors"},
        12: {"quality": "Bad", "result": "Expenditure, losses"},
    },
    "Moon": {
        1: {"quality": "Good", "result": "Comfort, good spirits"},
        2: {"quality": "Bad", "result": "Obstacles, losses"},
        3: {"quality": "Good", "result": "Gains, happiness"},
        4: {"quality": "Bad", "result": "Lack of peace of mind, distrust"},
        5: {"quality": "Bad", "result": "Failures, disappointments, sadness"},
        6: {"quality": "Good", "result": "Happiness, health, wealth"},
        7: {"quality": "Good", "result": "Respect, gains"},
        8: {"quality": "Bad", "result": "Losses, tension, worries"},
        9: {"quality": "Bad", "result": "Mental uneasiness"},
        10: {"quality": "Good", "result": "Success, gains, authority"},
        11: {"quality": "Good", "result": "Prosperity, comforts, gains"},
        12: {"quality": "Bad", "result": "Injuries, expenditure, sadness"},
    },
    "Mars": {
        1: {"quality": "Bad", "result": "Troubles, bodily afflictions"},
        2: {"quality": "Bad", "result": "Accidents, losses, thefts, quarrels"},
        3: {"quality": "Good", "result": "Gains, power, wealth"},
        4: {"quality": "Bad", "result": "Stomach problems, fevers, bad health"},
        5: {"quality": "Bad", "result": "Troubles from enemies, trouble with children"},
        6: {"quality": "Good", "result": "Success over enemies, wealth, well-being"},
        7: {"quality": "Bad", "result": "Quarrels, marital troubles, eye problems"},
        8: {"quality": "Bad", "result": "Worries, accidents, bad name, losses"},
        9: {"quality": "Bad", "result": "Losses, insults, illness"},
        10: {"quality": "Bad", "result": "Change of place, unexpected wealth"},
        11: {"quality": "Good", "result": "Authority, gains, good name"},
        12: {"quality": "Bad", "result": "Expenses, quarrels with wife, diseases"},
    },
    "Mercury": {
        1: {"quality": "Bad", "result": "Quarrels, imprisonment, losses, poor advice"},
        2: {"quality": "Good", "result": "Success, wealth, gains"},
        3: {"quality": "Bad", "result": "Wandering, losses, trouble from authorities"},
        4: {"quality": "Good", "result": "Prosperity in family, gains"},
        5: {"quality": "Bad", "result": "Quarrels with wife and children, suffering"},
        6: {"quality": "Good", "result": "Renown, success, ornaments"},
        7: {"quality": "Bad", "result": "Quarrels, mental discomfort, addictions"},
        8: {"quality": "Good", "result": "Childbirth, happiness, gains, success"},
        9: {"quality": "Bad", "result": "Mental worries, obstacles"},
        10: {"quality": "Good", "result": "Money, happiness, domestic harmony, success"},
        11: {"quality": "Good", "result": "Childbirth, happiness, wealth"},
        12: {"quality": "Bad", "result": "Disease, domestic disharmony, losses"},
    },
    "Jupiter": {
        1: {"quality": "Bad", "result": "Loss of money and intelligence, wandering"},
        2: {"quality": "Good", "result": "Happiness, domestic harmony, success"},
        3: {"quality": "Bad", "result": "Obstacles, loss of position, travels"},
        4: {"quality": "Bad", "result": "Troubles, defeat, losses"},
        5: {"quality": "Good", "result": "Childbirth, intelligence, prosperity, wealth"},
        6: {"quality": "Bad", "result": "Mental uneasiness, enemies, worries"},
        7: {"quality": "Good", "result": "Health, happiness, erotic pleasures, well-being"},
        8: {"quality": "Bad", "result": "Disease, imprisonment, illness, grief"},
        9: {"quality": "Good", "result": "Success, wealth, childbirth, religiousness"},
        10: {"quality": "Bad", "result": "Loss of position and money, ill-health"},
        11: {"quality": "Good", "result": "Recovery of health and position, happiness"},
        12: {"quality": "Bad", "result": "Fall from grace, misconduct, grief"},
    },
    "Venus": {
        1: {"quality": "Good", "result": "Comforts, pleasures, happiness, good spirits"},
        2: {"quality": "Good", "result": "Money, fortune, erotic pleasures, childbirth"},
        3: {"quality": "Good", "result": "Respect, wealth, good spirits"},
        4: {"quality": "Good", "result": "Prosperity, success, comforts"},
        5: {"quality": "Good", "result": "Fame, power, good name"},
        6: {"quality": "Bad", "result": "Loss of fame, bad name, quarrels"},
        7: {"quality": "Bad", "result": "Humiliation, disease, troubles"},
        8: {"quality": "Bad", "result": "Fears, mental worries, injuries, troubles"},
        9: {"quality": "Good", "result": "Fortune, luxuries, marital happiness"},
        10: {"quality": "Bad", "result": "Virtuous acts, troubles, disgrace"},
        11: {"quality": "Good", "result": "Gains, happiness, prosperity, comforts"},
        12: {"quality": "Good", "result": "New friends, money, pleasures, gains"},
    },
    "Saturn": {
        1: {"quality": "Bad", "result": "Fear of incarceration, worries, foreign trips"},
        2: {"quality": "Bad", "result": "Physical weakness, discomfort, unhappiness"},
        3: {"quality": "Good", "result": "Wealth, health, happiness, all-round success"},
        4: {"quality": "Bad", "result": "Stomach problems, wickedness, family separation"},
        5: {"quality": "Bad", "result": "Separation from children, uneasiness, quarrels"},
        6: {"quality": "Good", "result": "Freedom from disease and enemies, success"},
        7: {"quality": "Bad", "result": "Wandering, spouse quarrels, authority trouble"},
        8: {"quality": "Bad", "result": "Suffering, loss of status, imprisonment"},
        9: {"quality": "Bad", "result": "Diseases, suffering, loss of status"},
        10: {"quality": "Bad", "result": "Loss of money, bad name, career changes"},
        11: {"quality": "Good", "result": "Wealth, success, gains"},
        12: {"quality": "Bad", "result": "Grief, misery, losses, ill-health, frustration"},
    },
    "Rahu": {
        1: {"quality": "Bad", "result": "Fear, worries, foreign influences"},
        2: {"quality": "Bad", "result": "Financial losses, family discord"},
        3: {"quality": "Good", "result": "Courage, gains through unconventional means"},
        4: {"quality": "Bad", "result": "Domestic troubles, mother's health concerns"},
        5: {"quality": "Bad", "result": "Confusion, trouble with children"},
        6: {"quality": "Good", "result": "Victory over enemies, overcoming obstacles"},
        7: {"quality": "Bad", "result": "Partnership troubles, foreign connections"},
        8: {"quality": "Bad", "result": "Sudden troubles, hidden enemies"},
        9: {"quality": "Bad", "result": "Troubles with father, religious confusion"},
        10: {"quality": "Bad", "result": "Career instability, reputation issues"},
        11: {"quality": "Good", "result": "Gains through foreign sources, networking"},
        12: {"quality": "Bad", "result": "Expenses, foreign residence, isolation"},
    },
    "Ketu": {
        1: {"quality": "Bad", "result": "Health issues, spiritual confusion"},
        2: {"quality": "Bad", "result": "Speech problems, family detachment"},
        3: {"quality": "Good", "result": "Courage, spiritual pursuits"},
        4: {"quality": "Bad", "result": "Emotional detachment, property issues"},
        5: {"quality": "Bad", "result": "Detachment from children, past karma"},
        6: {"quality": "Good", "result": "Victory through surrender, healing"},
        7: {"quality": "Bad", "result": "Partnership dissolution, spiritual seeking"},
        8: {"quality": "Bad", "result": "Transformation, occult experiences"},
        9: {"quality": "Good", "result": "Spiritual advancement, liberation"},
        10: {"quality": "Bad", "result": "Career detachment, service orientation"},
        11: {"quality": "Good", "result": "Gains through letting go"},
        12: {"quality": "Good", "result": "Moksha, spiritual liberation, meditation"},
    },
}

# House-Area correlations
HOUSE_AREA_MEANING = {
    1: "self, body, personality, general well-being",
    2: "wealth, family, speech, food, savings",
    3: "siblings, courage, communication, short travels, skills",
    4: "mother, home, property, vehicles, happiness, education",
    5: "children, intelligence, creativity, romance, speculation",
    6: "enemies, diseases, debts, service, daily work, obstacles",
    7: "spouse, marriage, partnerships, business, public dealings",
    8: "longevity, obstacles, sudden events, inheritance, transformation",
    9: "father, fortune, dharma, higher education, long journeys",
    10: "career, profession, status, authority, government, fame",
    11: "gains, income, elder siblings, friends, aspirations",
    12: "losses, expenses, foreign residence, moksha, isolation",
}

# Planet-Area natural significations
PLANET_NATURAL_SIGNIFICATIONS = {
    "Sun": "soul, authority, government, health, father, willpower",
    "Moon": "mind, emotions, mother, public, travel, peace",
    "Mars": "courage, property, siblings, legal matters, accidents, energy",
    "Mercury": "education, business, communication, intelligence, friends",
    "Jupiter": "wisdom, children, education, spirituality, fortune, expansion",
    "Venus": "marriage, relationships, love, vehicles, wealth, comforts",
    "Saturn": "longevity, livelihood, fears, obstacles, foreign, delays",
    "Rahu": "foreign, technology, unconventional, sudden changes, obsession",
    "Ketu": "spirituality, moksha, detachment, loss, past karma",
}


def generate_detailed_explanation(
    area: str,
    area_result,
    transit_results: List[Dict],
) -> DetailedExplanation:
    """
    Generate a detailed explanation with reasoning for an area prediction.
    
    Args:
        area: The life area being analyzed
        area_result: The AreaAnalysisResult object from area_analysis
        transit_results: List of planet transit results
    
    Returns:
        DetailedExplanation with complete reasoning
    """
    # Convert area_result to dict if it's an object
    if hasattr(area_result, 'score'):
        area_analysis = {
            "score": area_result.score,
            "outlook": area_result.overall_outlook,
            "strengths": area_result.strengths,
            "challenges": area_result.challenges,
        }
    else:
        area_analysis = area_result
    
    conclusion_steps = []
    supporting_factors = []
    challenging_factors = []
    textbook_refs = []
    confidence_breakdown = {}
    
    # Step 1: Identify relevant houses for this area
    area_houses = _get_area_houses(area)
    conclusion_steps.append(
        f"Step 1: Identified relevant houses for {area}: {area_houses}. "
        f"These houses govern {_get_house_meanings(area_houses)}."
    )
    textbook_refs.append("BPHS Ch. 7: Houses and Their Significations")
    
    # Step 2: Analyze each relevant planet transit
    for transit in transit_results:
        planet = transit.get("planet", "")
        house = transit.get("house_from_moon", 0)
        status = transit.get("final_status", "Neutral")
        
        # Get textbook result for this transit
        textbook_result = TRANSIT_RESULTS_DESCRIPTIONS.get(planet, {}).get(house, {})
        
        # Check if this transit affects the area
        is_relevant = (
            house in area_houses or
            _planet_signifies_area(planet, area)
        )
        
        if is_relevant:
            detail = {
                "planet": planet,
                "house": house,
                "status": status,
                "textbook_result": textbook_result.get("result", "mixed results"),
                "reasoning": f"{planet} transiting {house}th house from Moon "
                            f"indicates: {textbook_result.get('result', 'mixed results')}"
            }
            
            if status == "Good":
                supporting_factors.append(detail)
                confidence_breakdown[f"{planet}_support"] = 0.15
            elif status == "Bad":
                challenging_factors.append(detail)
                confidence_breakdown[f"{planet}_challenge"] = -0.15
    
    # Step 3: Build the reasoning
    conclusion_steps.append(
        f"Step 2: Analyzed {len(transit_results)} planetary transits. "
        f"Found {len(supporting_factors)} supporting and {len(challenging_factors)} challenging factors."
    )
    textbook_refs.append("BPHS Tables 53-59: Transit Results from Moon")
    
    # Step 4: Synthesize conclusion
    score = area_analysis.get("score", 0)
    outlook = area_analysis.get("outlook", "Neutral")
    
    if score >= 20:
        why = (
            f"The overall score of {score:.1f} indicates favorable transits for {area}. "
            f"This is because {len(supporting_factors)} planets are positively influencing "
            f"the houses related to {area} ({', '.join(map(str, area_houses))}), "
            f"while only {len(challenging_factors)} planets pose challenges."
        )
    elif score <= -20:
        why = (
            f"The overall score of {score:.1f} indicates challenging transits for {area}. "
            f"This is because {len(challenging_factors)} planets are creating obstacles in "
            f"the houses related to {area} ({', '.join(map(str, area_houses))}), "
            f"outweighing the {len(supporting_factors)} supporting influences."
        )
    else:
        why = (
            f"The overall score of {score:.1f} indicates mixed transits for {area}. "
            f"The {len(supporting_factors)} supporting factors are balanced by "
            f"{len(challenging_factors)} challenging factors. Selective action is recommended."
        )
    
    conclusion_steps.append(f"Step 3: Calculated weighted score: {score:.1f} → {outlook} outlook")
    conclusion_steps.append(f"Step 4: {why}")
    textbook_refs.append("Vedic Astrology Ch. 25: Transits and Natal References")
    
    # Generate summary
    summary = _generate_detailed_summary(area, outlook, supporting_factors, challenging_factors)
    
    return DetailedExplanation(
        summary=summary,
        conclusion_steps=conclusion_steps,
        why_this_conclusion=why,
        supporting_factors=supporting_factors,
        challenging_factors=challenging_factors,
        textbook_references=textbook_refs,
        confidence_breakdown=confidence_breakdown,
    )


def _get_area_houses(area: str) -> List[int]:
    """Get the houses relevant to an area."""
    area_house_map = {
        "career": [10, 6, 2],
        "job": [6, 10, 2],
        "business": [7, 10, 11],
        "finance": [2, 11, 5, 9],
        "wealth": [2, 11, 5],
        "health": [1, 6, 8],
        "marriage": [7, 2, 4, 11],
        "relationships": [7, 5, 11],
        "love": [5, 7, 11],
        "education": [4, 5, 9],
        "travel": [3, 9, 12],
        "foreign": [9, 12, 7],
        "family": [2, 4, 5],
        "children": [5, 9, 11],
        "spirituality": [9, 12, 5],
        "property": [4, 2, 11],
        "legal": [6, 9, 7],
        "general": [1, 2, 4, 7, 10],
    }
    return area_house_map.get(area, [1, 2, 4, 7, 10])


def _get_house_meanings(houses: List[int]) -> str:
    """Get the meanings of a list of houses."""
    meanings = []
    for h in houses[:3]:  # Limit to 3 for brevity
        if h in HOUSE_AREA_MEANING:
            meanings.append(HOUSE_AREA_MEANING[h].split(",")[0].strip())
    return ", ".join(meanings)


def _planet_signifies_area(planet: str, area: str) -> bool:
    """Check if a planet naturally signifies an area."""
    planet_areas = {
        "Sun": ["career", "health", "government", "father"],
        "Moon": ["family", "health", "travel", "mother"],
        "Mars": ["property", "health", "legal", "siblings"],
        "Mercury": ["education", "business", "career", "communication"],
        "Jupiter": ["finance", "children", "education", "spirituality", "wealth"],
        "Venus": ["marriage", "relationships", "finance", "love"],
        "Saturn": ["career", "longevity", "foreign", "job"],
        "Rahu": ["foreign", "career", "technology"],
        "Ketu": ["spirituality", "moksha", "health"],
    }
    return area in planet_areas.get(planet, [])


def _generate_detailed_summary(
    area: str,
    outlook: str,
    supporting: List[Dict],
    challenging: List[Dict]
) -> str:
    """Generate a detailed summary paragraph."""
    # Build supporting planets list
    support_planets = [f["planet"] for f in supporting]
    challenge_planets = [f["planet"] for f in challenging]
    
    if outlook == "Positive":
        summary = (
            f"Your {area} outlook is positive based on transit analysis. "
        )
        if support_planets:
            summary += (
                f"The favorable transits of {', '.join(support_planets[:3])} "
                f"are creating supportive conditions. "
            )
        if supporting:
            summary += f"Specifically, {supporting[0]['reasoning']}. "
        summary += "This is a good period to pursue your goals in this area."
        
    elif outlook == "Challenging":
        summary = (
            f"Your {area} outlook shows some challenges based on transit analysis. "
        )
        if challenge_planets:
            summary += (
                f"The transits of {', '.join(challenge_planets[:3])} "
                f"are creating obstacles. "
            )
        if challenging:
            summary += f"Specifically, {challenging[0]['reasoning']}. "
        summary += "Patience and careful planning are recommended during this period."
        
    else:
        summary = (
            f"Your {area} outlook is mixed based on transit analysis. "
        )
        if support_planets and challenge_planets:
            summary += (
                f"While {', '.join(support_planets[:2])} provide support, "
                f"{', '.join(challenge_planets[:2])} create some resistance. "
            )
        summary += "Selective action focusing on strengths will yield best results."
    
    return summary


def get_transit_description(planet: str, house: int) -> Dict:
    """Get the textbook description for a transit."""
    return TRANSIT_RESULTS_DESCRIPTIONS.get(planet, {}).get(house, {
        "quality": "Neutral",
        "result": "Mixed results expected"
    })
