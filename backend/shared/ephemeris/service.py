"""
Ephemeris Service
High-level astronomical calculation service for Vedic astrology
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import math

try:
    import swisseph as swe
    SWISSEPH_AVAILABLE = True
except ImportError:
    SWISSEPH_AVAILABLE = False
    swe = None

from .calculator import (
    PlanetCalculator, 
    HouseCalculator, 
    HouseSystem,
    PLANET_CODES,
    NAVAGRAHA,
    NAKSHATRAS,
    NAKSHATRA_LORDS,
    ZODIAC_SIGNS,
    SIGN_LORDS
)


# ============================================
# AYANAMSA TYPES
# ============================================

class AyanamsaType(str, Enum):
    """Supported Ayanamsa systems"""
    LAHIRI = "lahiri"
    RAMAN = "raman"
    KRISHNAMURTI = "krishnamurti"
    FAGAN_BRADLEY = "fagan_bradley"
    TRUE_CHITRAPAKSHA = "true_chitrapaksha"


# Map to Swiss Ephemeris constants
AYANAMSA_MODES = {
    AyanamsaType.LAHIRI: 1,  # swe.SIDM_LAHIRI
    AyanamsaType.RAMAN: 3,  # swe.SIDM_RAMAN
    AyanamsaType.KRISHNAMURTI: 5,  # swe.SIDM_KRISHNAMURTI
    AyanamsaType.FAGAN_BRADLEY: 0,  # swe.SIDM_FAGAN_BRADLEY
    AyanamsaType.TRUE_CHITRAPAKSHA: 27,  # swe.SIDM_TRUE_CITRA
}


# ============================================
# RESULT DATA CLASSES
# ============================================

@dataclass
class PlanetPositionResult:
    """Complete planet position with all derived data"""
    planet: str
    longitude: float
    latitude: float
    speed: float
    is_retrograde: bool
    
    # Sign data
    sign: str
    sign_number: int
    degree_in_sign: float
    sign_lord: str
    
    # Nakshatra data
    nakshatra: str
    nakshatra_pada: int
    nakshatra_lord: str
    
    # House placement (filled after house calculation)
    house: int = 0


@dataclass
class HousePositionResult:
    """House cusp position result"""
    house_number: int
    cusp_longitude: float
    sign: str
    sign_number: int
    degree_in_sign: float
    lord: str


@dataclass 
class ChartCalculationResult:
    """Complete chart calculation result"""
    # Input data
    julian_day: float
    latitude: float
    longitude: float
    ayanamsa_type: AyanamsaType
    ayanamsa_value: float
    
    # Ascendant
    ascendant: float
    ascendant_sign: str
    ascendant_degree: float
    ascendant_nakshatra: str
    ascendant_nakshatra_pada: int
    ascendant_lord: str
    
    # Planets
    planets: Dict[str, PlanetPositionResult] = field(default_factory=dict)
    
    # Houses
    houses: Dict[int, HousePositionResult] = field(default_factory=dict)
    
    # Additional data
    mc: float = 0.0  # Medium Coeli
    sidereal_time: float = 0.0


# ============================================
# EPHEMERIS SERVICE
# ============================================

class EphemerisService:
    """
    High-level ephemeris service for Vedic astrology calculations
    
    This service provides:
    - Sidereal planet positions (with nakshatra and pada)
    - House cusp calculations
    - Full chart calculation
    """
    
    def __init__(
        self, 
        ephemeris_path: Optional[str] = None,
        default_ayanamsa: AyanamsaType = AyanamsaType.LAHIRI,
        house_system: HouseSystem = HouseSystem.WHOLE_SIGN  # Use Whole Sign for Vedic
    ):
        self.planet_calc = PlanetCalculator(ephemeris_path)
        self.house_calc = HouseCalculator(ephemeris_path)
        self.default_ayanamsa = default_ayanamsa
        self.house_system = house_system
    
    def calculate_julian_day(
        self, 
        year: int, 
        month: int, 
        day: int, 
        hour: float = 12.0
    ) -> float:
        """
        Calculate Julian Day from date and time
        
        Args:
            year: Year (e.g., 1990)
            month: Month (1-12)
            day: Day (1-31)
            hour: Hour as decimal (e.g., 14.5 for 2:30 PM)
        
        Returns:
            Julian Day number
        """
        if not SWISSEPH_AVAILABLE:
            # Fallback calculation
            return self._calculate_jd_fallback(year, month, day, hour)
        
        return swe.julday(year, month, day, hour)
    
    def _calculate_jd_fallback(self, year: int, month: int, day: int, hour: float) -> float:
        """Fallback Julian Day calculation without Swiss Ephemeris"""
        a = (14 - month) // 12
        y = year + 4800 - a
        m = month + 12 * a - 3
        
        jdn = day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045
        jd = jdn + (hour - 12) / 24.0
        return jd
    
    def get_ayanamsa(
        self, 
        julian_day: float, 
        ayanamsa_type: Optional[AyanamsaType] = None
    ) -> float:
        """Get ayanamsa value for given Julian Day"""
        ayanamsa = ayanamsa_type or self.default_ayanamsa
        mode = AYANAMSA_MODES.get(ayanamsa, 1)
        return self.planet_calc.get_ayanamsa(julian_day, mode)
    
    def calculate_planet_position(
        self,
        julian_day: float,
        planet_name: str,
        ayanamsa_type: Optional[AyanamsaType] = None
    ) -> PlanetPositionResult:
        """
        Calculate complete position of a single planet
        
        Args:
            julian_day: Julian Day for calculation
            planet_name: Name of planet (Sun, Moon, Mars, etc.)
            ayanamsa_type: Ayanamsa to use (defaults to service default)
        
        Returns:
            Complete planet position with sign, nakshatra, etc.
        """
        ayanamsa = ayanamsa_type or self.default_ayanamsa
        mode = AYANAMSA_MODES.get(ayanamsa, 1)
        
        # Get planet code
        planet_code = PLANET_CODES.get(planet_name)
        if planet_code is None:
            raise ValueError(f"Unknown planet: {planet_name}")
        
        # Calculate position
        raw = self.planet_calc.calculate_planet_sidereal(julian_day, planet_code, mode)
        
        # Handle Ketu (180° from Rahu)
        longitude = raw.longitude
        if planet_name == 'Ketu':
            longitude = (raw.longitude + 180) % 360
        
        # Get sign information
        sign, sign_num, deg_in_sign = PlanetCalculator.longitude_to_sign(longitude)
        sign_lord = SIGN_LORDS[sign_num - 1]
        
        # Get nakshatra information
        nakshatra, pada, nak_lord = PlanetCalculator.longitude_to_nakshatra(longitude)
        
        return PlanetPositionResult(
            planet=planet_name,
            longitude=longitude,
            latitude=raw.latitude,
            speed=raw.speed_longitude,
            is_retrograde=raw.speed_longitude < 0,
            sign=sign,
            sign_number=sign_num,
            degree_in_sign=deg_in_sign,
            sign_lord=sign_lord,
            nakshatra=nakshatra,
            nakshatra_pada=pada,
            nakshatra_lord=nak_lord
        )
    
    def calculate_all_planets(
        self,
        julian_day: float,
        ayanamsa_type: Optional[AyanamsaType] = None,
        include_outer_planets: bool = False
    ) -> Dict[str, PlanetPositionResult]:
        """
        Calculate positions of all Navagraha (9 planets)
        
        Args:
            julian_day: Julian Day for calculation
            ayanamsa_type: Ayanamsa to use
            include_outer_planets: Include Uranus, Neptune, Pluto
        
        Returns:
            Dictionary of planet positions keyed by planet name
        """
        planets = {}
        
        for planet_name in NAVAGRAHA:
            planets[planet_name] = self.calculate_planet_position(
                julian_day, planet_name, ayanamsa_type
            )
        
        return planets
    
    def calculate_houses(
        self,
        julian_day: float,
        latitude: float,
        longitude: float,
        ayanamsa_type: Optional[AyanamsaType] = None
    ) -> Tuple[Dict[int, HousePositionResult], float, float]:
        """
        Calculate house cusps
        
        Args:
            julian_day: Julian Day for calculation
            latitude: Geographic latitude
            longitude: Geographic longitude
            ayanamsa_type: Ayanamsa to use
        
        Returns:
            Tuple of (houses dict, ascendant longitude, MC longitude)
        """
        ayanamsa = ayanamsa_type or self.default_ayanamsa
        mode = AYANAMSA_MODES.get(ayanamsa, 1)
        
        house_data = self.house_calc.calculate_houses_sidereal(
            julian_day, latitude, longitude, mode, self.house_system
        )
        
        houses = {}
        for i in range(12):
            cusp = house_data.cusps[i]
            sign, sign_num, deg = PlanetCalculator.longitude_to_sign(cusp)
            lord = SIGN_LORDS[sign_num - 1]
            
            houses[i + 1] = HousePositionResult(
                house_number=i + 1,
                cusp_longitude=cusp,
                sign=sign,
                sign_number=sign_num,
                degree_in_sign=deg,
                lord=lord
            )
        
        return houses, house_data.ascendant, house_data.mc
    
    def calculate_full_chart(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        latitude: float,
        longitude: float,
        ayanamsa_type: Optional[AyanamsaType] = None,
        timezone_offset: float = 5.5  # Default to IST (UTC+5:30)
    ) -> ChartCalculationResult:
        """
        Calculate complete birth chart
        
        Args:
            year, month, day: Birth date
            hour, minute: Birth time (in local timezone)
            latitude, longitude: Birth place coordinates
            ayanamsa_type: Ayanamsa to use
            timezone_offset: Timezone offset from UTC in hours (default: 5.5 for IST)
        
        Returns:
            Complete chart calculation result
        """
        ayanamsa = ayanamsa_type or self.default_ayanamsa
        
        # Convert local time to UTC for Julian Day calculation
        # Swiss Ephemeris expects UTC time
        hour_decimal = hour + minute / 60.0
        utc_hour = hour_decimal - timezone_offset
        
        # Handle day rollover
        calc_year, calc_month, calc_day = year, month, day
        if utc_hour < 0:
            utc_hour += 24
            # Go to previous day
            calc_day -= 1
            if calc_day < 1:
                calc_month -= 1
                if calc_month < 1:
                    calc_month = 12
                    calc_year -= 1
                # Get days in previous month
                if calc_month in [1, 3, 5, 7, 8, 10, 12]:
                    calc_day = 31
                elif calc_month in [4, 6, 9, 11]:
                    calc_day = 30
                elif calc_month == 2:
                    if calc_year % 4 == 0 and (calc_year % 100 != 0 or calc_year % 400 == 0):
                        calc_day = 29
                    else:
                        calc_day = 28
        elif utc_hour >= 24:
            utc_hour -= 24
            # Go to next day
            calc_day += 1
            # Handle month overflow
            days_in_month = 31
            if calc_month in [4, 6, 9, 11]:
                days_in_month = 30
            elif calc_month == 2:
                if calc_year % 4 == 0 and (calc_year % 100 != 0 or calc_year % 400 == 0):
                    days_in_month = 29
                else:
                    days_in_month = 28
            if calc_day > days_in_month:
                calc_day = 1
                calc_month += 1
                if calc_month > 12:
                    calc_month = 1
                    calc_year += 1
        
        jd = self.calculate_julian_day(calc_year, calc_month, calc_day, utc_hour)
        
        # Get ayanamsa value
        ayanamsa_value = self.get_ayanamsa(jd, ayanamsa)
        
        # Calculate houses first (to get ascendant)
        houses, ascendant, mc = self.calculate_houses(jd, latitude, longitude, ayanamsa)
        
        # Calculate ascendant details
        asc_sign, asc_sign_num, asc_deg = PlanetCalculator.longitude_to_sign(ascendant)
        asc_nak, asc_pada, _ = PlanetCalculator.longitude_to_nakshatra(ascendant)
        asc_lord = SIGN_LORDS[asc_sign_num - 1]
        
        # Calculate all planets
        planets = self.calculate_all_planets(jd, ayanamsa)
        
        # Assign house positions to planets using Whole Sign house system
        cusps = [houses[i].cusp_longitude for i in range(1, 13)]
        for planet_name, planet_pos in planets.items():
            planet_pos.house = self.house_calc.determine_house(
                planet_pos.longitude, cusps, self.house_system
            )
        
        return ChartCalculationResult(
            julian_day=jd,
            latitude=latitude,
            longitude=longitude,
            ayanamsa_type=ayanamsa,
            ayanamsa_value=ayanamsa_value,
            ascendant=ascendant,
            ascendant_sign=asc_sign,
            ascendant_degree=asc_deg,
            ascendant_nakshatra=asc_nak,
            ascendant_nakshatra_pada=asc_pada,
            ascendant_lord=asc_lord,
            planets=planets,
            houses=houses,
            mc=mc
        )
    
    def get_planet_in_house(
        self, 
        chart: ChartCalculationResult, 
        planet: str
    ) -> int:
        """Get house number where planet is placed"""
        if planet in chart.planets:
            return chart.planets[planet].house
        return 0
    
    def get_planets_in_house(
        self, 
        chart: ChartCalculationResult, 
        house: int
    ) -> List[str]:
        """Get list of planets in a specific house"""
        return [
            name for name, pos in chart.planets.items() 
            if pos.house == house
        ]
    
    def get_house_lord(
        self, 
        chart: ChartCalculationResult, 
        house: int
    ) -> str:
        """Get lord of a specific house"""
        if house in chart.houses:
            return chart.houses[house].lord
        return ""
