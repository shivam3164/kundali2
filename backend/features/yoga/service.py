"""
Yoga Feature - Service Layer
Yoga detection and analysis following BPHS
"""

from typing import Dict, List, Optional, Any, Set
from dataclasses import dataclass, field


# ============================================
# YOGA DEFINITIONS FROM BPHS
# ============================================

# Kendra houses (quadrants)
KENDRAS = [1, 4, 7, 10]

# Trikona houses (trines)
TRIKONAS = [1, 5, 9]

# Dusthana houses (malefic houses)
DUSTHANAS = [6, 8, 12]

# Upachaya houses (growth houses)
UPACHAYAS = [3, 6, 10, 11]

# Natural benefics
NATURAL_BENEFICS = ["Jupiter", "Venus", "Mercury", "Moon"]

# Natural malefics
NATURAL_MALEFICS = ["Sun", "Mars", "Saturn", "Rahu", "Ketu"]


# ============================================
# YOGA SERVICE
# ============================================

class YogaService:
    """
    Yoga detection service following BPHS
    
    Detects various yogas:
    - Raja Yogas (power/authority)
    - Dhana Yogas (wealth)
    - Pancha Mahapurusha Yogas (5 great person yogas)
    - Nabhash Yogas (celestial pattern yogas)
    - Chandra Yogas (Moon-based yogas)
    - Surya Yogas (Sun-based yogas)
    - Daridra Yogas (poverty yogas)
    - Viparita Raja Yogas (reverse raja yogas)
    """
    
    def __init__(self, knowledge=None):
        self.knowledge = knowledge
    
    def detect_all_yogas(self, chart_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Detect all yogas in a chart
        
        Args:
            chart_data: Chart data from ChartService
        
        Returns:
            Complete yoga analysis
        """
        yogas = {
            "raja_yoga": [],
            "dhana_yoga": [],
            "pancha_mahapurusha": [],
            "nabhash_yoga": [],
            "chandra_yoga": [],
            "surya_yoga": [],
            "daridra_yoga": [],
            "viparita_raja_yoga": [],
            "other": [],
        }
        
        # Extract chart info
        planets = chart_data.get("planets", {})
        houses = chart_data.get("houses", {})
        ascendant = chart_data.get("ascendant", {})
        lagna_sign = chart_data.get("lagna_sign", "")
        
        # Build helper structures
        planet_houses = {name: data.get("house", 0) for name, data in planets.items()}
        planet_signs = {name: data.get("sign", "") for name, data in planets.items()}
        house_planets = self._get_house_planets(planets)
        house_lords = {int(k): v.get("lord", "") for k, v in houses.items()}
        
        # Detect each type of yoga
        yogas["raja_yoga"] = self._detect_raja_yogas(
            planet_houses, house_lords, house_planets, lagna_sign
        )
        
        yogas["dhana_yoga"] = self._detect_dhana_yogas(
            planet_houses, house_lords, house_planets
        )
        
        yogas["pancha_mahapurusha"] = self._detect_mahapurusha_yogas(
            planet_houses, planet_signs, planets
        )
        
        yogas["nabhash_yoga"] = self._detect_nabhash_yogas(
            planet_houses, house_planets
        )
        
        yogas["chandra_yoga"] = self._detect_chandra_yogas(
            planets, planet_houses
        )
        
        yogas["surya_yoga"] = self._detect_surya_yogas(
            planets, planet_houses
        )
        
        yogas["daridra_yoga"] = self._detect_daridra_yogas(
            planet_houses, house_lords, house_planets
        )
        
        yogas["viparita_raja_yoga"] = self._detect_viparita_raja_yogas(
            planet_houses, house_lords
        )
        
        # Compile all yogas
        all_yogas = []
        for category, yoga_list in yogas.items():
            all_yogas.extend(yoga_list)
        
        # Generate summary
        summary = self._generate_summary(yogas, all_yogas)
        
        return {
            "birth_data": chart_data.get("birth_data", {}),
            "yogas": yogas,
            "all_yogas": all_yogas,
            "summary": summary,
        }
    
    def _get_house_planets(self, planets: Dict) -> Dict[int, List[str]]:
        """Get planets in each house"""
        house_planets = {i: [] for i in range(1, 13)}
        for name, data in planets.items():
            house = data.get("house", 0)
            if house in house_planets:
                house_planets[house].append(name)
        return house_planets
    
    def _detect_raja_yogas(
        self,
        planet_houses: Dict[str, int],
        house_lords: Dict[int, str],
        house_planets: Dict[int, List[str]],
        lagna_sign: str
    ) -> List[Dict]:
        """
        Detect Raja Yogas (BPHS Ch. 41)
        
        Raja Yoga occurs when:
        1. Lords of Kendra and Trikona are in conjunction or mutual aspect
        2. Lord of 9th and 10th are in conjunction
        3. Lord of 1st, 4th, 5th, 9th, 10th in Kendra/Trikona
        """
        yogas = []
        
        # Get lords of key houses
        lords_1 = house_lords.get(1, "")
        lords_4 = house_lords.get(4, "")
        lords_5 = house_lords.get(5, "")
        lords_7 = house_lords.get(7, "")
        lords_9 = house_lords.get(9, "")
        lords_10 = house_lords.get(10, "")
        
        # Yoga 1: 9th and 10th lords conjunction
        if lords_9 and lords_10:
            house_9th_lord = planet_houses.get(lords_9, 0)
            house_10th_lord = planet_houses.get(lords_10, 0)
            
            if house_9th_lord == house_10th_lord and house_9th_lord > 0:
                yogas.append({
                    "name": "Dharma-Karmadhipati Raja Yoga",
                    "category": "raja_yoga",
                    "is_present": True,
                    "strength": "full",
                    "forming_planets": [lords_9, lords_10],
                    "forming_houses": [9, 10, house_9th_lord],
                    "description": "Lords of 9th (dharma) and 10th (karma) houses are conjunct",
                    "effects": "High position in life, authority, fame, success in career and dharmic pursuits",
                    "bphs_reference": "BPHS Ch. 41",
                    "conditions_met": ["9th and 10th lords conjunct"],
                    "conditions_partial": [],
                })
        
        # Yoga 2: 1st and 5th lords conjunction
        if lords_1 and lords_5:
            house_1st_lord = planet_houses.get(lords_1, 0)
            house_5th_lord = planet_houses.get(lords_5, 0)
            
            if house_1st_lord == house_5th_lord and house_1st_lord > 0:
                yogas.append({
                    "name": "Lagna-Panchamesh Raja Yoga",
                    "category": "raja_yoga",
                    "is_present": True,
                    "strength": "full",
                    "forming_planets": [lords_1, lords_5],
                    "forming_houses": [1, 5, house_1st_lord],
                    "description": "Lords of 1st and 5th houses are conjunct",
                    "effects": "Intelligence, fame, children, creativity, and overall prosperity",
                    "bphs_reference": "BPHS Ch. 41",
                    "conditions_met": ["1st and 5th lords conjunct"],
                    "conditions_partial": [],
                })
        
        # Yoga 3: 4th and 5th lords conjunction
        if lords_4 and lords_5:
            house_4th_lord = planet_houses.get(lords_4, 0)
            house_5th_lord = planet_houses.get(lords_5, 0)
            
            if house_4th_lord == house_5th_lord and house_4th_lord > 0:
                yogas.append({
                    "name": "Kendra-Trikona Raja Yoga",
                    "category": "raja_yoga",
                    "is_present": True,
                    "strength": "full",
                    "forming_planets": [lords_4, lords_5],
                    "forming_houses": [4, 5, house_4th_lord],
                    "description": "Lords of Kendra (4th) and Trikona (5th) are conjunct",
                    "effects": "Prosperity, happiness, good education, property, and spiritual inclination",
                    "bphs_reference": "BPHS Ch. 41",
                    "conditions_met": ["4th and 5th lords conjunct"],
                    "conditions_partial": [],
                })
        
        # Yoga 4: 9th and 4th lords conjunction  
        if lords_9 and lords_4:
            house_9th_lord = planet_houses.get(lords_9, 0)
            house_4th_lord = planet_houses.get(lords_4, 0)
            
            if house_9th_lord == house_4th_lord and house_9th_lord > 0:
                yogas.append({
                    "name": "Bhagya-Sukha Raja Yoga",
                    "category": "raja_yoga",
                    "is_present": True,
                    "strength": "full",
                    "forming_planets": [lords_9, lords_4],
                    "forming_houses": [9, 4, house_9th_lord],
                    "description": "Lords of 9th (fortune) and 4th (happiness) are conjunct",
                    "effects": "Fortune, happiness, comfort, vehicles, property, spiritual blessings",
                    "bphs_reference": "BPHS Ch. 41",
                    "conditions_met": ["9th and 4th lords conjunct"],
                    "conditions_partial": [],
                })
        
        # Yoga 5: Benefics in Kendras (Partial Raja Yoga)
        kendras_with_benefics = []
        for kendra in KENDRAS:
            planets_in_kendra = house_planets.get(kendra, [])
            benefics = [p for p in planets_in_kendra if p in NATURAL_BENEFICS]
            if benefics:
                kendras_with_benefics.extend(benefics)
        
        if len(kendras_with_benefics) >= 2:
            yogas.append({
                "name": "Kendradhipati Yoga",
                "category": "raja_yoga",
                "is_present": True,
                "strength": "partial",
                "forming_planets": kendras_with_benefics,
                "forming_houses": KENDRAS,
                "description": "Multiple benefics placed in Kendra houses",
                "effects": "Good fortune, support from authority, overall prosperity",
                "bphs_reference": "BPHS Ch. 41",
                "conditions_met": [f"{len(kendras_with_benefics)} benefics in Kendras"],
                "conditions_partial": [],
            })
        
        return yogas
    
    def _detect_dhana_yogas(
        self,
        planet_houses: Dict[str, int],
        house_lords: Dict[int, str],
        house_planets: Dict[int, List[str]]
    ) -> List[Dict]:
        """
        Detect Dhana Yogas (Wealth Yogas) - BPHS Ch. 42
        
        Dhana Yoga occurs when:
        1. Lords of 2nd, 5th, 9th, 11th houses are strong
        2. Lords of wealth houses are in mutual connection
        3. Jupiter/Venus in 2nd, 5th, 9th, or 11th
        """
        yogas = []
        
        # Wealth houses
        wealth_houses = [2, 5, 9, 11]
        
        lords_2 = house_lords.get(2, "")
        lords_5 = house_lords.get(5, "")
        lords_9 = house_lords.get(9, "")
        lords_11 = house_lords.get(11, "")
        
        # Yoga 1: 2nd and 11th lords conjunction
        if lords_2 and lords_11:
            house_2nd_lord = planet_houses.get(lords_2, 0)
            house_11th_lord = planet_houses.get(lords_11, 0)
            
            if house_2nd_lord == house_11th_lord and house_2nd_lord > 0:
                yogas.append({
                    "name": "Dhana Yoga (2nd-11th)",
                    "category": "dhana_yoga",
                    "is_present": True,
                    "strength": "full",
                    "forming_planets": [lords_2, lords_11],
                    "forming_houses": [2, 11, house_2nd_lord],
                    "description": "Lords of 2nd (wealth) and 11th (gains) houses are conjunct",
                    "effects": "Accumulation of wealth, financial prosperity, gains from various sources",
                    "bphs_reference": "BPHS Ch. 42",
                    "conditions_met": ["2nd and 11th lords conjunct"],
                    "conditions_partial": [],
                })
        
        # Yoga 2: 5th and 9th lords conjunction (Lakshmi Yoga component)
        if lords_5 and lords_9:
            house_5th_lord = planet_houses.get(lords_5, 0)
            house_9th_lord = planet_houses.get(lords_9, 0)
            
            if house_5th_lord == house_9th_lord and house_5th_lord > 0:
                yogas.append({
                    "name": "Lakshmi Yoga",
                    "category": "dhana_yoga",
                    "is_present": True,
                    "strength": "full",
                    "forming_planets": [lords_5, lords_9],
                    "forming_houses": [5, 9, house_5th_lord],
                    "description": "Lords of 5th and 9th houses (both Trikonas) are conjunct",
                    "effects": "Blessed by Lakshmi, wealth through fortune and past-life merits",
                    "bphs_reference": "BPHS Ch. 42",
                    "conditions_met": ["5th and 9th lords conjunct"],
                    "conditions_partial": [],
                })
        
        # Yoga 3: Jupiter or Venus in wealth houses
        for planet in ["Jupiter", "Venus"]:
            house = planet_houses.get(planet, 0)
            if house in wealth_houses:
                yogas.append({
                    "name": f"{planet} Dhana Yoga",
                    "category": "dhana_yoga",
                    "is_present": True,
                    "strength": "partial",
                    "forming_planets": [planet],
                    "forming_houses": [house],
                    "description": f"{planet} placed in wealth house {house}",
                    "effects": f"Financial blessings through {planet}'s significations",
                    "bphs_reference": "BPHS Ch. 42",
                    "conditions_met": [f"{planet} in house {house}"],
                    "conditions_partial": [],
                })
        
        return yogas
    
    def _detect_mahapurusha_yogas(
        self,
        planet_houses: Dict[str, int],
        planet_signs: Dict[str, str],
        planets: Dict[str, Any]
    ) -> List[Dict]:
        """
        Detect Pancha Mahapurusha Yogas - BPHS Ch. 75
        
        These occur when Mars, Mercury, Jupiter, Venus, or Saturn is:
        1. In its own sign or exaltation
        2. In a Kendra from Lagna
        """
        yogas = []
        
        mahapurusha_planets = {
            "Mars": {
                "yoga_name": "Ruchaka Yoga",
                "own_signs": ["Aries", "Scorpio"],
                "exaltation": "Capricorn",
                "effects": "Valor, military success, leadership, courage, competitive nature"
            },
            "Mercury": {
                "yoga_name": "Bhadra Yoga", 
                "own_signs": ["Gemini", "Virgo"],
                "exaltation": "Virgo",
                "effects": "Intelligence, eloquence, learning, communication skills, business acumen"
            },
            "Jupiter": {
                "yoga_name": "Hamsa Yoga",
                "own_signs": ["Sagittarius", "Pisces"],
                "exaltation": "Cancer",
                "effects": "Wisdom, spirituality, good fortune, respect, teaching ability"
            },
            "Venus": {
                "yoga_name": "Malavya Yoga",
                "own_signs": ["Taurus", "Libra"],
                "exaltation": "Pisces",
                "effects": "Beauty, luxury, artistic talents, romantic happiness, comfort"
            },
            "Saturn": {
                "yoga_name": "Shasha Yoga",
                "own_signs": ["Capricorn", "Aquarius"],
                "exaltation": "Libra",
                "effects": "Authority, discipline, perseverance, success through hard work"
            }
        }
        
        for planet, config in mahapurusha_planets.items():
            house = planet_houses.get(planet, 0)
            sign = planet_signs.get(planet, "")
            
            # Check if in Kendra
            if house not in KENDRAS:
                continue
            
            # Check if in own sign or exaltation
            in_own = sign in config["own_signs"]
            in_exalt = sign == config["exaltation"]
            
            if in_own or in_exalt:
                dignity = "exalted" if in_exalt else "own sign"
                yogas.append({
                    "name": config["yoga_name"],
                    "category": "pancha_mahapurusha",
                    "is_present": True,
                    "strength": "full",
                    "forming_planets": [planet],
                    "forming_houses": [house],
                    "description": f"{planet} in {dignity} ({sign}) in Kendra house {house}",
                    "effects": config["effects"],
                    "bphs_reference": "BPHS Ch. 75",
                    "conditions_met": [f"{planet} in {dignity}", f"{planet} in Kendra {house}"],
                    "conditions_partial": [],
                })
        
        return yogas
    
    def _detect_nabhash_yogas(
        self,
        planet_houses: Dict[str, int],
        house_planets: Dict[int, List[str]]
    ) -> List[Dict]:
        """
        Detect Nabhash Yogas (Pattern Yogas) - BPHS Ch. 13
        
        These are based on how planets are distributed across houses.
        """
        yogas = []
        
        # Count occupied houses
        occupied_houses = [h for h, planets in house_planets.items() if planets]
        num_occupied = len(occupied_houses)
        
        # Gola Yoga: All planets in one sign
        if num_occupied == 1:
            yogas.append({
                "name": "Gola Yoga",
                "category": "nabhash_yoga",
                "is_present": True,
                "strength": "full",
                "forming_planets": list(planet_houses.keys()),
                "forming_houses": occupied_houses,
                "description": "All planets concentrated in one house",
                "effects": "Extreme focus but limited scope, poverty or wealth depending on the house",
                "bphs_reference": "BPHS Ch. 13",
                "conditions_met": ["All planets in one house"],
                "conditions_partial": [],
            })
        
        # Yuga Yoga: All planets in 2 signs
        elif num_occupied == 2:
            yogas.append({
                "name": "Yuga Yoga",
                "category": "nabhash_yoga",
                "is_present": True,
                "strength": "full",
                "forming_planets": list(planet_houses.keys()),
                "forming_houses": occupied_houses,
                "description": "All planets in two houses",
                "effects": "Moderate scope, partnerships important",
                "bphs_reference": "BPHS Ch. 13",
                "conditions_met": ["All planets in two houses"],
                "conditions_partial": [],
            })
        
        # Sula Yoga: All planets in 3 signs
        elif num_occupied == 3:
            yogas.append({
                "name": "Sula Yoga",
                "category": "nabhash_yoga",
                "is_present": True,
                "strength": "partial",
                "forming_planets": list(planet_houses.keys()),
                "forming_houses": occupied_houses,
                "description": "All planets in three houses",
                "effects": "Focused energy in specific life areas",
                "bphs_reference": "BPHS Ch. 13",
                "conditions_met": ["All planets in three houses"],
                "conditions_partial": [],
            })
        
        # Kedara Yoga: All planets in 4 signs
        elif num_occupied == 4:
            yogas.append({
                "name": "Kedara Yoga",
                "category": "nabhash_yoga",
                "is_present": True,
                "strength": "partial",
                "forming_planets": list(planet_houses.keys()),
                "forming_houses": occupied_houses,
                "description": "All planets in four houses",
                "effects": "Agricultural success, land ownership, steady income",
                "bphs_reference": "BPHS Ch. 13",
                "conditions_met": ["All planets in four houses"],
                "conditions_partial": [],
            })
        
        # Gada Yoga: All planets in 2 consecutive Kendras
        kendra_pairs = [(1, 4), (4, 7), (7, 10), (10, 1)]
        for pair in kendra_pairs:
            if all(h in occupied_houses for h in pair) and num_occupied == 2:
                yogas.append({
                    "name": "Gada Yoga",
                    "category": "nabhash_yoga",
                    "is_present": True,
                    "strength": "full",
                    "forming_planets": list(planet_houses.keys()),
                    "forming_houses": list(pair),
                    "description": f"All planets in consecutive Kendras {pair}",
                    "effects": "Wealth through sustained effort, eventual comfort",
                    "bphs_reference": "BPHS Ch. 13",
                    "conditions_met": ["Planets in consecutive Kendras"],
                    "conditions_partial": [],
                })
                break
        
        return yogas
    
    def _detect_chandra_yogas(
        self,
        planets: Dict[str, Any],
        planet_houses: Dict[str, int]
    ) -> List[Dict]:
        """
        Detect Chandra (Moon) Yogas - BPHS Ch. 36-37
        """
        yogas = []
        
        moon_house = planet_houses.get("Moon", 0)
        if not moon_house:
            return yogas
        
        # Sunafa Yoga: Planet (not Sun) in 2nd from Moon
        second_from_moon = (moon_house % 12) + 1
        planets_in_second = [p for p, h in planet_houses.items() 
                           if h == second_from_moon and p not in ["Sun", "Moon", "Rahu", "Ketu"]]
        
        if planets_in_second:
            yogas.append({
                "name": "Sunafa Yoga",
                "category": "chandra_yoga",
                "is_present": True,
                "strength": "full",
                "forming_planets": planets_in_second + ["Moon"],
                "forming_houses": [moon_house, second_from_moon],
                "description": f"{', '.join(planets_in_second)} in 2nd from Moon",
                "effects": "Self-made wealth, intelligence, good reputation",
                "bphs_reference": "BPHS Ch. 36",
                "conditions_met": [f"Planet(s) in 2nd from Moon"],
                "conditions_partial": [],
            })
        
        # Anafa Yoga: Planet (not Sun) in 12th from Moon
        twelfth_from_moon = ((moon_house - 2) % 12) + 1
        planets_in_twelfth = [p for p, h in planet_houses.items() 
                            if h == twelfth_from_moon and p not in ["Sun", "Moon", "Rahu", "Ketu"]]
        
        if planets_in_twelfth:
            yogas.append({
                "name": "Anafa Yoga",
                "category": "chandra_yoga",
                "is_present": True,
                "strength": "full",
                "forming_planets": planets_in_twelfth + ["Moon"],
                "forming_houses": [moon_house, twelfth_from_moon],
                "description": f"{', '.join(planets_in_twelfth)} in 12th from Moon",
                "effects": "Healthy constitution, virtuous, well-dressed, happy",
                "bphs_reference": "BPHS Ch. 36",
                "conditions_met": [f"Planet(s) in 12th from Moon"],
                "conditions_partial": [],
            })
        
        # Durudhara Yoga: Planets on both sides of Moon
        if planets_in_second and planets_in_twelfth:
            yogas.append({
                "name": "Durudhara Yoga",
                "category": "chandra_yoga",
                "is_present": True,
                "strength": "full",
                "forming_planets": planets_in_second + planets_in_twelfth + ["Moon"],
                "forming_houses": [twelfth_from_moon, moon_house, second_from_moon],
                "description": "Planets on both sides of Moon (Sunafa + Anafa)",
                "effects": "Wealth, vehicles, generosity, enjoys life's comforts",
                "bphs_reference": "BPHS Ch. 36",
                "conditions_met": ["Planets on both sides of Moon"],
                "conditions_partial": [],
            })
        
        # Kemadruma Yoga: No planets on either side of Moon
        if not planets_in_second and not planets_in_twelfth:
            # Check if any planet is in Kendra from Moon (cancels Kemadruma)
            kendras_from_moon = [
                (moon_house % 12) + 1,  # 2nd is not kendra
                ((moon_house + 2) % 12) + 1,  # 4th from Moon
                ((moon_house + 5) % 12) + 1,  # 7th from Moon
                ((moon_house + 8) % 12) + 1,  # 10th from Moon
            ]
            
            planets_in_kendra_from_moon = [
                p for p, h in planet_houses.items() 
                if h in kendras_from_moon[1:] and p not in ["Moon", "Rahu", "Ketu"]
            ]
            
            if not planets_in_kendra_from_moon:
                yogas.append({
                    "name": "Kemadruma Yoga",
                    "category": "chandra_yoga",
                    "is_present": True,
                    "strength": "full",
                    "forming_planets": ["Moon"],
                    "forming_houses": [moon_house],
                    "description": "No planets adjacent to Moon and none in Kendra from Moon",
                    "effects": "Poverty, struggles, lack of support (can be cancelled by other factors)",
                    "bphs_reference": "BPHS Ch. 36",
                    "conditions_met": ["No planets around Moon"],
                    "conditions_partial": [],
                })
        
        # Gajakesari Yoga: Jupiter in Kendra from Moon
        jupiter_house = planet_houses.get("Jupiter", 0)
        if jupiter_house:
            # Calculate house distance from Moon
            distance = (jupiter_house - moon_house) % 12
            if distance in [0, 3, 6, 9]:  # 1st, 4th, 7th, 10th from Moon
                yogas.append({
                    "name": "Gajakesari Yoga",
                    "category": "chandra_yoga",
                    "is_present": True,
                    "strength": "full",
                    "forming_planets": ["Moon", "Jupiter"],
                    "forming_houses": [moon_house, jupiter_house],
                    "description": "Jupiter in Kendra from Moon",
                    "effects": "Fame, leadership, intelligence, lasting reputation, spiritual wisdom",
                    "bphs_reference": "BPHS Ch. 36",
                    "conditions_met": ["Jupiter in Kendra from Moon"],
                    "conditions_partial": [],
                })
        
        return yogas
    
    def _detect_surya_yogas(
        self,
        planets: Dict[str, Any],
        planet_houses: Dict[str, int]
    ) -> List[Dict]:
        """
        Detect Surya (Sun) Yogas - BPHS Ch. 37
        """
        yogas = []
        
        sun_house = planet_houses.get("Sun", 0)
        if not sun_house:
            return yogas
        
        # Vesi Yoga: Planet (not Moon) in 2nd from Sun
        second_from_sun = (sun_house % 12) + 1
        planets_in_second = [p for p, h in planet_houses.items() 
                           if h == second_from_sun and p not in ["Sun", "Moon", "Rahu", "Ketu"]]
        
        if planets_in_second:
            yogas.append({
                "name": "Vesi Yoga",
                "category": "surya_yoga",
                "is_present": True,
                "strength": "full",
                "forming_planets": planets_in_second + ["Sun"],
                "forming_houses": [sun_house, second_from_sun],
                "description": f"{', '.join(planets_in_second)} in 2nd from Sun",
                "effects": "Truthful, slow in nature, balanced, even-tempered",
                "bphs_reference": "BPHS Ch. 37",
                "conditions_met": [f"Planet(s) in 2nd from Sun"],
                "conditions_partial": [],
            })
        
        # Vosi Yoga: Planet (not Moon) in 12th from Sun
        twelfth_from_sun = ((sun_house - 2) % 12) + 1
        planets_in_twelfth = [p for p, h in planet_houses.items() 
                            if h == twelfth_from_sun and p not in ["Sun", "Moon", "Rahu", "Ketu"]]
        
        if planets_in_twelfth:
            yogas.append({
                "name": "Vosi Yoga",
                "category": "surya_yoga",
                "is_present": True,
                "strength": "full",
                "forming_planets": planets_in_twelfth + ["Sun"],
                "forming_houses": [sun_house, twelfth_from_sun],
                "description": f"{', '.join(planets_in_twelfth)} in 12th from Sun",
                "effects": "Skilled, charitable, learned, good memory",
                "bphs_reference": "BPHS Ch. 37",
                "conditions_met": [f"Planet(s) in 12th from Sun"],
                "conditions_partial": [],
            })
        
        # Ubhayachari Yoga: Planets on both sides of Sun
        if planets_in_second and planets_in_twelfth:
            yogas.append({
                "name": "Ubhayachari Yoga",
                "category": "surya_yoga",
                "is_present": True,
                "strength": "full",
                "forming_planets": planets_in_second + planets_in_twelfth + ["Sun"],
                "forming_houses": [twelfth_from_sun, sun_house, second_from_sun],
                "description": "Planets on both sides of Sun",
                "effects": "Equal to a king, eloquent speaker, prosperous, handsome",
                "bphs_reference": "BPHS Ch. 37",
                "conditions_met": ["Planets on both sides of Sun"],
                "conditions_partial": [],
            })
        
        return yogas
    
    def _detect_daridra_yogas(
        self,
        planet_houses: Dict[str, int],
        house_lords: Dict[int, str],
        house_planets: Dict[int, List[str]]
    ) -> List[Dict]:
        """
        Detect Daridra (Poverty) Yogas - BPHS Ch. 43
        """
        yogas = []
        
        # 11th lord in 6th, 8th, or 12th (Dusthana)
        lord_11 = house_lords.get(11, "")
        if lord_11:
            house_of_11th_lord = planet_houses.get(lord_11, 0)
            if house_of_11th_lord in DUSTHANAS:
                yogas.append({
                    "name": "Daridra Yoga (11th Lord)",
                    "category": "daridra_yoga",
                    "is_present": True,
                    "strength": "partial",
                    "forming_planets": [lord_11],
                    "forming_houses": [11, house_of_11th_lord],
                    "description": f"11th lord ({lord_11}) in Dusthana house {house_of_11th_lord}",
                    "effects": "Difficulty in gains, obstacles to income",
                    "bphs_reference": "BPHS Ch. 43",
                    "conditions_met": ["11th lord in Dusthana"],
                    "conditions_partial": [],
                })
        
        # 2nd lord in 6th, 8th, or 12th
        lord_2 = house_lords.get(2, "")
        if lord_2:
            house_of_2nd_lord = planet_houses.get(lord_2, 0)
            if house_of_2nd_lord in DUSTHANAS:
                yogas.append({
                    "name": "Daridra Yoga (2nd Lord)",
                    "category": "daridra_yoga",
                    "is_present": True,
                    "strength": "partial",
                    "forming_planets": [lord_2],
                    "forming_houses": [2, house_of_2nd_lord],
                    "description": f"2nd lord ({lord_2}) in Dusthana house {house_of_2nd_lord}",
                    "effects": "Difficulty in accumulating wealth, family challenges",
                    "bphs_reference": "BPHS Ch. 43",
                    "conditions_met": ["2nd lord in Dusthana"],
                    "conditions_partial": [],
                })
        
        return yogas
    
    def _detect_viparita_raja_yogas(
        self,
        planet_houses: Dict[str, int],
        house_lords: Dict[int, str]
    ) -> List[Dict]:
        """
        Detect Viparita Raja Yogas - BPHS Ch. 41
        
        These occur when lords of Dusthanas (6, 8, 12) are placed in other Dusthanas.
        """
        yogas = []
        
        lord_6 = house_lords.get(6, "")
        lord_8 = house_lords.get(8, "")
        lord_12 = house_lords.get(12, "")
        
        # Harsha Yoga: 6th lord in 8th or 12th
        if lord_6:
            house_of_6th_lord = planet_houses.get(lord_6, 0)
            if house_of_6th_lord in [8, 12]:
                yogas.append({
                    "name": "Harsha Yoga",
                    "category": "viparita_raja_yoga",
                    "is_present": True,
                    "strength": "full",
                    "forming_planets": [lord_6],
                    "forming_houses": [6, house_of_6th_lord],
                    "description": f"6th lord ({lord_6}) in house {house_of_6th_lord}",
                    "effects": "Victory over enemies, happiness through overcoming obstacles",
                    "bphs_reference": "BPHS Ch. 41",
                    "conditions_met": ["6th lord in 8th or 12th"],
                    "conditions_partial": [],
                })
        
        # Sarala Yoga: 8th lord in 6th or 12th
        if lord_8:
            house_of_8th_lord = planet_houses.get(lord_8, 0)
            if house_of_8th_lord in [6, 12]:
                yogas.append({
                    "name": "Sarala Yoga",
                    "category": "viparita_raja_yoga",
                    "is_present": True,
                    "strength": "full",
                    "forming_planets": [lord_8],
                    "forming_houses": [8, house_of_8th_lord],
                    "description": f"8th lord ({lord_8}) in house {house_of_8th_lord}",
                    "effects": "Longevity, overcoming hidden enemies, success in research/occult",
                    "bphs_reference": "BPHS Ch. 41",
                    "conditions_met": ["8th lord in 6th or 12th"],
                    "conditions_partial": [],
                })
        
        # Vimala Yoga: 12th lord in 6th or 8th
        if lord_12:
            house_of_12th_lord = planet_houses.get(lord_12, 0)
            if house_of_12th_lord in [6, 8]:
                yogas.append({
                    "name": "Vimala Yoga",
                    "category": "viparita_raja_yoga",
                    "is_present": True,
                    "strength": "full",
                    "forming_planets": [lord_12],
                    "forming_houses": [12, house_of_12th_lord],
                    "description": f"12th lord ({lord_12}) in house {house_of_12th_lord}",
                    "effects": "Spiritual liberation, control over expenses, foreign gains",
                    "bphs_reference": "BPHS Ch. 41",
                    "conditions_met": ["12th lord in 6th or 8th"],
                    "conditions_partial": [],
                })
        
        return yogas
    
    def _generate_summary(
        self,
        yogas_by_category: Dict[str, List],
        all_yogas: List[Dict]
    ) -> Dict:
        """Generate summary of yoga analysis"""
        total = len(all_yogas)
        raja_count = len(yogas_by_category.get("raja_yoga", []))
        dhana_count = len(yogas_by_category.get("dhana_yoga", []))
        mahapurusha_count = len(yogas_by_category.get("pancha_mahapurusha", []))
        negative_count = len(yogas_by_category.get("daridra_yoga", []))
        
        # Find strongest yogas (full strength)
        strongest = [y["name"] for y in all_yogas if y.get("strength") == "full"][:5]
        
        # Notable combinations
        notable = []
        if raja_count >= 2:
            notable.append(f"{raja_count} Raja Yogas present")
        if mahapurusha_count > 0:
            names = [y["name"] for y in yogas_by_category.get("pancha_mahapurusha", [])]
            notable.append(f"Mahapurusha: {', '.join(names)}")
        if any(y["name"] == "Gajakesari Yoga" for y in all_yogas):
            notable.append("Gajakesari Yoga (fame and wisdom)")
        
        return {
            "total_yogas_found": total,
            "raja_yogas_count": raja_count,
            "dhana_yogas_count": dhana_count,
            "mahapurusha_yogas_count": mahapurusha_count,
            "negative_yogas_count": negative_count,
            "strongest_yogas": strongest,
            "notable_combinations": notable,
        }
