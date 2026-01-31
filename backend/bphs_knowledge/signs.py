# BPHS Chapter 4: Zodiacal Rashis Described
# Complete sign characteristics from Brihat Parashara Hora Shastra

SIGNS = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 
         'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']

SIGN_CHARACTERISTICS = {
    'Aries': {
        'sanskrit_name': 'Mesha',
        'number': 1,
        'lord': 'Mars',
        'element': 'fire',
        'quality': 'movable',
        'gender': 'male',
        'nature': 'malefic',
        'direction': 'East',
        'body_part': 'head',
        'rising_type': 'prishtodaya',  # rises from back
        'humor': 'bilious',
        'caste': 'Kshatriya',
        'description': 'Represents the head of Kaal Purusha',
        'reference': 'BPHS Ch. 4'
    },
    'Taurus': {
        'sanskrit_name': 'Vrishabha',
        'number': 2,
        'lord': 'Venus',
        'element': 'earth',
        'quality': 'fixed',
        'gender': 'female',
        'nature': 'benefic',
        'direction': 'South',
        'body_part': 'face',
        'rising_type': 'prishtodaya',
        'humor': 'windy',
        'caste': 'Vaishya',
        'description': 'Represents the face of Kaal Purusha',
        'reference': 'BPHS Ch. 4'
    },
    'Gemini': {
        'sanskrit_name': 'Mithuna',
        'number': 3,
        'lord': 'Mercury',
        'element': 'air',
        'quality': 'dual',
        'gender': 'male',
        'nature': 'benefic',
        'direction': 'West',
        'body_part': 'arms',
        'rising_type': 'shirshodaya',  # rises from head
        'humor': 'mixed',
        'caste': 'Shudra',
        'description': 'Represents the arms of Kaal Purusha',
        'reference': 'BPHS Ch. 4'
    },
    'Cancer': {
        'sanskrit_name': 'Karka',
        'number': 4,
        'lord': 'Moon',
        'element': 'water',
        'quality': 'movable',
        'gender': 'female',
        'nature': 'benefic',
        'direction': 'North',
        'body_part': 'heart',
        'rising_type': 'prishtodaya',
        'humor': 'phlegmatic',
        'caste': 'Brahmin',
        'description': 'Represents the heart of Kaal Purusha',
        'reference': 'BPHS Ch. 4'
    },
    'Leo': {
        'sanskrit_name': 'Simha',
        'number': 5,
        'lord': 'Sun',
        'element': 'fire',
        'quality': 'fixed',
        'gender': 'male',
        'nature': 'malefic',
        'direction': 'East',
        'body_part': 'stomach',
        'rising_type': 'shirshodaya',
        'humor': 'bilious',
        'caste': 'Kshatriya',
        'description': 'Represents the stomach of Kaal Purusha',
        'reference': 'BPHS Ch. 4'
    },
    'Virgo': {
        'sanskrit_name': 'Kanya',
        'number': 6,
        'lord': 'Mercury',
        'element': 'earth',
        'quality': 'dual',
        'gender': 'female',
        'nature': 'benefic',
        'direction': 'South',
        'body_part': 'hip',
        'rising_type': 'shirshodaya',
        'humor': 'windy',
        'caste': 'Vaishya',
        'description': 'Represents the hip of Kaal Purusha',
        'reference': 'BPHS Ch. 4'
    },
    'Libra': {
        'sanskrit_name': 'Tula',
        'number': 7,
        'lord': 'Venus',
        'element': 'air',
        'quality': 'movable',
        'gender': 'male',
        'nature': 'benefic',
        'direction': 'West',
        'body_part': 'space below navel',
        'rising_type': 'shirshodaya',
        'humor': 'mixed',
        'caste': 'Shudra',
        'description': 'Represents the space below navel of Kaal Purusha',
        'reference': 'BPHS Ch. 4'
    },
    'Scorpio': {
        'sanskrit_name': 'Vrischika',
        'number': 8,
        'lord': 'Mars',
        'element': 'water',
        'quality': 'fixed',
        'gender': 'female',
        'nature': 'malefic',
        'direction': 'North',
        'body_part': 'privities',
        'rising_type': 'prishtodaya',
        'humor': 'phlegmatic',
        'caste': 'Brahmin',
        'description': 'Represents the privities of Kaal Purusha',
        'reference': 'BPHS Ch. 4'
    },
    'Sagittarius': {
        'sanskrit_name': 'Dhanu',
        'number': 9,
        'lord': 'Jupiter',
        'element': 'fire',
        'quality': 'dual',
        'gender': 'male',
        'nature': 'benefic',
        'direction': 'East',
        'body_part': 'thighs',
        'rising_type': 'prishtodaya',
        'humor': 'bilious',
        'caste': 'Kshatriya',
        'description': 'Represents the thighs of Kaal Purusha',
        'reference': 'BPHS Ch. 4'
    },
    'Capricorn': {
        'sanskrit_name': 'Makara',
        'number': 10,
        'lord': 'Saturn',
        'element': 'earth',
        'quality': 'movable',
        'gender': 'female',
        'nature': 'malefic',
        'direction': 'South',
        'body_part': 'knees',
        'rising_type': 'prishtodaya',
        'humor': 'windy',
        'caste': 'Vaishya',
        'description': 'Represents the knees of Kaal Purusha',
        'reference': 'BPHS Ch. 4'
    },
    'Aquarius': {
        'sanskrit_name': 'Kumbha',
        'number': 11,
        'lord': 'Saturn',
        'element': 'air',
        'quality': 'fixed',
        'gender': 'male',
        'nature': 'malefic',
        'direction': 'West',
        'body_part': 'ankles',
        'rising_type': 'shirshodaya',
        'humor': 'mixed',
        'caste': 'Shudra',
        'description': 'Represents the ankles of Kaal Purusha',
        'reference': 'BPHS Ch. 4'
    },
    'Pisces': {
        'sanskrit_name': 'Meena',
        'number': 12,
        'lord': 'Jupiter',
        'element': 'water',
        'quality': 'dual',
        'gender': 'female',
        'nature': 'benefic',
        'direction': 'North',
        'body_part': 'feet',
        'rising_type': 'ubhayodaya',  # rises from both
        'humor': 'phlegmatic',
        'caste': 'Brahmin',
        'description': 'Represents the feet of Kaal Purusha',
        'reference': 'BPHS Ch. 4'
    }
}

# Sign classifications
SIGN_CLASSIFICATIONS = {
    'movable': ['Aries', 'Cancer', 'Libra', 'Capricorn'],      # Chara
    'fixed': ['Taurus', 'Leo', 'Scorpio', 'Aquarius'],         # Sthira
    'dual': ['Gemini', 'Virgo', 'Sagittarius', 'Pisces'],      # Dwiswabhava
    
    'fire': ['Aries', 'Leo', 'Sagittarius'],
    'earth': ['Taurus', 'Virgo', 'Capricorn'],
    'air': ['Gemini', 'Libra', 'Aquarius'],
    'water': ['Cancer', 'Scorpio', 'Pisces'],
    
    'odd': ['Aries', 'Gemini', 'Leo', 'Libra', 'Sagittarius', 'Aquarius'],
    'even': ['Taurus', 'Cancer', 'Virgo', 'Scorpio', 'Capricorn', 'Pisces'],
    
    'male': ['Aries', 'Gemini', 'Leo', 'Libra', 'Sagittarius', 'Aquarius'],
    'female': ['Taurus', 'Cancer', 'Virgo', 'Scorpio', 'Capricorn', 'Pisces'],
    
    'shirshodaya': ['Gemini', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Aquarius'],  # rises from head
    'prishtodaya': ['Aries', 'Taurus', 'Cancer', 'Sagittarius', 'Capricorn'],   # rises from back
    'ubhayodaya': ['Pisces']  # rises from both
}

# Sign aspects (Rashi Drishti) - BPHS Ch. 8
SIGN_ASPECTS = {
    'movable': {
        'aspects': ['fixed'],  # Movable signs aspect all fixed signs except adjacent
        'except_adjacent': True
    },
    'fixed': {
        'aspects': ['movable'],  # Fixed signs aspect all movable signs except adjacent
        'except_adjacent': True
    },
    'dual': {
        'aspects': ['dual'],  # Dual signs aspect other dual signs
        'except_adjacent': False
    }
}
