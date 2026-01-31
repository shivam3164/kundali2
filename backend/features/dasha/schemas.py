"""
Dasha Feature - Pydantic Schemas
Request and response schemas for Dasha calculations
"""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date, datetime


# ============================================
# REQUEST SCHEMAS
# ============================================

class DashaRequest(BaseModel):
    """Dasha calculation request"""
    
    # Moon's nakshatra position (can be provided directly)
    moon_longitude: Optional[float] = Field(
        default=None, 
        description="Moon's longitude in degrees (0-360)"
    )
    moon_nakshatra: Optional[str] = Field(
        default=None,
        description="Moon's nakshatra name"
    )
    moon_nakshatra_pada: Optional[int] = Field(
        default=None,
        ge=1, le=4,
        description="Moon's nakshatra pada (1-4)"
    )
    
    # Or birth details to calculate Moon position
    year: Optional[int] = Field(default=None, description="Birth year")
    month: Optional[int] = Field(default=None, ge=1, le=12, description="Birth month")
    day: Optional[int] = Field(default=None, ge=1, le=31, description="Birth day")
    hour: Optional[int] = Field(default=12, ge=0, le=23, description="Birth hour")
    minute: Optional[int] = Field(default=0, ge=0, le=59, description="Birth minute")
    lat: Optional[float] = Field(default=None, description="Birth latitude")
    lon: Optional[float] = Field(default=None, description="Birth longitude")
    
    # Target date for current dasha
    target_date: Optional[date] = Field(
        default=None,
        description="Date to find current dasha for (defaults to today)"
    )
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "moon_longitude": 45.5,
                    "year": 1990,
                    "month": 5,
                    "day": 15,
                    "target_date": "2024-01-01"
                }
            ]
        }
    }


# ============================================
# RESPONSE SCHEMAS
# ============================================

class DashaPeriod(BaseModel):
    """Single Dasha period"""
    level: str  # "mahadasha", "antardasha", "pratyantardasha"
    planet: str
    start_date: date
    end_date: date
    duration_years: float
    duration_months: float
    duration_days: int
    
    # Status
    is_current: bool = False
    elapsed_percentage: Optional[float] = None
    
    # Interpretation hints
    planet_dignity: Optional[str] = None  # If chart provided
    planet_house: Optional[int] = None


class MahadashaInfo(BaseModel):
    """Mahadasha with its sub-periods"""
    planet: str
    start_date: date
    end_date: date
    duration_years: float
    is_current: bool = False
    
    # Sub-periods (Antardashas)
    antardashas: List[DashaPeriod] = []


class CurrentDashaInfo(BaseModel):
    """Current running dasha periods"""
    mahadasha: DashaPeriod
    antardasha: DashaPeriod
    pratyantardasha: Optional[DashaPeriod] = None
    
    # Summary
    summary: str


class DashaResponse(BaseModel):
    """Complete Dasha response"""
    
    # Input echo
    moon_nakshatra: str
    moon_nakshatra_pada: int
    birth_date: date
    
    # Balance of Dasha at birth
    balance_at_birth: dict  # {"planet": str, "years": float, "months": float, "days": int}
    
    # All Mahadashas
    mahadashas: List[MahadashaInfo]
    
    # Current periods
    current_dasha: Optional[CurrentDashaInfo] = None
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "moon_nakshatra": "Rohini",
                    "moon_nakshatra_pada": 2,
                    "birth_date": "1990-05-15",
                    "balance_at_birth": {
                        "planet": "Moon",
                        "years": 8,
                        "months": 4,
                        "days": 15
                    }
                }
            ]
        }
    }


class AntardashaResponse(BaseModel):
    """Antardasha periods for a specific Mahadasha"""
    mahadasha_planet: str
    mahadasha_start: date
    mahadasha_end: date
    antardashas: List[DashaPeriod]
