# BPHS Dashas (Planetary Periods)
# From Brihat Parashara Hora Shastra Chapter 46

"""
Dasha Systems from BPHS
Primary focus on Vimshottari Dasha as recommended by Parasara
"""

# ============================================
# VIMSHOTTARI DASHA SYSTEM - BPHS Ch. 46
# ============================================

# Total years in Vimshottari cycle = 120 years
VIMSHOTTARI_TOTAL_YEARS = 120

# Dasha lords and their periods in years
VIMSHOTTARI_PERIODS = {
    'Ketu': 7,
    'Venus': 20,
    'Sun': 6,
    'Moon': 10,
    'Mars': 7,
    'Rahu': 18,
    'Jupiter': 16,
    'Saturn': 19,
    'Mercury': 17
}

# Dasha sequence starting from Ketu
VIMSHOTTARI_SEQUENCE = [
    'Ketu', 'Venus', 'Sun', 'Moon', 'Mars',
    'Rahu', 'Jupiter', 'Saturn', 'Mercury'
]

# Nakshatra-wise starting Dasha lord (1st Pada of each Nakshatra)
NAKSHATRA_DASHA_LORD = {
    'Ashwini': 'Ketu',
    'Bharani': 'Venus',
    'Krittika': 'Sun',
    'Rohini': 'Moon',
    'Mrigashira': 'Mars',
    'Ardra': 'Rahu',
    'Punarvasu': 'Jupiter',
    'Pushya': 'Saturn',
    'Ashlesha': 'Mercury',
    'Magha': 'Ketu',
    'Purva Phalguni': 'Venus',
    'Uttara Phalguni': 'Sun',
    'Hasta': 'Moon',
    'Chitra': 'Mars',
    'Swati': 'Rahu',
    'Vishakha': 'Jupiter',
    'Anuradha': 'Saturn',
    'Jyeshtha': 'Mercury',
    'Mula': 'Ketu',
    'Purva Ashadha': 'Venus',
    'Uttara Ashadha': 'Sun',
    'Shravana': 'Moon',
    'Dhanishta': 'Mars',
    'Shatabhisha': 'Rahu',
    'Purva Bhadrapada': 'Jupiter',
    'Uttara Bhadrapada': 'Saturn',
    'Revati': 'Mercury'
}

# ============================================
# DASHA EFFECTS - BPHS Ch. 46-60
# ============================================

MAHADASHA_EFFECTS = {
    'Sun': {
        'description': 'A period focusing on career, authority, ego, and your relationship with your father. It typically brings increased vitality and opportunities for leadership.',
        'favorable': {
            'conditions': ['exalted', 'own_sign', 'kendra', 'trikona', 'strong'],
            'effects': [
                'Acquisition of kingdom or high position',
                'Victory over enemies',
                'Gains of wealth from government',
                'Fame and recognition',
                'Success in endeavors',
                'Good health and vitality'
            ]
        },
        'unfavorable': {
            'conditions': ['debilitated', 'enemy_sign', '6th', '8th', '12th', 'combust'],
            'effects': [
                'Troubles from government',
                'Diseases related to head, eyes, heart',
                'Conflicts with father',
                'Loss of position',
                'Mental distress',
                'Wandering or travel to foreign places'
            ]
        },
        'source': 'BPHS Ch. 48'
    },
    'Moon': {
        'description': 'A time of emotional experiences, focusing on home, mother, and mental well-being. Expect fluctuations in specific moods and general outlook.',
        'favorable': {
            'conditions': ['waxing', 'exalted', 'own_sign', 'kendra', 'benefic_aspect'],
            'effects': [
                'Happiness from mother',
                'Gain of vehicles and comforts',
                'Good relations with women',
                'Prosperity in trade',
                'Mental peace',
                'Recognition and fame'
            ]
        },
        'unfavorable': {
            'conditions': ['waning', 'debilitated', 'malefic_aspect', 'weak'],
            'effects': [
                'Mental disturbances',
                'Troubles through women',
                'Problems related to water',
                'Illness of mother',
                'Financial losses',
                'Anxiety and depression'
            ]
        },
        'source': 'BPHS Ch. 49'
    },
    'Mars': {
        'description': 'A high-energy period favoring action, courage, and initiative. It brings drive but one must watch out for conflicts, impulsiveness, or accidents.',
        'favorable': {
            'conditions': ['exalted', 'own_sign', 'kendra', 'yoga_karaka', 'strong'],
            'effects': [
                'Acquisition of land and property',
                'Success in litigation',
                'Victory over enemies',
                'Gain through brothers',
                'Valor and courage recognized',
                'Physical strength and energy'
            ]
        },
        'unfavorable': {
            'conditions': ['debilitated', 'enemy_sign', '6th', '8th', '12th', 'afflicted'],
            'effects': [
                'Accidents and injuries',
                'Blood-related diseases',
                'Conflicts with brothers',
                'Legal troubles',
                'Property disputes',
                'Fevers and inflammations'
            ]
        },
        'source': 'BPHS Ch. 50'
    },
    'Mercury': {
        'description': 'Focuses on communication, business, intellect, and learning. Excellent for writing, trading, skill development, and networking.',
        'favorable': {
            'conditions': ['exalted', 'own_sign', 'kendra', 'benefic_conjunction'],
            'effects': [
                'Success in education',
                'Gains through intellect and communication',
                'Good relations with relatives',
                'Success in business and trade',
                'Writing and literary success',
                'Skill development'
            ]
        },
        'unfavorable': {
            'conditions': ['debilitated', 'malefic_conjunction', 'weak', 'combust'],
            'effects': [
                'Nervous disorders',
                'Speech problems',
                'Business losses',
                'Deception by others',
                'Skin diseases',
                'Educational obstacles'
            ]
        },
        'source': 'BPHS Ch. 51'
    },
    'Jupiter': {
        'description': 'A benevolent period for growth, learning, wisdom, progeny, and prosperity. Favorable for spiritual activities and higher education.',
        'favorable': {
            'conditions': ['exalted', 'own_sign', 'kendra', 'trikona', 'strong'],
            'effects': [
                'Spiritual growth and wisdom',
                'Birth of children',
                'Gain of wealth and prosperity',
                'Religious activities',
                'Good fortune',
                'Respect from elders and teachers'
            ]
        },
        'unfavorable': {
            'conditions': ['debilitated', 'enemy_sign', '6th', '8th', '12th'],
            'effects': [
                'Troubles with children',
                'Loss of wealth',
                'Religious conflicts',
                'Liver and digestive problems',
                'Obstruction in education',
                'Fall from grace'
            ]
        },
        'source': 'BPHS Ch. 52'
    },
    'Venus': {
        'description': 'A time for relationships, creativity, luxury, and comfort. Favors romance, marriage, artistic pursuits, and enjoyment of life pleasures.',
        'favorable': {
            'conditions': ['exalted', 'own_sign', 'kendra', 'trikona', 'strong'],
            'effects': [
                'Marriage or relationship happiness',
                'Acquisition of vehicles and luxuries',
                'Artistic success',
                'Gains through women',
                'Comforts and pleasures',
                'Financial prosperity'
            ]
        },
        'unfavorable': {
            'conditions': ['debilitated', 'enemy_sign', '6th', '8th', '12th', 'combust'],
            'effects': [
                'Marital disharmony',
                'Sexual problems',
                'Eye diseases',
                'Loss of wealth through women',
                'Kidney and reproductive issues',
                'Troubles through pleasure-seeking'
            ]
        },
        'source': 'BPHS Ch. 53'
    },
    'Saturn': {
        'description': 'A time for discipline, hard work, structure, and responsibility. Success comes through patience, perseverance, and facing reality without shortcuts.',
        'favorable': {
            'conditions': ['exalted', 'own_sign', 'yoga_karaka', 'kendra_lord', 'strong'],
            'effects': [
                'Success through hard work',
                'Gains in property and real estate',
                'Position of authority',
                'Long-term achievements',
                'Success in politics',
                'Land acquisition'
            ]
        },
        'unfavorable': {
            'conditions': ['debilitated', 'enemy_sign', '8th_lord', 'afflicted'],
            'effects': [
                'Chronic diseases',
                'Delays and obstructions',
                'Separation from family',
                'Loss of position',
                'Depression and sorrow',
                'Troubles from servants and low-caste people'
            ]
        },
        'source': 'BPHS Ch. 54'
    },
    'Rahu': {
        'description': 'A period of ambition, sudden changes, and worldly desires. Often brings execution of big plans, foreign travel, or unconventional success.',
        'favorable': {
            'conditions': ['kendra', 'trikona', 'exalted_sign', 'benefic_conjunction'],
            'effects': [
                'Sudden gains and windfalls',
                'Success in foreign lands',
                'Gains through unconventional means',
                'Technical or scientific success',
                'Rise in status',
                'Material prosperity'
            ]
        },
        'unfavorable': {
            'conditions': ['dusthana', 'malefic_conjunction', 'weak'],
            'effects': [
                'Fear and anxiety',
                'Problems from enemies',
                'Diseases difficult to diagnose',
                'Legal troubles',
                'Scandals and disgrace',
                'Troubles through lower classes'
            ]
        },
        'source': 'BPHS Ch. 55'
    },
    'Ketu': {
        'description': 'A period of detachment, spirituality, and introspection. May bring sudden breaks, unexpected events, or release from past patterns.',
        'favorable': {
            'conditions': ['benefic_conjunction', 'trikona', '12th_for_moksha'],
            'effects': [
                'Spiritual progress',
                'Liberation from worldly attachments',
                'Success in occult sciences',
                'Sudden insights',
                'Gains through ancestors',
                'Healing abilities'
            ]
        },
        'unfavorable': {
            'conditions': ['dusthana', 'malefic_conjunction', 'afflicted'],
            'effects': [
                'Accidents and injuries',
                'Mysterious diseases',
                'Separation from family',
                'Mental confusion',
                'Losses through carelessness',
                'Problems in abdomen and stomach'
            ]
        },
        'source': 'BPHS Ch. 56'
    }
}

# ============================================
# ANTARDASHA (SUB-PERIOD) CALCULATIONS
# ============================================

def calculate_antardasha_proportion(mahadasha_lord, antardasha_lord):
    """
    Calculate the proportion of Antardasha period
    Antardasha period = (Mahadasha years * Antardasha years) / 120
    """
    md_years = VIMSHOTTARI_PERIODS[mahadasha_lord]
    ad_years = VIMSHOTTARI_PERIODS[antardasha_lord]
    return (md_years * ad_years) / VIMSHOTTARI_TOTAL_YEARS

def get_antardasha_sequence(mahadasha_lord):
    """
    Get the sequence of Antardashas within a Mahadasha
    Sequence starts from Mahadasha lord itself
    """
    start_index = VIMSHOTTARI_SEQUENCE.index(mahadasha_lord)
    sequence = []
    for i in range(9):
        idx = (start_index + i) % 9
        sequence.append(VIMSHOTTARI_SEQUENCE[idx])
    return sequence

# ============================================
# PRATYANTARDASHA (SUB-SUB-PERIOD)
# ============================================

def calculate_pratyantardasha_proportion(mahadasha_lord, antardasha_lord, pratyantardasha_lord):
    """
    Calculate the proportion of Pratyantardasha period
    Pratyantardasha = (MD * AD * PD) / (120 * 120)
    """
    md_years = VIMSHOTTARI_PERIODS[mahadasha_lord]
    ad_years = VIMSHOTTARI_PERIODS[antardasha_lord]
    pd_years = VIMSHOTTARI_PERIODS[pratyantardasha_lord]
    return (md_years * ad_years * pd_years) / (VIMSHOTTARI_TOTAL_YEARS ** 2)

# ============================================
# DASHA BALANCE AT BIRTH
# ============================================

def calculate_dasha_balance(moon_longitude):
    """
    Calculate the balance of Mahadasha at birth based on Moon's position
    
    1. Find the Nakshatra from Moon's longitude
    2. Find how much of the Nakshatra has been traversed
    3. Calculate remaining Dasha period
    """
    nakshatra_span = 360 / 27  # 13.333... degrees
    nakshatra_index = int(moon_longitude // nakshatra_span)
    
    NAKSHATRAS = [
        'Ashwini', 'Bharani', 'Krittika', 'Rohini', 'Mrigashira', 'Ardra',
        'Punarvasu', 'Pushya', 'Ashlesha', 'Magha', 'Purva Phalguni', 'Uttara Phalguni',
        'Hasta', 'Chitra', 'Swati', 'Vishakha', 'Anuradha', 'Jyeshtha',
        'Mula', 'Purva Ashadha', 'Uttara Ashadha', 'Shravana', 'Dhanishta', 'Shatabhisha',
        'Purva Bhadrapada', 'Uttara Bhadrapada', 'Revati'
    ]
    
    nakshatra_name = NAKSHATRAS[nakshatra_index]
    dasha_lord = NAKSHATRA_DASHA_LORD[nakshatra_name]
    
    # Position within nakshatra (0 to 1)
    position_in_nakshatra = (moon_longitude % nakshatra_span) / nakshatra_span
    
    # Remaining portion of nakshatra
    remaining_portion = 1 - position_in_nakshatra
    
    # Balance of dasha at birth (in years)
    dasha_years = VIMSHOTTARI_PERIODS[dasha_lord]
    balance_years = remaining_portion * dasha_years
    
    return {
        'nakshatra': nakshatra_name,
        'dasha_lord': dasha_lord,
        'total_dasha_years': dasha_years,
        'balance_years': balance_years,
        'balance_months': balance_years * 12,
        'balance_days': balance_years * 365.25
    }

# ============================================
# DASHA INTERPRETATION RULES - BPHS
# ============================================

DASHA_INTERPRETATION_RULES = {
    'rule_1': {
        'description': 'Dasha lord in own sign or exaltation',
        'effects': 'Favorable results throughout the period',
        'source': 'BPHS Ch. 47'
    },
    'rule_2': {
        'description': 'Dasha lord in debilitation or enemy sign',
        'effects': 'Unfavorable results, obstacles and difficulties',
        'source': 'BPHS Ch. 47'
    },
    'rule_3': {
        'description': 'Dasha lord in Kendra (1, 4, 7, 10)',
        'effects': 'Success, recognition, achievements',
        'source': 'BPHS Ch. 47'
    },
    'rule_4': {
        'description': 'Dasha lord in Trikona (1, 5, 9)',
        'effects': 'Good fortune, spiritual growth, dharmic activities',
        'source': 'BPHS Ch. 47'
    },
    'rule_5': {
        'description': 'Dasha lord in Dusthana (6, 8, 12)',
        'effects': 'Health issues, obstacles, losses',
        'source': 'BPHS Ch. 47'
    },
    'rule_6': {
        'description': 'Dasha lord with benefics',
        'effects': 'Enhanced positive results',
        'source': 'BPHS Ch. 47'
    },
    'rule_7': {
        'description': 'Dasha lord with malefics',
        'effects': 'Reduced positive results, some negative effects',
        'source': 'BPHS Ch. 47'
    },
    'rule_8': {
        'description': 'Antardasha lord friendly to Mahadasha lord',
        'effects': 'Harmonious sub-period, good results',
        'source': 'BPHS Ch. 47'
    },
    'rule_9': {
        'description': 'Antardasha lord inimical to Mahadasha lord',
        'effects': 'Conflicting results, some difficulties',
        'source': 'BPHS Ch. 47'
    },
}

# ============================================
# PLANET RELATIONSHIPS FOR DASHA ANALYSIS
# ============================================

PLANETARY_FRIENDSHIPS = {
    'Sun': {
        'friends': ['Moon', 'Mars', 'Jupiter'],
        'enemies': ['Venus', 'Saturn'],
        'neutral': ['Mercury']
    },
    'Moon': {
        'friends': ['Sun', 'Mercury'],
        'enemies': [],
        'neutral': ['Mars', 'Jupiter', 'Venus', 'Saturn']
    },
    'Mars': {
        'friends': ['Sun', 'Moon', 'Jupiter'],
        'enemies': ['Mercury'],
        'neutral': ['Venus', 'Saturn']
    },
    'Mercury': {
        'friends': ['Sun', 'Venus'],
        'enemies': ['Moon'],
        'neutral': ['Mars', 'Jupiter', 'Saturn']
    },
    'Jupiter': {
        'friends': ['Sun', 'Moon', 'Mars'],
        'enemies': ['Mercury', 'Venus'],
        'neutral': ['Saturn']
    },
    'Venus': {
        'friends': ['Mercury', 'Saturn'],
        'enemies': ['Sun', 'Moon'],
        'neutral': ['Mars', 'Jupiter']
    },
    'Saturn': {
        'friends': ['Mercury', 'Venus'],
        'enemies': ['Sun', 'Moon', 'Mars'],
        'neutral': ['Jupiter']
    },
    'Rahu': {
        'friends': ['Venus', 'Saturn'],
        'enemies': ['Sun', 'Moon', 'Mars'],
        'neutral': ['Mercury', 'Jupiter']
    },
    'Ketu': {
        'friends': ['Mars', 'Venus', 'Saturn'],
        'enemies': ['Sun', 'Moon'],
        'neutral': ['Mercury', 'Jupiter']
    }
}

# ============================================
# SPECIAL DASHA CONSIDERATIONS
# ============================================

SPECIAL_DASHA_RULES = {
    'yogini_dasha': {
        'description': 'Alternative Dasha system mentioned in BPHS',
        'total_years': 36,
        'note': 'Used by some astrologers for specific purposes'
    },
    'ashtottari_dasha': {
        'description': 'Alternative 108-year Dasha system',
        'total_years': 108,
        'applicable': 'When Rahu is in Kendra from Lagna lord'
    },
    'kaal_chakra_dasha': {
        'description': 'Time-wheel based Dasha',
        'note': 'Complex system based on Navamsha placements'
    }
}
