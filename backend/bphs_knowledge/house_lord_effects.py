# BPHS House Lord Effects
# From Brihat Parashara Hora Shastra Chapters 24-25, 34

"""
Effects of House Lords in Various Houses - BPHS Ch. 24-25
This is critical for predicting life events based on house lord placements
"""

# ============================================
# HOUSE LORDS IN HOUSES - BPHS Ch. 24
# ============================================

HOUSE_LORD_EFFECTS = {
    1: {  # First house lord
        1: {
            'effect': 'Happy, strong body, intelligent, endowed with good fortune',
            'strength': 'Best placement for 1st lord',
            'health': 'Good physical constitution'
        },
        2: {
            'effect': 'Wealthy, happy family life, good speech, gains through own effort',
            'financial': 'Self-made wealth',
            'source': 'BPHS Ch. 24, Sloka 2'
        },
        3: {
            'effect': 'Brave, helpful siblings, interested in fine arts',
            'courage': 'Valorous and courageous',
            'siblings': 'Good relationship with younger siblings'
        },
        4: {
            'effect': 'Happy, blessed with mother, property, vehicles, education',
            'property': 'Gains landed property',
            'education': 'Good education',
            'source': 'BPHS Ch. 24, Sloka 4'
        },
        5: {
            'effect': 'Intelligent, happy children, speculative gains',
            'intelligence': 'Sharp intellect',
            'children': 'Good progeny'
        },
        6: {
            'effect': 'Sickly, trouble from enemies, debt issues',
            'health': 'Health problems',
            'enemies': 'Faces opposition',
            'debt': 'May incur debts'
        },
        7: {
            'effect': 'Passionate, devoted to spouse, travels',
            'marriage': 'Strong marriage inclination',
            'travel': 'Foreign connections'
        },
        8: {
            'effect': 'Sickly, short-lived (if afflicted), occult interests',
            'longevity': 'Questions on longevity',
            'transformation': 'Major life transformations'
        },
        9: {
            'effect': 'Fortunate, religious, blessed by father',
            'fortune': 'Very lucky',
            'father': 'Good relationship with father',
            'source': 'BPHS Ch. 24, Sloka 9'
        },
        10: {
            'effect': 'Successful career, respected, powerful',
            'career': 'Excellent professional success',
            'status': 'High social standing'
        },
        11: {
            'effect': 'Gains from all sources, fulfilled desires',
            'gains': 'Multiple income sources',
            'fulfillment': 'Wishes come true'
        },
        12: {
            'effect': 'Expenses, loss of vitality, foreign residence',
            'expenses': 'High expenditure',
            'foreign': 'May live abroad',
            'spiritual': 'Spiritual inclinations'
        }
    },
    2: {  # Second house lord
        1: 'Wealthy through own efforts, good family values',
        2: 'Very wealthy, good speech, strong family',
        3: 'Earns through siblings, communications, writing',
        4: 'Wealth from property, mother, education',
        5: 'Intelligent earnings, speculation gains',
        6: 'Wealth through service, competitors, loans',
        7: 'Wealth through marriage, partnerships, business',
        8: 'Hidden wealth, inheritance, financial ups and downs',
        9: 'Fortunate in wealth, religious spending',
        10: 'Wealth through career, public recognition',
        11: 'Excellent gains, multiple income sources',
        12: 'Expenses on good causes, loss of wealth, foreign earnings'
    },
    3: {  # Third house lord
        1: 'Brave, self-made, good communication skills',
        2: 'Earns through communication, siblings help in finance',
        3: 'Very brave, artistic, good siblings',
        4: 'Property through own efforts, short journeys',
        5: 'Creative intelligence, performing arts',
        6: 'Conflicts with siblings, competitive',
        7: 'Business partnerships, travel for marriage',
        8: 'Accidents in journeys, sibling troubles',
        9: 'Religious journeys, father-sibling connections',
        10: 'Career in communications, media, arts',
        11: 'Gains through siblings, communications',
        12: 'Loss through siblings, foreign journeys'
    },
    4: {  # Fourth house lord
        1: 'Happy disposition, property owner, good education',
        2: 'Wealth from property, family property',
        3: 'Property through courage, siblings connection',
        4: 'Excellent for property, vehicles, mother, education',
        5: 'Academic achievements, blessed children',
        6: 'Mother\'s health issues, property disputes',
        7: 'Property through spouse, foreign property',
        8: 'Hidden property, inheritance, mother\'s longevity',
        9: 'Fortunate in property, religious education',
        10: 'Career involves property, government, authority',
        11: 'Gains through property, fulfilled domestic wishes',
        12: 'Loss of property, foreign residence'
    },
    5: {  # Fifth house lord
        1: 'Intelligent, creative, child-like nature',
        2: 'Wealth through intelligence, speculative gains',
        3: 'Creative communications, artistic siblings',
        4: 'Educated, blessed mother, academic property',
        5: 'Very intelligent, blessed children, spiritual',
        6: 'Children\'s health, competitive intelligence',
        7: 'Love marriage, intelligent spouse',
        8: 'First child issues, occult knowledge',
        9: 'Very fortunate, religious, past life merit',
        10: 'Career through intelligence, creative profession',
        11: 'Gains through speculation, intelligent friends',
        12: 'Foreign children, spiritual intelligence'
    },
    6: {  # Sixth house lord
        1: 'Health issues early life, competitive nature',
        2: 'Earns through service, debt management',
        3: 'Conflicts with siblings, competitive communications',
        4: 'Mother\'s health, property disputes',
        5: 'Children\'s health, competitive intelligence',
        6: 'Viparita Raja Yoga possibility, overcomes enemies',
        7: 'Marital disputes, competitive partnerships',
        8: 'Chronic diseases, Viparita Raja Yoga',
        9: 'Father\'s health, religious conflicts',
        10: 'Service career, medical profession',
        11: 'Gains through service, competitive gains',
        12: 'Viparita Raja Yoga, enemies become friends'
    },
    7: {  # Seventh house lord
        1: 'Passionate, spouse oriented, business minded',
        2: 'Wealth through marriage/partnership',
        3: 'Travels for business, spouse-sibling connection',
        4: 'Property through marriage, happy marriage',
        5: 'Love affairs, children through marriage',
        6: 'Marital problems, competitive spouse',
        7: 'Good marriage, successful partnerships',
        8: 'Spouse longevity issues, transformative relationships',
        9: 'Foreign spouse, fortunate marriage',
        10: 'Career through partnerships, business success',
        11: 'Gains through marriage, spouse brings gains',
        12: 'Foreign spouse, bed pleasures, foreign partnerships'
    },
    8: {  # Eighth house lord
        1: 'Health issues, interest in occult, transformation',
        2: 'Inheritance, hidden family wealth',
        3: 'Accidents in travel, sibling longevity',
        4: 'Mother longevity, hidden property',
        5: 'First child issues, tantric knowledge',
        6: 'Chronic diseases, Viparita Raja Yoga',
        7: 'Spouse longevity, marital transformation',
        8: 'Long life, deep occult knowledge',
        9: 'Father longevity, sudden fortune changes',
        10: 'Career in research, investigation, occult',
        11: 'Sudden gains, inheritance from friends',
        12: 'Viparita Raja Yoga, spiritual transformation'
    },
    9: {  # Ninth house lord
        1: 'Very fortunate, religious, blessed life',
        2: 'Wealth through fortune, religious wealth',
        3: 'Religious journeys, fortunate siblings',
        4: 'Blessed with property, fortunate mother',
        5: 'Very fortunate, Purva Punya, blessed children',
        6: 'Father\'s health, fortune through service',
        7: 'Fortunate marriage, foreign spouse',
        8: 'Father longevity, hidden fortune',
        9: 'Extremely fortunate, religious, dharmic',
        10: 'Excellent career, fortune through profession',
        11: 'Excellent gains, all desires fulfilled',
        12: 'Foreign fortune, spiritual liberation'
    },
    10: {  # Tenth house lord
        1: 'Career oriented, self-made success',
        2: 'Wealth through career, family business',
        3: 'Career in communications, courageous profession',
        4: 'Career from home, government position',
        5: 'Career through intelligence, creative profession',
        6: 'Career in service, competition',
        7: 'Career through partnerships, business',
        8: 'Career interruptions, transformation in career',
        9: 'Fortunate career, father helps in career',
        10: 'Excellent career, fame, recognition',
        11: 'Gains through career, achieves ambitions',
        12: 'Foreign career, career expenses'
    },
    11: {  # Eleventh house lord
        1: 'Gains through self, desires fulfilled',
        2: 'Multiple income sources, wealthy',
        3: 'Gains through siblings, communications',
        4: 'Gains through property, mother helps',
        5: 'Gains through speculation, intelligent gains',
        6: 'Gains through service, competitors',
        7: 'Gains through marriage, partnerships',
        8: 'Sudden gains, inheritance',
        9: 'Fortunate gains, dharmic income',
        10: 'Gains through career, professional success',
        11: 'Excellent gains, all wishes fulfilled',
        12: 'Gains abroad, expenses on gains'
    },
    12: {  # Twelfth house lord
        1: 'Expenditure oriented, spiritual, foreign connections',
        2: 'Family expenses, loss of wealth',
        3: 'Expenses on siblings, foreign travel',
        4: 'Loss of property, mother lives abroad',
        5: 'Children abroad, loss in speculation',
        6: 'Viparita Raja Yoga, enemies destroyed',
        7: 'Spouse from abroad, bed pleasures',
        8: 'Viparita Raja Yoga, spiritual transformation',
        9: 'Father abroad, religious expenses',
        10: 'Career abroad, foreign profession',
        11: 'Gains from abroad, foreign friends',
        12: 'Excellent for spirituality, moksha'
    }
}

# ============================================
# FUNCTIONAL BENEFICS/MALEFICS BY ASCENDANT
# ============================================

FUNCTIONAL_NATURE_BY_LAGNA = {
    'Aries': {
        'benefics': ['Sun', 'Moon', 'Jupiter'],
        'malefics': ['Saturn', 'Mercury'],
        'yoga_karaka': 'Sun',
        'marak': ['Venus', 'Mercury'],
        'neutral': ['Mars'],
        'notes': 'Sun rules 5th, Jupiter rules 9th. Saturn rules 10th & 11th (bad).'
    },
    'Taurus': {
        'benefics': ['Saturn', 'Mercury', 'Sun'],
        'malefics': ['Jupiter', 'Moon', 'Venus'],
        'yoga_karaka': 'Saturn',
        'marak': ['Mars', 'Jupiter'],
        'neutral': ['Venus'],
        'notes': 'Saturn rules 9th & 10th (Yoga Karaka). Jupiter rules 8th & 11th.'
    },
    'Gemini': {
        'benefics': ['Venus', 'Saturn'],
        'malefics': ['Mars', 'Jupiter', 'Sun'],
        'yoga_karaka': 'Venus',
        'marak': ['Mars'],
        'neutral': ['Mercury'],
        'notes': 'Venus rules 5th & 12th. Mars rules 6th & 11th.'
    },
    'Cancer': {
        'benefics': ['Mars', 'Jupiter', 'Moon'],
        'malefics': ['Venus', 'Mercury'],
        'yoga_karaka': 'Mars',
        'marak': ['Saturn', 'Mercury'],
        'neutral': ['Sun'],
        'notes': 'Mars rules 5th & 10th (Yoga Karaka). Venus rules 4th & 11th.'
    },
    'Leo': {
        'benefics': ['Mars', 'Sun', 'Jupiter'],
        'malefics': ['Saturn', 'Venus'],
        'yoga_karaka': 'Mars',
        'marak': ['Saturn', 'Mercury'],
        'neutral': ['Moon'],
        'notes': 'Mars rules 4th & 9th (Yoga Karaka). Saturn rules 6th & 7th.'
    },
    'Virgo': {
        'benefics': ['Venus', 'Mercury'],
        'malefics': ['Mars', 'Moon', 'Jupiter'],
        'yoga_karaka': 'Venus',
        'marak': ['Mars', 'Jupiter'],
        'neutral': ['Saturn'],
        'notes': 'Venus rules 2nd & 9th. Mars rules 3rd & 8th.'
    },
    'Libra': {
        'benefics': ['Saturn', 'Mercury', 'Venus'],
        'malefics': ['Jupiter', 'Sun', 'Mars'],
        'yoga_karaka': 'Saturn',
        'marak': ['Mars', 'Jupiter'],
        'neutral': ['Moon'],
        'notes': 'Saturn rules 4th & 5th (Yoga Karaka). Jupiter rules 3rd & 6th.'
    },
    'Scorpio': {
        'benefics': ['Jupiter', 'Moon', 'Sun'],
        'malefics': ['Mercury', 'Venus'],
        'yoga_karaka': 'Moon',
        'marak': ['Venus', 'Mercury'],
        'neutral': ['Mars'],
        'notes': 'Moon rules 9th. Jupiter rules 2nd & 5th. Venus rules 7th & 12th.'
    },
    'Sagittarius': {
        'benefics': ['Mars', 'Sun', 'Jupiter'],
        'malefics': ['Venus', 'Saturn'],
        'yoga_karaka': 'Mars',
        'marak': ['Venus'],
        'neutral': ['Moon', 'Mercury'],
        'notes': 'Mars rules 5th & 12th. Sun rules 9th. Venus rules 6th & 11th.'
    },
    'Capricorn': {
        'benefics': ['Venus', 'Mercury', 'Saturn'],
        'malefics': ['Mars', 'Jupiter', 'Moon'],
        'yoga_karaka': 'Venus',
        'marak': ['Moon', 'Mars'],
        'neutral': ['Sun'],
        'notes': 'Venus rules 5th & 10th (Yoga Karaka). Mars rules 4th & 11th.'
    },
    'Aquarius': {
        'benefics': ['Venus', 'Saturn'],
        'malefics': ['Jupiter', 'Moon', 'Mars'],
        'yoga_karaka': 'Venus',
        'marak': ['Mars', 'Jupiter'],
        'neutral': ['Sun', 'Mercury'],
        'notes': 'Venus rules 4th & 9th (Yoga Karaka). Jupiter rules 2nd & 11th.'
    },
    'Pisces': {
        'benefics': ['Moon', 'Mars', 'Jupiter'],
        'malefics': ['Saturn', 'Sun', 'Venus', 'Mercury'],
        'yoga_karaka': 'Moon',
        'marak': ['Saturn'],
        'neutral': [],
        'notes': 'Moon rules 5th. Mars rules 2nd & 9th. Saturn rules 11th & 12th.'
    }
}

# ============================================
# KENDRA-TRIKONA LORDS - RAJA YOGA
# ============================================

RAJA_YOGA_COMBINATIONS = {
    'kendra_lords': [1, 4, 7, 10],
    'trikona_lords': [1, 5, 9],
    'effect': 'When Kendra lord combines with Trikona lord, Raja Yoga forms',
    'combination_types': {
        'conjunction': 'Both lords in same sign',
        'mutual_aspect': 'Both lords aspect each other',
        'exchange': 'Lords exchange signs (Parivartana)',
        'one_in_others_sign': 'One lord in sign of other'
    },
    'strength_factors': [
        'Both planets should be strong',
        'Not afflicted by malefics',
        'In good dignity',
        'Not combust'
    ]
}

# ============================================
# DUSTHANA LORDS (6, 8, 12) EFFECTS
# ============================================

DUSTHANA_LORD_EFFECTS = {
    6: {
        'positive': 'Overcomes enemies, competitive success',
        'negative': 'Health issues, debts, enemies',
        'when_strong': 'Success in service, medical field',
        'when_weak': 'Chronic health problems, legal issues'
    },
    8: {
        'positive': 'Occult knowledge, inheritance, longevity',
        'negative': 'Sudden obstacles, accidents, scandals',
        'when_strong': 'Research abilities, transformation',
        'when_weak': 'Chronic issues, longevity concerns'
    },
    12: {
        'positive': 'Spiritual progress, foreign connections, liberation',
        'negative': 'Losses, expenses, isolation',
        'when_strong': 'Success abroad, spiritual advancement',
        'when_weak': 'Financial losses, hospitalization'
    }
}

# ============================================
# VIPARITA RAJA YOGA
# ============================================

VIPARITA_RAJA_YOGA = {
    'harsha_yoga': {
        'combination': '6th lord in 6th, 8th, or 12th',
        'effect': 'Success over enemies, good health despite odds'
    },
    'sarala_yoga': {
        'combination': '8th lord in 6th, 8th, or 12th',
        'effect': 'Long life, fame, authority, fearlessness'
    },
    'vimala_yoga': {
        'combination': '12th lord in 6th, 8th, or 12th',
        'effect': 'Respected, wealthy, spends on good causes'
    },
    'conditions': [
        'Dusthana lords should be in dusthanas only',
        'Should not be aspected by dusthana lords',
        'Stronger if in own or exalted sign'
    ]
}

# Source reference
HOUSE_LORD_SOURCE = 'BPHS Ch. 24-25, Slokas 1-50'
