"""
Chart Feature - Pydantic Schemas
Request and response schemas for the chart API
"""

from pydantic import BaseModel, Field, field_validator
from typing import Optional, Dict, List, Any
from datetime import datetime


# ============================================
# REQUEST SCHEMAS
# ============================================

class ChartRequest(BaseModel):
    """Birth chart calculation request"""
    
    # Date
    year: int = Field(..., ge=1, le=3000, description="Birth year")
    month: int = Field(..., ge=1, le=12, description="Birth month (1-12)")
    day: int = Field(..., ge=1, le=31, description="Birth day (1-31)")
    
    # Time
    hour: int = Field(default=12, ge=0, le=23, description="Birth hour (0-23)")
    minute: int = Field(default=0, ge=0, le=59, description="Birth minute (0-59)")
    second: int = Field(default=0, ge=0, le=59, description="Birth second (0-59)")
    
    # Location
    lat: float = Field(..., ge=-90, le=90, description="Latitude (-90 to 90)")
    lon: float = Field(..., ge=-180, le=180, description="Longitude (-180 to 180)")
    
    # Optional
    name: Optional[str] = Field(default=None, max_length=100, description="Name of the person")
    place_name: Optional[str] = Field(default=None, max_length=200, description="Birth place name")
    timezone: Optional[str] = Field(default=None, description="Timezone (e.g., 'Asia/Kolkata')")
    ayanamsa: str = Field(default="lahiri", description="Ayanamsa system to use")
    
    @field_validator('ayanamsa')
    @classmethod
    def validate_ayanamsa(cls, v: str) -> str:
        valid = ['lahiri', 'raman', 'krishnamurti', 'fagan_bradley', 'true_chitrapaksha']
        if v.lower() not in valid:
            raise ValueError(f"Invalid ayanamsa. Must be one of: {valid}")
        return v.lower()
    
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
                    "name": "Test Person",
                    "place_name": "New Delhi, India",
                    "ayanamsa": "lahiri"
                }
            ]
        }
    }


# ============================================
# RESPONSE SCHEMAS
# ============================================

class PlanetInfo(BaseModel):
    """Planet position information"""
    planet: str
    longitude: float
    latitude: float
    speed: float
    is_retrograde: bool
    
    # Sign info
    sign: str
    sign_number: int
    degree_in_sign: float
    sign_lord: str
    
    # Nakshatra info
    nakshatra: str
    nakshatra_pada: int
    nakshatra_lord: str
    
    # House placement
    house: int
    
    # Additional analysis (filled by service)
    dignity: Optional[str] = None  # exalted, own_sign, moolatrikona, debilitated, neutral
    is_combust: Optional[bool] = None
    aspects: Optional[List[str]] = None


class HouseInfo(BaseModel):
    """House cusp information"""
    house_number: int
    cusp_longitude: float
    sign: str
    sign_number: int
    degree_in_sign: float
    lord: str
    
    # Planets in this house
    planets_in_house: List[str] = []
    
    # House significations
    significations: Optional[List[str]] = None


class AscendantInfo(BaseModel):
    """Ascendant information"""
    longitude: float
    sign: str
    degree_in_sign: float
    nakshatra: str
    nakshatra_pada: int
    lord: str


class ChartMetadata(BaseModel):
    """Chart calculation metadata"""
    julian_day: float
    ayanamsa_type: str
    ayanamsa_value: float
    sidereal_time: Optional[float] = None
    calculation_time_ms: Optional[float] = None


class ChartResponse(BaseModel):
    """Complete birth chart response"""
    
    # Input echo
    birth_data: Dict[str, Any]
    
    # Ascendant
    ascendant: AscendantInfo
    
    # Planets
    planets: Dict[str, PlanetInfo]
    
    # Houses
    houses: Dict[str, HouseInfo]  # String keys for JSON compatibility
    
    # Summary
    lagna_sign: str
    moon_sign: str
    sun_sign: str
    moon_nakshatra: str
    
    # Metadata
    metadata: ChartMetadata
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "birth_data": {
                        "year": 1990,
                        "month": 5,
                        "day": 15,
                        "hour": 10,
                        "minute": 30,
                        "lat": 28.6139,
                        "lon": 77.2090
                    },
                    "ascendant": {
                        "longitude": 45.5,
                        "sign": "Taurus",
                        "degree_in_sign": 15.5,
                        "nakshatra": "Rohini",
                        "nakshatra_pada": 2,
                        "lord": "Venus"
                    },
                    "lagna_sign": "Taurus",
                    "moon_sign": "Gemini",
                    "sun_sign": "Taurus"
                }
            ]
        }
    }
