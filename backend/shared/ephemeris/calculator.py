"""
Planet and House Calculators
Low-level astronomical calculations using Swiss Ephemeris
"""

from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum, IntEnum
import math

try:
    import swisseph as swe
    SWISSEPH_AVAILABLE = True
except ImportError:
    SWISSEPH_AVAILABLE = False
    swe = None


# ============================================
# PLANET CODE MAPPING
# ============================================

class SwePlanet(IntEnum):
    """Swiss Ephemeris planet codes"""
    SUN = 0
    MOON = 1
    MERCURY = 2
    VENUS = 3
    MARS = 4
    JUPITER = 5
    SATURN = 6
    URANUS = 7
    NEPTUNE = 8
    PLUTO = 9
    MEAN_NODE = 10  # Mean Rahu
    TRUE_NODE = 11  # True Rahu
    MEAN_APOGEE = 12  # Mean Lilith
    CHIRON = 15


# Mapping from planet names to Swiss Ephemeris codes
PLANET_CODES = {
    'Sun': SwePlanet.SUN,
    'Moon': SwePlanet.MOON,
    'Mars': SwePlanet.MARS,
    'Mercury': SwePlanet.MERCURY,
    'Jupiter': SwePlanet.JUPITER,
    'Venus': SwePlanet.VENUS,
    'Saturn': SwePlanet.SATURN,
    'Rahu': SwePlanet.TRUE_NODE,  # True Node for Rahu
    'Ketu': SwePlanet.TRUE_NODE,  # Ketu is 180° from Rahu
}

# Navagraha (9 planets) used in Vedic astrology
NAVAGRAHA = ['Sun', 'Moon', 'Mars', 'Mercury', 'Jupiter', 'Venus', 'Saturn', 'Rahu', 'Ketu']


# ============================================
# NAKSHATRA DATA
# ============================================

NAKSHATRAS = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
    "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
    "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha",
    "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
    "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

NAKSHATRA_LORDS = [
    "Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu",
    "Jupiter", "Saturn", "Mercury", "Ketu", "Venus", "Sun",
    "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury",
    "Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu",
    "Jupiter", "Saturn", "Mercury"
]

ZODIAC_SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

SIGN_LORDS = [
    "Mars", "Venus", "Mercury", "Moon", "Sun", "Mercury",
    "Venus", "Mars", "Jupiter", "Saturn", "Saturn", "Jupiter"
]


# ============================================
# PLANET CALCULATOR
# ============================================

@dataclass
class RawPlanetData:
    """Raw planet calculation result"""
    longitude: float
    latitude: float
    distance: float
    speed_longitude: float
    speed_latitude: float
    speed_distance: float


class PlanetCalculator:
    """
    Low-level planet position calculator using Swiss Ephemeris
    """
    
    def __init__(self, ephemeris_path: Optional[str] = None):
        if not SWISSEPH_AVAILABLE:
            raise ImportError("Swiss Ephemeris (swisseph) is required for astronomical calculations")
        
        if ephemeris_path:
            swe.set_ephe_path(ephemeris_path)
    
    def calculate_planet_raw(self, julian_day: float, planet_code: int) -> RawPlanetData:
        """Calculate raw planet position"""
        flags = swe.FLG_SWIEPH | swe.FLG_SPEED
        result, ret_flags = swe.calc_ut(julian_day, planet_code, flags)
        
        return RawPlanetData(
            longitude=result[0],
            latitude=result[1],
            distance=result[2],
            speed_longitude=result[3],
            speed_latitude=result[4],
            speed_distance=result[5]
        )
    
    def calculate_planet_sidereal(
        self, 
        julian_day: float, 
        planet_code: int, 
        ayanamsa_mode: int
    ) -> RawPlanetData:
        """Calculate planet position in sidereal zodiac"""
        # Set ayanamsa mode
        swe.set_sid_mode(ayanamsa_mode, 0, 0)
        
        flags = swe.FLG_SWIEPH | swe.FLG_SPEED | swe.FLG_SIDEREAL
        result, ret_flags = swe.calc_ut(julian_day, planet_code, flags)
        
        return RawPlanetData(
            longitude=result[0],
            latitude=result[1],
            distance=result[2],
            speed_longitude=result[3],
            speed_latitude=result[4],
            speed_distance=result[5]
        )
    
    def get_ayanamsa(self, julian_day: float, ayanamsa_mode: int) -> float:
        """Get ayanamsa value for given Julian day"""
        swe.set_sid_mode(ayanamsa_mode, 0, 0)
        return swe.get_ayanamsa_ut(julian_day)
    
    @staticmethod
    def longitude_to_sign(longitude: float) -> Tuple[str, int, float]:
        """
        Convert longitude to sign, sign number, and degree in sign
        Returns: (sign_name, sign_number_1_based, degree_in_sign)
        """
        # Normalize longitude to 0-360
        longitude = longitude % 360
        
        sign_index = int(longitude / 30)
        sign_name = ZODIAC_SIGNS[sign_index]
        sign_number = sign_index + 1
        degree_in_sign = longitude % 30
        
        return sign_name, sign_number, degree_in_sign
    
    @staticmethod
    def longitude_to_nakshatra(longitude: float) -> Tuple[str, int, str]:
        """
        Convert longitude to nakshatra, pada, and nakshatra lord
        Returns: (nakshatra_name, pada_1_to_4, nakshatra_lord)
        """
        # Normalize longitude to 0-360
        longitude = longitude % 360
        
        # Each nakshatra spans 13°20' (360/27)
        nakshatra_span = 360 / 27
        nakshatra_index = int(longitude / nakshatra_span)
        nakshatra_name = NAKSHATRAS[nakshatra_index]
        nakshatra_lord = NAKSHATRA_LORDS[nakshatra_index]
        
        # Each pada is 3°20' (nakshatra_span / 4)
        pada_span = nakshatra_span / 4
        degree_in_nakshatra = longitude % nakshatra_span
        pada = int(degree_in_nakshatra / pada_span) + 1
        
        return nakshatra_name, pada, nakshatra_lord


# ============================================
# HOUSE CALCULATOR
# ============================================

class HouseSystem(str, Enum):
    """House calculation systems"""
    PLACIDUS = 'P'
    KOCH = 'K'
    EQUAL = 'E'
    WHOLE_SIGN = 'W'
    CAMPANUS = 'C'
    REGIOMONTANUS = 'R'
    MERIDIAN = 'X'
    PORPHYRY = 'O'


@dataclass
class HouseData:
    """House calculation result"""
    cusps: List[float]  # 12 house cusps (index 0 = 1st house)
    ascendant: float
    mc: float  # Medium Coeli (10th house cusp in quadrant systems)
    armc: float  # Sidereal time
    vertex: float
    equatorial_ascendant: float


class HouseCalculator:
    """
    House cusp calculator using Swiss Ephemeris
    """
    
    def __init__(self, ephemeris_path: Optional[str] = None):
        if not SWISSEPH_AVAILABLE:
            raise ImportError("Swiss Ephemeris (swisseph) is required for astronomical calculations")
        
        if ephemeris_path:
            swe.set_ephe_path(ephemeris_path)
    
    def calculate_houses(
        self,
        julian_day: float,
        latitude: float,
        longitude: float,
        house_system: HouseSystem = HouseSystem.PLACIDUS
    ) -> HouseData:
        """
        Calculate house cusps using specified house system
        """
        cusps, ascmc = swe.houses(
            julian_day, 
            latitude, 
            longitude, 
            house_system.value.encode()
        )
        
        return HouseData(
            cusps=list(cusps[0:12]),  # First 12 values are house cusps
            ascendant=ascmc[0],
            mc=ascmc[1],
            armc=ascmc[2],
            vertex=ascmc[3],
            equatorial_ascendant=ascmc[4]
        )
    
    def calculate_houses_sidereal(
        self,
        julian_day: float,
        latitude: float,
        longitude: float,
        ayanamsa_mode: int,
        house_system: HouseSystem = HouseSystem.PLACIDUS
    ) -> HouseData:
        """
        Calculate house cusps in sidereal zodiac
        """
        # Set ayanamsa for sidereal calculation
        swe.set_sid_mode(ayanamsa_mode, 0, 0)
        
        # Get ayanamsa value
        ayanamsa = swe.get_ayanamsa_ut(julian_day)
        
        # Calculate tropical houses
        cusps, ascmc = swe.houses(
            julian_day, 
            latitude, 
            longitude, 
            house_system.value.encode()
        )
        
        # Convert to sidereal by subtracting ayanamsa
        sidereal_cusps = [(c - ayanamsa) % 360 for c in cusps[0:12]]
        sidereal_asc = (ascmc[0] - ayanamsa) % 360
        sidereal_mc = (ascmc[1] - ayanamsa) % 360
        
        return HouseData(
            cusps=sidereal_cusps,
            ascendant=sidereal_asc,
            mc=sidereal_mc,
            armc=ascmc[2],
            vertex=(ascmc[3] - ayanamsa) % 360,
            equatorial_ascendant=(ascmc[4] - ayanamsa) % 360
        )
    
    def determine_house(self, longitude: float, cusps: List[float], house_system: HouseSystem = HouseSystem.PLACIDUS) -> int:
        """
        Determine which house a planet is in based on house cusps
        Returns house number (1-12)
        """
        longitude = longitude % 360
        
        # For Whole Sign houses, use sign-based calculation
        if house_system == HouseSystem.WHOLE_SIGN:
            # Get ascendant sign (from first cusp)
            asc_sign = int(cusps[0] / 30)
            planet_sign = int(longitude / 30)
            # House = (planet_sign - asc_sign) % 12 + 1
            return (planet_sign - asc_sign) % 12 + 1
        
        # For other house systems, use cusp-based calculation
        for i in range(12):
            cusp_start = cusps[i]
            cusp_end = cusps[(i + 1) % 12]
            
            # Handle wrap-around at 0°
            if cusp_start > cusp_end:  # Wraps around 360°
                if longitude >= cusp_start or longitude < cusp_end:
                    return i + 1
            else:
                if cusp_start <= longitude < cusp_end:
                    return i + 1
        
        # Fallback - should not reach here
        return 1
