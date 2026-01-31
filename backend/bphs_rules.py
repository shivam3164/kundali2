# Brihat Parashara Hora Shastra Knowledge Base
# This file encodes yogas, planetary effects, and dasha interpretations from BPHS

YOGAS = [
    {
        'name': 'Gaja Kesari Yoga',
        'description': 'Moon and Jupiter in kendra from lagna.',
        'reference': 'BPHS Ch. 36',
        'conditions': {
            'planets': ['Moon', 'Jupiter'],
            'houses': [1, 4, 7, 10]
        }
    },
    {
        'name': 'Chandra-Mangal Yoga',
        'description': 'Moon and Mars are conjunct.',
        'reference': 'BPHS Ch. 36',
        'conditions': {
            'conjunction': ['Moon', 'Mars']
        }
    },
    {
        'name': 'Budha-Aditya Yoga',
        'description': 'Sun and Mercury are together in same house.',
        'reference': 'BPHS Ch. 36',
        'conditions': {
            'conjunction': ['Sun', 'Mercury']
        }
    },
    {
        'name': 'Neechabhanga Raj Yoga',
        'description': 'Debilitated planet whose dispositor is in kendra from lagna.',
        'reference': 'BPHS Ch. 39',
        'conditions': {
            'debilitated': ['Sun'],
            'dispositor_kendra': ['Venus']
        }
    },
    {
        'name': 'Vipreet Raj Yoga',
        'description': 'Lord of 6th, 8th, or 12th house in its own or another dusthana.',
        'reference': 'BPHS Ch. 40',
        'conditions': {
            'dusthana': ['Mars']
        }
    }
    # Add more yogas as needed
]

PLANETARY_EFFECTS = {
    'Sun': {
        'exaltation': 'Aries',
        'debilitation': 'Libra',
        'general_effects': 'Represents soul, authority, father, health.',
        'house_effects': {
            1: 'Strong vitality and leadership.',
            10: 'Success in career and public life.'
            # Add all 12 houses
        }
    },
    'Moon': {
        'exaltation': 'Taurus',
        'debilitation': 'Scorpio',
        'general_effects': 'Represents mind, emotions, mother, fluids.',
        'house_effects': {
            4: 'Emotional stability, good home life.',
            6: 'Mental stress, health issues.'
            # Add all 12 houses
        }
    }
    # Add all planets
}

DASHA_INTERPRETATIONS = {
    'Ketu': 'Spiritual growth, detachment, obstacles.',
    'Venus': 'Material comforts, relationships, creativity.',
    'Sun': 'Authority, career, health.',
    'Moon': 'Emotions, mind, travel.',
    'Mars': 'Energy, conflict, ambition.',
    'Rahu': 'Desires, foreign connections, confusion.',
    'Jupiter': 'Wisdom, expansion, children.',
    'Saturn': 'Discipline, delays, hard work.',
    'Mercury': 'Intellect, communication, business.'
}
