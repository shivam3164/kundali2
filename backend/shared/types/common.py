"""
Common Types - Shared across all features
These are the foundational types that define the core data structures
"""

from dataclasses import dataclass, field
from typing import Optional, Dict, List, Any, TypeVar, Generic
from datetime import datetime
from enum import Enum


# ============================================
# ENUMS
# ============================================

class Planet(str, Enum):
    """Nine planets (Navagraha) as per BPHS"""
    SUN = "Sun"
    MOON = "Moon"
    MARS = "Mars"
    MERCURY = "Mercury"
    JUPITER = "Jupiter"
    VENUS = "Venus"
    SATURN = "Saturn"
    RAHU = "Rahu"
    KETU = "Ketu"


class Sign(str, Enum):
    """Twelve zodiac signs (Rashis)"""
    ARIES = "Aries"
    TAURUS = "Taurus"
    GEMINI = "Gemini"
    CANCER = "Cancer"
    LEO = "Leo"
    VIRGO = "Virgo"
    LIBRA = "Libra"
    SCORPIO = "Scorpio"
    SAGITTARIUS = "Sagittarius"
    CAPRICORN = "Capricorn"
    AQUARIUS = "Aquarius"
    PISCES = "Pisces"


class House(int, Enum):
    """Twelve houses (Bhavas)"""
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    FIFTH = 5
    SIXTH = 6
    SEVENTH = 7
    EIGHTH = 8
    NINTH = 9
    TENTH = 10
    ELEVENTH = 11
    TWELFTH = 12


class Ayanamsa(str, Enum):
    """Ayanamsa types for sidereal calculations"""
    LAHIRI = "lahiri"
    RAMAN = "raman"
    KRISHNAMURTI = "krishnamurti"
    FAGAN_BRADLEY = "fagan_bradley"


# ============================================
# LOCATION & TIME
# ============================================

@dataclass
class Location:
    """Geographic location for chart calculation"""
    latitude: float
    longitude: float
    timezone: Optional[str] = None
    place_name: Optional[str] = None
    
    def __post_init__(self):
        if not -90 <= self.latitude <= 90:
            raise ValueError(f"Latitude must be between -90 and 90, got {self.latitude}")
        if not -180 <= self.longitude <= 180:
            raise ValueError(f"Longitude must be between -180 and 180, got {self.longitude}")


@dataclass
class DateTime:
    """Date and time for chart calculation"""
    year: int
    month: int
    day: int
    hour: int = 12
    minute: int = 0
    second: int = 0
    
    def to_datetime(self) -> datetime:
        return datetime(self.year, self.month, self.day, self.hour, self.minute, self.second)
    
    def to_julian_day(self) -> float:
        """Convert to Julian Day for astronomical calculations"""
        a = (14 - self.month) // 12
        y = self.year + 4800 - a
        m = self.month + 12 * a - 3
        
        jdn = self.day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045
        jd = jdn + (self.hour - 12) / 24.0 + self.minute / 1440.0 + self.second / 86400.0
        return jd


@dataclass
class BirthData:
    """Complete birth data for chart generation"""
    datetime: DateTime
    location: Location
    name: Optional[str] = None
    ayanamsa: Ayanamsa = Ayanamsa.LAHIRI
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'BirthData':
        """Create BirthData from API request dictionary"""
        return cls(
            datetime=DateTime(
                year=data['year'],
                month=data['month'],
                day=data['day'],
                hour=data.get('hour', 12),
                minute=data.get('minute', 0),
                second=data.get('second', 0)
            ),
            location=Location(
                latitude=data['lat'],
                longitude=data['lon'],
                place_name=data.get('place_name')
            ),
            name=data.get('name'),
            ayanamsa=Ayanamsa(data.get('ayanamsa', 'lahiri'))
        )


# ============================================
# PLANETARY POSITIONS
# ============================================

@dataclass
class PlanetPosition:
    """Position of a planet in the chart"""
    planet: str
    longitude: float  # 0-360 degrees
    latitude: float = 0.0
    speed: float = 0.0  # degrees per day
    is_retrograde: bool = False
    
    # Derived positions
    sign: str = ""
    sign_number: int = 0
    degree_in_sign: float = 0.0
    nakshatra: str = ""
    nakshatra_pada: int = 0
    nakshatra_lord: str = ""
    house: int = 0
    
    def __post_init__(self):
        if self.longitude and not self.sign:
            self._calculate_derived()
    
    def _calculate_derived(self):
        """Calculate derived positions from longitude"""
        signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
                 "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
        
        self.sign_number = int(self.longitude / 30) + 1
        self.sign = signs[self.sign_number - 1]
        self.degree_in_sign = self.longitude % 30
        self.is_retrograde = self.speed < 0
        
        # Calculate Nakshatra (27 nakshatras, each 13°20')
        nakshatra_index = int(self.longitude / (360 / 27))
        self.nakshatra_pada = int((self.longitude % (360 / 27)) / (360 / 108)) + 1


@dataclass
class HousePosition:
    """House cusp position"""
    house_number: int
    cusp_longitude: float
    sign: str = ""
    degree_in_sign: float = 0.0
    lord: str = ""
    
    def __post_init__(self):
        if self.cusp_longitude and not self.sign:
            self._calculate_derived()
    
    def _calculate_derived(self):
        signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
                 "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
        lords = ["Mars", "Venus", "Mercury", "Moon", "Sun", "Mercury",
                 "Venus", "Mars", "Jupiter", "Saturn", "Saturn", "Jupiter"]
        
        sign_index = int(self.cusp_longitude / 30)
        self.sign = signs[sign_index]
        self.degree_in_sign = self.cusp_longitude % 30
        self.lord = lords[sign_index]


# ============================================
# CHART DATA
# ============================================

@dataclass
class ChartData:
    """Complete chart data structure"""
    birth_data: BirthData
    ascendant: float
    ascendant_sign: str = ""
    planet_positions: Dict[str, PlanetPosition] = field(default_factory=dict)
    house_cusps: Dict[int, HousePosition] = field(default_factory=dict)
    
    # Additional chart info
    ayanamsa_value: float = 0.0
    sidereal_time: float = 0.0
    julian_day: float = 0.0
    
    def get_planet(self, planet: str) -> Optional[PlanetPosition]:
        """Get position of a specific planet"""
        return self.planet_positions.get(planet)
    
    def get_planets_in_house(self, house: int) -> List[PlanetPosition]:
        """Get all planets in a specific house"""
        return [p for p in self.planet_positions.values() if p.house == house]
    
    def get_planets_in_sign(self, sign: str) -> List[PlanetPosition]:
        """Get all planets in a specific sign"""
        return [p for p in self.planet_positions.values() if p.sign == sign]
    
    def get_house_lord(self, house: int) -> Optional[str]:
        """Get the lord of a specific house"""
        if house in self.house_cusps:
            return self.house_cusps[house].lord
        return None


# ============================================
# API RESPONSE TYPES
# ============================================

T = TypeVar('T')

@dataclass
class ApiResponse(Generic[T]):
    """Standard API response wrapper"""
    success: bool
    data: Optional[T] = None
    message: str = ""
    errors: List[str] = field(default_factory=list)
    
    @classmethod
    def ok(cls, data: T, message: str = "Success") -> 'ApiResponse[T]':
        return cls(success=True, data=data, message=message)
    
    @classmethod
    def error(cls, message: str, errors: List[str] = None) -> 'ApiResponse[T]':
        return cls(success=False, message=message, errors=errors or [])


@dataclass
class ErrorResponse:
    """Standard error response"""
    error: str
    detail: str
    code: str = "UNKNOWN_ERROR"
    
    def to_dict(self) -> Dict[str, str]:
        return {
            "error": self.error,
            "detail": self.detail,
            "code": self.code
        }
