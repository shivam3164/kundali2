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
    
    def _calculate_house_strength(
        self,
        house_num: int,
        lord: str,
        lord_house: int,
        lord_sign: str,
        planets_in_house: List[str],
        planets: Dict
    ) -> Dict[str, Any]:
        """Calculate overall house strength"""
        
        scores = {}
        total = 0
        max_possible = 0
        
        # 1. Lord dignity (0-5 points)
        dignity = self._get_planet_dignity(lord, lord_sign)
        dignity_scores = {"exalted": 5, "own_sign": 4, "moolatrikona": 4, 
                        "friendly": 3, "neutral": 2, "enemy": 1, "debilitated": 0}
        dignity_score = dignity_scores.get(dignity, 2)
        scores["lord_dignity"] = {"score": dignity_score, "max": 5, "dignity": dignity}
        total += dignity_score
        max_possible += 5
        
        # 2. Lord placement (0-5 points)
        placement_score = 2  # neutral
        if lord_house in self.TRIKONA_HOUSES:
            placement_score = 5
        elif lord_house in self.KENDRA_HOUSES:
            placement_score = 4
        elif lord_house in self.UPACHAYA_HOUSES:
            placement_score = 3
        elif lord_house in self.DUSTHANA_HOUSES:
            placement_score = 1
        if lord_house == house_num:
            placement_score = 5  # Own house
        scores["lord_placement"] = {"score": placement_score, "max": 5, "house": lord_house}
        total += placement_score
        max_possible += 5
        
        # 3. Benefic occupation (+2 each, max +6)
        # 4. Malefic occupation (-1 each, max -3)
        occupation_score = 0
        benefic_count = 0
        malefic_count = 0
        for planet in planets_in_house:
            if planet in self.NATURAL_BENEFICS:
                occupation_score += 2
                benefic_count += 1
            elif planet in self.NATURAL_MALEFICS:
                occupation_score -= 1
                malefic_count += 1
        occupation_score = max(min(occupation_score, 6), -3)
        scores["occupation"] = {
            "score": occupation_score + 3,  # Normalize to 0-6
            "max": 6,
            "benefics": benefic_count,
            "malefics": malefic_count
        }
        total += occupation_score + 3
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
            "breakdown": scores
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
