# Knowledge Base - BPHS Knowledge re-exported from bphs_knowledge
# This module provides a cleaner import path for the knowledge base

import sys
import os

# Add backend to path if needed
backend_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if backend_path not in sys.path:
    sys.path.insert(0, backend_path)

from bphs_knowledge import (
    # Planets
    PLANETS,
    PLANET_CHARACTERISTICS,
    PLANET_RELATIONSHIPS,
    EXALTATION_POINTS,
    DEBILITATION_POINTS,
    MOOLATRIKONA,
    
    # Signs
    SIGNS,
    SIGN_CHARACTERISTICS,
    SIGN_CLASSIFICATIONS,
    SIGN_LORDS,
    
    # Houses
    HOUSES,
    HOUSE_MEANINGS,
    HOUSE_KARAKAS,
    HOUSE_CLASSIFICATIONS,
    
    # Nakshatras
    NAKSHATRAS,
    NAKSHATRA_LORDS,
    
    # Yogas
    RAJ_YOGAS,
    DHANA_YOGAS,
    PANCHA_MAHAPURUSHA_YOGAS,
    NABHASH_YOGAS,
    CHANDRA_YOGAS,
    SURYA_YOGAS,
    DARIDRA_YOGAS,
    VIPARITA_RAJ_YOGAS,
    CHAPTER_36_YOGAS,
    SPECIAL_YOGAS,
    YOGA_KARAKAS_BY_LAGNA,
    
    # Dashas
    VIMSHOTTARI_PERIODS,
    DASHA_SEQUENCE,
    MAHADASHA_EFFECTS,
    
    # Divisional Charts
    SHODASHVARGA,
    VARGA_USAGE,
    
    # Aspects
    SPECIAL_ASPECTS,
    RASHI_DRISHTI_MAP,
    
    # Strengths
    SHADBALA_COMPONENTS,
    DIGNITY_STRENGTHS,
    
    # Avasthas
    BAAL_ADI_AVASTHAS,
    JAGRAT_ADI_AVASTHAS,
    DEEPTADI_AVASTHAS,
    SHAYANADI_AVASTHAS,
    
    # House Lord Effects
    HOUSE_LORD_EFFECTS,
    FUNCTIONAL_NATURE_BY_LAGNA,
    
    # New Planet Data
    PLANET_CABINET,
    PLANET_ABODES,
    PLANET_PERIODS,
    PLANET_TREES,
    PLANET_ROBES,
    PLANET_CLASSIFICATIONS,
    PLANET_SEASONS,
    PLANET_STRENGTH_RATIOS,
    DIRECTIONAL_STRENGTHS,
    TIME_STRENGTHS,
    NATURAL_STRENGTH_ORDER,
    COMBUSTION_ORBS,
)

# Create aliases for the features to use
PLANET_NATURES = {p: PLANET_CHARACTERISTICS.get(p, {}).get('nature', 'neutral') 
                  for p in PLANETS if p in PLANET_CHARACTERISTICS}

SIGN_ELEMENTS = {}
for element in ['fire', 'earth', 'air', 'water']:
    for sign in SIGN_CLASSIFICATIONS.get(element, []):
        SIGN_ELEMENTS[sign] = element.title()

SIGN_MODALITIES = {}
for modality in ['movable', 'fixed', 'dual']:
    for sign in SIGN_CLASSIFICATIONS.get(modality, []):
        SIGN_MODALITIES[sign] = modality.title()

NAKSHATRA_PADAS = {nak: [1, 2, 3, 4] for nak in NAKSHATRAS}

# Rename for consistency
RAJA_YOGAS = RAJ_YOGAS
VIPARITA_RAJA_YOGAS = VIPARITA_RAJ_YOGAS
DIVISIONAL_CHARTS = SHODASHVARGA
VARGA_SIGNIFICATIONS = VARGA_USAGE
GRAHA_DRISHTI = SPECIAL_ASPECTS
RASHI_DRISHTI = RASHI_DRISHTI_MAP  # Alias for consistency
STHANA_BALA = DIGNITY_STRENGTHS
DIG_BALA = {}  # Will be populated if needed
KALA_BALA = {}  # Will be populated if needed
BALA_AVASTHA = BAAL_ADI_AVASTHAS
JAGRAT_AVASTHA = JAGRAT_ADI_AVASTHAS
DEEPTADI_AVASTHA = DEEPTADI_AVASTHAS  # Alias for consistency
SHAYANADI_AVASTHA = SHAYANADI_AVASTHAS  # Alias for consistency
VIMSHOTTARI_ORDER = DASHA_SEQUENCE
DASHA_EFFECTS = MAHADASHA_EFFECTS
HOUSE_GROUPINGS = HOUSE_CLASSIFICATIONS  # Alias for consistency
PANCHA_MAHAPURUSHA = PANCHA_MAHAPURUSHA_YOGAS  # Alias for consistency
FUNCTIONAL_BENEFICS = {}
FUNCTIONAL_MALEFICS = {}

# Populate functional benefics/malefics from FUNCTIONAL_NATURE_BY_LAGNA
for lagna, nature in FUNCTIONAL_NATURE_BY_LAGNA.items():
    FUNCTIONAL_BENEFICS[lagna] = nature.get('benefics', [])
    FUNCTIONAL_MALEFICS[lagna] = nature.get('malefics', [])

# Create a unified knowledge interface
class BPHSKnowledge:
    """
    Unified interface to access all BPHS knowledge
    """
    
    # Planets
    planets = PLANETS
    planet_characteristics = PLANET_CHARACTERISTICS  # Dict with full planet info
    planet_natures = PLANET_NATURES
    planet_relationships = PLANET_RELATIONSHIPS
    exaltation_points = EXALTATION_POINTS
    debilitation_points = DEBILITATION_POINTS
    moolatrikona = MOOLATRIKONA
    
    # Signs
    signs = SIGNS
    sign_elements = SIGN_ELEMENTS
    sign_modalities = SIGN_MODALITIES
    sign_lords = SIGN_LORDS
    sign_characteristics = SIGN_CHARACTERISTICS
    
    # Houses
    houses = HOUSES
    house_meanings = HOUSE_MEANINGS  # Dict with house significations
    house_karakas = HOUSE_KARAKAS
    house_groupings = HOUSE_GROUPINGS
    
    # Nakshatras
    nakshatras = NAKSHATRAS
    nakshatra_lords = NAKSHATRA_LORDS
    nakshatra_padas = NAKSHATRA_PADAS
    
    # Yogas
    raja_yogas = RAJA_YOGAS
    dhana_yogas = DHANA_YOGAS
    pancha_mahapurusha = PANCHA_MAHAPURUSHA
    nabhash_yogas = NABHASH_YOGAS
    chandra_yogas = CHANDRA_YOGAS
    surya_yogas = SURYA_YOGAS
    daridra_yogas = DARIDRA_YOGAS
    viparita_raja_yogas = VIPARITA_RAJA_YOGAS
    
    # Dashas
    vimshottari_periods = VIMSHOTTARI_PERIODS
    vimshottari_order = VIMSHOTTARI_ORDER
    dasha_effects = DASHA_EFFECTS
    
    # Divisional Charts
    divisional_charts = DIVISIONAL_CHARTS
    varga_significations = VARGA_SIGNIFICATIONS
    
    # Aspects
    graha_drishti = GRAHA_DRISHTI
    rashi_drishti = RASHI_DRISHTI
    special_aspects = SPECIAL_ASPECTS
    
    # Strengths
    shadbala_components = SHADBALA_COMPONENTS
    sthana_bala = STHANA_BALA
    dig_bala = DIG_BALA
    kala_bala = KALA_BALA
    
    # Avasthas
    bala_avastha = BALA_AVASTHA
    jagrat_avastha = JAGRAT_AVASTHA
    deeptadi_avastha = DEEPTADI_AVASTHA
    shayanadi_avastha = SHAYANADI_AVASTHA
    
    # House Lord Effects
    house_lord_effects = HOUSE_LORD_EFFECTS
    functional_benefics = FUNCTIONAL_BENEFICS
    functional_malefics = FUNCTIONAL_MALEFICS
    
    @classmethod
    def get_planet_info(cls, planet: str) -> dict:
        """Get comprehensive info about a planet"""
        return {
            "basic": cls.planets.get(planet, {}),
            "nature": cls.planet_natures.get(planet),
            "relationships": cls.planet_relationships.get(planet, {}),
            "exaltation": cls.exaltation_points.get(planet),
            "debilitation": cls.debilitation_points.get(planet),
            "moolatrikona": cls.moolatrikona.get(planet),
        }
    
    @classmethod
    def get_sign_info(cls, sign: str) -> dict:
        """Get comprehensive info about a sign"""
        return {
            "basic": cls.signs.get(sign, {}),
            "element": cls.sign_elements.get(sign),
            "modality": cls.sign_modalities.get(sign),
            "lord": cls.sign_lords.get(sign),
            "characteristics": cls.sign_characteristics.get(sign, {}),
        }
    
    @classmethod
    def get_house_info(cls, house: int) -> dict:
        """Get comprehensive info about a house"""
        return {
            "basic": cls.house_meanings.get(house, {}),
            "karakas": cls.house_karakas.get(house, []),
        }
    
    @classmethod
    def get_nakshatra_info(cls, nakshatra: str) -> dict:
        """Get comprehensive info about a nakshatra"""
        return {
            "basic": cls.nakshatras.get(nakshatra, {}),
            "lord": cls.nakshatra_lords.get(nakshatra),
            "padas": cls.nakshatra_padas.get(nakshatra, []),
        }


# Export singleton instance
bphs_knowledge = BPHSKnowledge()

__all__ = [
    'bphs_knowledge',
    'BPHSKnowledge',
]
