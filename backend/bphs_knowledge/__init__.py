# BPHS Knowledge Base
# Brihat Parashara Hora Shastra - Complete Knowledge Extraction
# This package contains all rules, yogas, planetary effects, and interpretations from BPHS

"""
Complete BPHS Knowledge Base for Kundali Analysis
Extracted from Brihat Parashara Hora Shastra (45 Chapters)

Modules:
- planets: Planet characteristics, relationships, dignities (Ch. 3)
- signs: Sign characteristics, classifications (Ch. 4)
- houses: House meanings, karakas, significations (Ch. 11-23)
- nakshatras: 27 Nakshatras, lords, classifications (Ch. 3)
- yogas: All yogas including Raj, Nabhash, Pancha Mahapurusha (Ch. 34-36)
- dashas: Vimshottari Dasha system and calculations (Ch. 46+)
- divisional_charts: Shodashvarga (16 divisional charts) (Ch. 6-7)
- aspects: Planetary aspects (Drishti) (Ch. 26)
- strengths: Shadbala (6-fold strength) (Ch. 27)
- avasthas: Planetary states and their effects (Ch. 45)
- house_lord_effects: Effects of house lords in various houses (Ch. 24-25)
"""

# Planets - BPHS Ch. 3
from .planets import (
    PLANETS,
    PLANET_CHARACTERISTICS,
    PLANET_RELATIONSHIPS,
    PLANET_STRENGTH_RATIOS,
    DIRECTIONAL_STRENGTHS,
    TIME_STRENGTHS,
    PLANET_CABINET,
    PLANET_ABODES,
    PLANET_PERIODS,
    PLANET_TREES,
    PLANET_ROBES,
    PLANET_CLASSIFICATIONS,
    PLANET_SEASONS,
    NATURAL_STRENGTH_ORDER,
    COMBUSTION_ORBS
)

# For backwards compatibility, create aliases
NATURAL_FRIENDSHIPS = PLANET_RELATIONSHIPS.get('natural', {})
EXALTATION_POINTS = {p: PLANET_CHARACTERISTICS[p].get('exaltation', {}) for p in PLANETS if p in PLANET_CHARACTERISTICS}
DEBILITATION_POINTS = {p: PLANET_CHARACTERISTICS[p].get('debilitation', {}) for p in PLANETS if p in PLANET_CHARACTERISTICS}
MOOLATRIKONA = {p: PLANET_CHARACTERISTICS[p].get('moolatrikona', {}) for p in PLANETS if p in PLANET_CHARACTERISTICS}
OWN_SIGNS = {p: PLANET_CHARACTERISTICS[p].get('own_signs', []) for p in PLANETS if p in PLANET_CHARACTERISTICS}

# Signs - BPHS Ch. 4
from .signs import (
    SIGNS,
    SIGN_CHARACTERISTICS,
    SIGN_CLASSIFICATIONS,
    SIGN_ASPECTS
)

# Create sign-related aliases
SIGN_LORDS = {sign: data.get('lord', '') for sign, data in SIGN_CHARACTERISTICS.items()}
SIGN_ELEMENTS = SIGN_CLASSIFICATIONS.get('fire', []) + SIGN_CLASSIFICATIONS.get('earth', []) + \
                SIGN_CLASSIFICATIONS.get('air', []) + SIGN_CLASSIFICATIONS.get('water', [])
SIGN_MODALITIES = {
    'movable': SIGN_CLASSIFICATIONS.get('movable', []),
    'fixed': SIGN_CLASSIFICATIONS.get('fixed', []),
    'dual': SIGN_CLASSIFICATIONS.get('dual', [])
}
SIGN_DIRECTIONS = {sign: data.get('direction', '') for sign, data in SIGN_CHARACTERISTICS.items()}

# Houses - BPHS Ch. 11-23
from .houses import (
    HOUSES,
    HOUSE_MEANINGS,
    HOUSE_CLASSIFICATIONS
)

# Create house-related aliases
HOUSE_KARAKAS = {h: data.get('karaka', '') for h, data in HOUSE_MEANINGS.items()}

# Nakshatras - BPHS Ch. 3
from .nakshatras import (
    NAKSHATRAS,
    NAKSHATRA_LORDS,
    VIMSHOTTARI_SEQUENCE,
    NAKSHATRA_CLASSIFICATIONS,
    get_nakshatra_from_longitude
)

# Yogas - BPHS Ch. 34-36
from .yogas import (
    RAJ_YOGAS,
    NABHASH_YOGAS,
    PANCHA_MAHAPURUSHA_YOGAS,
    CHANDRA_YOGAS,
    SURYA_YOGAS,
    DHANA_YOGAS,
    DARIDRA_YOGAS,
    VIPARITA_RAJ_YOGAS,
    YOGA_KARAKAS_BY_LAGNA,
    SPECIAL_YOGAS,
    CHAPTER_36_YOGAS
)

# Dashas - BPHS Ch. 46+
from .dashas import (
    VIMSHOTTARI_PERIODS,
    VIMSHOTTARI_SEQUENCE as DASHA_SEQUENCE,
    NAKSHATRA_DASHA_LORD,
    MAHADASHA_EFFECTS,
    DASHA_INTERPRETATION_RULES,
    PLANETARY_FRIENDSHIPS,
    calculate_dasha_balance,
    get_antardasha_sequence
)

# Divisional Charts - BPHS Ch. 6-7
from .divisional_charts import (
    SHODASHVARGA,
    VARGA_CLASSIFICATIONS,
    VIMSHOPAK_DIGNITIES,
    VARGA_USAGE
)

# Aspects - BPHS Ch. 26
from .aspects import (
    SPECIAL_ASPECTS,
    STANDARD_ASPECT_PLANETS,
    ASPECT_STRENGTHS,
    ASPECT_BY_DISTANCE,
    RASHI_DRISHTI_MAP,
    ASPECT_EFFECTS,
    get_aspects_from_house,
    get_aspect_strength,
    is_planet_aspecting_house
)

# Strengths - BPHS Ch. 27
from .strengths import (
    SHADBALA_COMPONENTS,
    MINIMUM_SHADBALA,
    BHAVA_BALA_COMPONENTS,
    ISHTA_KASHTA,
    DIGNITY_STRENGTHS,
    NEECHABHANGA_RULES,
    VIMSOPAKA_DIGNITY_POINTS,
    VIMSOPAKA_DESIGNATIONS,
    COMBUSTION_EFFECTS
)

# Avasthas - BPHS Ch. 45
from .avasthas import (
    BAAL_ADI_AVASTHAS,
    JAGRAT_ADI_AVASTHAS,
    DEEPTADI_AVASTHAS,
    LAJJITADI_AVASTHAS,
    SHAYANADI_AVASTHAS,
    PLANET_ADDITIVES,
    SYLLABLE_VALUES
)

# House Lord Effects - BPHS Ch. 24-25
from .house_lord_effects import (
    HOUSE_LORD_EFFECTS,
    FUNCTIONAL_NATURE_BY_LAGNA,
    RAJA_YOGA_COMBINATIONS,
    DUSTHANA_LORD_EFFECTS,
    VIPARITA_RAJA_YOGA
)

__all__ = [
    # Planets
    'PLANETS', 'PLANET_CHARACTERISTICS', 'PLANET_RELATIONSHIPS',
    'NATURAL_FRIENDSHIPS', 'EXALTATION_POINTS', 'DEBILITATION_POINTS',
    'MOOLATRIKONA', 'OWN_SIGNS', 'PLANET_STRENGTH_RATIOS',
    'DIRECTIONAL_STRENGTHS', 'TIME_STRENGTHS',
    'PLANET_CABINET', 'PLANET_ABODES', 'PLANET_PERIODS', 'PLANET_TREES',
    'PLANET_ROBES', 'PLANET_CLASSIFICATIONS', 'PLANET_SEASONS',
    'NATURAL_STRENGTH_ORDER', 'COMBUSTION_ORBS',
    
    # Signs
    'SIGNS', 'SIGN_CHARACTERISTICS', 'SIGN_LORDS', 'SIGN_ELEMENTS',
    'SIGN_MODALITIES', 'SIGN_DIRECTIONS', 'SIGN_CLASSIFICATIONS', 'SIGN_ASPECTS',
    
    # Houses
    'HOUSES', 'HOUSE_MEANINGS', 'HOUSE_KARAKAS', 'HOUSE_CLASSIFICATIONS',
    
    # Nakshatras
    'NAKSHATRAS', 'NAKSHATRA_LORDS', 'VIMSHOTTARI_SEQUENCE', 'NAKSHATRA_CLASSIFICATIONS',
    'get_nakshatra_from_longitude',
    
    # Yogas
    'RAJ_YOGAS', 'NABHASH_YOGAS', 'PANCHA_MAHAPURUSHA_YOGAS',
    'CHANDRA_YOGAS', 'SURYA_YOGAS', 'DHANA_YOGAS', 'DARIDRA_YOGAS',
    'VIPARITA_RAJ_YOGAS', 'YOGA_KARAKAS_BY_LAGNA', 'SPECIAL_YOGAS',
    'CHAPTER_36_YOGAS',
    
    # Dashas
    'VIMSHOTTARI_PERIODS', 'DASHA_SEQUENCE', 'NAKSHATRA_DASHA_LORD',
    'MAHADASHA_EFFECTS', 'DASHA_INTERPRETATION_RULES', 'PLANETARY_FRIENDSHIPS',
    'calculate_dasha_balance', 'get_antardasha_sequence',
    
    # Divisional Charts
    'SHODASHVARGA', 'VARGA_CLASSIFICATIONS', 'VIMSHOPAK_DIGNITIES', 'VARGA_USAGE',
    
    # Aspects
    'SPECIAL_ASPECTS', 'STANDARD_ASPECT_PLANETS', 'ASPECT_STRENGTHS',
    'ASPECT_BY_DISTANCE', 'RASHI_DRISHTI_MAP', 'ASPECT_EFFECTS',
    'get_aspects_from_house', 'get_aspect_strength', 'is_planet_aspecting_house',
    
    # Strengths
    'SHADBALA_COMPONENTS', 'MINIMUM_SHADBALA', 'BHAVA_BALA_COMPONENTS',
    'ISHTA_KASHTA', 'DIGNITY_STRENGTHS', 'NEECHABHANGA_RULES',
    'VIMSOPAKA_DIGNITY_POINTS', 'VIMSOPAKA_DESIGNATIONS', 'COMBUSTION_EFFECTS',
    
    # Avasthas
    'BAAL_ADI_AVASTHAS', 'JAGRAT_ADI_AVASTHAS', 'DEEPTADI_AVASTHAS',
    'LAJJITADI_AVASTHAS', 'SHAYANADI_AVASTHAS', 'PLANET_ADDITIVES', 'SYLLABLE_VALUES',
    
    # House Lord Effects
    'HOUSE_LORD_EFFECTS', 'FUNCTIONAL_NATURE_BY_LAGNA', 'RAJA_YOGA_COMBINATIONS',
    'DUSTHANA_LORD_EFFECTS', 'VIPARITA_RAJA_YOGA'
]
