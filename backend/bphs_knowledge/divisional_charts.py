# BPHS Divisional Charts (Vargas)
# From Brihat Parashara Hora Shastra Chapter 6-7

"""
Shodashvarga (16 Divisional Charts) from BPHS
These charts are used to analyze specific areas of life
"""

# ============================================
# VARGA DEFINITIONS - BPHS Ch. 6
# ============================================

SHODASHVARGA = {
    'D1': {
        'name': 'Rashi (Natal Chart)',
        'sanskrit': 'Rashi',
        'division': 1,
        'area': 'Physical body, overall life, physique',
        'vimshopak_points': {
            'shadvarga': 6,
            'saptvarga': 5,
            'dashvarga': 3,
            'shodashvarga': 3.5
        },
        'source': 'BPHS Ch. 6, Sloka 5'
    },
    'D2': {
        'name': 'Hora',
        'sanskrit': 'Hora',
        'division': 2,
        'calculation': 'First half of odd sign = Sun Hora, Second half = Moon Hora. Reverse for even signs.',
        'area': 'Wealth, financial prosperity',
        'vimshopak_points': {
            'shadvarga': 2,
            'saptvarga': 2,
            'dashvarga': 1.5,
            'shodashvarga': 1
        },
        'source': 'BPHS Ch. 6, Sloka 5-6'
    },
    'D3': {
        'name': 'Drekkana',
        'sanskrit': 'Dreshkana',
        'division': 3,
        'calculation': '1st decanate: same sign, 2nd: 5th sign, 3rd: 9th sign from it',
        'area': 'Siblings, courage, valor, short journeys',
        'deities': ['Narada', 'Agastya', 'Durvasa'],
        'vimshopak_points': {
            'shadvarga': 4,
            'saptvarga': 3,
            'dashvarga': 1.5,
            'shodashvarga': 1
        },
        'source': 'BPHS Ch. 6, Sloka 7-8'
    },
    'D4': {
        'name': 'Chaturthamsha',
        'sanskrit': 'Turyamsha',
        'division': 4,
        'calculation': 'Lords of 4 Kendras from the sign become D4 lords',
        'area': 'Fortune, property, fixed assets, home',
        'deities': ['Sanaka', 'Sananda', 'Kumara', 'Sanatana'],
        'vimshopak_points': {
            'dashvarga': 1.5,
            'shodashvarga': 0.5
        },
        'source': 'BPHS Ch. 6, Sloka 9'
    },
    'D7': {
        'name': 'Saptamsha',
        'sanskrit': 'Saptamsha',
        'division': 7,
        'calculation': 'For odd signs: count from same sign. For even signs: count from 7th sign.',
        'area': 'Children, progeny, creative intelligence',
        'divisions': ['Kshara', 'Ksheera', 'Dadhi', 'Ghrita', 'Ikshu', 'Rasa', 'Suddha Jala'],
        'vimshopak_points': {
            'saptvarga': 2.5,
            'dashvarga': 1.5,
            'shodashvarga': 0.5
        },
        'source': 'BPHS Ch. 6, Sloka 10-11'
    },
    'D9': {
        'name': 'Navamsha',
        'sanskrit': 'Navamsha',
        'division': 9,
        'calculation': 'Movable sign: from Aries, Fixed: from 9th, Dual: from 5th',
        'area': 'Marriage, spouse, dharma, overall fortune, soul purpose',
        'designations': ['Deva', 'Manushya', 'Rakshasa'],
        'vimshopak_points': {
            'shadvarga': 5,
            'saptvarga': 4.5,
            'dashvarga': 1.5,
            'shodashvarga': 3
        },
        'source': 'BPHS Ch. 6, Sloka 12'
    },
    'D10': {
        'name': 'Dashamsha',
        'sanskrit': 'Dashamsha',
        'division': 10,
        'calculation': 'For odd signs: from same sign. For even signs: from 9th sign.',
        'area': 'Career, profession, power, authority',
        'deities': ['Indra', 'Agni', 'Yama', 'Rakshasa', 'Varuna', 'Vayu', 'Kubera', 'Ishana', 'Brahma', 'Ananta'],
        'vimshopak_points': {
            'dashvarga': 1.5,
            'shodashvarga': 0.5
        },
        'source': 'BPHS Ch. 6, Sloka 13-14'
    },
    'D12': {
        'name': 'Dvadashamsha',
        'sanskrit': 'Dvadashamsha',
        'division': 12,
        'calculation': 'Count from same sign (1st part = same sign, 2nd = next, etc.)',
        'area': 'Parents, ancestors, lineage',
        'deities': ['Ganesha', 'Ashwini Kumar', 'Yama', 'Sarpa'] * 3,
        'vimshopak_points': {
            'shadvarga': 2,
            'saptvarga': 2,
            'dashvarga': 1.5,
            'shodashvarga': 0.5
        },
        'source': 'BPHS Ch. 6, Sloka 15'
    },
    'D16': {
        'name': 'Shodashamsha',
        'sanskrit': 'Kalamsha',
        'division': 16,
        'calculation': 'Movable: from Aries, Fixed: from Leo, Dual: from Sagittarius',
        'area': 'Vehicles, conveyances, comforts, luxuries',
        'deities': ['Brahma', 'Vishnu', 'Shiva', 'Surya'] * 4,
        'vimshopak_points': {
            'dashvarga': 1.5,
            'shodashvarga': 2
        },
        'source': 'BPHS Ch. 6, Sloka 16'
    },
    'D20': {
        'name': 'Vimshamsha',
        'sanskrit': 'Vimshamsha',
        'division': 20,
        'calculation': 'Movable: from Aries, Fixed: from Sagittarius, Dual: from Leo',
        'area': 'Spiritual life, worship, religious inclinations',
        'deities_odd': ['Kali', 'Gauri', 'Jaya', 'Lakshmi', 'Vijaya', 'Vimala', 'Sati', 'Tara', 'Jvalamukhi', 'Sveta', 'Lalita', 'Bagalamukhi', 'Pratyangira', 'Shachi', 'Raudri', 'Bhavani', 'Varada', 'Jaya', 'Tripura', 'Sumukhi'],
        'vimshopak_points': {
            'shodashvarga': 0.5
        },
        'source': 'BPHS Ch. 6, Sloka 17-21'
    },
    'D24': {
        'name': 'Chaturvimshamsha',
        'sanskrit': 'Chaturvimshamsha',
        'division': 24,
        'calculation': 'For odd signs: from Leo. For even signs: from Cancer.',
        'area': 'Education, learning, academic achievements',
        'deities': ['Skanda', 'Parashudhara', 'Anala', 'Vishwakarma', 'Bhaga', 'Mitra', 'Maya', 'Antaka', 'Vrishadhvaja', 'Govinda', 'Madana', 'Bhima'] * 2,
        'vimshopak_points': {
            'shodashvarga': 0.5
        },
        'source': 'BPHS Ch. 6, Sloka 22-23'
    },
    'D27': {
        'name': 'Saptavimshamsha',
        'sanskrit': 'Nakshatramsha / Bhamsha',
        'division': 27,
        'calculation': 'All signs start from Aries, one Nakshatra per division',
        'area': 'General strength, physical constitution',
        'deities': 'Lords of 27 Nakshatras',
        'vimshopak_points': {
            'shodashvarga': 0.5
        },
        'source': 'BPHS Ch. 6, Sloka 24-26'
    },
    'D30': {
        'name': 'Trimshamsha',
        'sanskrit': 'Trimshamsha',
        'division': 30,
        'calculation': 'For odd signs: Mars 5°, Saturn 5°, Jupiter 8°, Mercury 7°, Venus 5°. Reverse for even.',
        'area': 'Misfortunes, evils, sufferings, diseases',
        'lords_odd': {'Mars': 5, 'Saturn': 5, 'Jupiter': 8, 'Mercury': 7, 'Venus': 5},
        'lords_even': {'Venus': 5, 'Mercury': 7, 'Jupiter': 8, 'Saturn': 5, 'Mars': 5},
        'vimshopak_points': {
            'shadvarga': 1,
            'saptvarga': 1,
            'shodashvarga': 0.5
        },
        'source': 'BPHS Ch. 6, Sloka 27-28'
    },
    'D40': {
        'name': 'Khavedamsha',
        'sanskrit': 'Chatvarimsamsha',
        'division': 40,
        'calculation': 'For odd signs: from Aries. For even signs: from Libra.',
        'area': 'Auspicious and inauspicious effects',
        'deities': ['Vishnu', 'Chandra', 'Marichi', 'Tvashta', 'Dhata', 'Shiva', 'Ravi', 'Yama', 'Yaksha', 'Gandharva', 'Kala', 'Varuna'] * 4,
        'vimshopak_points': {
            'shodashvarga': 0.5
        },
        'source': 'BPHS Ch. 6, Sloka 29-30'
    },
    'D45': {
        'name': 'Akshavedamsha',
        'sanskrit': 'Panchamarimsha',
        'division': 45,
        'calculation': 'Movable: from Aries, Fixed: from Leo, Dual: from Sagittarius',
        'area': 'General indications, moral character',
        'deities': ['Brahma', 'Shiva', 'Vishnu'] * 15,
        'vimshopak_points': {
            'shodashvarga': 0.5
        },
        'source': 'BPHS Ch. 6, Sloka 31-32'
    },
    'D60': {
        'name': 'Shashtiamsha',
        'sanskrit': 'Shashtiamsha',
        'division': 60,
        'calculation': 'Divide sign into 60 parts of 30\' each. Lord = sign where part falls counting from sign itself.',
        'area': 'All indications, past karma, general well-being',
        'names_odd': [
            'Ghora', 'Rakshasa', 'Deva', 'Kubera', 'Yaksha', 'Kinnara', 'Bhrashta', 'Kulaghna',
            'Garala', 'Vahni', 'Maya', 'Purishaka', 'Apampati', 'Marutwan', 'Kala', 'Sarpa',
            'Amrita', 'Indu', 'Mridu', 'Komala', 'Heramba', 'Brahma', 'Vishnu', 'Maheshwara',
            'Deva', 'Ardra', 'Kalinasa', 'Kshitisa', 'Kamalakar', 'Gulika', 'Mrityu', 'Kala',
            'Davagni', 'Ghora', 'Yama', 'Kantaka', 'Suddha', 'Amrita', 'Purnachandra', 'Vishadagdha',
            'Kulanasa', 'Vamshakshaya', 'Utpata', 'Kala', 'Saumya', 'Komala', 'Shitala', 'Karaladamstra',
            'Chandramukhi', 'Pravina', 'Kalapavaka', 'Dhannayudh', 'Nirmala', 'Saumya', 'Krura',
            'Atishitala', 'Amrita', 'Payodhi', 'Brahman', 'Chandrarekha'
        ],
        'vimshopak_points': {
            'dashvarga': 5,
            'shodashvarga': 4
        },
        'source': 'BPHS Ch. 6, Sloka 33-41'
    }
}

# ============================================
# VARGA CLASSIFICATION SCHEMES - BPHS Ch. 6
# ============================================

VARGA_CLASSIFICATIONS = {
    'shadvarga': {
        'name': 'Shadvarga (6 divisions)',
        'vargas': ['D1', 'D2', 'D3', 'D9', 'D12', 'D30'],
        'designations': {
            2: 'Kimshuka',
            3: 'Vyanjana',
            4: 'Chamara',
            5: 'Chatra',
            6: 'Kundala'
        },
        'source': 'BPHS Ch. 6, Sloka 42-53'
    },
    'saptvarga': {
        'name': 'Saptvarga (7 divisions)',
        'vargas': ['D1', 'D2', 'D3', 'D7', 'D9', 'D12', 'D30'],
        'designations': {
            2: 'Kimshuka',
            3: 'Vyanjana',
            4: 'Chamara',
            5: 'Chatra',
            6: 'Kundala',
            7: 'Mukuta'
        },
        'source': 'BPHS Ch. 6, Sloka 42-53'
    },
    'dashvarga': {
        'name': 'Dashvarga (10 divisions)',
        'vargas': ['D1', 'D2', 'D3', 'D7', 'D9', 'D10', 'D12', 'D16', 'D30', 'D60'],
        'designations': {
            2: 'Parijata',
            3: 'Uttama',
            4: 'Gopura',
            5: 'Simhasana',
            6: 'Paravata',
            7: 'Devaloka',
            8: 'Brahmaloka',
            9: 'Shakravahana',
            10: 'Shridhama'
        },
        'source': 'BPHS Ch. 6, Sloka 42-53'
    },
    'shodashvarga': {
        'name': 'Shodashvarga (16 divisions)',
        'vargas': ['D1', 'D2', 'D3', 'D4', 'D7', 'D9', 'D10', 'D12', 'D16', 'D20', 'D24', 'D27', 'D30', 'D40', 'D45', 'D60'],
        'designations': {
            2: 'Bhedaka',
            3: 'Kusuma',
            4: 'Nagapushpa',
            5: 'Kanduka',
            6: 'Kerala',
            7: 'Kalpa Vriksha',
            8: 'Chandana Vana',
            9: 'Poornachandra',
            10: 'Uchchaisrava',
            11: 'Dhanvantari',
            12: 'Suryakanta',
            13: 'Vidruma',
            14: 'Chakra Simhasana',
            15: 'Goloka',
            16: 'Shri Vallabha'
        },
        'source': 'BPHS Ch. 6, Sloka 42-53'
    }
}

# ============================================
# VIMSHOPAK BALA (20-POINT STRENGTH)
# ============================================

VIMSHOPAK_DIGNITIES = {
    'own': 20,
    'pramudit': 18,
    'shant': 15,
    'svastha': 10,
    'duhkhit': 7,
    'khal': 5
}

# ============================================
# DIVISIONAL CHART USAGE - BPHS Ch. 7
# ============================================

VARGA_USAGE = {
    'D1': 'Physical body, overall life assessment',
    'D2': 'Wealth accumulation and financial status',
    'D3': 'Siblings, courage, communication',
    'D4': 'Fortune in fixed assets, property',
    'D7': 'Children and progeny',
    'D9': 'Spouse and marriage (most important after D1)',
    'D10': 'Career, profession, and public image',
    'D12': 'Parents (father especially)',
    'D16': 'Vehicles, conveyances, happiness from luxury',
    'D20': 'Spiritual progress and worship',
    'D24': 'Education and learning',
    'D27': 'Strength and weakness analysis',
    'D30': 'Evils, misfortunes, troubles',
    'D40': 'Auspicious/inauspicious effects',
    'D45': 'General well-being',
    'D60': 'All matters (most detailed analysis)'
}

# Source reference
VARGA_SOURCE = 'BPHS Ch. 7, Sloka 1-8'
