"""
Chart Feature - Service Layer
Business logic for chart calculation and analysis
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass
import time

from shared.ephemeris import EphemerisService, AyanamsaType
from shared.ephemeris.service import ChartCalculationResult, PlanetPositionResult


# ============================================
# CHART SERVICE
# ============================================

class ChartService:
    """
    Chart calculation and analysis service
    
    Responsibilities:
    - Calculate birth charts using ephemeris
    - Analyze planetary dignities
    - Determine combustion
    - Identify aspects
    - Enrich chart data with BPHS knowledge
    """
    
    def __init__(self, ephemeris: EphemerisService, knowledge=None):
        self.ephemeris = ephemeris
        self.knowledge = knowledge
    
    def calculate_chart(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        latitude: float,
        longitude: float,
        ayanamsa: str = "lahiri"
    ) -> Dict[str, Any]:
        """
        Calculate complete birth chart
        
        Returns dictionary with all chart data ready for API response
        """
        start_time = time.time()
        
        # Map ayanamsa string to enum
        ayanamsa_type = self._get_ayanamsa_type(ayanamsa)
        
        # Calculate chart using ephemeris
        chart_result = self.ephemeris.calculate_full_chart(
            year=year,
            month=month,
            day=day,
            hour=hour,
            minute=minute,
            latitude=latitude,
            longitude=longitude,
            ayanamsa_type=ayanamsa_type
        )
        
        # Enrich with analysis
        planets = self._process_planets(chart_result)
        houses = self._process_houses(chart_result)
        
        # Build response
        calculation_time = (time.time() - start_time) * 1000
        
        return {
            "birth_data": {
                "year": year,
                "month": month,
                "day": day,
                "hour": hour,
                "minute": minute,
                "lat": latitude,
                "lon": longitude,
            },
            "ascendant": {
                "longitude": chart_result.ascendant,
                "sign": chart_result.ascendant_sign,
                "degree_in_sign": chart_result.ascendant_degree,
                "nakshatra": chart_result.ascendant_nakshatra,
                "nakshatra_pada": chart_result.ascendant_nakshatra_pada,
                "lord": chart_result.ascendant_lord,
            },
            "planets": planets,
            "houses": houses,
            "lagna_sign": chart_result.ascendant_sign,
            "moon_sign": chart_result.planets.get("Moon", {}).sign if hasattr(chart_result.planets.get("Moon"), 'sign') else "",
            "sun_sign": chart_result.planets.get("Sun", {}).sign if hasattr(chart_result.planets.get("Sun"), 'sign') else "",
            "moon_nakshatra": chart_result.planets.get("Moon", {}).nakshatra if hasattr(chart_result.planets.get("Moon"), 'nakshatra') else "",
            "metadata": {
                "julian_day": chart_result.julian_day,
                "ayanamsa_type": ayanamsa,
                "ayanamsa_value": chart_result.ayanamsa_value,
                "calculation_time_ms": calculation_time,
            }
        }
    
    def _get_ayanamsa_type(self, ayanamsa: str) -> AyanamsaType:
        """Convert ayanamsa string to enum"""
        mapping = {
            "lahiri": AyanamsaType.LAHIRI,
            "raman": AyanamsaType.RAMAN,
            "krishnamurti": AyanamsaType.KRISHNAMURTI,
            "fagan_bradley": AyanamsaType.FAGAN_BRADLEY,
            "true_chitrapaksha": AyanamsaType.TRUE_CHITRAPAKSHA,
        }
        return mapping.get(ayanamsa.lower(), AyanamsaType.LAHIRI)
    
    def _process_planets(self, chart: ChartCalculationResult) -> Dict[str, Dict]:
        """Process and enrich planet data"""
        planets = {}
        
        for name, pos in chart.planets.items():
            planet_data = {
                "planet": pos.planet,
                "longitude": pos.longitude,
                "latitude": pos.latitude,
                "speed": pos.speed,
                "is_retrograde": pos.is_retrograde,
                "sign": pos.sign,
                "sign_number": pos.sign_number,
                "degree_in_sign": pos.degree_in_sign,
                "sign_lord": pos.sign_lord,
                "nakshatra": pos.nakshatra,
                "nakshatra_pada": pos.nakshatra_pada,
                "nakshatra_lord": pos.nakshatra_lord,
                "house": pos.house,
                "dignity": self._calculate_dignity(name, pos),
                "is_combust": self._check_combustion(name, pos, chart),
                "aspects": self._get_aspects(name, pos, chart),
            }
            planets[name] = planet_data
        
        return planets
    
    def _process_houses(self, chart: ChartCalculationResult) -> Dict[str, Dict]:
        """Process house data"""
        houses = {}
        
        for house_num, house_pos in chart.houses.items():
            # Find planets in this house
            planets_in_house = [
                name for name, pos in chart.planets.items()
                if pos.house == house_num
            ]
            
            # Get house significations from knowledge base
            significations = []
            if self.knowledge:
                house_info = self.knowledge.get_house_info(house_num)
                significations = house_info.get("basic", {}).get("significations", [])
            
            houses[str(house_num)] = {
                "house_number": house_num,
                "cusp_longitude": house_pos.cusp_longitude,
                "sign": house_pos.sign,
                "sign_number": house_pos.sign_number,
                "degree_in_sign": house_pos.degree_in_sign,
                "lord": house_pos.lord,
                "planets_in_house": planets_in_house,
                "significations": significations,
            }
        
        return houses
    
    def _calculate_dignity(self, planet_name: str, position: PlanetPositionResult) -> str:
        """
        Calculate planetary dignity based on BPHS
        
        Dignities (from highest to lowest):
        - exalted: Planet in exaltation sign
        - moolatrikona: Planet in moolatrikona portion
        - own_sign: Planet in own sign
        - friendly: Planet in friendly sign
        - neutral: Planet in neutral sign
        - enemy: Planet in enemy sign
        - debilitated: Planet in debilitation sign
        """
        if not self.knowledge:
            return "neutral"
        
        sign = position.sign
        degree = position.degree_in_sign
        
        # Check exaltation
        exalt_info = self.knowledge.exaltation_points.get(planet_name) or {}
        if exalt_info.get("sign") == sign:
            return "exalted"
        
        # Check debilitation
        debil_info = self.knowledge.debilitation_points.get(planet_name) or {}
        if debil_info.get("sign") == sign:
            return "debilitated"
        
        # Check moolatrikona (not all planets have moolatrikona)
        moola_info = self.knowledge.moolatrikona.get(planet_name) or {}
        if moola_info and moola_info.get("sign") == sign:
            start = moola_info.get("start", moola_info.get("start_degree", 0))
            end = moola_info.get("end", moola_info.get("end_degree", 30))
            if start <= degree <= end:
                return "moolatrikona"
        
        # Check own sign
        planet_info = self.knowledge.planet_characteristics.get(planet_name) or {}
        own_signs = planet_info.get("own_signs", [])
        if sign in own_signs:
            return "own_sign"
        
        # Check relationships
        relationships = self.knowledge.planet_relationships.get(planet_name) or {}
        sign_lord = self.knowledge.sign_lords.get(sign)
        
        if sign_lord in relationships.get("friends", []):
            return "friendly"
        elif sign_lord in relationships.get("enemies", []):
            return "enemy"
        
        return "neutral"
    
    def _check_combustion(
        self, 
        planet_name: str, 
        position: PlanetPositionResult, 
        chart: ChartCalculationResult
    ) -> bool:
        """
        Check if planet is combust (too close to Sun)
        
        BPHS combustion orbs:
        - Moon: 12°
        - Mars: 17°
        - Mercury: 14° (12° if retrograde)
        - Jupiter: 11°
        - Venus: 10° (8° if retrograde)
        - Saturn: 15°
        """
        if planet_name == "Sun":
            return False  # Sun cannot be combust
        
        if planet_name in ["Rahu", "Ketu"]:
            return False  # Nodes are not subject to combustion
        
        sun_pos = chart.planets.get("Sun")
        if not sun_pos:
            return False
        
        # Combustion orbs per BPHS
        combustion_orbs = {
            "Moon": 12,
            "Mars": 17,
            "Mercury": 14,
            "Jupiter": 11,
            "Venus": 10,
            "Saturn": 15,
        }
        
        orb = combustion_orbs.get(planet_name, 10)
        
        # Reduced orb for retrograde Mercury and Venus
        if position.is_retrograde:
            if planet_name == "Mercury":
                orb = 12
            elif planet_name == "Venus":
                orb = 8
        
        # Calculate angular distance from Sun
        distance = abs(position.longitude - sun_pos.longitude)
        if distance > 180:
            distance = 360 - distance
        
        return distance <= orb
    
    def _get_aspects(
        self, 
        planet_name: str, 
        position: PlanetPositionResult, 
        chart: ChartCalculationResult
    ) -> List[str]:
        """
        Get planets aspected by this planet
        
        BPHS aspects:
        - All planets aspect 7th house from their position
        - Mars: Additional 4th and 8th aspects
        - Jupiter: Additional 5th and 9th aspects
        - Saturn: Additional 3rd and 10th aspects
        - Rahu/Ketu: 5th and 9th aspects (like Jupiter)
        """
        aspects = []
        planet_house = position.house
        
        # Standard 7th aspect (all planets)
        aspected_houses = [((planet_house + 6) % 12) + 1]  # 7th from position
        
        # Special aspects
        if planet_name == "Mars":
            aspected_houses.extend([
                ((planet_house + 3) % 12) + 1,  # 4th aspect
                ((planet_house + 7) % 12) + 1,  # 8th aspect
            ])
        elif planet_name == "Jupiter":
            aspected_houses.extend([
                ((planet_house + 4) % 12) + 1,  # 5th aspect
                ((planet_house + 8) % 12) + 1,  # 9th aspect
            ])
        elif planet_name == "Saturn":
            aspected_houses.extend([
                ((planet_house + 2) % 12) + 1,  # 3rd aspect
                ((planet_house + 9) % 12) + 1,  # 10th aspect
            ])
        elif planet_name in ["Rahu", "Ketu"]:
            aspected_houses.extend([
                ((planet_house + 4) % 12) + 1,  # 5th aspect
                ((planet_house + 8) % 12) + 1,  # 9th aspect
            ])
        
        # Find planets in aspected houses
        for other_name, other_pos in chart.planets.items():
            if other_name != planet_name and other_pos.house in aspected_houses:
                aspects.append(other_name)
        
        return aspects
    
    def get_planet_summary(self, chart_data: Dict) -> Dict[str, str]:
        """Generate a summary of planetary positions"""
        summary = {}
        
        for name, data in chart_data.get("planets", {}).items():
            sign = data.get("sign", "")
            house = data.get("house", 0)
            dignity = data.get("dignity", "neutral")
            retro = " (R)" if data.get("is_retrograde") else ""
            combust = " [Combust]" if data.get("is_combust") else ""
            
            summary[name] = f"{sign} in House {house} ({dignity}){retro}{combust}"
        
        return summary
