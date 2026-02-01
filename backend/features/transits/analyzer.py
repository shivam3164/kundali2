"""
Transit Analyzer - End-to-End Implementation.
Combines BPHS foundation with Vedic Astrology enhancements.

Architecture:
- Layer 1 (BPHS): Basic Moon transit rules (Good/Bad houses)
- Layer 2 (Vedha): Obstruction analysis that blocks favorable transits
- Layer 3 (Tara): Nakshatra-based star strength
- Layer 4 (Murthi): Form quality based on Moon at rasi entry
"""
from typing import Dict, List, Optional
from datetime import datetime

from .rules import MOON_TRANSIT_RULES
from .vedha import check_vedha_obstruction, get_favorable_houses
from .taras import calculate_tara, is_favorable_tara, get_tara_strength_score
from .murthi import get_murthi_for_transit, get_murthi_modifier
from .types import (
    SIGN_NAMES,
    NAKSHATRA_NAMES,
    PLANET_NAMES,
    PlanetTransitResult,
    VedhaResult,
    TaraResult,
    MurthiResult,
    TransitSummary,
    TransitReport,
)


def get_sign_from_longitude(longitude: float) -> int:
    """Convert longitude (0-360) to sign index (1-12)."""
    return int(longitude // 30) + 1


def get_nakshatra_from_longitude(longitude: float) -> int:
    """Convert longitude (0-360) to nakshatra index (1-27)."""
    return int(longitude // (360 / 27)) + 1


def calculate_house_from_sign(reference_sign: int, planet_sign: int) -> int:
    """Calculate house number (1-12) from a reference sign."""
    house = planet_sign - reference_sign + 1
    if house <= 0:
        house += 12
    return house


class TransitAnalyzer:
    """
    Comprehensive Transit Analysis Engine.
    
    This class combines multiple layers of Vedic astrology transit analysis:
    1. BPHS Foundation: Basic Moon transit rules
    2. Vedha Enhancement: Obstruction analysis
    3. Tara Enhancement: Nakshatra-based strength
    4. Murthi Enhancement: Form quality at rasi entry
    """
    
    def __init__(
        self,
        natal_moon_sign: int,
        natal_moon_nakshatra: int,
        natal_moon_longitude: float
    ):
        """
        Initialize with natal chart data.
        
        Args:
            natal_moon_sign: Sign of natal Moon (1-12)
            natal_moon_nakshatra: Nakshatra of natal Moon (1-27)
            natal_moon_longitude: Longitude of natal Moon (0-360)
        """
        self.natal_moon_sign = natal_moon_sign
        self.natal_moon_nakshatra = natal_moon_nakshatra
        self.natal_moon_longitude = natal_moon_longitude
    
    def analyze_single_planet(
        self,
        planet: str,
        transit_longitude: float,
        all_transit_houses: Dict[str, int],
        murthi_moon_sign: Optional[int] = None
    ) -> PlanetTransitResult:
        """
        Analyze a single planet's transit comprehensively.
        
        Args:
            planet: Planet name
            transit_longitude: Current longitude of planet (0-360)
            all_transit_houses: All planets' houses from natal Moon
            murthi_moon_sign: Moon's sign when this planet entered its current sign
        
        Returns:
            PlanetTransitResult with all analysis layers
        """
        transit_sign = get_sign_from_longitude(transit_longitude)
        transit_nakshatra = get_nakshatra_from_longitude(transit_longitude)
        house_from_moon = calculate_house_from_sign(self.natal_moon_sign, transit_sign)
        
        # Layer 1: BPHS Foundation
        basic_result = self._get_basic_transit_result(planet, house_from_moon)
        
        # Layer 2: Vedha Analysis
        vedha_result = self._analyze_vedha(planet, house_from_moon, all_transit_houses)
        
        # Layer 3: Tara Analysis
        tara_result = self._analyze_tara(transit_nakshatra)
        
        # Layer 4: Murthi Analysis (if data available)
        murthi_result = None
        if murthi_moon_sign is not None:
            murthi_result = self._analyze_murthi(murthi_moon_sign)
        
        # Synthesize final result
        final_status, final_prediction, confidence = self._synthesize_result(
            planet, basic_result, vedha_result, tara_result, murthi_result
        )
        
        return PlanetTransitResult(
            planet=planet,
            transit_sign=transit_sign,
            transit_sign_name=SIGN_NAMES[transit_sign],
            transit_nakshatra=transit_nakshatra,
            transit_nakshatra_name=NAKSHATRA_NAMES[transit_nakshatra],
            house_from_moon=house_from_moon,
            basic_status=basic_result["status"],
            basic_prediction=basic_result["text"],
            vedha=vedha_result,
            tara=tara_result,
            murthi=murthi_result,
            final_status=final_status,
            final_prediction=final_prediction,
            confidence=confidence,
        )
    
    def analyze_all_planets(
        self,
        transit_positions: Dict[str, float],
        murthi_data: Optional[Dict[str, int]] = None
    ) -> List[PlanetTransitResult]:
        """
        Analyze all planets' transits comprehensively.
        
        Args:
            transit_positions: Dict of planet names to their current longitudes
            murthi_data: Optional dict of Moon signs at each planet's rasi entry
        
        Returns:
            List of PlanetTransitResult for all planets
        """
        # First pass: calculate all houses from Moon
        all_transit_houses = {}
        for planet, longitude in transit_positions.items():
            sign = get_sign_from_longitude(longitude)
            all_transit_houses[planet] = calculate_house_from_sign(
                self.natal_moon_sign, sign
            )
        
        # Second pass: analyze each planet
        results = []
        for planet in PLANET_NAMES:
            if planet in transit_positions:
                murthi_moon = murthi_data.get(planet) if murthi_data else None
                result = self.analyze_single_planet(
                    planet,
                    transit_positions[planet],
                    all_transit_houses,
                    murthi_moon
                )
                results.append(result)
        
        return results
    
    def _get_basic_transit_result(self, planet: str, house: int) -> Dict[str, str]:
        """Get BPHS foundation transit result."""
        if planet in MOON_TRANSIT_RULES and house in MOON_TRANSIT_RULES[planet]:
            return MOON_TRANSIT_RULES[planet][house]
        return {"status": "Neutral", "text": "No specific prediction available"}
    
    def _analyze_vedha(
        self,
        planet: str,
        house: int,
        all_houses: Dict[str, int]
    ) -> VedhaResult:
        """Analyze Vedha (obstruction) for a transit."""
        is_obstructed, obstructor, vedha_house = check_vedha_obstruction(
            planet, house, all_houses
        )
        return VedhaResult(
            is_obstructed=is_obstructed,
            obstructing_planet=obstructor,
            vedha_house=vedha_house,
        )
    
    def _analyze_tara(self, transit_nakshatra: int) -> TaraResult:
        """Analyze Tara (star strength) for a transit."""
        tara_data = calculate_tara(self.natal_moon_nakshatra, transit_nakshatra)
        return TaraResult(
            tara_name=tara_data["tara_name"],
            tara_quality=tara_data["tara_quality"],
            nakshatra_distance=tara_data["nakshatra_distance"],
            special_nakshatra=tara_data.get("special_nakshatra"),
        )
    
    def _analyze_murthi(self, moon_sign_at_entry: int) -> MurthiResult:
        """Analyze Murthi (form) for a transit."""
        murthi_data = get_murthi_for_transit(
            self.natal_moon_sign, moon_sign_at_entry
        )
        return MurthiResult(
            murthi_type=murthi_data["murthi_type"],
            moon_house_at_entry=murthi_data["moon_house_at_entry"],
            result_quality=murthi_data["result_quality"],
        )
    
    def _synthesize_result(
        self,
        planet: str,
        basic: Dict[str, str],
        vedha: VedhaResult,
        tara: TaraResult,
        murthi: Optional[MurthiResult]
    ) -> tuple:
        """
        Synthesize all layers into final prediction.
        
        Priority:
        1. If Vedha obstructs a Good transit -> downgrade to Obstructed
        2. Tara quality modifies confidence
        3. Murthi modifies intensity
        """
        basic_status = basic["status"]
        basic_text = basic["text"]
        
        # Start with basic status
        final_status = basic_status
        modifiers = []
        confidence = "Medium"
        
        # Vedha modification (most important for Good transits)
        if vedha.is_obstructed and basic_status == "Good":
            final_status = "Obstructed"
            modifiers.append(
                f"Good transit blocked by {vedha.obstructing_planet} in house {vedha.vedha_house}"
            )
            confidence = "High"
        
        # Tara modification
        tara_favorable = is_favorable_tara(tara.tara_name)
        tara_score = get_tara_strength_score(tara.tara_name)
        
        if basic_status == "Good" and not tara_favorable:
            modifiers.append(f"Weakened by {tara.tara_name} Tara (unfavorable star)")
            if confidence != "High":
                confidence = "Low"
        elif basic_status == "Bad" and tara_favorable:
            modifiers.append(f"Somewhat mitigated by {tara.tara_name} Tara (favorable star)")
        elif basic_status == "Good" and tara_favorable:
            if confidence != "High":
                confidence = "High"
        
        # Murthi modification
        if murthi:
            murthi_modifier = get_murthi_modifier(murthi.murthi_type)
            if murthi_modifier < 0.5 and basic_status == "Good":
                modifiers.append(
                    f"Results reduced by {murthi.murthi_type} Murthi ({murthi.result_quality})"
                )
                confidence = "Low"
            elif murthi_modifier >= 0.75 and basic_status == "Good":
                if not vedha.is_obstructed:
                    confidence = "High"
        
        # Build final prediction
        if modifiers:
            final_prediction = f"{basic_text}. Note: {'; '.join(modifiers)}."
        else:
            final_prediction = basic_text
        
        return final_status, final_prediction, confidence


def create_transit_report(
    natal_moon_sign: int,
    natal_moon_nakshatra: int,
    natal_moon_longitude: float,
    transit_positions: Dict[str, float],
    transit_date: str,
    murthi_data: Optional[Dict[str, int]] = None
) -> TransitReport:
    """
    Create a comprehensive transit report.
    
    This is the main entry point for transit analysis.
    
    Args:
        natal_moon_sign: Sign of natal Moon (1-12)
        natal_moon_nakshatra: Nakshatra of natal Moon (1-27)
        natal_moon_longitude: Longitude of natal Moon
        transit_positions: Dict of planet names to current longitudes
        transit_date: Date string for the transit
        murthi_data: Optional Moon signs at planet rasi entries
    
    Returns:
        Complete TransitReport
    """
    analyzer = TransitAnalyzer(natal_moon_sign, natal_moon_nakshatra, natal_moon_longitude)
    results = analyzer.analyze_all_planets(transit_positions, murthi_data)
    
    # Categorize results
    favorable = [r for r in results if r.final_status == "Good"]
    unfavorable = [r for r in results if r.final_status == "Bad"]
    obstructed = [r for r in results if r.final_status == "Obstructed"]
    
    # Overall assessment
    good_count = len(favorable)
    bad_count = len(unfavorable)
    
    if good_count > bad_count + 2:
        overall = "Favorable Period"
    elif bad_count > good_count + 2:
        overall = "Challenging Period"
    else:
        overall = "Mixed Period"
    
    return TransitReport(
        natal_moon_sign=SIGN_NAMES[natal_moon_sign],
        natal_moon_nakshatra=NAKSHATRA_NAMES[natal_moon_nakshatra],
        transit_date=transit_date,
        analysis_results=results,
        summary=TransitSummary(
            favorable_transits=len(favorable),
            unfavorable_transits=len(unfavorable),
            obstructed_transits=len(obstructed),
            overall_assessment=overall,
        ),
        favorable_planets=[r.planet for r in favorable],
        unfavorable_planets=[r.planet for r in unfavorable],
    )
