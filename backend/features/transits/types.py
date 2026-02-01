"""
Type definitions for Transit Analysis.
Source: BPHS (Foundation) + Vedic Astrology: An Integrated Approach (Enhancement)
"""
from typing import TypedDict, Optional, Dict, List
from enum import Enum
from pydantic import BaseModel


class TransitStatus(str, Enum):
    """Transit result status classification."""
    HIGHLY_FAVORABLE = "Highly Favorable"
    FAVORABLE = "Favorable"
    NEUTRAL = "Neutral"
    UNFAVORABLE = "Unfavorable"
    HIGHLY_UNFAVORABLE = "Highly Unfavorable"
    OBSTRUCTED = "Obstructed"


class MurthiType(str, Enum):
    """Murthi (Form) classification based on Moon's position at rasi entry."""
    SWARNA = "Swarna"   # Golden - Highly Favorable (Houses 1, 6, 11)
    RAJATA = "Rajata"   # Silver - Favorable (Houses 2, 5, 9)
    TAAMRA = "Taamra"   # Copper - Unfavorable (Houses 3, 7, 10)
    LOHA = "Loha"       # Iron - Highly Unfavorable (Houses 4, 8, 12)


class TaraType(str, Enum):
    """Tara (Star) classification based on nakshatra distance from birth star."""
    JANMA = "Janma"             # Birth (1, 10, 19) - Mixed
    SAMPAT = "Sampat"           # Wealth (2, 11, 20) - Good
    VIPAT = "Vipat"             # Danger (3, 12, 21) - Bad
    KSHEMA = "Kshema"           # Well-being (4, 13, 22) - Good
    PRATYAK = "Pratyak"         # Obstacles (5, 14, 23) - Bad
    SAADHANA = "Saadhana"       # Achievement (6, 15, 24) - Good
    NAIDHANA = "Naidhana"       # Death (7, 16, 25) - Bad
    MITRA = "Mitra"             # Friend (8, 17, 26) - Good
    PARAMA_MITRA = "Parama Mitra"  # Best Friend (9, 18, 27) - Good


# Pydantic models for API
class VedhaResult(BaseModel):
    """Result of Vedha (obstruction) analysis."""
    is_obstructed: bool
    obstructing_planet: Optional[str] = None
    vedha_house: Optional[int] = None


class TaraResult(BaseModel):
    """Result of Tara (star) analysis."""
    tara_name: str
    tara_quality: str  # Good, Bad, Mixed
    nakshatra_distance: int
    special_nakshatra: Optional[str] = None


class MurthiResult(BaseModel):
    """Result of Murthi (form) analysis."""
    murthi_type: str
    moon_house_at_entry: int
    result_quality: str


class PlanetTransitResult(BaseModel):
    """Complete transit result for a single planet."""
    planet: str
    transit_sign: int
    transit_sign_name: str
    transit_nakshatra: int
    transit_nakshatra_name: str
    house_from_moon: int
    
    # BPHS Foundation
    basic_status: str
    basic_prediction: str
    
    # Vedic Astro Enhancements
    vedha: VedhaResult
    tara: TaraResult
    murthi: Optional[MurthiResult] = None
    
    # Final synthesized result
    final_status: str
    final_prediction: str
    confidence: str  # High, Medium, Low


class TransitSummary(BaseModel):
    """Summary of overall transit analysis."""
    favorable_transits: int
    unfavorable_transits: int
    obstructed_transits: int
    overall_assessment: str


class TransitReport(BaseModel):
    """Complete transit analysis report."""
    natal_moon_sign: str
    natal_moon_nakshatra: str
    transit_date: str
    analysis_results: List[PlanetTransitResult]
    summary: TransitSummary
    favorable_planets: List[str]
    unfavorable_planets: List[str]


# Request/Response models for API
class TransitRequest(BaseModel):
    """Request model for transit analysis."""
    # Natal chart data
    year: int
    month: int
    day: int
    hour: int
    minute: int
    lat: float
    lon: float
    
    # Transit date (optional - defaults to current date)
    transit_year: Optional[int] = None
    transit_month: Optional[int] = None
    transit_day: Optional[int] = None


class TransitResponse(BaseModel):
    """Response model for transit analysis."""
    success: bool
    data: Optional[TransitReport] = None
    error: Optional[str] = None


# Constants
SIGN_NAMES = [
    "", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

NAKSHATRA_NAMES = [
    "", "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
    "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
    "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha",
    "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishtha",
    "Shatabhisha", "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

PLANET_NAMES = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn", "Rahu", "Ketu"]
