# BPHS Chapter 3: Grah Characters and Description
# Complete planetary characteristics from Brihat Parashara Hora Shastra

PLANETS = ['Sun', 'Moon', 'Mars', 'Mercury', 'Jupiter', 'Venus', 'Saturn', 'Rahu', 'Ketu']

PLANET_CHARACTERISTICS = {
    'Sun': {
        'sanskrit_name': 'Surya',
        'nature': 'malefic',
        'gender': 'male',
        'caste': 'Kshatriya',
        'guna': 'Sattvic',
        'element': 'fire',
        'deity': 'Agni',
        'day': 'Sunday',
        'direction': 'East',
        'color': 'blood-red',
        'gem': 'Ruby',
        'metal': 'copper',
        'taste': 'pungent',
        'dhatu': 'bones',
        'exaltation': {'sign': 'Aries', 'degree': 10},
        'debilitation': {'sign': 'Libra', 'degree': 10},
        'own_signs': ['Leo'],
        'moolatrikona': {'sign': 'Leo', 'start': 0, 'end': 20},
        'friends': ['Moon', 'Mars', 'Jupiter'],
        'enemies': ['Venus', 'Saturn'],
        'neutral': ['Mercury'],
        'dasha_years': 6,
        'karaka': 'soul, authority, father, health, government',
        'body_parts': 'heart, eyes, head, bones',
        'diseases': 'heart diseases, eye problems, fevers, headaches',
        'description': 'Surya has honey-coloured eyes, square body, clean habits, bilious, intelligent, limited hair.',
        'reference': 'BPHS Ch. 3, Slokas 23'
    },
    'Moon': {
        'sanskrit_name': 'Chandra',
        'nature': 'benefic',  # benefic when waxing, malefic when waning
        'gender': 'female',
        'caste': 'Vaishya',
        'guna': 'Sattvic',
        'element': 'water',
        'deity': 'Varuna',
        'day': 'Monday',
        'direction': 'North-West',
        'color': 'tawny/white',
        'gem': 'Pearl',
        'metal': 'silver',
        'taste': 'saline',
        'dhatu': 'blood',
        'exaltation': {'sign': 'Taurus', 'degree': 3},
        'debilitation': {'sign': 'Scorpio', 'degree': 3},
        'own_signs': ['Cancer'],
        'moolatrikona': {'sign': 'Taurus', 'start': 3, 'end': 30},
        'friends': ['Sun', 'Mercury'],
        'enemies': [],
        'neutral': ['Mars', 'Jupiter', 'Venus', 'Saturn'],
        'dasha_years': 10,
        'karaka': 'mind, emotions, mother, fluids, travel',
        'body_parts': 'blood, lungs, left eye, breast',
        'diseases': 'mental disorders, cold, cough, asthma',
        'description': 'Chandr is windy and phlegmatic, learned, round body, auspicious looks, sweet speech, fickle-minded, lustful.',
        'reference': 'BPHS Ch. 3, Slokas 24'
    },
    'Mars': {
        'sanskrit_name': 'Mangal',
        'nature': 'malefic',
        'gender': 'male',
        'caste': 'Kshatriya',
        'guna': 'Tamasic',
        'element': 'fire',
        'deity': 'Subrahmanya',
        'day': 'Tuesday',
        'direction': 'South',
        'color': 'blood-red',
        'gem': 'Red Coral',
        'metal': 'copper',
        'taste': 'bitter',
        'dhatu': 'marrow',
        'exaltation': {'sign': 'Capricorn', 'degree': 28},
        'debilitation': {'sign': 'Cancer', 'degree': 28},
        'own_signs': ['Aries', 'Scorpio'],
        'moolatrikona': {'sign': 'Aries', 'start': 0, 'end': 12},
        'friends': ['Sun', 'Moon', 'Jupiter'],
        'enemies': ['Mercury'],
        'neutral': ['Venus', 'Saturn'],
        'dasha_years': 7,
        'karaka': 'courage, energy, siblings, property, accidents',
        'body_parts': 'muscles, bone marrow, blood',
        'diseases': 'accidents, burns, surgeries, blood disorders',
        'description': 'Mangal has blood-red eyes, fickle-minded, liberal, bilious, given to anger, thin waist and physique.',
        'reference': 'BPHS Ch. 3, Slokas 25'
    },
    'Mercury': {
        'sanskrit_name': 'Budha',
        'nature': 'neutral',  # benefic with benefics, malefic with malefics
        'gender': 'neuter',
        'caste': 'Vaishya',
        'guna': 'Rajasic',
        'element': 'earth',
        'deity': 'Maha Vishnu',
        'day': 'Wednesday',
        'direction': 'North',
        'color': 'green',
        'gem': 'Emerald',
        'metal': 'bronze',
        'taste': 'mixed',
        'dhatu': 'skin',
        'exaltation': {'sign': 'Virgo', 'degree': 15},
        'debilitation': {'sign': 'Pisces', 'degree': 15},
        'own_signs': ['Gemini', 'Virgo'],
        'moolatrikona': {'sign': 'Virgo', 'start': 15, 'end': 20},
        'friends': ['Sun', 'Venus'],
        'enemies': ['Moon'],
        'neutral': ['Mars', 'Jupiter', 'Saturn'],
        'dasha_years': 17,
        'karaka': 'intelligence, speech, communication, business, education',
        'body_parts': 'skin, nervous system, speech',
        'diseases': 'nervous disorders, skin diseases, speech defects',
        'description': 'Budha has attractive physique, uses words with many meanings, fond of jokes, mix of all three humours.',
        'reference': 'BPHS Ch. 3, Slokas 26'
    },
    'Jupiter': {
        'sanskrit_name': 'Guru',
        'nature': 'benefic',
        'gender': 'male',
        'caste': 'Brahmin',
        'guna': 'Sattvic',
        'element': 'space/ether',
        'deity': 'Indra',
        'day': 'Thursday',
        'direction': 'North-East',
        'color': 'tawny/yellow',
        'gem': 'Yellow Sapphire',
        'metal': 'gold',
        'taste': 'sweet',
        'dhatu': 'fat',
        'exaltation': {'sign': 'Cancer', 'degree': 5},
        'debilitation': {'sign': 'Capricorn', 'degree': 5},
        'own_signs': ['Sagittarius', 'Pisces'],
        'moolatrikona': {'sign': 'Sagittarius', 'start': 0, 'end': 10},
        'friends': ['Sun', 'Moon', 'Mars'],
        'enemies': ['Mercury', 'Venus'],
        'neutral': ['Saturn'],
        'dasha_years': 16,
        'karaka': 'wisdom, knowledge, children, fortune, dharma',
        'body_parts': 'liver, fat, thighs',
        'diseases': 'liver disorders, diabetes, obesity',
        'description': 'Guru has big body, tawny hair and eyes, phlegmatic, intelligent, learned in all Shastras.',
        'reference': 'BPHS Ch. 3, Slokas 27'
    },
    'Venus': {
        'sanskrit_name': 'Shukra',
        'nature': 'benefic',
        'gender': 'female',
        'caste': 'Brahmin',
        'guna': 'Rajasic',
        'element': 'water',
        'deity': 'Shachi Devi',
        'day': 'Friday',
        'direction': 'South-East',
        'color': 'variegated/white',
        'gem': 'Diamond',
        'metal': 'silver',
        'taste': 'acidulous/sour',
        'dhatu': 'semen',
        'exaltation': {'sign': 'Pisces', 'degree': 27},
        'debilitation': {'sign': 'Virgo', 'degree': 27},
        'own_signs': ['Taurus', 'Libra'],
        'moolatrikona': {'sign': 'Libra', 'start': 0, 'end': 15},
        'friends': ['Mercury', 'Saturn'],
        'enemies': ['Sun', 'Moon'],
        'neutral': ['Mars', 'Jupiter'],
        'dasha_years': 20,
        'karaka': 'marriage, love, arts, luxury, vehicles, spouse',
        'body_parts': 'reproductive organs, face, eyes',
        'diseases': 'reproductive disorders, kidney problems, diabetes',
        'description': 'Shukra is charming, splendorous physique, excellent disposition, charming eyes, poet, phlegmatic and windy, curly hair.',
        'reference': 'BPHS Ch. 3, Slokas 28'
    },
    'Saturn': {
        'sanskrit_name': 'Shani',
        'nature': 'malefic',
        'gender': 'neuter',
        'caste': 'Shudra',
        'guna': 'Tamasic',
        'element': 'air',
        'deity': 'Brahma',
        'day': 'Saturday',
        'direction': 'West',
        'color': 'dark/black',
        'gem': 'Blue Sapphire',
        'metal': 'iron',
        'taste': 'astringent',
        'dhatu': 'muscles',
        'exaltation': {'sign': 'Libra', 'degree': 20},
        'debilitation': {'sign': 'Aries', 'degree': 20},
        'own_signs': ['Capricorn', 'Aquarius'],
        'moolatrikona': {'sign': 'Aquarius', 'start': 0, 'end': 20},
        'friends': ['Mercury', 'Venus'],
        'enemies': ['Sun', 'Moon', 'Mars'],
        'neutral': ['Jupiter'],
        'dasha_years': 19,
        'karaka': 'longevity, death, grief, discipline, servants, obstacles',
        'body_parts': 'legs, joints, nerves',
        'diseases': 'chronic diseases, arthritis, paralysis, delays',
        'description': 'Shani has emaciated and long physique, tawny eyes, windy temperament, big teeth, indolent, lame, coarse hair.',
        'reference': 'BPHS Ch. 3, Slokas 29'
    },
    'Rahu': {
        'sanskrit_name': 'Rahu',
        'nature': 'malefic',
        'gender': 'neuter',
        'caste': 'outcaste',
        'guna': 'Tamasic',
        'element': 'air',
        'deity': None,
        'day': None,
        'direction': 'South-West',
        'color': 'smoky/blue',
        'gem': 'Hessonite',
        'metal': 'lead',
        'taste': None,
        'dhatu': None,
        'exaltation': {'sign': 'Taurus', 'degree': None},
        'debilitation': {'sign': 'Scorpio', 'degree': None},
        'own_signs': ['Aquarius'],  # Some texts say Virgo
        'moolatrikona': None,
        'friends': ['Mercury', 'Venus', 'Saturn'],
        'enemies': ['Sun', 'Moon', 'Mars'],
        'neutral': ['Jupiter'],
        'dasha_years': 18,
        'karaka': 'obsession, foreign, sudden events, illusion, confusion',
        'body_parts': 'head',
        'diseases': 'mysterious diseases, poisoning, insanity',
        'description': 'Rahu has smoky appearance with blue mix physique, resides in forests, horrible, windy temperament, intelligent.',
        'reference': 'BPHS Ch. 3, Slokas 30'
    },
    'Ketu': {
        'sanskrit_name': 'Ketu',
        'nature': 'malefic',
        'gender': 'neuter',
        'caste': 'mixed',
        'guna': 'Tamasic',
        'element': 'fire',
        'deity': None,
        'day': None,
        'direction': 'North-West',
        'color': 'smoky',
        'gem': 'Cat\'s Eye',
        'metal': 'lead',
        'taste': None,
        'dhatu': None,
        'exaltation': {'sign': 'Scorpio', 'degree': None},
        'debilitation': {'sign': 'Taurus', 'degree': None},
        'own_signs': ['Scorpio'],  # Some texts say Pisces
        'moolatrikona': None,
        'friends': ['Mars', 'Venus', 'Saturn'],
        'enemies': ['Sun', 'Moon'],
        'neutral': ['Mercury', 'Jupiter'],
        'dasha_years': 7,
        'karaka': 'spirituality, moksha, detachment, past karma',
        'body_parts': 'feet',
        'diseases': 'mysterious diseases, wounds, surgery',
        'description': 'Ketu is akin to Rahu in appearance.',
        'reference': 'BPHS Ch. 3, Slokas 30'
    }
}

# Natural relationships as per BPHS Ch. 3, Slokas 55-58
PLANET_RELATIONSHIPS = {
    'natural': {
        'Sun': {'friends': ['Moon', 'Mars', 'Jupiter'], 'enemies': ['Venus', 'Saturn'], 'neutral': ['Mercury']},
        'Moon': {'friends': ['Sun', 'Mercury'], 'enemies': [], 'neutral': ['Mars', 'Jupiter', 'Venus', 'Saturn']},
        'Mars': {'friends': ['Sun', 'Moon', 'Jupiter'], 'enemies': ['Mercury'], 'neutral': ['Venus', 'Saturn']},
        'Mercury': {'friends': ['Sun', 'Venus'], 'enemies': ['Moon'], 'neutral': ['Mars', 'Jupiter', 'Saturn']},
        'Jupiter': {'friends': ['Sun', 'Moon', 'Mars'], 'enemies': ['Mercury', 'Venus'], 'neutral': ['Saturn']},
        'Venus': {'friends': ['Mercury', 'Saturn'], 'enemies': ['Sun', 'Moon'], 'neutral': ['Mars', 'Jupiter']},
        'Saturn': {'friends': ['Mercury', 'Venus'], 'enemies': ['Sun', 'Moon', 'Mars'], 'neutral': ['Jupiter']},
        'Rahu': {'friends': ['Mercury', 'Venus', 'Saturn'], 'enemies': ['Sun', 'Moon', 'Mars'], 'neutral': ['Jupiter']},
        'Ketu': {'friends': ['Mars', 'Venus', 'Saturn'], 'enemies': ['Sun', 'Moon'], 'neutral': ['Mercury', 'Jupiter']}
    },
    # Temporary relationships are calculated based on positions (2,3,4,10,11,12 = friend; rest = enemy)
    'temporary_friend_houses': [2, 3, 4, 10, 11, 12],
    'compound_relationships': {
        # natural_friend + temporary_friend = great_friend
        # natural_friend + temporary_enemy = neutral
        # natural_neutral + temporary_friend = friend
        # natural_neutral + temporary_enemy = enemy
        # natural_enemy + temporary_friend = neutral
        # natural_enemy + temporary_enemy = great_enemy
    }
}

# ============================================
# PLANET CABINET - BPHS Ch. 3, Slokas 14-15
# ============================================
PLANET_CABINET = {
    'Sun': {'role': 'King', 'description': 'Royal status'},
    'Moon': {'role': 'Queen', 'description': 'Royal status'},
    'Mars': {'role': 'Army Chief', 'description': 'Commander of armed forces'},
    'Mercury': {'role': 'Crown Prince', 'description': 'Prince-apparent'},
    'Jupiter': {'role': 'Minister', 'description': 'Ministerial grah'},
    'Venus': {'role': 'Minister', 'description': 'Ministerial grah'},
    'Saturn': {'role': 'Servant', 'description': 'Servile grah'},
    'Rahu': {'role': 'Army', 'description': 'Part of grah army'},
    'Ketu': {'role': 'Army', 'description': 'Part of grah army'}
}

# ============================================
# PLANET ABODES - BPHS Ch. 3, Sloka 32
# ============================================
PLANET_ABODES = {
    'Sun': 'Temple',
    'Moon': 'Watery place',
    'Mars': 'Place of fire',
    'Mercury': 'Sport-ground/Playground',
    'Jupiter': 'Treasure-house',
    'Venus': 'Bed-room',
    'Saturn': 'Filthy ground/Dirty places'
}

# ============================================
# PLANET TIME PERIODS - BPHS Ch. 3, Sloka 33
# ============================================
PLANET_PERIODS = {
    'Sun': 'Ayan (6 months)',
    'Moon': 'Muhurta (48 minutes)',
    'Mars': 'A day (day and night)',
    'Mercury': 'Ritu (2 months/season)',
    'Jupiter': 'Month',
    'Venus': 'Fortnight (Paksha)',
    'Saturn': 'Year'
}

# ============================================
# PLANET TREE ASSOCIATIONS - BPHS Ch. 3, Slokas 39-40
# ============================================
PLANET_TREES = {
    'Sun': 'Strong trees (with stout trunks)',
    'Moon': 'Milky trees (rubber yielding plants)',
    'Mars': 'Bitter trees (like lemon plants)',
    'Mercury': 'Fruitless trees',
    'Jupiter': 'Fruitful trees',
    'Venus': 'Floral plants',
    'Saturn': 'Useless trees'
}

# ============================================
# PLANET ROBES/CLOTHES - BPHS Ch. 3, Slokas 41-44
# ============================================
PLANET_ROBES = {
    'Sun': 'Red silken',
    'Moon': 'White silken',
    'Mars': 'Red',
    'Mercury': 'Black silken',
    'Jupiter': 'Saffron',
    'Venus': 'Silken',
    'Saturn': 'Multi-coloured',
    'Rahu': 'Multi-coloured clothes',
    'Ketu': 'Rags'
}

# ============================================
# DHATU, MOOL, JIVA DIVISIONS - BPHS Ch. 3, Sloka 47
# ============================================
PLANET_CLASSIFICATIONS = {
    'dhatu': ['Rahu', 'Mars', 'Saturn', 'Moon'],  # Minerals
    'moola': ['Sun', 'Venus'],                     # Vegetables
    'jiva': ['Mercury', 'Jupiter', 'Ketu']         # Living beings
}

# ============================================
# PLANET SEASONS - BPHS Ch. 3, Slokas 45-46
# ============================================
PLANET_SEASONS = {
    'Venus': 'Vasanta (Spring)',
    'Mars': 'Greeshma (Summer)',
    'Moon': 'Varsha (Rainy)',
    'Mercury': 'Sharad (Autumn)',
    'Jupiter': 'Hemanta (Pre-winter)',
    'Saturn': 'Shishir (Winter)',
    'Rahu': '8 months period',
    'Ketu': '3 months period'
}

# Planet strengths based on placement (BPHS Ch. 3, Slokas 59-60)
PLANET_STRENGTH_RATIOS = {
    'exaltation': 1.0,        # Full strength
    'moolatrikona': 0.75,     # Three-fourths
    'own_sign': 0.50,         # Half
    'friend_sign': 0.25,      # One-fourth
    'neutral_sign': 0.125,    # One-eighth
    'enemy_sign': 0.0,        # Nil
    'debilitation': 0.0       # Nil
}

# ============================================
# DIRECTIONAL STRENGTHS - BPHS Ch. 3, Slokas 35-38
# ============================================
DIRECTIONAL_STRENGTHS = {
    'Sun': {
        'strong_direction': 'South',
        'strong_house': 10,
        'dig_bala_house': 10,
        'description': 'Sun is strong in the South (10th house)'
    },
    'Moon': {
        'strong_direction': 'North',
        'strong_house': 4,
        'dig_bala_house': 4,
        'description': 'Moon is strong in the North (4th house)'
    },
    'Mars': {
        'strong_direction': 'South',
        'strong_house': 10,
        'dig_bala_house': 10,
        'description': 'Mars is strong in the South (10th house)'
    },
    'Mercury': {
        'strong_direction': 'East',
        'strong_house': 1,
        'dig_bala_house': 1,
        'description': 'Mercury is strong in the East (1st house/Lagna)'
    },
    'Jupiter': {
        'strong_direction': 'East',
        'strong_house': 1,
        'dig_bala_house': 1,
        'description': 'Jupiter is strong in the East (1st house/Lagna)'
    },
    'Venus': {
        'strong_direction': 'North',
        'strong_house': 4,
        'dig_bala_house': 4,
        'description': 'Venus is strong in the North (4th house)'
    },
    'Saturn': {
        'strong_direction': 'West',
        'strong_house': 7,
        'dig_bala_house': 7,
        'description': 'Saturn is strong in the West (7th house)'
    },
    'Rahu': {
        'strong_direction': 'South-West',
        'strong_house': None,
        'dig_bala_house': None,
        'description': 'Rahu has no specific dig bala'
    },
    'Ketu': {
        'strong_direction': 'North-West',
        'strong_house': None,
        'dig_bala_house': None,
        'description': 'Ketu has no specific dig bala'
    }
}

# ============================================
# TIME-BASED STRENGTHS - BPHS Ch. 3, Slokas 35-38
# ============================================
TIME_STRENGTHS = {
    # Planets strong during day
    'day_strong': ['Sun', 'Jupiter', 'Venus'],
    # Planets strong during night
    'night_strong': ['Moon', 'Mars', 'Saturn'],
    # Mercury is always strong (day and night)
    'always_strong': ['Mercury'],
    # Benefics strong in Shukla Paksha (bright half)
    'bright_half_strong': ['Moon', 'Mercury', 'Jupiter', 'Venus'],
    # Malefics strong in Krishna Paksha (dark half)
    'dark_half_strong': ['Sun', 'Mars', 'Saturn', 'Rahu', 'Ketu'],
    # Benefics strong in Uttarayana (Sun moving North)
    'uttarayana_strong': ['Moon', 'Mercury', 'Jupiter', 'Venus'],
    # Malefics strong in Dakshinayana (Sun moving South)
    'dakshinayana_strong': ['Sun', 'Mars', 'Saturn', 'Rahu', 'Ketu']
}

# ============================================
# NATURAL STRENGTH ORDER - BPHS Ch. 3, Sloka 38
# ============================================
NATURAL_STRENGTH_ORDER = {
    # Stronger in ascending order (weakest to strongest)
    'ascending_order': ['Saturn', 'Mars', 'Mercury', 'Jupiter', 'Venus', 'Moon', 'Sun'],
    'description': 'Saturn is weakest, Sun is strongest in natural strength'
}

# ============================================
# BENEFIC/MALEFIC STRENGTH ORDER - BPHS Ch. 3, Slokas 8-10
# ============================================
BENEFIC_STRENGTH_ORDER = ['Full Moon', 'Mercury', 'Jupiter', 'Venus']
MALEFIC_STRENGTH_ORDER = ['Weak Moon', 'Sun', 'Saturn', 'Mars']

# ============================================
# COMBUSTION RULES
# ============================================
COMBUSTION_ORBS = {
    'Moon': 12,      # Degrees from Sun
    'Mars': 17,
    'Mercury': 14,   # 12 when retrograde
    'Jupiter': 11,
    'Venus': 10,     # 8 when retrograde
    'Saturn': 15
}
