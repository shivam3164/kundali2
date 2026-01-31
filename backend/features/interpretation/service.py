"""
Interpretation Feature - Service Layer
Chart interpretation following BPHS principles
"""

from typing import Dict, List, Optional, Any


# ============================================
# INTERPRETATION TEMPLATES
# ============================================

# Planet in sign interpretations
PLANET_SIGN_EFFECTS = {
    "Sun": {
        "Aries": "Leadership, courage, pioneering spirit. Natural authority.",
        "Taurus": "Steady determination, artistic appreciation, material focus.",
        "Gemini": "Intellectual curiosity, communication skills, versatility.",
        "Cancer": "Emotional sensitivity, nurturing, family-oriented.",
        "Leo": "Strong ego, creativity, natural performer, generous.",
        "Virgo": "Analytical, service-oriented, attention to detail.",
        "Libra": "Diplomatic, partnership-focused, aesthetic sense.",
        "Scorpio": "Intense, transformative, research-oriented.",
        "Sagittarius": "Philosophical, adventurous, teaching ability.",
        "Capricorn": "Ambitious, disciplined, career-focused.",
        "Aquarius": "Humanitarian, innovative, independent thinker.",
        "Pisces": "Spiritual, compassionate, intuitive.",
    },
    "Moon": {
        "Aries": "Quick emotions, independent, needs action.",
        "Taurus": "Stable emotions, comfort-seeking, sensual.",
        "Gemini": "Changeable emotions, needs mental stimulation.",
        "Cancer": "Deep emotions, nurturing, home-loving.",
        "Leo": "Proud emotions, needs recognition, dramatic.",
        "Virgo": "Analytical emotions, health-conscious, critical.",
        "Libra": "Needs harmony, partnership-oriented, indecisive.",
        "Scorpio": "Intense emotions, secretive, transformative.",
        "Sagittarius": "Optimistic emotions, freedom-loving, philosophical.",
        "Capricorn": "Reserved emotions, responsible, ambitious.",
        "Aquarius": "Detached emotions, humanitarian, unconventional.",
        "Pisces": "Intuitive, compassionate, escapist tendencies.",
    },
}

# Planet in house interpretations
PLANET_HOUSE_EFFECTS = {
    "Sun": {
        1: "Strong personality, leadership, good health, self-confident.",
        2: "Wealth through self-effort, authoritative speech, family pride.",
        3: "Brave, good siblings, communication skills, short travels.",
        4: "Government property, strong mother, domestic leadership.",
        5: "Creative intelligence, children, speculation success.",
        6: "Victory over enemies, health issues, service to others.",
        7: "Dominant partner, business success, public recognition.",
        8: "Interest in occult, inheritance, health concerns.",
        9: "Fortunate, philosophical, father figure, long travels.",
        10: "Career success, authority, government favor.",
        11: "Gains through government, influential friends, fulfilled desires.",
        12: "Spiritual, foreign residence, hidden enemies.",
    },
    "Moon": {
        1: "Emotional, changeable, public appeal, travels.",
        2: "Fluctuating wealth, sweet speech, family focus.",
        3: "Emotional courage, sisters, short journeys.",
        4: "Happy home life, property, mother's blessing.",
        5: "Emotional intelligence, many children, creative.",
        6: "Health fluctuations, emotional enemies, service.",
        7: "Marriage important, emotional partnerships.",
        8: "Emotional upheavals, interest in mysteries.",
        9: "Spiritual emotions, fortunate travels.",
        10: "Public career, emotional reputation.",
        11: "Gains through public, many friends.",
        12: "Emotional isolation, spiritual, foreign lands.",
    },
}

# House significations
HOUSE_MEANINGS = {
    1: {"area": "Self, body, personality", "life_themes": ["Identity", "Physical health", "First impressions"]},
    2: {"area": "Wealth, family, speech", "life_themes": ["Finances", "Family values", "Communication"]},
    3: {"area": "Siblings, courage, skills", "life_themes": ["Siblings", "Short travels", "Talents"]},
    4: {"area": "Home, mother, happiness", "life_themes": ["Property", "Mother", "Emotional security"]},
    5: {"area": "Children, creativity, intelligence", "life_themes": ["Children", "Romance", "Speculation"]},
    6: {"area": "Enemies, health, service", "life_themes": ["Health", "Enemies", "Daily work"]},
    7: {"area": "Marriage, partnerships, business", "life_themes": ["Marriage", "Business", "Public dealings"]},
    8: {"area": "Longevity, transformation, occult", "life_themes": ["Death/rebirth", "Inheritance", "Research"]},
    9: {"area": "Fortune, dharma, higher learning", "life_themes": ["Luck", "Father", "Spirituality"]},
    10: {"area": "Career, status, authority", "life_themes": ["Profession", "Reputation", "Public image"]},
    11: {"area": "Gains, desires, elder siblings", "life_themes": ["Income", "Friends", "Aspirations"]},
    12: {"area": "Loss, liberation, foreign", "life_themes": ["Expenses", "Spirituality", "Foreign lands"]},
}

# Dignity effects
DIGNITY_EFFECTS = {
    "exalted": "Planet is at its strongest, giving excellent results in its significations.",
    "own_sign": "Planet is comfortable and gives good results naturally.",
    "moolatrikona": "Planet is very strong, gives positive results in its domain.",
    "friendly": "Planet is supported, gives moderately good results.",
    "neutral": "Planet gives average results, neither particularly good nor bad.",
    "enemy": "Planet faces obstacles, may give delayed or mixed results.",
    "debilitated": "Planet is at its weakest, may give challenges in its significations.",
}


# ============================================
# INTERPRETATION SERVICE
# ============================================

class InterpretationService:
    """
    Chart interpretation service following BPHS
    
    Provides interpretations for:
    - Planets in signs and houses
    - House lords and their placements
    - Life areas (career, relationships, etc.)
    - Yoga effects
    - Dasha periods
    - Remedial measures
    """
    
    def __init__(self, knowledge=None):
        self.knowledge = knowledge
    
    def generate_full_interpretation(
        self,
        chart_data: Dict[str, Any],
        yoga_data: Optional[Dict[str, Any]] = None,
        dasha_data: Optional[Dict[str, Any]] = None,
        areas: Optional[List[str]] = None,
        depth: str = "standard",
        include_remedies: bool = True
    ) -> Dict[str, Any]:
        """
        Generate complete chart interpretation
        """
        planets = chart_data.get("planets", {})
        houses = chart_data.get("houses", {})
        ascendant = chart_data.get("ascendant", {})
        
        # Generate interpretations
        planet_interps = self._interpret_planets(planets, depth)
        house_interps = self._interpret_houses(houses, planets, depth)
        
        # Generate area interpretations
        all_areas = areas or ["personality", "career", "relationships", "health", "wealth", "spirituality"]
        area_interps = {
            area: self._interpret_area(area, chart_data, yoga_data, depth)
            for area in all_areas
        }
        
        # Overall summary
        overall = self._generate_overall_summary(chart_data, yoga_data)
        
        # Yoga effects
        yoga_effects = self._interpret_yogas(yoga_data) if yoga_data else []
        
        # Dasha interpretation
        dasha_interp = self._interpret_dasha(dasha_data) if dasha_data else None
        
        # Remedies
        remedies = self._generate_remedies(chart_data, yoga_data) if include_remedies else None
        
        return {
            "birth_data": chart_data.get("birth_data", {}),
            "overall_summary": overall,
            "planet_interpretations": planet_interps,
            "house_interpretations": house_interps,
            "area_interpretations": area_interps,
            "yoga_effects": yoga_effects,
            "current_dasha_interpretation": dasha_interp,
            "recommended_remedies": remedies,
        }
    
    def _interpret_planets(self, planets: Dict, depth: str) -> Dict[str, Dict]:
        """Interpret each planet's placement"""
        interpretations = {}
        
        for name, data in planets.items():
            house = data.get("house", 0)
            sign = data.get("sign", "")
            dignity = data.get("dignity", "neutral")
            
            # Get sign effects
            sign_effect = PLANET_SIGN_EFFECTS.get(name, {}).get(sign, "")
            
            # Get house effects
            house_effect = PLANET_HOUSE_EFFECTS.get(name, {}).get(house, "")
            
            # Get dignity effect
            dignity_effect = DIGNITY_EFFECTS.get(dignity, "")
            
            # Determine strengths and challenges
            strengths = []
            challenges = []
            
            if dignity in ["exalted", "own_sign", "moolatrikona"]:
                strengths.append(f"{name} is strong in {sign}")
            elif dignity in ["debilitated", "enemy"]:
                challenges.append(f"{name} faces challenges in {sign}")
            
            if data.get("is_retrograde"):
                challenges.append(f"{name} is retrograde - internalized energy")
            
            if data.get("is_combust"):
                challenges.append(f"{name} is combust - diminished expression")
            
            interpretations[name] = {
                "planet": name,
                "house": house,
                "sign": sign,
                "dignity": dignity,
                "general": f"{name} in {sign} in house {house}. {dignity_effect}",
                "house_effects": house_effect or f"{name} influences house {house} matters.",
                "sign_effects": sign_effect or f"{name} expresses through {sign} qualities.",
                "strengths": strengths,
                "challenges": challenges,
            }
        
        return interpretations
    
    def _interpret_houses(self, houses: Dict, planets: Dict, depth: str) -> Dict[str, Dict]:
        """Interpret each house"""
        interpretations = {}
        
        # Build planet houses lookup
        planet_houses = {name: data.get("house", 0) for name, data in planets.items()}
        
        for house_num_str, data in houses.items():
            house_num = int(house_num_str)
            sign = data.get("sign", "")
            lord = data.get("lord", "")
            planets_in_house = data.get("planets_in_house", [])
            
            # Get lord's house
            lord_house = planet_houses.get(lord, 0)
            
            # Get house meaning
            meaning = HOUSE_MEANINGS.get(house_num, {})
            
            # Generate interpretation
            general = f"House {house_num} ({meaning.get('area', '')}) is in {sign}, ruled by {lord}."
            
            with_planets = ""
            if planets_in_house:
                with_planets = f"Contains {', '.join(planets_in_house)}, emphasizing this area of life."
            else:
                with_planets = "No planets in this house, results depend on the lord."
            
            lord_placement = f"{lord} (lord) is in house {lord_house}."
            if lord_house == house_num:
                lord_placement += " The lord in own house strengthens this area."
            
            interpretations[house_num_str] = {
                "house_number": house_num,
                "sign": sign,
                "lord": lord,
                "lord_house": lord_house,
                "planets": planets_in_house,
                "general": general,
                "life_area": meaning.get("area", ""),
                "with_planets": with_planets,
                "lord_placement": lord_placement,
            }
        
        return interpretations
    
    def _interpret_area(
        self, 
        area: str, 
        chart_data: Dict,
        yoga_data: Optional[Dict],
        depth: str
    ) -> Dict:
        """Interpret a specific life area"""
        planets = chart_data.get("planets", {})
        houses = chart_data.get("houses", {})
        
        # Define key houses for each area
        area_houses = {
            "personality": [1],
            "career": [10, 6, 2],
            "relationships": [7, 5, 11],
            "health": [1, 6, 8],
            "wealth": [2, 11, 5, 9],
            "spirituality": [9, 12, 5],
            "education": [4, 5, 9],
            "family": [4, 2, 5],
        }
        
        key_houses = area_houses.get(area, [1])
        key_indicators = []
        strengths = []
        challenges = []
        opportunities = []
        
        # Analyze key houses
        for house_num in key_houses:
            house_data = houses.get(str(house_num), {})
            lord = house_data.get("lord", "")
            planets_in = house_data.get("planets_in_house", [])
            
            key_indicators.append(f"House {house_num}: {house_data.get('sign', '')} with {lord} as lord")
            
            # Check lord placement
            lord_data = planets.get(lord, {})
            lord_dignity = lord_data.get("dignity", "neutral")
            
            if lord_dignity in ["exalted", "own_sign"]:
                strengths.append(f"{lord} (lord of house {house_num}) is strong")
            elif lord_dignity in ["debilitated"]:
                challenges.append(f"{lord} (lord of house {house_num}) needs attention")
            
            # Check benefics/malefics in house
            for planet in planets_in:
                if planet in ["Jupiter", "Venus", "Mercury"]:
                    strengths.append(f"Benefic {planet} in house {house_num}")
                elif planet in ["Saturn", "Mars", "Rahu", "Ketu"]:
                    if house_num in [3, 6, 10, 11]:  # Upachaya - malefics do well
                        opportunities.append(f"{planet} in upachaya house {house_num} - growth potential")
                    else:
                        challenges.append(f"{planet} in house {house_num} may create challenges")
        
        # Add yoga-related insights
        if yoga_data:
            relevant_yogas = self._find_relevant_yogas(yoga_data, area)
            for yoga in relevant_yogas:
                if "daridra" in yoga.lower():
                    challenges.append(f"Yoga: {yoga}")
                else:
                    strengths.append(f"Yoga: {yoga}")
        
        interpretation = self._generate_area_text(area, strengths, challenges, chart_data)
        
        return {
            "area": area,
            "title": area.replace("_", " ").title(),
            "key_indicators": key_indicators,
            "interpretation": interpretation,
            "strengths": strengths[:5],  # Limit to top 5
            "challenges": challenges[:5],
            "opportunities": opportunities[:3],
            "remedies": self._get_area_remedies(area, challenges) if challenges else None,
        }
    
    def _generate_overall_summary(self, chart_data: Dict, yoga_data: Optional[Dict]) -> Dict:
        """Generate overall chart summary"""
        ascendant = chart_data.get("ascendant", {})
        planets = chart_data.get("planets", {})
        
        lagna_sign = chart_data.get("lagna_sign", "")
        moon_sign = chart_data.get("moon_sign", "")
        sun_sign = chart_data.get("sun_sign", "")
        
        # Element analysis
        elements = {"Fire": 0, "Earth": 0, "Air": 0, "Water": 0}
        element_signs = {
            "Fire": ["Aries", "Leo", "Sagittarius"],
            "Earth": ["Taurus", "Virgo", "Capricorn"],
            "Air": ["Gemini", "Libra", "Aquarius"],
            "Water": ["Cancer", "Scorpio", "Pisces"],
        }
        
        for planet_data in planets.values():
            sign = planet_data.get("sign", "")
            for element, signs in element_signs.items():
                if sign in signs:
                    elements[element] += 1
        
        dominant_element = max(elements, key=elements.get)
        
        # Quality analysis
        qualities = {"Cardinal": 0, "Fixed": 0, "Mutable": 0}
        quality_signs = {
            "Cardinal": ["Aries", "Cancer", "Libra", "Capricorn"],
            "Fixed": ["Taurus", "Leo", "Scorpio", "Aquarius"],
            "Mutable": ["Gemini", "Virgo", "Sagittarius", "Pisces"],
        }
        
        for planet_data in planets.values():
            sign = planet_data.get("sign", "")
            for quality, signs in quality_signs.items():
                if sign in signs:
                    qualities[quality] += 1
        
        dominant_quality = max(qualities, key=qualities.get)
        
        # Key themes
        key_themes = []
        if yoga_data:
            summary = yoga_data.get("summary", {})
            if summary.get("raja_yogas_count", 0) > 0:
                key_themes.append("Leadership and authority potential")
            if summary.get("dhana_yogas_count", 0) > 0:
                key_themes.append("Wealth accumulation capacity")
            if summary.get("mahapurusha_yogas_count", 0) > 0:
                key_themes.append("Special planetary combinations for greatness")
        
        # Major strengths and challenges
        major_strengths = []
        major_challenges = []
        
        for name, data in planets.items():
            dignity = data.get("dignity", "neutral")
            if dignity in ["exalted", "own_sign"]:
                major_strengths.append(f"{name} in {dignity}")
            elif dignity == "debilitated":
                major_challenges.append(f"{name} debilitated")
        
        return {
            "ascendant_analysis": f"Ascendant in {lagna_sign} gives {self._get_sign_nature(lagna_sign)} personality.",
            "moon_sign_analysis": f"Moon in {moon_sign} indicates {self._get_sign_nature(moon_sign)} emotional nature.",
            "sun_sign_analysis": f"Sun in {sun_sign} shows {self._get_sign_nature(sun_sign)} core identity.",
            "dominant_element": dominant_element,
            "dominant_quality": dominant_quality,
            "key_life_themes": key_themes or ["Individual growth", "Self-realization"],
            "major_strengths": major_strengths[:5],
            "major_challenges": major_challenges[:5],
            "life_purpose": self._get_life_purpose(lagna_sign, planets),
            "karmic_lessons": self._get_karmic_lessons(planets),
        }
    
    def _interpret_yogas(self, yoga_data: Dict) -> List[Dict]:
        """Interpret yoga effects"""
        effects = []
        
        all_yogas = yoga_data.get("all_yogas", [])
        for yoga in all_yogas[:10]:  # Limit to top 10 yogas
            effects.append({
                "yoga_name": yoga.get("name", ""),
                "category": yoga.get("category", ""),
                "strength": yoga.get("strength", ""),
                "effects": yoga.get("effects", ""),
                "formed_by": ", ".join(yoga.get("forming_planets", [])),
            })
        
        return effects
    
    def _interpret_dasha(self, dasha_data: Dict) -> Dict:
        """Interpret current Dasha period"""
        current = dasha_data.get("current_dasha", {})
        if not current:
            return None
        
        mahadasha = current.get("mahadasha", {})
        antardasha = current.get("antardasha", {})
        
        md_planet = mahadasha.get("planet", "")
        ad_planet = antardasha.get("planet", "")
        
        return {
            "current_period": current.get("summary", ""),
            "mahadasha_planet": md_planet,
            "mahadasha_effects": f"{md_planet} Mahadasha brings focus on {md_planet}'s significations.",
            "antardasha_planet": ad_planet,
            "antardasha_effects": f"{ad_planet} Antardasha modifies with its own influences.",
            "advice": f"During {md_planet}-{ad_planet} period, balance both planetary energies.",
        }
    
    def _generate_remedies(self, chart_data: Dict, yoga_data: Optional[Dict]) -> List[Dict]:
        """Generate remedial measures"""
        remedies = []
        planets = chart_data.get("planets", {})
        
        # Remedies for weak planets
        planet_remedies = {
            "Sun": {"gemstone": "Ruby", "mantra": "Om Suryaya Namah", "charity": "Wheat, copper, red items"},
            "Moon": {"gemstone": "Pearl", "mantra": "Om Chandraya Namah", "charity": "Rice, white items, milk"},
            "Mars": {"gemstone": "Red Coral", "mantra": "Om Mangalaya Namah", "charity": "Red lentils, copper"},
            "Mercury": {"gemstone": "Emerald", "mantra": "Om Budhaya Namah", "charity": "Green items, education"},
            "Jupiter": {"gemstone": "Yellow Sapphire", "mantra": "Om Gurave Namah", "charity": "Yellow items, education"},
            "Venus": {"gemstone": "Diamond", "mantra": "Om Shukraya Namah", "charity": "White items, sweets"},
            "Saturn": {"gemstone": "Blue Sapphire", "mantra": "Om Shanicharaya Namah", "charity": "Black items, sesame"},
            "Rahu": {"gemstone": "Hessonite", "mantra": "Om Rahave Namah", "charity": "Black items, coal"},
            "Ketu": {"gemstone": "Cat's Eye", "mantra": "Om Ketave Namah", "charity": "Multi-colored items"},
        }
        
        for name, data in planets.items():
            dignity = data.get("dignity", "neutral")
            if dignity in ["debilitated", "enemy"]:
                remedy_info = planet_remedies.get(name, {})
                remedies.append({
                    "for_planet": name,
                    "reason": f"{name} is {dignity}",
                    "gemstone": remedy_info.get("gemstone", ""),
                    "mantra": remedy_info.get("mantra", ""),
                    "charity": remedy_info.get("charity", ""),
                })
        
        return remedies[:5]  # Limit to 5 remedies
    
    def _find_relevant_yogas(self, yoga_data: Dict, area: str) -> List[str]:
        """Find yogas relevant to a life area"""
        relevant = []
        area_yogas = {
            "career": ["raja_yoga", "pancha_mahapurusha"],
            "wealth": ["dhana_yoga"],
            "relationships": ["chandra_yoga"],
            "health": ["nabhash_yoga"],
        }
        
        relevant_categories = area_yogas.get(area, [])
        
        for yoga in yoga_data.get("all_yogas", []):
            if yoga.get("category") in relevant_categories:
                relevant.append(yoga.get("name", ""))
        
        return relevant
    
    def _generate_area_text(self, area: str, strengths: List, challenges: List, chart_data: Dict) -> str:
        """Generate text interpretation for an area"""
        if strengths and not challenges:
            return f"The {area} area shows strong potential with favorable planetary placements."
        elif challenges and not strengths:
            return f"The {area} area may face some challenges that require attention and effort."
        else:
            return f"The {area} area shows mixed indications with both opportunities and challenges."
    
    def _get_area_remedies(self, area: str, challenges: List) -> List[str]:
        """Get remedies for an area"""
        area_remedies = {
            "career": ["Strengthen the 10th lord", "Worship Lord Vishnu on Thursdays"],
            "wealth": ["Strengthen the 2nd and 11th lords", "Donate to charity regularly"],
            "relationships": ["Strengthen Venus and 7th lord", "Worship Lord Shiva-Parvati"],
            "health": ["Strengthen the Ascendant lord", "Practice yoga and meditation"],
        }
        return area_remedies.get(area, ["General spiritual practices recommended"])
    
    def _get_sign_nature(self, sign: str) -> str:
        """Get brief nature of a sign"""
        natures = {
            "Aries": "pioneering and energetic",
            "Taurus": "stable and sensual",
            "Gemini": "curious and communicative",
            "Cancer": "nurturing and emotional",
            "Leo": "confident and creative",
            "Virgo": "analytical and service-oriented",
            "Libra": "balanced and diplomatic",
            "Scorpio": "intense and transformative",
            "Sagittarius": "philosophical and adventurous",
            "Capricorn": "ambitious and disciplined",
            "Aquarius": "innovative and humanitarian",
            "Pisces": "intuitive and compassionate",
        }
        return natures.get(sign, "balanced")
    
    def _get_life_purpose(self, lagna_sign: str, planets: Dict) -> str:
        """Determine life purpose based on chart"""
        purposes = {
            "Aries": "To lead and pioneer new paths",
            "Taurus": "To build lasting value and beauty",
            "Gemini": "To communicate and connect ideas",
            "Cancer": "To nurture and protect",
            "Leo": "To create and inspire others",
            "Virgo": "To serve and improve",
            "Libra": "To create harmony and justice",
            "Scorpio": "To transform and regenerate",
            "Sagittarius": "To teach and expand horizons",
            "Capricorn": "To achieve and structure",
            "Aquarius": "To innovate and reform",
            "Pisces": "To transcend and heal",
        }
        return purposes.get(lagna_sign, "To grow and evolve through life experiences")
    
    def _get_karmic_lessons(self, planets: Dict) -> List[str]:
        """Determine karmic lessons from chart"""
        lessons = []
        
        # Check Rahu/Ketu axis
        rahu_house = planets.get("Rahu", {}).get("house", 0)
        ketu_house = planets.get("Ketu", {}).get("house", 0)
        
        axis_lessons = {
            (1, 7): "Balance between self and relationships",
            (2, 8): "Transform approach to resources and shared assets",
            (3, 9): "Balance practical skills with higher wisdom",
            (4, 10): "Balance home life with career ambitions",
            (5, 11): "Balance personal creativity with collective goals",
            (6, 12): "Balance service with spiritual growth",
        }
        
        for axis, lesson in axis_lessons.items():
            if rahu_house in axis or ketu_house in axis:
                lessons.append(lesson)
        
        # Check Saturn placement
        saturn_house = planets.get("Saturn", {}).get("house", 0)
        if saturn_house:
            lessons.append(f"Develop discipline and patience in house {saturn_house} matters")
        
        return lessons[:3]
