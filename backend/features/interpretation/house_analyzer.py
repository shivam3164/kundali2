"""
House Analyzer Service
Provides detailed house-wise interpretation following BPHS principles
"""

from typing import Dict, List, Optional, Any

# Import BPHS knowledge
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from bphs_knowledge.house_interpretations import (
    HOUSE_SIGNIFICATIONS,
    PLANET_IN_HOUSE_EFFECTS,
    HOUSE_LORD_IN_HOUSES,
    HOUSE_STRENGTH_FACTORS,
    HOUSE_REMEDIES
)


class HouseAnalyzer:
    """
    Analyzes houses in a birth chart following BPHS principles.
    
    Features:
    - House significations from BPHS
    - Planet in house effects
    - House lord placement effects
    - House strength calculation
    - Remedial measures
    """
    
    # Sign to lord mapping
    SIGN_LORDS = {
        "Aries": "Mars", "Taurus": "Venus", "Gemini": "Mercury",
        "Cancer": "Moon", "Leo": "Sun", "Virgo": "Mercury",
        "Libra": "Venus", "Scorpio": "Mars", "Sagittarius": "Jupiter",
        "Capricorn": "Saturn", "Aquarius": "Saturn", "Pisces": "Jupiter"
    }
    
    # Exaltation signs
    EXALTATION = {
        "Sun": "Aries", "Moon": "Taurus", "Mars": "Capricorn",
        "Mercury": "Virgo", "Jupiter": "Cancer", "Venus": "Pisces",
        "Saturn": "Libra", "Rahu": "Gemini", "Ketu": "Sagittarius"
    }
    
    # Debilitation signs
    DEBILITATION = {
        "Sun": "Libra", "Moon": "Scorpio", "Mars": "Cancer",
        "Mercury": "Pisces", "Jupiter": "Capricorn", "Venus": "Virgo",
        "Saturn": "Aries", "Rahu": "Sagittarius", "Ketu": "Gemini"
    }
    
    # Own signs
    OWN_SIGNS = {
        "Sun": ["Leo"], "Moon": ["Cancer"],
        "Mars": ["Aries", "Scorpio"], "Mercury": ["Gemini", "Virgo"],
        "Jupiter": ["Sagittarius", "Pisces"], "Venus": ["Taurus", "Libra"],
        "Saturn": ["Capricorn", "Aquarius"], "Rahu": ["Aquarius"], "Ketu": ["Scorpio"]
    }
    
    # House categories
    KENDRA_HOUSES = [1, 4, 7, 10]  # Angular houses
    TRIKONA_HOUSES = [1, 5, 9]     # Trinal houses
    UPACHAYA_HOUSES = [3, 6, 10, 11]  # Growth houses
    DUSTHANA_HOUSES = [6, 8, 12]   # Difficult houses
    MARAKA_HOUSES = [2, 7]         # Death-inflicting houses
    
    # Natural benefics and malefics
    NATURAL_BENEFICS = ["Jupiter", "Venus", "Mercury", "Moon"]
    NATURAL_MALEFICS = ["Saturn", "Mars", "Sun", "Rahu", "Ketu"]
    
    def __init__(self):
        pass
    
    def analyze_all_houses(
        self,
        chart_data: Dict[str, Any],
        include_remedies: bool = True
    ) -> Dict[str, Any]:
        """
        Analyze all 12 houses in the chart
        
        Args:
            chart_data: Full chart data with planets and houses
            include_remedies: Whether to include remedial measures
            
        Returns:
            Complete house-wise analysis
        """
        planets = chart_data.get("planets", {})
        houses = chart_data.get("houses", {})
        ascendant = chart_data.get("ascendant", {})
        
        # Build planet lookup
        planet_positions = self._build_planet_positions(planets)
        
        house_analyses = {}
        overall_strength = {}
        
        for house_num in range(1, 13):
            analysis = self.analyze_single_house(
                house_num=house_num,
                houses=houses,
                planets=planets,
                planet_positions=planet_positions,
                include_remedies=include_remedies
            )
            house_analyses[house_num] = analysis
            overall_strength[house_num] = analysis.get("strength", {}).get("total_score", 0)
        
        # Identify strongest and weakest houses
        sorted_houses = sorted(overall_strength.items(), key=lambda x: x[1], reverse=True)
        strongest = [h for h, s in sorted_houses[:3]]
        weakest = [h for h, s in sorted_houses[-3:]]
        
        return {
            "houses": house_analyses,
            "summary": {
                "strongest_houses": strongest,
                "weakest_houses": weakest,
                "kendra_strength": self._average_strength([overall_strength.get(h, 0) for h in self.KENDRA_HOUSES]),
                "trikona_strength": self._average_strength([overall_strength.get(h, 0) for h in self.TRIKONA_HOUSES]),
                "dusthana_strength": self._average_strength([overall_strength.get(h, 0) for h in self.DUSTHANA_HOUSES]),
            },
            "life_areas_summary": self._generate_life_areas_summary(house_analyses)
        }
    
    def analyze_single_house(
        self,
        house_num: int,
        houses: Dict,
        planets: Dict,
        planet_positions: Dict = None,
        include_remedies: bool = True
    ) -> Dict[str, Any]:
        """
        Analyze a single house in detail
        """
        if planet_positions is None:
            planet_positions = self._build_planet_positions(planets)
        
        # Get house data
        house_key = str(house_num)
        house_data = houses.get(house_key, {})
        
        sign = house_data.get("sign", "")
        lord = house_data.get("lord", self.SIGN_LORDS.get(sign, ""))
        planets_in_house = house_data.get("planets_in_house", [])
        
        # Get lord's position
        lord_house = planet_positions.get(lord, {}).get("house", 0)
        lord_sign = planet_positions.get(lord, {}).get("sign", "")
        
        # Get BPHS significations
        significations = HOUSE_SIGNIFICATIONS.get(house_num, {})
        
        # Analyze planets in house
        planet_effects = self._analyze_planets_in_house(house_num, planets_in_house, planets)
        
        # Analyze lord placement
        lord_analysis = self._analyze_lord_placement(house_num, lord, lord_house, lord_sign)
        
        # Calculate house strength
        strength = self._calculate_house_strength(
            house_num=house_num,
            lord=lord,
            lord_house=lord_house,
            lord_sign=lord_sign,
            planets_in_house=planets_in_house,
            planets=planets
        )
        
        # Generate interpretation
        interpretation = self._generate_house_interpretation(
            house_num=house_num,
            significations=significations,
            lord=lord,
            lord_house=lord_house,
            planet_effects=planet_effects,
            lord_analysis=lord_analysis,
            strength=strength
        )
        
        result = {
            "house_number": house_num,
            "name": significations.get("name", f"House {house_num}"),
            "english_name": significations.get("english", ""),
            "sign": sign,
            "lord": lord,
            "lord_house": lord_house,
            "lord_sign": lord_sign,
            "planets_in_house": planets_in_house,
            "significations": {
                "karaka": significations.get("karaka", ""),
                "body_parts": significations.get("body_parts", []),
                "primary": significations.get("significations", {}).get("primary", []),
                "secondary": significations.get("significations", {}).get("secondary", []),
                "represents": significations.get("represents", ""),
            },
            "planet_effects": planet_effects,
            "lord_analysis": lord_analysis,
            "strength": strength,
            "interpretation": interpretation,
            "source": significations.get("source", "BPHS")
        }
        
        if include_remedies:
            result["remedies"] = self._get_remedies(house_num, strength)
        
        return result
    
    def _build_planet_positions(self, planets: Dict) -> Dict:
        """Build lookup for planet positions"""
        positions = {}
        for name, data in planets.items():
            positions[name] = {
                "house": data.get("house", 0),
                "sign": data.get("sign", ""),
                "degree": data.get("degree", 0),
                "dignity": data.get("dignity", "neutral"),
                "is_retrograde": data.get("is_retrograde", False),
                "is_combust": data.get("is_combust", False)
            }
        return positions
    
    def _analyze_planets_in_house(
        self,
        house_num: int,
        planets_in_house: List[str],
        planets: Dict
    ) -> List[Dict]:
        """Analyze effects of planets placed in the house"""
        effects = []
        
        for planet_name in planets_in_house:
            planet_data = planets.get(planet_name, {})
            
            # Get BPHS effect
            bphs_effect = PLANET_IN_HOUSE_EFFECTS.get(planet_name, {}).get(house_num, {})
            
            effect_text = bphs_effect.get("effect", f"{planet_name} influences house {house_num}")
            positive = bphs_effect.get("positive", [])
            negative = bphs_effect.get("negative", [])
            
            # Determine if planet is benefic or malefic for this placement
            is_natural_benefic = planet_name in self.NATURAL_BENEFICS
            
            # Check dignity
            dignity = planet_data.get("dignity", "neutral")
            is_strong = dignity in ["exalted", "own_sign", "moolatrikona"]
            is_weak = dignity in ["debilitated", "enemy"]
            
            # Retrograde consideration
            is_retrograde = planet_data.get("is_retrograde", False)
            
            effects.append({
                "planet": planet_name,
                "effect": effect_text,
                "positive_results": positive,
                "negative_results": negative,
                "is_natural_benefic": is_natural_benefic,
                "dignity": dignity,
                "is_strong": is_strong,
                "is_weak": is_weak,
                "is_retrograde": is_retrograde,
                "source": bphs_effect.get("source", "BPHS")
            })
        
        return effects
    
    def _analyze_lord_placement(
        self,
        house_num: int,
        lord: str,
        lord_house: int,
        lord_sign: str
    ) -> Dict[str, Any]:
        """Analyze the effect of house lord's placement"""
        
        # Get BPHS effect for lord placement
        lord_effect = HOUSE_LORD_IN_HOUSES.get(house_num, {}).get(lord_house, {})
        
        effect_text = lord_effect.get("effect", f"Lord of house {house_num} is in house {lord_house}")
        source = lord_effect.get("source", "BPHS Ch.24")
        
        # Determine placement quality
        placement_quality = "neutral"
        placement_notes = []
        
        if lord_house in self.KENDRA_HOUSES:
            placement_quality = "good"
            placement_notes.append("Lord in Kendra (angular house) - strengthens the house")
        
        if lord_house in self.TRIKONA_HOUSES:
            placement_quality = "excellent"
            placement_notes.append("Lord in Trikona (trinal house) - very auspicious")
        
        if lord_house in self.DUSTHANA_HOUSES and lord_house != house_num:
            if placement_quality == "neutral":
                placement_quality = "challenging"
            placement_notes.append("Lord in Dusthana - may cause difficulties")
        
        if lord_house == house_num:
            placement_quality = "excellent"
            placement_notes.append("Lord in own house - very strong")
        
        # Check dignity
        dignity = self._get_planet_dignity(lord, lord_sign)
        if dignity in ["exalted", "own_sign"]:
            placement_notes.append(f"Lord is {dignity} - enhanced results")
        elif dignity == "debilitated":
            placement_notes.append("Lord is debilitated - reduced results, needs remedies")
        
        return {
            "lord": lord,
            "placed_in_house": lord_house,
            "placed_in_sign": lord_sign,
            "bphs_effect": effect_text,
            "placement_quality": placement_quality,
            "notes": placement_notes,
            "dignity": dignity,
            "source": source
        }
    
    def _get_planet_dignity(self, planet: str, sign: str) -> str:
        """Determine planet's dignity in a sign"""
        if self.EXALTATION.get(planet) == sign:
            return "exalted"
        if self.DEBILITATION.get(planet) == sign:
            return "debilitated"
        if sign in self.OWN_SIGNS.get(planet, []):
            return "own_sign"
        return "neutral"
    
    def _calculate_house_strength_legacy(
        self,
        house_num: int,
        lord: str,
        lord_house: int,
        lord_sign: str,
        planets_in_house: List[str],
        planets: Dict
    ) -> Dict[str, Any]:
        """
        Calculate house strength using the LEGACY formula (unchanged from original).
        Returns full transparency: factor-by-factor and planet-by-planet breakdown.
        """
        scores = {}
        total = 0
        max_possible = 0
        explanation_lines = []
        
        # 1. Lord dignity (0-5 points)
        dignity = self._get_planet_dignity(lord, lord_sign)
        dignity_scores = {"exalted": 5, "own_sign": 4, "moolatrikona": 4, 
                        "friendly": 3, "neutral": 2, "enemy": 1, "debilitated": 0}
        dignity_score = dignity_scores.get(dignity, 2)
        dignity_reason = f"{lord} is {dignity} in {lord_sign}"
        scores["lord_dignity"] = {
            "score": dignity_score,
            "max": 5,
            "lord": lord,
            "sign": lord_sign,
            "dignity": dignity,
            "reason": dignity_reason
        }
        explanation_lines.append(f"Lord Dignity: {dignity_score}/5 — {dignity_reason}")
        total += dignity_score
        max_possible += 5
        
        # 2. Lord placement (0-5 points)
        placement_score = 2  # neutral
        placement_category = "neutral"
        if lord_house == house_num:
            placement_score = 5
            placement_category = "own_house"
            placement_reason = f"{lord} is in its own house (H{lord_house}) — excellent"
        elif lord_house in self.TRIKONA_HOUSES:
            placement_score = 5
            placement_category = "trikona"
            placement_reason = f"{lord} is in trikona house H{lord_house} — very auspicious"
        elif lord_house in self.KENDRA_HOUSES:
            placement_score = 4
            placement_category = "kendra"
            placement_reason = f"{lord} is in kendra house H{lord_house} — strong"
        elif lord_house in self.UPACHAYA_HOUSES:
            placement_score = 3
            placement_category = "upachaya"
            placement_reason = f"{lord} is in upachaya house H{lord_house} — growth over time"
        elif lord_house in self.DUSTHANA_HOUSES:
            placement_score = 1
            placement_category = "dusthana"
            placement_reason = f"{lord} is in dusthana house H{lord_house} — challenges"
        else:
            placement_reason = f"{lord} is in house H{lord_house} — neutral placement"
        
        scores["lord_placement"] = {
            "score": placement_score,
            "max": 5,
            "lord": lord,
            "house": lord_house,
            "category": placement_category,
            "reason": placement_reason
        }
        explanation_lines.append(f"Lord Placement: {placement_score}/5 — {placement_reason}")
        total += placement_score
        max_possible += 5
        
        # 3. Occupation: benefics (+2 each), malefics (-1 each)
        raw_occupation_score = 0
        benefic_planets = []
        malefic_planets = []
        contributions = []
        
        for planet in planets_in_house:
            if planet in self.NATURAL_BENEFICS:
                raw_occupation_score += 2
                benefic_planets.append(planet)
                contributions.append({
                    "planet": planet,
                    "kind": "natural_benefic",
                    "delta": +2,
                    "rule": f"{planet} is a natural benefic → +2"
                })
            elif planet in self.NATURAL_MALEFICS:
                raw_occupation_score -= 1
                malefic_planets.append(planet)
                contributions.append({
                    "planet": planet,
                    "kind": "natural_malefic",
                    "delta": -1,
                    "rule": f"{planet} is a natural malefic → −1"
                })
        
        # Clamp to [-3, +6] then normalize to [0, 6]
        clamped_score = max(min(raw_occupation_score, 6), -3)
        normalized_score = clamped_score + 3  # shift to 0-6 range
        
        if planets_in_house:
            occupation_reason = f"Planets in house: benefics {benefic_planets or 'none'}, malefics {malefic_planets or 'none'} → raw {raw_occupation_score}, normalized {normalized_score}/6"
        else:
            occupation_reason = "No planets occupy this house → neutral score 3/6"
            normalized_score = 3
        
        scores["occupation"] = {
            "score": normalized_score,
            "max": 6,
            "raw_score": raw_occupation_score,
            "clamped_score": clamped_score,
            "benefic_planets": benefic_planets,
            "malefic_planets": malefic_planets,
            "contributions": contributions,
            "reason": occupation_reason
        }
        explanation_lines.append(f"Occupation: {normalized_score}/6 — {occupation_reason}")
        total += normalized_score
        max_possible += 6
        
        # Calculate percentage
        percentage = (total / max_possible) * 100 if max_possible > 0 else 50
        
        # Determine strength level
        if percentage >= 80:
            level = "Very Strong"
        elif percentage >= 60:
            level = "Strong"
        elif percentage >= 40:
            level = "Average"
        elif percentage >= 20:
            level = "Weak"
        else:
            level = "Very Weak"
        
        return {
            "total_score": total,
            "max_score": max_possible,
            "percentage": round(percentage, 1),
            "level": level,
            "breakdown": scores,
            "explanation": explanation_lines,
            "formula": "legacy: lord_dignity(0-5) + lord_placement(0-5) + occupation(0-6)"
        }
    
    def _calculate_house_strength_recommended(
        self,
        house_num: int,
        lord: str,
        lord_house: int,
        lord_sign: str,
        planets_in_house: List[str],
        planets: Dict
    ) -> Dict[str, Any]:
        """
        Calculate house strength using the RECOMMENDED formula with additional BPHS factors.
        Factors:
          1. Lord dignity (0-5)
          2. Lord placement (0-5)
          3. Occupation by benefics/malefics (0-6)
          4. House type modifier (0-3) — kendra/trikona get bonus
          5. Combustion penalty (-1 per combust planet in house)
          6. Retrograde consideration (+1 for retrograde benefic, -1 for retrograde malefic)
        """
        scores = {}
        total = 0
        max_possible = 0
        explanation_lines = []
        
        # 1. Lord dignity (0-5 points) — same as legacy
        dignity = self._get_planet_dignity(lord, lord_sign)
        dignity_scores = {"exalted": 5, "own_sign": 4, "moolatrikona": 4, 
                        "friendly": 3, "neutral": 2, "enemy": 1, "debilitated": 0}
        dignity_score = dignity_scores.get(dignity, 2)
        dignity_reason = f"{lord} is {dignity} in {lord_sign}"
        scores["lord_dignity"] = {
            "score": dignity_score,
            "max": 5,
            "lord": lord,
            "sign": lord_sign,
            "dignity": dignity,
            "reason": dignity_reason
        }
        explanation_lines.append(f"Lord Dignity: {dignity_score}/5 — {dignity_reason}")
        total += dignity_score
        max_possible += 5
        
        # 2. Lord placement (0-5 points) — same as legacy
        placement_score = 2
        placement_category = "neutral"
        if lord_house == house_num:
            placement_score = 5
            placement_category = "own_house"
            placement_reason = f"{lord} in own house H{lord_house} — excellent"
        elif lord_house in self.TRIKONA_HOUSES:
            placement_score = 5
            placement_category = "trikona"
            placement_reason = f"{lord} in trikona H{lord_house} — very auspicious"
        elif lord_house in self.KENDRA_HOUSES:
            placement_score = 4
            placement_category = "kendra"
            placement_reason = f"{lord} in kendra H{lord_house} — strong"
        elif lord_house in self.UPACHAYA_HOUSES:
            placement_score = 3
            placement_category = "upachaya"
            placement_reason = f"{lord} in upachaya H{lord_house} — growth"
        elif lord_house in self.DUSTHANA_HOUSES:
            placement_score = 1
            placement_category = "dusthana"
            placement_reason = f"{lord} in dusthana H{lord_house} — challenges"
        else:
            placement_reason = f"{lord} in H{lord_house} — neutral"
        
        scores["lord_placement"] = {
            "score": placement_score,
            "max": 5,
            "lord": lord,
            "house": lord_house,
            "category": placement_category,
            "reason": placement_reason
        }
        explanation_lines.append(f"Lord Placement: {placement_score}/5 — {placement_reason}")
        total += placement_score
        max_possible += 5
        
        # 3. Occupation (0-6) — same logic as legacy with planet ledger
        raw_occupation_score = 0
        benefic_planets = []
        malefic_planets = []
        contributions = []
        
        for planet in planets_in_house:
            if planet in self.NATURAL_BENEFICS:
                raw_occupation_score += 2
                benefic_planets.append(planet)
                contributions.append({"planet": planet, "kind": "natural_benefic", "delta": +2, "rule": f"{planet} benefic → +2"})
            elif planet in self.NATURAL_MALEFICS:
                raw_occupation_score -= 1
                malefic_planets.append(planet)
                contributions.append({"planet": planet, "kind": "natural_malefic", "delta": -1, "rule": f"{planet} malefic → −1"})
        
        clamped = max(min(raw_occupation_score, 6), -3)
        normalized = clamped + 3
        if not planets_in_house:
            normalized = 3
            occupation_reason = "No planets → neutral 3/6"
        else:
            occupation_reason = f"Benefics {benefic_planets or '[]'}, malefics {malefic_planets or '[]'} → {normalized}/6"
        
        scores["occupation"] = {
            "score": normalized,
            "max": 6,
            "raw_score": raw_occupation_score,
            "benefic_planets": benefic_planets,
            "malefic_planets": malefic_planets,
            "contributions": contributions,
            "reason": occupation_reason
        }
        explanation_lines.append(f"Occupation: {normalized}/6 — {occupation_reason}")
        total += normalized
        max_possible += 6
        
        # 4. House type modifier (0-3) — NEW in recommended
        house_type_score = 1  # neutral
        if house_num in self.KENDRA_HOUSES:
            house_type_score = 3
            house_type_reason = f"H{house_num} is a kendra (angular) house — naturally strong"
        elif house_num in self.TRIKONA_HOUSES:
            house_type_score = 3
            house_type_reason = f"H{house_num} is a trikona (trinal) house — auspicious"
        elif house_num in self.UPACHAYA_HOUSES:
            house_type_score = 2
            house_type_reason = f"H{house_num} is an upachaya (growth) house — improves with time"
        elif house_num in self.DUSTHANA_HOUSES:
            house_type_score = 0
            house_type_reason = f"H{house_num} is a dusthana (difficult) house — inherently challenging"
        else:
            house_type_reason = f"H{house_num} is a neutral house"
        
        scores["house_type"] = {
            "score": house_type_score,
            "max": 3,
            "house_num": house_num,
            "reason": house_type_reason
        }
        explanation_lines.append(f"House Type: {house_type_score}/3 — {house_type_reason}")
        total += house_type_score
        max_possible += 3
        
        # 5. Combustion penalty (-1 per combust planet in house, min 0, max contribution 0)
        combust_penalty = 0
        combust_planets = []
        for planet in planets_in_house:
            planet_data = planets.get(planet, {})
            if planet_data.get("is_combust", False):
                combust_penalty -= 1
                combust_planets.append(planet)
        
        # This is a penalty factor: score range is -3 to 0, we add 3 for 0-3 scale
        combust_normalized = max(combust_penalty, -3) + 3
        if combust_planets:
            combust_reason = f"Combust planets {combust_planets} weaken house → penalty {combust_penalty}"
        else:
            combust_reason = "No combust planets — no penalty"
        
        scores["combustion"] = {
            "score": combust_normalized,
            "max": 3,
            "raw_penalty": combust_penalty,
            "combust_planets": combust_planets,
            "reason": combust_reason
        }
        explanation_lines.append(f"Combustion: {combust_normalized}/3 — {combust_reason}")
        total += combust_normalized
        max_possible += 3
        
        # 6. Retrograde consideration (benefic retro +1, malefic retro -1)
        retro_score = 0
        retro_effects = []
        for planet in planets_in_house:
            planet_data = planets.get(planet, {})
            if planet_data.get("is_retrograde", False):
                if planet in self.NATURAL_BENEFICS:
                    retro_score += 1
                    retro_effects.append({"planet": planet, "delta": +1, "rule": f"{planet} retrograde benefic intensifies positive → +1"})
                elif planet in self.NATURAL_MALEFICS:
                    retro_score -= 1
                    retro_effects.append({"planet": planet, "delta": -1, "rule": f"{planet} retrograde malefic intensifies negative → −1"})
        
        retro_normalized = max(min(retro_score, 2), -2) + 2  # range 0-4
        if retro_effects:
            retro_reason = f"Retrograde effects: {[e['planet'] for e in retro_effects]} → {retro_normalized}/4"
        else:
            retro_reason = "No retrograde planets in house → neutral 2/4"
            retro_normalized = 2
        
        scores["retrograde"] = {
            "score": retro_normalized,
            "max": 4,
            "raw_score": retro_score,
            "effects": retro_effects,
            "reason": retro_reason
        }
        explanation_lines.append(f"Retrograde: {retro_normalized}/4 — {retro_reason}")
        total += retro_normalized
        max_possible += 4
        
        # Calculate percentage
        percentage = (total / max_possible) * 100 if max_possible > 0 else 50
        
        # Determine strength level
        if percentage >= 80:
            level = "Very Strong"
        elif percentage >= 60:
            level = "Strong"
        elif percentage >= 40:
            level = "Average"
        elif percentage >= 20:
            level = "Weak"
        else:
            level = "Very Weak"
        
        return {
            "total_score": total,
            "max_score": max_possible,
            "percentage": round(percentage, 1),
            "level": level,
            "breakdown": scores,
            "explanation": explanation_lines,
            "formula": "recommended: lord_dignity(0-5) + lord_placement(0-5) + occupation(0-6) + house_type(0-3) + combustion(0-3) + retrograde(0-4)"
        }
    
    def _calculate_house_strength(
        self,
        house_num: int,
        lord: str,
        lord_house: int,
        lord_sign: str,
        planets_in_house: List[str],
        planets: Dict
    ) -> Dict[str, Any]:
        """
        Calculate both legacy and recommended house strength.
        Returns combined result with backward compatibility.
        """
        legacy = self._calculate_house_strength_legacy(
            house_num, lord, lord_house, lord_sign, planets_in_house, planets
        )
        recommended = self._calculate_house_strength_recommended(
            house_num, lord, lord_house, lord_sign, planets_in_house, planets
        )
        
        # Return combined structure with backward compatibility
        return {
            # Backward compatible fields (mapped to legacy)
            "total_score": legacy["total_score"],
            "max_score": legacy["max_score"],
            "percentage": legacy["percentage"],
            "level": legacy["level"],
            "breakdown": legacy["breakdown"],
            # New detailed structure
            "legacy": legacy,
            "recommended": recommended
        }
    
    def _generate_house_interpretation(
        self,
        house_num: int,
        significations: Dict,
        lord: str,
        lord_house: int,
        planet_effects: List[Dict],
        lord_analysis: Dict,
        strength: Dict
    ) -> Dict[str, Any]:
        """Generate comprehensive interpretation text"""
        
        # Overview
        overview = f"{significations.get('english', f'House {house_num}')} ({significations.get('name', '')}) "
        overview += f"represents {significations.get('represents', 'various life matters')}. "
        overview += f"This house is ruled by {lord}, "
        
        if lord_house == house_num:
            overview += f"who is strongly placed in its own house."
        else:
            overview += f"who is placed in house {lord_house}."
        
        # Strength assessment
        strength_text = f"This house is {strength.get('level', 'Average')} "
        strength_text += f"with a strength score of {strength.get('percentage', 50)}%. "
        
        # Planet effects summary
        planet_summary = ""
        if planet_effects:
            planets = [e['planet'] for e in planet_effects]
            planet_summary = f"The presence of {', '.join(planets)} in this house "
            benefic_effects = [e for e in planet_effects if e.get('is_natural_benefic')]
            if benefic_effects:
                planet_summary += "brings positive influences. "
            else:
                planet_summary += "requires careful handling. "
        else:
            planet_summary = "No planets occupy this house, so results depend primarily on the lord's placement. "
        
        # Lord effect
        lord_text = f"The placement of {lord} in house {lord_house} indicates: "
        lord_text += lord_analysis.get('bphs_effect', 'various effects on this house')
        lord_text += f" ({lord_analysis.get('source', 'BPHS')})"
        
        # Key results
        key_results = []
        
        # Add based on significations
        if strength.get('percentage', 50) >= 60:
            key_results.append(f"Good results in {significations.get('significations', {}).get('primary', ['this area'])[0].lower()}")
            if significations.get('benefic_occupation'):
                key_results.append(significations.get('benefic_occupation'))
        else:
            if significations.get('malefic_occupation'):
                key_results.append(f"May face challenges: {significations.get('malefic_occupation', 'various obstacles')}")
        
        # Add lord-specific results
        if lord_analysis.get('placement_quality') == 'excellent':
            key_results.append(f"Excellent results from {lord} as house lord")
        elif lord_analysis.get('placement_quality') == 'challenging':
            key_results.append(f"Lord's challenging placement may delay results")
        
        return {
            "overview": overview,
            "strength_assessment": strength_text,
            "planet_summary": planet_summary,
            "lord_effect": lord_text,
            "key_results": key_results
        }
    
    def _get_remedies(self, house_num: int, strength: Dict) -> Dict[str, Any]:
        """Get remedial measures for the house"""
        
        remedies = HOUSE_REMEDIES.get(house_num, {})
        
        level = strength.get('level', 'Average')
        percentage = strength.get('percentage', 50)
        
        recommended = []
        
        if percentage < 40:
            # Weak house - suggest more remedies
            recommended.extend(remedies.get('weak_lord', [])[:2])
            recommended.extend(remedies.get('afflicted', [])[:1])
        elif percentage < 60:
            # Average house - general remedies
            recommended.extend(remedies.get('general', [])[:2])
        else:
            # Strong house - maintenance remedies
            recommended.extend(remedies.get('general', [])[:1])
        
        return {
            "required_level": "High" if percentage < 40 else "Medium" if percentage < 60 else "Low",
            "recommended": recommended,
            "all_remedies": remedies
        }
    
    def _average_strength(self, scores: List[float]) -> float:
        """Calculate average strength"""
        if not scores:
            return 0
        return round(sum(scores) / len(scores), 1)
    
    def _generate_life_areas_summary(self, house_analyses: Dict) -> Dict[str, Any]:
        """Generate summary for key life areas based on relevant houses"""
        
        life_areas = {
            "self_health": {
                "houses": [1, 6, 8],
                "description": "Physical self, health, and longevity"
            },
            "wealth_finances": {
                "houses": [2, 11],
                "description": "Wealth, income, and financial gains"
            },
            "family_home": {
                "houses": [2, 4],
                "description": "Family, mother, home, and property"
            },
            "career_status": {
                "houses": [10, 6],
                "description": "Career, profession, and social status"
            },
            "relationships": {
                "houses": [7, 5],
                "description": "Marriage, partnerships, and romance"
            },
            "children_creativity": {
                "houses": [5],
                "description": "Children, creativity, and intelligence"
            },
            "spirituality": {
                "houses": [9, 12],
                "description": "Spirituality, higher learning, and liberation"
            }
        }
        
        summaries = {}
        for area, config in life_areas.items():
            relevant_houses = config["houses"]
            strengths = []
            for h in relevant_houses:
                analysis = house_analyses.get(h, {})
                strength = analysis.get("strength", {}).get("percentage", 50)
                strengths.append(strength)
            
            avg_strength = self._average_strength(strengths)
            
            if avg_strength >= 70:
                outlook = "Very Favorable"
            elif avg_strength >= 50:
                outlook = "Favorable"
            elif avg_strength >= 30:
                outlook = "Mixed"
            else:
                outlook = "Challenging"
            
            summaries[area] = {
                "description": config["description"],
                "relevant_houses": relevant_houses,
                "average_strength": avg_strength,
                "outlook": outlook
            }
        
        return summaries


# Create singleton instance
house_analyzer = HouseAnalyzer()


def get_house_analysis(chart_data: Dict[str, Any], include_remedies: bool = True) -> Dict[str, Any]:
    """Convenience function to get house analysis"""
    return house_analyzer.analyze_all_houses(chart_data, include_remedies)


def get_single_house_analysis(
    house_num: int,
    chart_data: Dict[str, Any],
    include_remedies: bool = True
) -> Dict[str, Any]:
    """Convenience function to get single house analysis"""
    planets = chart_data.get("planets", {})
    houses = chart_data.get("houses", {})
    return house_analyzer.analyze_single_house(
        house_num=house_num,
        houses=houses,
        planets=planets,
        include_remedies=include_remedies
    )





