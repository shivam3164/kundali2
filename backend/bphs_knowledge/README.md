# BPHS Knowledge Base - Complete Documentation

## Overview

This knowledge base contains the complete extraction of rules, yogas, planetary effects, and interpretations from **Brihat Parashara Hora Shastra (BPHS)** - the foundational text of Vedic Astrology.

## Source Document

- **Text**: Brihat Parashara Hora Shastra
- **Author**: Maharishi Parashara
- **Chapters Covered**: 45 chapters
- **Source File**: `bphs_text.txt` (2280 lines)

## Module Structure

### 1. `planets.py` - BPHS Chapter 3
**Planet Characteristics and Relationships**
- `PLANETS`: List of 9 grahas
- `PLANET_CHARACTERISTICS`: Complete characteristics for each planet
  - Sanskrit name, nature, gender, caste, guna, element
  - Exaltation, debilitation, moolatrikona, own signs
  - Friends, enemies, neutral planets
  - Dasha years, karaka, body parts, diseases
- `PLANET_RELATIONSHIPS`: Natural and temporary relationships
- `DIRECTIONAL_STRENGTHS`: Dig Bala for each planet
- `TIME_STRENGTHS`: Day/night strengths

### 2. `signs.py` - BPHS Chapter 4
**Zodiacal Sign Characteristics**
- `SIGNS`: 12 zodiac signs
- `SIGN_CHARACTERISTICS`: Complete data for each sign
  - Sanskrit name, lord, element, quality
  - Gender, nature, direction, body part
  - Rising type, humor, caste
- `SIGN_CLASSIFICATIONS`: Movable/fixed/dual, elements, odd/even

### 3. `houses.py` - BPHS Chapters 11-23
**House Meanings and Significations**
- `HOUSES`: 12 bhavas
- `HOUSE_MEANINGS`: Complete significations for each house
- `HOUSE_CLASSIFICATIONS`: Kendra, Trikona, Dusthana, etc.
- `HOUSE_KARAKAS`: Significator planet for each house

### 4. `nakshatras.py` - BPHS Chapter 3
**27 Lunar Mansions**
- `NAKSHATRA_LORDS`: Lord, deity, and degree span for each
- `VIMSHOTTARI_SEQUENCE`: Dasha sequence with years
- `NAKSHATRA_CLASSIFICATIONS`: Gana, Yoni, Tara classifications
- `get_nakshatra_from_longitude()`: Helper function

### 5. `yogas.py` - BPHS Chapters 34-36
**Comprehensive Yoga Definitions**
- `RAJ_YOGAS`: Kendra-Trikona combinations
- `NABHASH_YOGAS`: 32 types (Asraya, Dala, Akriti, Sankhya)
- `PANCHA_MAHAPURUSHA_YOGAS`: Ruchaka, Bhadra, Hamsa, Malavya, Sasa
- `CHANDRA_YOGAS`: Sunapha, Anapha, Durudhara, Kemadruma, etc.
- `SURYA_YOGAS`: Vesi, Vosi, Ubhayachari
- `DHANA_YOGAS`: Wealth combinations
- `DARIDRA_YOGAS`: Poverty combinations
- `VIPARITA_RAJ_YOGAS`: Harsha, Sarala, Vimala
- `YOGA_KARAKAS_BY_LAGNA`: Functional benefics for all 12 lagnas
- `SPECIAL_YOGAS`: Gaja Kesari, Adhi Yoga, etc.

### 6. `dashas.py` - BPHS Chapters 46+
**Vimshottari Dasha System**
- `VIMSHOTTARI_PERIODS`: Years for each planet's Mahadasha
- `VIMSHOTTARI_SEQUENCE`: 120-year cycle sequence
- `NAKSHATRA_DASHA_LORD`: Map nakshatra to dasha lord
- `MAHADASHA_EFFECTS`: Favorable/unfavorable conditions for each
- `DASHA_INTERPRETATION_RULES`: Guidelines for prediction
- `PLANETARY_FRIENDSHIPS`: For antardasha calculations
- `calculate_dasha_balance()`: Calculate remaining dasha at birth
- `get_antardasha_periods()`: Calculate sub-periods

### 7. `divisional_charts.py` - BPHS Chapters 6-7
**Shodashvarga (16 Divisional Charts)**
- `SHODASHVARGA`: D1 through D60 definitions
  - Calculation method, area of life, Vimshopak points
- `VARGA_CLASSIFICATIONS`: Shadvarga, Saptvarga, Dashvarga, Shodashvarga
- `VIMSHOPAK_DIGNITIES`: Point system
- `VARGA_USAGE`: When to use each divisional chart

### 8. `aspects.py` - BPHS Chapter 26
**Planetary Aspects (Drishti)**
- `SPECIAL_ASPECTS`: Mars (4,7,8), Jupiter (5,7,9), Saturn (3,7,10)
- `STANDARD_ASPECT_PLANETS`: Planets with only 7th aspect
- `ASPECT_STRENGTHS`: Full, three-quarter, half, quarter
- `RASHI_DRISHTI_MAP`: Sign aspects
- `ASPECT_EFFECTS`: Benefic vs malefic aspects
- Helper functions: `get_aspects_from_house()`, `is_planet_aspecting_house()`

### 9. `strengths.py` - BPHS Chapter 27
**Shadbala (Six-fold Strength)**
- `SHADBALA_COMPONENTS`: All 6 components
  - Sthana Bala, Dig Bala, Kala Bala, Cheshta Bala, Naisargika Bala, Drik Bala
- `MINIMUM_SHADBALA`: Required strength for each planet
- `DIGNITY_STRENGTHS`: Strength based on placement
- `NEECHABHANGA_RULES`: Debilitation cancellation rules
- `COMBUSTION_EFFECTS`: Effects of combustion by Sun

### 10. `avasthas.py` - BPHS Chapter 45
**Planetary States**
- `BAAL_ADI_AVASTHAS`: Infant, Youthful, Adolescent, Old, Dead
- `JAGRAT_ADI_AVASTHAS`: Awakening, Dreaming, Sleeping
- `DEEPTADI_AVASTHAS`: 9 dignity-based states
- `LAJJITADI_AVASTHAS`: 6 special states with effects
- `SHAYANADI_AVASTHAS`: 12 activity states with detailed effects for each planet

### 11. `house_lord_effects.py` - BPHS Chapters 24-25
**Effects of House Lords**
- `HOUSE_LORD_EFFECTS`: 1st-12th lord in all 12 houses
- `FUNCTIONAL_NATURE_BY_LAGNA`: Benefics, malefics, yoga karakas for each lagna
- `RAJA_YOGA_COMBINATIONS`: Kendra-Trikona rules
- `DUSTHANA_LORD_EFFECTS`: Effects of 6th, 8th, 12th lords
- `VIPARITA_RAJA_YOGA`: Special dusthana combinations

## Usage

```python
from bphs_knowledge import (
    PLANET_CHARACTERISTICS,
    SIGN_CHARACTERISTICS,
    HOUSE_MEANINGS,
    NAKSHATRA_LORDS,
    RAJ_YOGAS,
    VIMSHOTTARI_PERIODS,
    calculate_dasha_balance,
    get_aspects_from_house,
    FUNCTIONAL_NATURE_BY_LAGNA
)

# Get planet info
sun_info = PLANET_CHARACTERISTICS['Sun']
print(f"Sun exaltation: {sun_info['exaltation']}")

# Get yoga karakas for Cancer lagna
cancer_yogas = FUNCTIONAL_NATURE_BY_LAGNA['Cancer']
print(f"Yoga Karaka: {cancer_yogas['yoga_karaka']}")

# Calculate dasha
balance = calculate_dasha_balance(120.5)  # Moon at 120.5°
print(f"Dasha at birth: {balance}")
```

## BPHS Reference

Each data structure includes source references to specific chapters and slokas from BPHS for verification and further study.

## Future Enhancements

1. Add calculation engines using this knowledge base
2. Create yoga detection functions
3. Implement Shadbala calculator
4. Add transit analysis rules
5. Implement Ashtakavarga system
