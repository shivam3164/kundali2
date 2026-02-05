"""
Dasha Feature - Service Layer
Vimshottari Dasha calculation following BPHS
"""

from typing import Dict, List, Optional, Tuple
from datetime import date, datetime, timedelta
from dataclasses import dataclass


# ============================================
# VIMSHOTTARI DASHA CONSTANTS (BPHS Ch. 46)
# ============================================

# Nakshatra to Dasha Lord mapping
NAKSHATRA_LORDS = [
    "Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu",
    "Jupiter", "Saturn", "Mercury", "Ketu", "Venus", "Sun",
    "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury",
    "Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu",
    "Jupiter", "Saturn", "Mercury"
]

NAKSHATRAS = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
    "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
    "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha",
    "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
    "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

# Vimshottari Dasha periods in years
DASHA_YEARS = {
    "Ketu": 7,
    "Venus": 20,
    "Sun": 6,
    "Moon": 10,
    "Mars": 7,
    "Rahu": 18,
    "Jupiter": 16,
    "Saturn": 19,
    "Mercury": 17,
}

# Total Vimshottari cycle = 120 years
TOTAL_CYCLE_YEARS = 120

# Dasha sequence
DASHA_ORDER = ["Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury"]


# ============================================
# DASHA SERVICE
# ============================================

class DashaService:
    """
    Vimshottari Dasha calculation service following BPHS
    
    Features:
    - Calculate Dasha balance at birth
    - Generate all Mahadasha periods
    - Calculate Antardasha and Pratyantardasha
    - Find current running Dasha
    """
    
    def __init__(self, knowledge=None):
        self.knowledge = knowledge
    
    def get_nakshatra_from_longitude(self, moon_longitude: float) -> Tuple[str, int, float]:
        """
        Get nakshatra, pada, and progress from Moon longitude
        
        Args:
            moon_longitude: Moon's longitude in degrees (0-360)
        
        Returns:
            Tuple of (nakshatra_name, pada, progress_in_nakshatra)
        """
        # Each nakshatra spans 13°20' (360/27 = 13.333...)
        nakshatra_span = 360 / 27
        
        # Normalize longitude
        longitude = moon_longitude % 360
        
        # Find nakshatra index (0-26)
        nakshatra_index = int(longitude / nakshatra_span)
        nakshatra_name = NAKSHATRAS[nakshatra_index]
        
        # Calculate progress within nakshatra (0 to 1)
        progress = (longitude % nakshatra_span) / nakshatra_span
        
        # Calculate pada (1-4)
        pada = int(progress * 4) + 1
        if pada > 4:
            pada = 4
        
        return nakshatra_name, pada, progress
    
    def calculate_dasha_balance(
        self, 
        moon_longitude: float
    ) -> Dict:
        """
        Calculate Dasha balance at birth
        
        The balance of Dasha at birth depends on how far the Moon has
        traversed in the nakshatra. The remaining portion of the nakshatra
        determines the remaining portion of the Dasha.
        
        Returns:
            Dictionary with planet, years, months, days remaining
        """
        nakshatra_name, pada, progress = self.get_nakshatra_from_longitude(moon_longitude)
        
        # Get Dasha lord
        nakshatra_index = NAKSHATRAS.index(nakshatra_name)
        dasha_lord = NAKSHATRA_LORDS[nakshatra_index]
        
        # Total years for this Dasha
        total_years = DASHA_YEARS[dasha_lord]
        
        # Remaining portion (1 - progress) of the Dasha
        remaining_ratio = 1 - progress
        remaining_years = total_years * remaining_ratio
        
        # Convert to years, months, days
        years = int(remaining_years)
        remaining = remaining_years - years
        months = int(remaining * 12)
        remaining = (remaining * 12) - months
        days = int(remaining * 30)
        
        return {
            "planet": dasha_lord,
            "years": years,
            "months": months,
            "days": days,
            "total_days": int(remaining_years * 365.25),
            "nakshatra": nakshatra_name,
            "pada": pada,
        }
    
    def generate_mahadashas(
        self,
        moon_longitude: float,
        birth_date: date,
        num_cycles: int = 1
    ) -> List[Dict]:
        """
        Generate all Mahadasha periods starting from birth
        
        Args:
            moon_longitude: Moon's longitude at birth
            birth_date: Birth date
            num_cycles: Number of 120-year cycles to generate
        
        Returns:
            List of Mahadasha periods
        """
        balance = self.calculate_dasha_balance(moon_longitude)
        dasha_lord = balance["planet"]
        
        # Find starting index in Dasha order
        start_index = DASHA_ORDER.index(dasha_lord)
        
        mahadashas = []
        current_date = birth_date
        
        for cycle in range(num_cycles):
            for i in range(9):
                planet_index = (start_index + i) % 9
                planet = DASHA_ORDER[planet_index]
                
                # Duration
                if i == 0 and cycle == 0:
                    # First Dasha - use balance
                    duration_days = balance["total_days"]
                else:
                    duration_days = int(DASHA_YEARS[planet] * 365.25)
                
                end_date = current_date + timedelta(days=duration_days)
                
                mahadashas.append({
                    "planet": planet,
                    "start_date": current_date,
                    "end_date": end_date,
                    "duration_years": duration_days / 365.25,
                    "duration_months": duration_days / 30.44,
                    "duration_days": duration_days,
                })
                
                current_date = end_date
        
        return mahadashas
    
    def generate_antardashas(
        self,
        mahadasha_planet: str,
        mahadasha_start: date,
        mahadasha_duration_days: int
    ) -> List[Dict]:
        """
        Generate Antardasha periods within a Mahadasha
        
        Antardasha periods follow the same sequence as Mahadasha,
        starting with the Mahadasha lord. The duration is proportional
        to the ratio of the Antardasha lord's period to the total cycle.
        
        Args:
            mahadasha_planet: Mahadasha lord
            mahadasha_start: Start date of Mahadasha
            mahadasha_duration_days: Total duration of Mahadasha in days
        
        Returns:
            List of Antardasha periods
        """
        # Start index for Antardasha sequence
        start_index = DASHA_ORDER.index(mahadasha_planet)
        
        antardashas = []
        current_date = mahadasha_start
        
        for i in range(9):
            planet_index = (start_index + i) % 9
            planet = DASHA_ORDER[planet_index]
            
            # Antardasha duration = Mahadasha duration × (Antardasha years / 120)
            ratio = DASHA_YEARS[planet] / TOTAL_CYCLE_YEARS
            duration_days = int(mahadasha_duration_days * ratio)
            
            end_date = current_date + timedelta(days=duration_days)
            
            antardashas.append({
                "level": "antardasha",
                "planet": planet,
                "start_date": current_date,
                "end_date": end_date,
                "duration_years": duration_days / 365.25,
                "duration_months": duration_days / 30.44,
                "duration_days": duration_days,
            })
            
            current_date = end_date
        
        return antardashas
    
    def generate_pratyantardashas(
        self,
        antardasha_planet: str,
        antardasha_start: date,
        antardasha_duration_days: int
    ) -> List[Dict]:
        """
        Generate Pratyantardasha periods within an Antardasha
        
        Same logic as Antardasha, but one level deeper.
        """
        start_index = DASHA_ORDER.index(antardasha_planet)
        
        pratyantardashas = []
        current_date = antardasha_start
        
        for i in range(9):
            planet_index = (start_index + i) % 9
            planet = DASHA_ORDER[planet_index]
            
            ratio = DASHA_YEARS[planet] / TOTAL_CYCLE_YEARS
            duration_days = int(antardasha_duration_days * ratio)
            
            end_date = current_date + timedelta(days=duration_days)
            
            pratyantardashas.append({
                "level": "pratyantardasha",
                "planet": planet,
                "start_date": current_date,
                "end_date": end_date,
                "duration_years": duration_days / 365.25,
                "duration_months": duration_days / 30.44,
                "duration_days": duration_days,
            })
            
            current_date = end_date
        
        return pratyantardashas
    
    def find_current_dasha(
        self,
        moon_longitude: float,
        birth_date: date,
        target_date: Optional[date] = None
    ) -> Dict:
        """
        Find the current running Dasha periods for a given date
        
        Args:
            moon_longitude: Moon's longitude at birth
            birth_date: Birth date
            target_date: Date to find Dasha for (defaults to today)
        
        Returns:
            Dictionary with current Mahadasha, Antardasha, and Pratyantardasha
        """
        if target_date is None:
            target_date = date.today()
        
        # Generate Mahadashas
        mahadashas = self.generate_mahadashas(moon_longitude, birth_date, num_cycles=2)
        
        # Find current Mahadasha
        current_mahadasha = None
        for md in mahadashas:
            if md["start_date"] <= target_date < md["end_date"]:
                current_mahadasha = md
                break
        
        if not current_mahadasha:
            return {"error": "Target date is outside calculated range"}
        
        # Generate Antardashas for current Mahadasha
        antardashas = self.generate_antardashas(
            current_mahadasha["planet"],
            current_mahadasha["start_date"],
            current_mahadasha["duration_days"]
        )
        
        # Find current Antardasha
        current_antardasha = None
        for ad in antardashas:
            if ad["start_date"] <= target_date < ad["end_date"]:
                current_antardasha = ad
                break
        
        if not current_antardasha:
            return {
                "mahadasha": current_mahadasha,
                "error": "Could not find Antardasha"
            }
        
        # Generate Pratyantardashas for current Antardasha
        pratyantardashas = self.generate_pratyantardashas(
            current_antardasha["planet"],
            current_antardasha["start_date"],
            current_antardasha["duration_days"]
        )
        
        # Find current Pratyantardasha
        current_pratyantardasha = None
        for pd in pratyantardashas:
            if pd["start_date"] <= target_date < pd["end_date"]:
                current_pratyantardasha = pd
                break
        
        # Calculate elapsed percentages
        md_elapsed = (target_date - current_mahadasha["start_date"]).days / current_mahadasha["duration_days"] * 100
        ad_elapsed = (target_date - current_antardasha["start_date"]).days / current_antardasha["duration_days"] * 100
        
        # Add is_current and elapsed_percentage
        current_mahadasha["is_current"] = True
        current_mahadasha["level"] = "mahadasha"
        current_mahadasha["elapsed_percentage"] = round(md_elapsed, 1)
        
        current_antardasha["is_current"] = True
        current_antardasha["elapsed_percentage"] = round(ad_elapsed, 1)
        
        if current_pratyantardasha:
            pd_elapsed = (target_date - current_pratyantardasha["start_date"]).days / current_pratyantardasha["duration_days"] * 100
            current_pratyantardasha["is_current"] = True
            current_pratyantardasha["elapsed_percentage"] = round(pd_elapsed, 1)
        
        # Summary
        summary = f"{current_mahadasha['planet']} Mahadasha - {current_antardasha['planet']} Antardasha"
        if current_pratyantardasha:
            summary += f" - {current_pratyantardasha['planet']} Pratyantardasha"
        
        return {
            "mahadasha": current_mahadasha,
            "antardasha": current_antardasha,
            "pratyantardasha": current_pratyantardasha,
            "summary": summary,
        }
    
    def get_dasha_interpretation(self, planet: str, level: str = "mahadasha") -> Dict:
        """
        Get interpretation hints for a Dasha period
        
        Uses BPHS knowledge base for planet significations
        """
        if not self.knowledge:
            return {"planet": planet, "level": level}
        
        planet_info = self.knowledge.get_planet_info(planet)
        dasha_effects = self.knowledge.dasha_effects.get(planet, {})
        
        return {
            "planet": planet,
            "level": level,
            "general_nature": planet_info.get("nature"),
            "significations": planet_info.get("basic", {}).get("significations", []),
            "dasha_effects": dasha_effects,
        }
    
    def calculate_full_dasha(
        self,
        moon_longitude: float,
        birth_date: date,
        target_date: Optional[date] = None,
        include_antardashas: bool = True
    ) -> Dict:
        """
        Calculate complete Dasha information
        
        Returns all Mahadashas with optional Antardashas and current period info
        """
        balance = self.calculate_dasha_balance(moon_longitude)
        mahadashas = self.generate_mahadashas(moon_longitude, birth_date)
        
        result = {
            "moon_nakshatra": balance["nakshatra"],
            "moon_nakshatra_pada": balance["pada"],
            "birth_date": birth_date,
            "balance_at_birth": balance,
            "mahadashas": [],
            "current_dasha": None,
        }
        
        # Process Mahadashas
        for md in mahadashas:
            md_info = {
                "planet": md["planet"],
                "start_date": md["start_date"],
                "end_date": md["end_date"],
                "duration_years": round(md["duration_years"], 2),
                "is_current": False,
                "description": self.knowledge.MAHADASHA_EFFECTS.get(md["planet"], {}).get("description", ""),
                "antardashas": [],
            }
            
            # Check if current
            if target_date:
                if md["start_date"] <= target_date < md["end_date"]:
                    md_info["is_current"] = True
            
            # Add Antardashas if requested
            if include_antardashas:
                ads = self.generate_antardashas(
                    md["planet"],
                    md["start_date"],
                    md["duration_days"]
                )
                md_info["antardashas"] = ads
            
            result["mahadashas"].append(md_info)
        
        # Find current Dasha
        if target_date:
            result["current_dasha"] = self.find_current_dasha(
                moon_longitude, birth_date, target_date
            )
        
        return result
