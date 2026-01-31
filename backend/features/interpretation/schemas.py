"""
Interpretation Feature - Pydantic Schemas
Request and response schemas for chart interpretation
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from enum import Enum


# ============================================
# ENUMS
# ============================================

class InterpretationArea(str, Enum):
    """Areas of life for interpretation"""
    PERSONALITY = "personality"
    CAREER = "career"
    RELATIONSHIPS = "relationships"
    HEALTH = "health"
    WEALTH = "wealth"
    SPIRITUALITY = "spirituality"
    EDUCATION = "education"
    FAMILY = "family"
    OVERALL = "overall"


class InterpretationDepth(str, Enum):
    """Depth of interpretation"""
    BRIEF = "brief"
    STANDARD = "standard"
    DETAILED = "detailed"


# ============================================
# REQUEST SCHEMAS
# ============================================

class InterpretationRequest(BaseModel):
    """Interpretation request"""
    
    # Can provide pre-calculated data
    chart_data: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Pre-calculated chart data"
    )
    yoga_data: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Pre-calculated yoga data"
    )
    dasha_data: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Pre-calculated dasha data"
    )
    
    # Or birth details
    year: Optional[int] = Field(default=None, description="Birth year")
    month: Optional[int] = Field(default=None, ge=1, le=12, description="Birth month")
    day: Optional[int] = Field(default=None, ge=1, le=31, description="Birth day")
    hour: Optional[int] = Field(default=12, ge=0, le=23, description="Birth hour")
    minute: Optional[int] = Field(default=0, ge=0, le=59, description="Birth minute")
    lat: Optional[float] = Field(default=None, description="Birth latitude")
    lon: Optional[float] = Field(default=None, description="Birth longitude")
    ayanamsa: str = Field(default="lahiri", description="Ayanamsa system")
    
    # Interpretation options
    areas: Optional[List[InterpretationArea]] = Field(
        default=None,
        description="Specific areas to interpret (all if not specified)"
    )
    depth: InterpretationDepth = Field(
        default=InterpretationDepth.STANDARD,
        description="Depth of interpretation"
    )
    include_remedies: bool = Field(
        default=True,
        description="Include remedial measures"
    )
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "year": 1990,
                    "month": 5,
                    "day": 15,
                    "hour": 10,
                    "minute": 30,
                    "lat": 28.6139,
                    "lon": 77.2090,
                    "areas": ["personality", "career"],
                    "depth": "detailed"
                }
            ]
        }
    }


# ============================================
# RESPONSE SCHEMAS
# ============================================

class PlanetInterpretation(BaseModel):
    """Interpretation for a single planet"""
    planet: str
    house: int
    sign: str
    dignity: str
    
    # Interpretation
    general: str
    house_effects: str
    sign_effects: str
    
    # Strengths and challenges
    strengths: List[str]
    challenges: List[str]


class HouseInterpretation(BaseModel):
    """Interpretation for a single house"""
    house_number: int
    sign: str
    lord: str
    lord_house: int
    
    # Planets in house
    planets: List[str]
    
    # Interpretation
    general: str
    life_area: str
    with_planets: str
    lord_placement: str


class AreaInterpretation(BaseModel):
    """Interpretation for a life area"""
    area: InterpretationArea
    title: str
    
    # Analysis
    key_indicators: List[str]
    interpretation: str
    
    # Predictions
    strengths: List[str]
    challenges: List[str]
    opportunities: List[str]
    
    # Remedies (if requested)
    remedies: Optional[List[str]] = None


class OverallSummary(BaseModel):
    """Overall chart summary"""
    # Core identity
    ascendant_analysis: str
    moon_sign_analysis: str
    sun_sign_analysis: str
    
    # Key themes
    dominant_element: str
    dominant_quality: str
    key_life_themes: List[str]
    
    # Strengths and challenges
    major_strengths: List[str]
    major_challenges: List[str]
    
    # Life path
    life_purpose: str
    karmic_lessons: List[str]


class InterpretationResponse(BaseModel):
    """Complete interpretation response"""
    
    # Input echo
    birth_data: Dict[str, Any]
    
    # Overall summary
    overall_summary: OverallSummary
    
    # Detailed interpretations
    planet_interpretations: Dict[str, PlanetInterpretation]
    house_interpretations: Dict[str, HouseInterpretation]
    area_interpretations: Dict[str, AreaInterpretation]
    
    # Yoga effects
    yoga_effects: List[Dict[str, str]]
    
    # Current Dasha interpretation
    current_dasha_interpretation: Optional[Dict[str, str]] = None
    
    # Remedies
    recommended_remedies: Optional[List[Dict[str, str]]] = None
