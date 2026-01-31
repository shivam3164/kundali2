# BPHS Chapter 3: Nakshatras (Lunar Mansions)
# 27 Nakshatras as described in Brihat Parashara Hora Shastra

NAKSHATRAS = [
    'Ashwini', 'Bharani', 'Krittika', 'Rohini', 'Mrigashira', 'Ardra',
    'Punarvasu', 'Pushya', 'Ashlesha', 'Magha', 'Purva Phalguni', 'Uttara Phalguni',
    'Hasta', 'Chitra', 'Swati', 'Vishakha', 'Anuradha', 'Jyeshtha',
    'Mula', 'Purva Ashadha', 'Uttara Ashadha', 'Shravana', 'Dhanishta', 'Shatabhisha',
    'Purva Bhadrapada', 'Uttara Bhadrapada', 'Revati'
]

# Nakshatra lords for Vimshottari Dasha (BPHS Ch. 46)
NAKSHATRA_LORDS = {
    'Ashwini': {'lord': 'Ketu', 'deity': 'Ashwini Kumars', 'span': (0, 13.333333)},
    'Bharani': {'lord': 'Venus', 'deity': 'Yama', 'span': (13.333333, 26.666667)},
    'Krittika': {'lord': 'Sun', 'deity': 'Agni', 'span': (26.666667, 40)},
    'Rohini': {'lord': 'Moon', 'deity': 'Brahma', 'span': (40, 53.333333)},
    'Mrigashira': {'lord': 'Mars', 'deity': 'Chandra', 'span': (53.333333, 66.666667)},
    'Ardra': {'lord': 'Rahu', 'deity': 'Rudra', 'span': (66.666667, 80)},
    'Punarvasu': {'lord': 'Jupiter', 'deity': 'Aditi', 'span': (80, 93.333333)},
    'Pushya': {'lord': 'Saturn', 'deity': 'Brihaspati', 'span': (93.333333, 106.666667)},
    'Ashlesha': {'lord': 'Mercury', 'deity': 'Sarpa', 'span': (106.666667, 120)},
    'Magha': {'lord': 'Ketu', 'deity': 'Pitris', 'span': (120, 133.333333)},
    'Purva Phalguni': {'lord': 'Venus', 'deity': 'Bhaga', 'span': (133.333333, 146.666667)},
    'Uttara Phalguni': {'lord': 'Sun', 'deity': 'Aryaman', 'span': (146.666667, 160)},
    'Hasta': {'lord': 'Moon', 'deity': 'Surya', 'span': (160, 173.333333)},
    'Chitra': {'lord': 'Mars', 'deity': 'Tvashtar', 'span': (173.333333, 186.666667)},
    'Swati': {'lord': 'Rahu', 'deity': 'Vayu', 'span': (186.666667, 200)},
    'Vishakha': {'lord': 'Jupiter', 'deity': 'Indra-Agni', 'span': (200, 213.333333)},
    'Anuradha': {'lord': 'Saturn', 'deity': 'Mitra', 'span': (213.333333, 226.666667)},
    'Jyeshtha': {'lord': 'Mercury', 'deity': 'Indra', 'span': (226.666667, 240)},
    'Mula': {'lord': 'Ketu', 'deity': 'Nirrti', 'span': (240, 253.333333)},
    'Purva Ashadha': {'lord': 'Venus', 'deity': 'Apas', 'span': (253.333333, 266.666667)},
    'Uttara Ashadha': {'lord': 'Sun', 'deity': 'Vishvadevas', 'span': (266.666667, 280)},
    'Shravana': {'lord': 'Moon', 'deity': 'Vishnu', 'span': (280, 293.333333)},
    'Dhanishta': {'lord': 'Mars', 'deity': 'Vasus', 'span': (293.333333, 306.666667)},
    'Shatabhisha': {'lord': 'Rahu', 'deity': 'Varuna', 'span': (306.666667, 320)},
    'Purva Bhadrapada': {'lord': 'Jupiter', 'deity': 'Ajaikapada', 'span': (320, 333.333333)},
    'Uttara Bhadrapada': {'lord': 'Saturn', 'deity': 'Ahirbudhnya', 'span': (333.333333, 346.666667)},
    'Revati': {'lord': 'Mercury', 'deity': 'Pushan', 'span': (346.666667, 360)}
}

# Vimshottari Dasha sequence and years (BPHS Ch. 46)
VIMSHOTTARI_SEQUENCE = [
    ('Ketu', 7),
    ('Venus', 20),
    ('Sun', 6),
    ('Moon', 10),
    ('Mars', 7),
    ('Rahu', 18),
    ('Jupiter', 16),
    ('Saturn', 19),
    ('Mercury', 17)
]

# Nakshatra-based classifications
NAKSHATRA_CLASSIFICATIONS = {
    # Ganas (Temperaments)
    'deva': ['Ashwini', 'Mrigashira', 'Punarvasu', 'Pushya', 'Hasta', 'Swati', 
             'Anuradha', 'Shravana', 'Revati'],
    'manushya': ['Bharani', 'Rohini', 'Ardra', 'Purva Phalguni', 'Uttara Phalguni',
                 'Purva Ashadha', 'Uttara Ashadha', 'Purva Bhadrapada', 'Uttara Bhadrapada'],
    'rakshasa': ['Krittika', 'Ashlesha', 'Magha', 'Chitra', 'Vishakha', 'Jyeshtha',
                 'Mula', 'Dhanishta', 'Shatabhisha'],
    
    # Yonis (Animal symbols for compatibility)
    'horse': ['Ashwini', 'Shatabhisha'],
    'elephant': ['Bharani', 'Revati'],
    'sheep': ['Krittika', 'Pushya'],
    'serpent': ['Rohini', 'Mrigashira'],
    'dog': ['Mula', 'Ardra'],
    'cat': ['Punarvasu', 'Ashlesha'],
    'rat': ['Magha', 'Purva Phalguni'],
    'cow': ['Uttara Phalguni', 'Uttara Bhadrapada'],
    'buffalo': ['Hasta', 'Swati'],
    'tiger': ['Chitra', 'Vishakha'],
    'deer': ['Anuradha', 'Jyeshtha'],
    'monkey': ['Purva Ashadha', 'Shravana'],
    'mongoose': ['Uttara Ashadha'],
    'lion': ['Dhanishta', 'Purva Bhadrapada'],
}

# Taras (Stars) for Vipat, Pratyak, Vadh calculation
TARA_POSITIONS = {
    'janma': 1,      # Birth star
    'sampat': 2,     # Wealth
    'vipat': 3,      # Danger
    'kshema': 4,     # Well-being
    'pratyak': 5,    # Obstacles
    'sadhana': 6,    # Achievement
    'vadha': 7,      # Death
    'mitra': 8,      # Friend
    'parama_mitra': 9  # Great friend
}

def get_nakshatra_from_longitude(longitude):
    """Get nakshatra name and pada from Moon's longitude"""
    nakshatra_span = 360 / 27  # 13.333... degrees per nakshatra
    pada_span = nakshatra_span / 4  # 3.333... degrees per pada
    
    nakshatra_index = int(longitude // nakshatra_span)
    pada = int((longitude % nakshatra_span) // pada_span) + 1
    
    nakshatra_name = NAKSHATRAS[nakshatra_index]
    return {
        'name': nakshatra_name,
        'index': nakshatra_index + 1,
        'pada': pada,
        'lord': NAKSHATRA_LORDS[nakshatra_name]['lord'],
        'deity': NAKSHATRA_LORDS[nakshatra_name]['deity']
    }
