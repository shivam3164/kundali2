# BPHS Planetary Aspects (Drishti)
# From Brihat Parashara Hora Shastra Chapter 26

"""
Drishti (Aspects) of Planets - BPHS Ch. 26
Each planet aspects certain houses from its position
"""

# ============================================
# STANDARD ASPECTS - BPHS Ch. 26
# ============================================

# All planets aspect the 7th house from their position with full strength
STANDARD_ASPECT = {
    'houses': [7],
    'strength': 'full',
    'description': 'All planets give full aspect to the 7th house'
}

# ============================================
# SPECIAL ASPECTS (Vishesh Drishti)
# ============================================

SPECIAL_ASPECTS = {
    'Mars': {
        'aspects': [4, 7, 8],
        'description': 'Mars aspects 4th, 7th, and 8th houses from its position',
        'strengths': {
            4: 'full',  # 4th house - full aspect
            7: 'full',  # 7th house - full aspect
            8: 'full'   # 8th house - full aspect
        },
        'source': 'BPHS Ch. 26, Sloka 5'
    },
    'Jupiter': {
        'aspects': [5, 7, 9],
        'description': 'Jupiter aspects 5th, 7th, and 9th houses from its position',
        'strengths': {
            5: 'full',  # 5th house - full aspect
            7: 'full',  # 7th house - full aspect
            9: 'full'   # 9th house - full aspect
        },
        'source': 'BPHS Ch. 26, Sloka 6'
    },
    'Saturn': {
        'aspects': [3, 7, 10],
        'description': 'Saturn aspects 3rd, 7th, and 10th houses from its position',
        'strengths': {
            3: 'full',   # 3rd house - full aspect
            7: 'full',   # 7th house - full aspect
            10: 'full'   # 10th house - full aspect
        },
        'source': 'BPHS Ch. 26, Sloka 7'
    },
    'Rahu': {
        'aspects': [5, 7, 9],
        'description': 'Rahu aspects like Jupiter - 5th, 7th, and 9th houses',
        'strengths': {
            5: 'full',
            7: 'full',
            9: 'full'
        },
        'note': 'Some traditions give Rahu aspects like Saturn (3, 7, 10)',
        'source': 'BPHS Ch. 26'
    },
    'Ketu': {
        'aspects': [5, 7, 9],
        'description': 'Ketu aspects like Jupiter - 5th, 7th, and 9th houses',
        'strengths': {
            5: 'full',
            7: 'full',
            9: 'full'
        },
        'note': 'Some traditions give Ketu aspects like Mars (4, 7, 8)',
        'source': 'BPHS Ch. 26'
    }
}

# Planets with only 7th aspect
STANDARD_ASPECT_PLANETS = ['Sun', 'Moon', 'Mercury', 'Venus']

# ============================================
# ASPECT STRENGTHS (Drishti Bala)
# ============================================

ASPECT_STRENGTHS = {
    'full': {
        'value': 60,  # Virupas
        'percentage': 100,
        'description': 'Full strength aspect'
    },
    'three_quarter': {
        'value': 45,
        'percentage': 75,
        'description': 'Three-quarter strength aspect'
    },
    'half': {
        'value': 30,
        'percentage': 50,
        'description': 'Half strength aspect'
    },
    'quarter': {
        'value': 15,
        'percentage': 25,
        'description': 'Quarter strength aspect'
    }
}

# Aspect strength based on house distance (for detailed calculations)
ASPECT_BY_DISTANCE = {
    3: {'strength': 'quarter', 'virupas': 15},      # 3rd house
    4: {'strength': 'three_quarter', 'virupas': 45}, # 4th house
    5: {'strength': 'half', 'virupas': 30},          # 5th house
    7: {'strength': 'full', 'virupas': 60},          # 7th house (full for all)
    8: {'strength': 'three_quarter', 'virupas': 45}, # 8th house
    9: {'strength': 'half', 'virupas': 30},          # 9th house
    10: {'strength': 'quarter', 'virupas': 15}       # 10th house
}

# ============================================
# RASHI DRISHTIS (Sign Aspects)
# ============================================

RASHI_DRISHTI = {
    'movable': {
        'signs': ['Aries', 'Cancer', 'Libra', 'Capricorn'],
        'aspects': 'Fixed signs except the one adjacent',
        'description': 'Movable signs aspect all fixed signs except the adjacent one'
    },
    'fixed': {
        'signs': ['Taurus', 'Leo', 'Scorpio', 'Aquarius'],
        'aspects': 'Movable signs except the one adjacent',
        'description': 'Fixed signs aspect all movable signs except the adjacent one'
    },
    'dual': {
        'signs': ['Gemini', 'Virgo', 'Sagittarius', 'Pisces'],
        'aspects': 'Other dual signs',
        'description': 'Dual signs aspect all other dual signs'
    }
}

# Detailed Rashi Drishti mapping
RASHI_DRISHTI_MAP = {
    'Aries': ['Leo', 'Scorpio', 'Aquarius'],      # Movable - aspects fixed except Taurus
    'Taurus': ['Cancer', 'Libra', 'Capricorn'],   # Fixed - aspects movable except Aries
    'Gemini': ['Virgo', 'Sagittarius', 'Pisces'], # Dual - aspects other duals
    'Cancer': ['Taurus', 'Scorpio', 'Aquarius'],  # Movable - aspects fixed except Leo
    'Leo': ['Aries', 'Libra', 'Capricorn'],       # Fixed - aspects movable except Cancer
    'Virgo': ['Gemini', 'Sagittarius', 'Pisces'], # Dual - aspects other duals
    'Libra': ['Taurus', 'Leo', 'Aquarius'],       # Movable - aspects fixed except Scorpio
    'Scorpio': ['Aries', 'Cancer', 'Capricorn'],  # Fixed - aspects movable except Libra
    'Sagittarius': ['Gemini', 'Virgo', 'Pisces'], # Dual - aspects other duals
    'Capricorn': ['Taurus', 'Leo', 'Scorpio'],    # Movable - aspects fixed except Aquarius
    'Aquarius': ['Aries', 'Cancer', 'Libra'],     # Fixed - aspects movable except Capricorn
    'Pisces': ['Gemini', 'Virgo', 'Sagittarius']  # Dual - aspects other duals
}

# ============================================
# BENEFIC AND MALEFIC ASPECTS
# ============================================

ASPECT_EFFECTS = {
    'benefic_aspect': {
        'planets': ['Jupiter', 'Venus', 'Mercury', 'Moon'],
        'effects': [
            'Protects and promotes the house aspected',
            'Reduces malefic influences',
            'Brings good fortune to the significations',
            'Jupiter\'s aspect is considered most benefic'
        ]
    },
    'malefic_aspect': {
        'planets': ['Saturn', 'Mars', 'Sun', 'Rahu', 'Ketu'],
        'effects': [
            'Causes difficulties to house significations',
            'Can damage or obstruct matters',
            'Saturn\'s aspect causes delay and restriction',
            'Mars\'s aspect causes conflict and aggression'
        ]
    }
}

# ============================================
# MUTUAL ASPECTS
# ============================================

MUTUAL_ASPECT_EFFECTS = {
    'benefic_mutual': {
        'description': 'Two benefics in mutual aspect',
        'effect': 'Creates Raja Yoga or other auspicious combinations'
    },
    'malefic_mutual': {
        'description': 'Two malefics in mutual aspect',
        'effect': 'Can cause serious difficulties, but also determination'
    },
    'benefic_malefic': {
        'description': 'Benefic and malefic in mutual aspect',
        'effect': 'Benefic mitigates malefic effects'
    }
}

# ============================================
# SPECIAL ASPECT COMBINATIONS - BPHS
# ============================================

ASPECT_YOGAS = {
    'guru_drishti_on_moon': {
        'combination': 'Jupiter aspects Moon',
        'effect': 'Gaja Kesari Yoga if Moon is in Kendra from Jupiter',
        'result': 'Wealth, intelligence, fame'
    },
    'saturn_drishti_on_sun': {
        'combination': 'Saturn aspects Sun',
        'effect': 'Creates obstacles to father, authority figures',
        'result': 'Challenges with government, father'
    },
    'mars_drishti_on_moon': {
        'combination': 'Mars aspects Moon',
        'effect': 'Can indicate Chandra Mangal Yoga',
        'result': 'Wealth but emotional volatility'
    },
    'jupiter_drishti_on_lagna': {
        'combination': 'Jupiter aspects Ascendant',
        'effect': 'Protects the native',
        'result': 'Good health, wisdom, spirituality'
    }
}

# ============================================
# HELPER FUNCTIONS
# ============================================

def get_aspects_from_house(planet, house_position):
    """
    Returns list of houses aspected by a planet from given house position.
    
    Args:
        planet: Name of the planet
        house_position: House number (1-12) where planet is placed
    
    Returns:
        List of house numbers being aspected
    """
    aspects = []
    
    # All planets aspect 7th house
    seventh = ((house_position - 1 + 7) % 12) + 1
    if seventh == 0:
        seventh = 12
    aspects.append(seventh)
    
    # Special aspects
    if planet in SPECIAL_ASPECTS:
        for asp in SPECIAL_ASPECTS[planet]['aspects']:
            if asp != 7:  # Already added 7th
                aspected_house = ((house_position - 1 + asp) % 12) + 1
                if aspected_house == 0:
                    aspected_house = 12
                aspects.append(aspected_house)
    
    return sorted(list(set(aspects)))


def get_aspect_strength(planet, aspected_house_distance):
    """
    Returns the strength of aspect for a planet at given distance.
    
    Args:
        planet: Name of the planet
        aspected_house_distance: Distance in houses (3, 4, 5, 7, 8, 9, or 10)
    
    Returns:
        Dictionary with strength info
    """
    if aspected_house_distance == 7:
        return {'strength': 'full', 'virupas': 60, 'percentage': 100}
    
    if planet in SPECIAL_ASPECTS:
        if aspected_house_distance in SPECIAL_ASPECTS[planet]['aspects']:
            return {'strength': 'full', 'virupas': 60, 'percentage': 100}
    
    # For general aspects (partial)
    if aspected_house_distance in ASPECT_BY_DISTANCE:
        return ASPECT_BY_DISTANCE[aspected_house_distance]
    
    return None


def is_planet_aspecting_house(planet, planet_house, target_house):
    """
    Checks if a planet aspects a particular house.
    
    Args:
        planet: Name of the planet
        planet_house: House where planet is placed (1-12)
        target_house: House to check for aspect (1-12)
    
    Returns:
        Boolean
    """
    aspected_houses = get_aspects_from_house(planet, planet_house)
    return target_house in aspected_houses


# Source reference
DRISHTI_SOURCE = 'BPHS Ch. 26, Slokas 1-15'
