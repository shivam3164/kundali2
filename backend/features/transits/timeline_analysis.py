"""
Timeline Analysis - 1-Year Transit Outlook

Calculates monthly transit scores for each life area over a 12-month period.
Provides data for graphing transit trends (0-100 scale).

Based on:
- Vedic Astrology: An Integrated Approach
- Ashtakavarga transit techniques
- Sodhya Pinda timing methods
"""
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from datetime import date, timedelta
import swisseph as swe


@dataclass
class MonthlyScore:
    """Score for a single month"""
    month: int  # 1-12
    year: int
    month_name: str
    raw_score: float  # -100 to +100
    normalized_score: int  # 0 to 100
    trend: str  # "improving", "stable", "declining"
    key_planets: List[str]
    brief_outlook: str


@dataclass
class YearlyTimeline:
    """Complete 12-month timeline for an area"""
    area: str
    area_display_name: str
    start_date: str
    end_date: str
    monthly_scores: List[MonthlyScore]
    best_months: List[int]
    challenging_months: List[int]
    overall_trend: str
    average_score: int
    peak_score: int
    lowest_score: int


# Simplified transit rules for quick calculation
QUICK_TRANSIT_SCORES = {
    "Sun": {3: 15, 6: 15, 10: 20, 11: 20, 1: -15, 2: -10, 4: -10, 5: -10, 7: -10, 8: -15, 9: -10, 12: -15},
    "Moon": {1: 10, 3: 15, 6: 15, 7: 15, 10: 20, 11: 20, 2: -10, 4: -10, 5: -15, 8: -15, 9: -10, 12: -15},
    "Mars": {3: 20, 6: 20, 11: 25, 1: -20, 2: -20, 4: -15, 5: -15, 7: -15, 8: -20, 9: -15, 10: -10, 12: -15},
    "Mercury": {2: 15, 4: 15, 6: 15, 8: 10, 10: 20, 11: 20, 1: -15, 3: -10, 5: -15, 7: -15, 9: -10, 12: -15},
    "Jupiter": {2: 20, 5: 25, 7: 20, 9: 25, 11: 25, 1: -15, 3: -15, 4: -15, 6: -15, 8: -20, 10: -15, 12: -20},
    "Venus": {1: 15, 2: 20, 3: 15, 4: 15, 5: 20, 9: 20, 11: 20, 12: 15, 6: -15, 7: -20, 8: -20, 10: -15},
    "Saturn": {3: 20, 6: 20, 11: 25, 1: -20, 2: -15, 4: -20, 5: -20, 7: -20, 8: -25, 9: -20, 10: -15, 12: -20},
    "Rahu": {3: 15, 6: 15, 11: 20, 1: -15, 2: -10, 4: -15, 5: -15, 7: -15, 8: -20, 9: -15, 10: -10, 12: -15},
    "Ketu": {3: 10, 6: 10, 11: 15, 9: 10, 12: 10, 1: -15, 2: -10, 4: -10, 5: -10, 7: -10, 8: -15, 10: -10},
}

# Area-specific planet weights
AREA_PLANET_WEIGHTS = {
    "career": {"Sun": 1.5, "Saturn": 1.3, "Mercury": 1.2, "Jupiter": 1.0, "Mars": 0.8},
    "finance": {"Jupiter": 1.5, "Venus": 1.3, "Mercury": 1.2, "Moon": 1.0, "Sun": 0.8},
    "health": {"Sun": 1.5, "Moon": 1.3, "Mars": 1.2, "Saturn": 1.0, "Mercury": 0.8},
    "marriage": {"Venus": 1.5, "Jupiter": 1.3, "Moon": 1.2, "Mars": 1.0, "Mercury": 0.8},
    "education": {"Jupiter": 1.5, "Mercury": 1.5, "Moon": 1.2, "Sun": 1.0, "Venus": 0.8},
    "travel": {"Moon": 1.3, "Mercury": 1.2, "Rahu": 1.3, "Jupiter": 1.0, "Venus": 0.8},
    "family": {"Moon": 1.5, "Jupiter": 1.3, "Venus": 1.2, "Mercury": 1.0, "Sun": 0.8},
    "spirituality": {"Jupiter": 1.5, "Ketu": 1.5, "Moon": 1.2, "Sun": 1.0, "Saturn": 1.0},
    "property": {"Mars": 1.5, "Venus": 1.3, "Jupiter": 1.2, "Saturn": 1.0, "Moon": 0.8},
    "children": {"Jupiter": 1.5, "Venus": 1.3, "Moon": 1.2, "Mercury": 1.0, "Sun": 0.8},
}

MONTH_NAMES = [
    "", "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]


def get_planetary_positions_for_date(target_date: date) -> Dict[str, float]:
    """Get planetary positions for a specific date."""
    swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)
    jd = swe.julday(target_date.year, target_date.month, target_date.day, 12.0)
    
    planets = {
        "Sun": swe.SUN,
        "Moon": swe.MOON,
        "Mars": swe.MARS,
        "Mercury": swe.MERCURY,
        "Jupiter": swe.JUPITER,
        "Venus": swe.VENUS,
        "Saturn": swe.SATURN,
        "Rahu": swe.TRUE_NODE,
    }
    
    positions = {}
    for name, code in planets.items():
        result = swe.calc_ut(jd, code, swe.FLG_SIDEREAL)
        positions[name] = result[0][0]
    
    positions["Ketu"] = (positions["Rahu"] + 180) % 360
    return positions


def get_house_from_moon(transit_longitude: float, natal_moon_sign: int) -> int:
    """Calculate house from Moon sign."""
    transit_sign = int(transit_longitude // 30) + 1
    house = ((transit_sign - natal_moon_sign) % 12) + 1
    if house == 0:
        house = 12
    return house


def calculate_month_score(
    natal_moon_sign: int,
    target_date: date,
    area: str
) -> Tuple[float, List[str], str]:
    """
    Calculate transit score for a specific month.
    
    Returns:
        Tuple of (raw_score, key_planets, brief_outlook)
    """
    positions = get_planetary_positions_for_date(target_date)
    
    total_score = 0.0
    key_planets = []
    planet_weights = AREA_PLANET_WEIGHTS.get(area, {})
    
    for planet, longitude in positions.items():
        house = get_house_from_moon(longitude, natal_moon_sign)
        base_score = QUICK_TRANSIT_SCORES.get(planet, {}).get(house, 0)
        
        # Apply area-specific weight
        weight = planet_weights.get(planet, 1.0)
        weighted_score = base_score * weight
        
        total_score += weighted_score
        
        # Track significant planets
        if abs(weighted_score) >= 15:
            key_planets.append(f"{planet}({'+'if weighted_score > 0 else '-'})")
    
    # Generate brief outlook
    if total_score >= 30:
        outlook = "Excellent period"
    elif total_score >= 10:
        outlook = "Good period"
    elif total_score >= -10:
        outlook = "Mixed influences"
    elif total_score >= -30:
        outlook = "Challenging period"
    else:
        outlook = "Difficult period"
    
    return total_score, key_planets[:3], outlook


def normalize_score(raw_score: float) -> int:
    """
    Convert raw score (-100 to +100) to normalized (0 to 100).
    
    50 = neutral
    >50 = positive
    <50 = negative
    """
    # Clamp raw score to reasonable range
    clamped = max(-80, min(80, raw_score))
    # Linear mapping: -80 -> 10, 0 -> 50, +80 -> 90
    normalized = int(50 + (clamped * 0.5))
    return max(0, min(100, normalized))


def add_months(source_date: date, months: int) -> date:
    """Add months to a date, handling year boundaries."""
    month = source_date.month - 1 + months
    year = source_date.year + month // 12
    month = month % 12 + 1
    day = min(source_date.day, [31, 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28, 
                                 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1])
    return date(year, month, day)


def calculate_yearly_timeline(
    natal_moon_sign: int,
    area: str,
    start_date: Optional[date] = None
) -> YearlyTimeline:
    """
    Calculate 12-month transit timeline for a life area.
    
    Args:
        natal_moon_sign: Sign number (1-12) of natal Moon
        area: Life area to analyze
        start_date: Starting date (defaults to today)
    
    Returns:
        YearlyTimeline with monthly scores
    """
    if start_date is None:
        start_date = date.today()
    
    monthly_scores = []
    prev_score = None
    
    for i in range(12):
        # Calculate for middle of each month
        month_date = add_months(start_date, i)
        target_date = date(month_date.year, month_date.month, 15)
        
        raw_score, key_planets, outlook = calculate_month_score(
            natal_moon_sign, target_date, area
        )
        
        normalized = normalize_score(raw_score)
        
        # Determine trend
        if prev_score is None:
            trend = "stable"
        elif normalized > prev_score + 5:
            trend = "improving"
        elif normalized < prev_score - 5:
            trend = "declining"
        else:
            trend = "stable"
        
        monthly_scores.append(MonthlyScore(
            month=target_date.month,
            year=target_date.year,
            month_name=MONTH_NAMES[target_date.month],
            raw_score=round(raw_score, 1),
            normalized_score=normalized,
            trend=trend,
            key_planets=key_planets,
            brief_outlook=outlook,
        ))
        
        prev_score = normalized
    
    # Calculate summary statistics
    scores = [m.normalized_score for m in monthly_scores]
    avg_score = int(sum(scores) / len(scores))
    peak_score = max(scores)
    lowest_score = min(scores)
    
    # Find best and challenging months
    best_months = [m.month for m in monthly_scores if m.normalized_score >= 60]
    challenging_months = [m.month for m in monthly_scores if m.normalized_score <= 40]
    
    # Determine overall trend
    first_half_avg = sum(scores[:6]) / 6
    second_half_avg = sum(scores[6:]) / 6
    if second_half_avg > first_half_avg + 5:
        overall_trend = "Improving over the year"
    elif second_half_avg < first_half_avg - 5:
        overall_trend = "Declining over the year"
    else:
        overall_trend = "Stable throughout the year"
    
    # Calculate end date
    end_date = add_months(start_date, 11)
    
    return YearlyTimeline(
        area=area,
        area_display_name=area.replace("_", " ").title(),
        start_date=start_date.strftime("%Y-%m-%d"),
        end_date=end_date.strftime("%Y-%m-%d"),
        monthly_scores=monthly_scores,
        best_months=best_months,
        challenging_months=challenging_months,
        overall_trend=overall_trend,
        average_score=avg_score,
        peak_score=peak_score,
        lowest_score=lowest_score,
    )


def calculate_all_areas_timeline(
    natal_moon_sign: int,
    start_date: Optional[date] = None
) -> Dict[str, YearlyTimeline]:
    """
    Calculate 12-month timeline for all major life areas.
    
    Returns dict with area name -> YearlyTimeline
    """
    areas = [
        "career", "finance", "health", "marriage",
        "education", "travel", "family", "spirituality",
        "property", "children"
    ]
    
    results = {}
    for area in areas:
        results[area] = calculate_yearly_timeline(natal_moon_sign, area, start_date)
    
    return results
