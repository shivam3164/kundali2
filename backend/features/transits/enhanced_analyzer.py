"""
Enhanced Transit Analyzer - Comprehensive Implementation

Integrates ALL transit analysis layers:
- Layer 1 (BPHS): Basic Moon transit rules
- Layer 2 (Vedha): Obstruction analysis
- Layer 3 (Tara): Nakshatra-based star strength  
- Layer 4 (Murthi): Form quality at rasi entry
- Layer 5 (Special Nakshatras): Extended special nakshatra analysis
- Layer 6 (Latta): Planetary kicks analysis
- Layer 7 (Body Parts): Health/body transit analysis
- Layer 8 (Ashtakavarga): Bindu-based transit scoring
"""
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime

from .rules import MOON_TRANSIT_RULES
from .vedha import check_vedha_obstruction, get_favorable_houses
from .taras import calculate_tara, is_favorable_tara, get_tara_strength_score
from .murthi import get_murthi_for_transit, get_murthi_modifier
from .special_nakshatras import (
    calculate_special_nakshatra,
    analyze_transit_in_special_nakshatra,
    check_planets_in_special_nakshatras,
    get_all_special_nakshatras_for_native,
    SPECIAL_NAKSHATRAS,
)
from .latta import (
    analyze_latta_effects,
    get_latta_for_all_planets,
    check_latta_on_nakshatra,
)
from .body_parts import (
    analyze_body_part_transits,
    get_health_sensitive_transits,
    analyze_regional_health,
)
from .ashtakavarga import (
    analyze_transit_ashtakavarga,
    analyze_all_transit_ashtakavarga,
    calculate_transit_strength_summary,
)
from .types import (
    SIGN_NAMES,
    NAKSHATRA_NAMES,
    PLANET_NAMES,
    PlanetTransitResult,
    VedhaResult,
    TaraResult,
    MurthiResult,
)


def get_sign_from_longitude(longitude: float) -> int:
    """Convert longitude to sign index (1-12)."""
    return int(longitude // 30) + 1


def get_nakshatra_from_longitude(longitude: float) -> int:
    """Convert longitude to nakshatra index (1-27)."""
    return int(longitude // (360 / 27)) + 1


def calculate_house_from_sign(reference_sign: int, planet_sign: int) -> int:
    """Calculate house number (1-12) from reference sign."""
    house = planet_sign - reference_sign + 1
    if house <= 0:
        house += 12
    return house


@dataclass
class EnhancedTransitResult:
    """Complete enhanced transit result for a planet"""
    planet: str
    transit_sign: int
    transit_sign_name: str
    transit_nakshatra: int
    transit_nakshatra_name: str
    house_from_moon: int
    house_from_lagna: int
    
    # Layer 1: BPHS
    basic_status: str
    basic_prediction: str
    
    # Layer 2: Vedha
    vedha: Dict
    
    # Layer 3: Tara
    tara: Dict
    
    # Layer 4: Murthi
    murthi: Optional[Dict] = None
    
    # Layer 5: Special Nakshatras
    special_nakshatra: Optional[Dict] = None
    
    # Layer 6: Latta
    latta: Optional[Dict] = None
    
    # Layer 7: Body Parts
    body_part_transit: Optional[Dict] = None
    
    # Layer 8: Ashtakavarga
    ashtakavarga: Optional[Dict] = None
    
    # Synthesized
    final_status: str = "Neutral"
    final_prediction: str = ""
    confidence: str = "Medium"
    score: float = 0.0


@dataclass
class EnhancedTransitReport:
    """Complete enhanced transit report"""
    native_data: Dict
    transit_date: str
    
    # Individual planet results
    planet_results: List[EnhancedTransitResult]
    
    # Summary analyses
    overall_summary: Dict = field(default_factory=dict)
    latta_analysis: Dict = field(default_factory=dict)
    special_nakshatra_analysis: Dict = field(default_factory=dict)
    body_parts_analysis: Dict = field(default_factory=dict)
    ashtakavarga_summary: Dict = field(default_factory=dict)
    health_analysis: Dict = field(default_factory=dict)
    
    # Categorized results
    favorable_planets: List[str] = field(default_factory=list)
    unfavorable_planets: List[str] = field(default_factory=list)
    obstructed_planets: List[str] = field(default_factory=list)
    
    # Life area impacts (for area-based queries)
    area_impacts: Dict = field(default_factory=dict)


class EnhancedTransitAnalyzer:
    """
    Comprehensive Transit Analyzer with all 8 layers.
    """
    
    def __init__(
        self,
        natal_moon_sign: int,
        natal_moon_nakshatra: int,
        natal_moon_longitude: float,
        natal_lagna_sign: int = None,
        natal_lagna_nakshatra: int = None,
        natal_positions: Dict[str, int] = None,  # For Ashtakavarga
        natal_house_lords: Dict[str, int] = None,  # For house lordship
    ):
        self.natal_moon_sign = natal_moon_sign
        self.natal_moon_nakshatra = natal_moon_nakshatra
        self.natal_moon_longitude = natal_moon_longitude
        self.natal_lagna_sign = natal_lagna_sign or natal_moon_sign
        self.natal_lagna_nakshatra = natal_lagna_nakshatra or natal_moon_nakshatra
        self.natal_positions = natal_positions or {}
        self.natal_house_lords = natal_house_lords or {}
        
        # Ensure Lagna is in natal_positions for Ashtakavarga
        if "Lagna" not in self.natal_positions:
            self.natal_positions["Lagna"] = self.natal_lagna_sign
    
    def analyze_planet(
        self,
        planet: str,
        transit_longitude: float,
        all_transit_houses: Dict[str, int],
        all_transit_nakshatras: Dict[str, int],
        all_transit_signs: Dict[str, int],
        murthi_moon_sign: Optional[int] = None
    ) -> EnhancedTransitResult:
        """Analyze a single planet with all 8 layers."""
        transit_sign = get_sign_from_longitude(transit_longitude)
        transit_nakshatra = get_nakshatra_from_longitude(transit_longitude)
        house_from_moon = calculate_house_from_sign(self.natal_moon_sign, transit_sign)
        house_from_lagna = calculate_house_from_sign(self.natal_lagna_sign, transit_sign)
        
        # Layer 1: BPHS Foundation
        basic = self._get_basic_result(planet, house_from_moon)
        
        # Layer 2: Vedha
        vedha = self._analyze_vedha(planet, house_from_moon, all_transit_houses)
        
        # Layer 3: Tara
        tara = self._analyze_tara(transit_nakshatra)
        
        # Layer 4: Murthi
        murthi = None
        if murthi_moon_sign is not None:
            murthi = self._analyze_murthi(murthi_moon_sign)
        
        # Layer 5: Special Nakshatra
        special_nak = analyze_transit_in_special_nakshatra(
            self.natal_moon_nakshatra,
            transit_nakshatra,
            planet
        )
        
        # Layer 6: Latta (only for planets with latta rules)
        latta_check = check_latta_on_nakshatra(
            self.natal_moon_nakshatra,
            {planet: transit_nakshatra}
        )
        latta = latta_check[0] if latta_check else None
        
        # Layer 7: Body Parts
        body_part = None  # Calculated at report level
        
        # Layer 8: Ashtakavarga
        ashtakavarga = None
        if self.natal_positions and planet not in ["Rahu", "Ketu"]:
            av_score = analyze_transit_ashtakavarga(
                planet, transit_sign, self.natal_positions, house_from_lagna
            )
            ashtakavarga = {
                "bav_score": av_score.bav_score,
                "sav_score": av_score.sav_score,
                "quality": av_score.quality,
                "interpretation": av_score.interpretation,
            }
        
        # Synthesize
        final_status, final_prediction, confidence, score = self._synthesize(
            planet, basic, vedha, tara, murthi, special_nak, latta, ashtakavarga
        )
        
        return EnhancedTransitResult(
            planet=planet,
            transit_sign=transit_sign,
            transit_sign_name=SIGN_NAMES[transit_sign],
            transit_nakshatra=transit_nakshatra,
            transit_nakshatra_name=NAKSHATRA_NAMES[transit_nakshatra],
            house_from_moon=house_from_moon,
            house_from_lagna=house_from_lagna,
            basic_status=basic["status"],
            basic_prediction=basic["text"],
            vedha=vedha,
            tara=tara,
            murthi=murthi,
            special_nakshatra=special_nak,
            latta=latta,
            ashtakavarga=ashtakavarga,
            final_status=final_status,
            final_prediction=final_prediction,
            confidence=confidence,
            score=score,
        )
    
    def analyze_all(
        self,
        transit_positions: Dict[str, float],
        transit_date: str = None,
        murthi_data: Optional[Dict[str, int]] = None,
    ) -> EnhancedTransitReport:
        """Analyze all planets with complete report."""
        if transit_date is None:
            transit_date = datetime.now().strftime("%Y-%m-%d")
        
        # Prepare transit data
        all_transit_signs = {}
        all_transit_nakshatras = {}
        all_transit_houses = {}
        
        for planet, longitude in transit_positions.items():
            sign = get_sign_from_longitude(longitude)
            nakshatra = get_nakshatra_from_longitude(longitude)
            all_transit_signs[planet] = sign
            all_transit_nakshatras[planet] = nakshatra
            all_transit_houses[planet] = calculate_house_from_sign(
                self.natal_moon_sign, sign
            )
        
        # Analyze each planet
        planet_results = []
        for planet in PLANET_NAMES:
            if planet in transit_positions:
                murthi_moon = murthi_data.get(planet) if murthi_data else None
                result = self.analyze_planet(
                    planet,
                    transit_positions[planet],
                    all_transit_houses,
                    all_transit_nakshatras,
                    all_transit_signs,
                    murthi_moon
                )
                planet_results.append(result)
        
        # Comprehensive latta analysis
        latta_analysis = analyze_latta_effects(
            self.natal_moon_nakshatra,
            self.natal_lagna_nakshatra,
            all_transit_nakshatras,
            self.natal_house_lords
        )
        
        # Special nakshatra mapping
        special_nakshatra_analysis = check_planets_in_special_nakshatras(
            self.natal_moon_nakshatra,
            all_transit_nakshatras
        )
        
        # Body parts analysis
        body_parts_analysis = analyze_body_part_transits(all_transit_nakshatras)
        
        # Health analysis
        health_analysis = get_health_sensitive_transits(
            self.natal_moon_nakshatra,
            all_transit_nakshatras
        )
        
        # Regional health
        regional_health = analyze_regional_health(all_transit_nakshatras)
        
        # Ashtakavarga summary
        ashtakavarga_summary = {}
        if self.natal_positions:
            ashtakavarga_summary = calculate_transit_strength_summary(
                all_transit_signs, self.natal_positions
            )
        
        # Categorize
        favorable = [r.planet for r in planet_results if r.final_status == "Good"]
        unfavorable = [r.planet for r in planet_results if r.final_status == "Bad"]
        obstructed = [r.planet for r in planet_results if r.final_status == "Obstructed"]
        
        # Calculate overall summary
        overall_summary = self._calculate_overall_summary(
            planet_results, latta_analysis, ashtakavarga_summary
        )
        
        # Life area impacts
        area_impacts = self._calculate_area_impacts(
            planet_results, all_transit_houses, special_nakshatra_analysis
        )
        
        return EnhancedTransitReport(
            native_data={
                "natal_moon_sign": SIGN_NAMES[self.natal_moon_sign],
                "natal_moon_nakshatra": NAKSHATRA_NAMES[self.natal_moon_nakshatra],
                "natal_lagna_sign": SIGN_NAMES[self.natal_lagna_sign],
            },
            transit_date=transit_date,
            planet_results=planet_results,
            overall_summary=overall_summary,
            latta_analysis=latta_analysis,
            special_nakshatra_analysis=special_nakshatra_analysis,
            body_parts_analysis=body_parts_analysis,
            ashtakavarga_summary=ashtakavarga_summary,
            health_analysis={
                "sensitive_transits": health_analysis,
                "regional_health": regional_health,
            },
            favorable_planets=favorable,
            unfavorable_planets=unfavorable,
            obstructed_planets=obstructed,
            area_impacts=area_impacts,
        )
    
    def _get_basic_result(self, planet: str, house: int) -> Dict[str, str]:
        """Get BPHS foundation result."""
        if planet in MOON_TRANSIT_RULES and house in MOON_TRANSIT_RULES[planet]:
            return MOON_TRANSIT_RULES[planet][house]
        return {"status": "Neutral", "text": "No specific prediction available"}
    
    def _analyze_vedha(
        self, planet: str, house: int, all_houses: Dict[str, int]
    ) -> Dict:
        """Analyze Vedha."""
        is_obstructed, obstructor, vedha_house = check_vedha_obstruction(
            planet, house, all_houses
        )
        return {
            "is_obstructed": is_obstructed,
            "obstructing_planet": obstructor,
            "vedha_house": vedha_house,
        }
    
    def _analyze_tara(self, transit_nakshatra: int) -> Dict:
        """Analyze Tara."""
        tara_data = calculate_tara(self.natal_moon_nakshatra, transit_nakshatra)
        return {
            "tara_name": tara_data["tara_name"],
            "tara_quality": tara_data["tara_quality"],
            "nakshatra_distance": tara_data["nakshatra_distance"],
            "special_nakshatra": tara_data.get("special_nakshatra"),
        }
    
    def _analyze_murthi(self, moon_sign_at_entry: int) -> Dict:
        """Analyze Murthi."""
        murthi_data = get_murthi_for_transit(
            self.natal_moon_sign, moon_sign_at_entry
        )
        return {
            "murthi_type": murthi_data["murthi_type"],
            "moon_house_at_entry": murthi_data["moon_house_at_entry"],
            "result_quality": murthi_data["result_quality"],
        }
    
    def _synthesize(
        self,
        planet: str,
        basic: Dict,
        vedha: Dict,
        tara: Dict,
        murthi: Optional[Dict],
        special_nak: Optional[Dict],
        latta: Optional[Dict],
        ashtakavarga: Optional[Dict],
    ) -> tuple:
        """Synthesize all layers into final result."""
        basic_status = basic["status"]
        basic_text = basic["text"]
        
        # Scoring system (-100 to +100)
        score = 0
        modifiers = []
        
        # Basic status score
        if basic_status == "Good":
            score += 30
        elif basic_status == "Bad":
            score -= 30
        
        # Vedha impact
        if vedha["is_obstructed"] and basic_status == "Good":
            score -= 25
            modifiers.append(f"Blocked by {vedha['obstructing_planet']}")
        
        # Tara impact
        tara_favorable = is_favorable_tara(tara["tara_name"])
        if tara_favorable:
            score += 15
        else:
            score -= 10
            if tara["tara_quality"] == "Bad":
                modifiers.append(f"Weakened by {tara['tara_name']} Tara")
        
        # Murthi impact
        if murthi:
            murthi_mod = get_murthi_modifier(murthi["murthi_type"])
            if murthi_mod >= 0.75:
                score += 10
            elif murthi_mod < 0.5:
                score -= 10
                modifiers.append(f"Reduced by {murthi['murthi_type']} Murthi")
        
        # Special Nakshatra impact
        if special_nak and special_nak.get("is_special"):
            if special_nak.get("quality") == "favorable":
                score += 15
            elif special_nak.get("quality") == "unfavorable":
                score -= 15
                modifiers.append(f"In {special_nak['name']} nakshatra (unfavorable)")
        
        # Latta impact
        if latta:
            score -= 20
            modifiers.append(f"{planet} has latta (kick) on birth star")
        
        # Ashtakavarga impact
        if ashtakavarga:
            bav = ashtakavarga["bav_score"]
            if bav >= 5:
                score += 15
            elif bav < 3:
                score -= 15
                modifiers.append(f"Low Ashtakavarga ({bav} bindus)")
        
        # Determine final status
        if vedha["is_obstructed"] and basic_status == "Good":
            final_status = "Obstructed"
        elif score >= 25:
            final_status = "Good"
        elif score <= -25:
            final_status = "Bad"
        else:
            final_status = "Neutral"
        
        # Confidence
        if abs(score) >= 40:
            confidence = "High"
        elif abs(score) >= 20:
            confidence = "Medium"
        else:
            confidence = "Low"
        
        # Final prediction
        if modifiers:
            final_prediction = f"{basic_text}. Note: {'; '.join(modifiers)}."
        else:
            final_prediction = basic_text
        
        return final_status, final_prediction, confidence, score
    
    def _calculate_overall_summary(
        self,
        results: List[EnhancedTransitResult],
        latta_analysis: Dict,
        ashtakavarga_summary: Dict,
    ) -> Dict:
        """Calculate overall transit period summary."""
        total_score = sum(r.score for r in results)
        avg_score = total_score / len(results) if results else 0
        
        good_count = len([r for r in results if r.final_status == "Good"])
        bad_count = len([r for r in results if r.final_status == "Bad"])
        
        # Overall assessment
        if avg_score >= 15:
            assessment = "Favorable Period"
            description = "Most transits support positive outcomes. Good time for new initiatives."
        elif avg_score <= -15:
            assessment = "Challenging Period"
            description = "Several transits indicate challenges. Focus on maintenance and caution."
        else:
            assessment = "Mixed Period"
            description = "Mixed influences. Selective approach recommended."
        
        # Factor in latta
        if latta_analysis.get("overall_latta_count", 0) >= 2:
            if "Favorable" in assessment:
                assessment = "Moderately Favorable Period"
                description += " However, multiple planetary kicks require attention."
        
        return {
            "assessment": assessment,
            "description": description,
            "total_score": total_score,
            "average_score": round(avg_score, 2),
            "favorable_count": good_count,
            "unfavorable_count": bad_count,
            "latta_severity": latta_analysis.get("severity", "None"),
            "ashtakavarga_quality": ashtakavarga_summary.get("overall_quality", "Unknown"),
        }
    
    def _calculate_area_impacts(
        self,
        results: List[EnhancedTransitResult],
        transit_houses: Dict[str, int],
        special_nak_analysis: Dict,
    ) -> Dict:
        """Calculate impacts on different life areas."""
        # House-based area mapping
        area_house_map = {
            "career": [10, 6, 2],
            "finance": [2, 11, 5],
            "health": [1, 6, 8],
            "relationships": [7, 5, 11],
            "marriage": [7, 2, 4],
            "education": [4, 5, 9],
            "travel": [3, 9, 12],
            "spirituality": [9, 12, 5],
            "family": [4, 2, 5],
            "property": [4, 2, 11],
        }
        
        # Planet-area associations
        planet_areas = {
            "Sun": ["career", "health", "authority"],
            "Moon": ["emotions", "relationships", "health"],
            "Mars": ["career", "property", "health"],
            "Mercury": ["education", "finance", "communication"],
            "Jupiter": ["finance", "education", "spirituality"],
            "Venus": ["relationships", "marriage", "finance"],
            "Saturn": ["career", "health", "longevity"],
            "Rahu": ["career", "travel", "technology"],
            "Ketu": ["spirituality", "health", "liberation"],
        }
        
        area_impacts = {}
        
        for area, houses in area_house_map.items():
            score = 0
            influencing_planets = []
            
            for result in results:
                # House influence
                if result.house_from_lagna in houses or result.house_from_moon in houses:
                    if result.final_status == "Good":
                        score += 10
                    elif result.final_status == "Bad":
                        score -= 10
                    influencing_planets.append({
                        "planet": result.planet,
                        "status": result.final_status,
                        "house_from_moon": result.house_from_moon,
                    })
                
                # Planet signification influence
                if area in planet_areas.get(result.planet, []):
                    if result.final_status == "Good":
                        score += 5
                    elif result.final_status == "Bad":
                        score -= 5
            
            # Determine area outlook
            if score >= 15:
                outlook = "Positive"
            elif score <= -15:
                outlook = "Challenging"
            else:
                outlook = "Neutral"
            
            area_impacts[area] = {
                "outlook": outlook,
                "score": score,
                "influencing_planets": influencing_planets[:3],  # Top 3
            }
        
        return area_impacts


def create_enhanced_transit_report(
    natal_moon_sign: int,
    natal_moon_nakshatra: int,
    natal_moon_longitude: float,
    natal_lagna_sign: int,
    natal_lagna_nakshatra: int,
    natal_positions: Dict[str, int],
    transit_positions: Dict[str, float],
    transit_date: str = None,
) -> EnhancedTransitReport:
    """
    Create comprehensive enhanced transit report.
    
    Main entry point for enhanced transit analysis.
    """
    analyzer = EnhancedTransitAnalyzer(
        natal_moon_sign=natal_moon_sign,
        natal_moon_nakshatra=natal_moon_nakshatra,
        natal_moon_longitude=natal_moon_longitude,
        natal_lagna_sign=natal_lagna_sign,
        natal_lagna_nakshatra=natal_lagna_nakshatra,
        natal_positions=natal_positions,
    )
    
    return analyzer.analyze_all(transit_positions, transit_date)
