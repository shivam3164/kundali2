"""
Yoga Feature - Pydantic Schemas
Request and response schemas for Yoga detection
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from enum import Enum


# ============================================
# ENUMS
# ============================================

class YogaCategory(str, Enum):
    """Categories of Yogas"""
    RAJA_YOGA = "raja_yoga"
    DHANA_YOGA = "dhana_yoga"
    PANCHA_MAHAPURUSHA = "pancha_mahapurusha"
    NABHASH_YOGA = "nabhash_yoga"
    CHANDRA_YOGA = "chandra_yoga"
    SURYA_YOGA = "surya_yoga"
    DARIDRA_YOGA = "daridra_yoga"
    VIPARITA_RAJA_YOGA = "viparita_raja_yoga"
    OTHER = "other"


class YogaStrength(str, Enum):
    """Yoga strength levels"""
    FULL = "full"
    PARTIAL = "partial"
    WEAK = "weak"


# ============================================
# REQUEST SCHEMAS
# ============================================

class YogaRequest(BaseModel):
    """Yoga detection request"""
    
    # Can provide pre-calculated chart data
    chart_data: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Pre-calculated chart data from /chart/calculate endpoint"
    )
    
    # Or birth details to calculate
    year: Optional[int] = Field(default=None, description="Birth year")
    month: Optional[int] = Field(default=None, ge=1, le=12, description="Birth month")
    day: Optional[int] = Field(default=None, ge=1, le=31, description="Birth day")
    hour: Optional[int] = Field(default=12, ge=0, le=23, description="Birth hour")
    minute: Optional[int] = Field(default=0, ge=0, le=59, description="Birth minute")
    lat: Optional[float] = Field(default=None, description="Birth latitude")
    lon: Optional[float] = Field(default=None, description="Birth longitude")
    ayanamsa: str = Field(default="lahiri", description="Ayanamsa system")
    
    # Filter options
    categories: Optional[List[YogaCategory]] = Field(
        default=None,
        description="Filter by yoga categories (returns all if not specified)"
    )
    include_negative: bool = Field(
        default=True,
        description="Include negative yogas (Daridra, etc.)"
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
                    "categories": ["raja_yoga", "pancha_mahapurusha"]
                }
            ]
        }
    }


# ============================================
# RESPONSE SCHEMAS
# ============================================

class YogaResult(BaseModel):
    """Individual yoga detection result"""
    name: str
    category: YogaCategory
    is_present: bool
    strength: YogaStrength = YogaStrength.FULL
    
    # Forming planets/factors
    forming_planets: List[str] = []
    forming_houses: List[int] = []
    
    # Interpretation
    description: str = ""
    effects: str = ""
    
    # Additional info
    bphs_reference: Optional[str] = None
    conditions_met: List[str] = []
    conditions_partial: List[str] = []


class YogaSummary(BaseModel):
    """Summary of yoga analysis"""
    total_yogas_found: int
    raja_yogas_count: int
    dhana_yogas_count: int
    mahapurusha_yogas_count: int
    negative_yogas_count: int
    
    # Key findings
    strongest_yogas: List[str]
    notable_combinations: List[str]


class YogaResponse(BaseModel):
    """Complete yoga analysis response"""
    
    # Input echo
    birth_data: Dict[str, Any]
    
    # Results grouped by category
    yogas: Dict[str, List[YogaResult]]
    
    # All yogas in flat list
    all_yogas: List[YogaResult]
    
    # Summary
    summary: YogaSummary
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "birth_data": {"year": 1990, "month": 5, "day": 15},
                    "summary": {
                        "total_yogas_found": 5,
                        "raja_yogas_count": 2,
                        "dhana_yogas_count": 1,
                        "mahapurusha_yogas_count": 1,
                        "negative_yogas_count": 1
                    }
                }
            ]
        }
    }
