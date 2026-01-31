# BPHS Chapters 11-23: House (Bhava) Meanings and Effects
# Complete house significations from Brihat Parashara Hora Shastra

HOUSES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

HOUSE_MEANINGS = {
    1: {
        'name': 'Tanu Bhava',
        'english_name': 'First House / Ascendant',
        'primary_significations': [
            'Physical body', 'Personality', 'Self', 'Health', 'Vitality',
            'Appearance', 'Character', 'Temperament', 'Fame', 'Strength'
        ],
        'karaka': 'Sun',
        'body_part': 'Head',
        'classification': 'Kendra (Angular)',
        'nature': 'benefic',
        'direction': 'East',
        'reference': 'BPHS Ch. 11'
    },
    2: {
        'name': 'Dhana Bhava',
        'english_name': 'Second House',
        'primary_significations': [
            'Wealth', 'Family', 'Speech', 'Food', 'Right eye',
            'Face', 'Early childhood', 'Learning', 'Accumulated wealth'
        ],
        'karaka': 'Jupiter',
        'body_part': 'Face, Right eye',
        'classification': 'Panapara (Succedent)',
        'nature': 'neutral',
        'direction': 'North',
        'reference': 'BPHS Ch. 13'
    },
    3: {
        'name': 'Sahaja Bhava',
        'english_name': 'Third House',
        'primary_significations': [
            'Younger siblings', 'Courage', 'Short journeys', 'Communication',
            'Neighbors', 'Hands', 'Arms', 'Writing', 'Servants'
        ],
        'karaka': 'Mars',
        'body_part': 'Arms, Hands, Shoulders',
        'classification': 'Apoklima (Cadent), Upachaya',
        'nature': 'neutral',
        'direction': 'West',
        'reference': 'BPHS Ch. 14'
    },
    4: {
        'name': 'Bandhu Bhava',
        'english_name': 'Fourth House',
        'primary_significations': [
            'Mother', 'Home', 'Property', 'Vehicles', 'Education',
            'Comforts', 'Happiness', 'Land', 'Domestic peace', 'Heart'
        ],
        'karaka': 'Moon',
        'body_part': 'Chest, Heart, Lungs',
        'classification': 'Kendra (Angular), Chaturasra',
        'nature': 'benefic',
        'direction': 'North',
        'reference': 'BPHS Ch. 15'
    },
    5: {
        'name': 'Putra Bhava',
        'english_name': 'Fifth House',
        'primary_significations': [
            'Children', 'Intelligence', 'Education', 'Romance', 'Speculation',
            'Past life merit', 'Mantras', 'Creativity', 'Stomach'
        ],
        'karaka': 'Jupiter',
        'body_part': 'Stomach, Upper abdomen',
        'classification': 'Trikona (Trine), Panapara',
        'nature': 'very benefic',
        'direction': 'East',
        'reference': 'BPHS Ch. 16'
    },
    6: {
        'name': 'Ari Bhava',
        'english_name': 'Sixth House',
        'primary_significations': [
            'Enemies', 'Diseases', 'Debts', 'Obstacles', 'Servants',
            'Maternal uncle', 'Injuries', 'Litigation', 'Competition'
        ],
        'karaka': 'Mars',
        'body_part': 'Waist, Lower abdomen, Intestines',
        'classification': 'Dusthana, Upachaya, Apoklima',
        'nature': 'malefic',
        'direction': 'South',
        'reference': 'BPHS Ch. 17'
    },
    7: {
        'name': 'Yuvati Bhava',
        'english_name': 'Seventh House',
        'primary_significations': [
            'Spouse', 'Marriage', 'Partnership', 'Business', 'Foreign travel',
            'Public dealings', 'Trade', 'Death (maraka)', 'Lower abdomen'
        ],
        'karaka': 'Venus',
        'body_part': 'Lower abdomen, Kidneys',
        'classification': 'Kendra (Angular)',
        'nature': 'benefic',
        'direction': 'West',
        'reference': 'BPHS Ch. 18'
    },
    8: {
        'name': 'Randhra Bhava',
        'english_name': 'Eighth House',
        'primary_significations': [
            'Death', 'Longevity', 'Obstacles', 'Inheritance', 'Occult',
            'Transformation', 'Hidden matters', 'Chronic diseases', 'Research'
        ],
        'karaka': 'Saturn',
        'body_part': 'Genitals, Chronic diseases',
        'classification': 'Dusthana, Chaturasra, Panapara',
        'nature': 'very malefic',
        'direction': 'North',
        'reference': 'BPHS Ch. 19'
    },
    9: {
        'name': 'Dharma Bhava',
        'english_name': 'Ninth House',
        'primary_significations': [
            'Father', 'Fortune', 'Religion', 'Higher education', 'Long journeys',
            'Guru', 'Philosophy', 'Dharma', 'Luck', 'Previous life merit'
        ],
        'karaka': 'Jupiter',
        'body_part': 'Thighs, Hips',
        'classification': 'Trikona (Trine), Apoklima',
        'nature': 'very benefic',
        'direction': 'East',
        'reference': 'BPHS Ch. 20'
    },
    10: {
        'name': 'Karma Bhava',
        'english_name': 'Tenth House',
        'primary_significations': [
            'Career', 'Profession', 'Status', 'Authority', 'Fame',
            'Government', 'Father (some texts)', 'Actions', 'Reputation'
        ],
        'karaka': 'Mercury',
        'body_part': 'Knees',
        'classification': 'Kendra (Angular), Upachaya',
        'nature': 'benefic',
        'direction': 'South',
        'reference': 'BPHS Ch. 21'
    },
    11: {
        'name': 'Labha Bhava',
        'english_name': 'Eleventh House',
        'primary_significations': [
            'Gains', 'Income', 'Elder siblings', 'Friends', 'Desires',
            'Aspirations', 'Social circle', 'Left ear', 'Prosperity'
        ],
        'karaka': 'Jupiter',
        'body_part': 'Left ear, Legs',
        'classification': 'Upachaya, Panapara',
        'nature': 'benefic',
        'direction': 'North',
        'reference': 'BPHS Ch. 22'
    },
    12: {
        'name': 'Vyaya Bhava',
        'english_name': 'Twelfth House',
        'primary_significations': [
            'Losses', 'Expenses', 'Foreign lands', 'Moksha', 'Hospitalization',
            'Imprisonment', 'Bed pleasures', 'Left eye', 'Feet', 'Salvation'
        ],
        'karaka': 'Saturn',
        'body_part': 'Feet, Left eye',
        'classification': 'Dusthana, Apoklima',
        'nature': 'malefic',
        'direction': 'West',
        'reference': 'BPHS Ch. 23'
    }
}

# House classifications (BPHS Ch. 7, Slokas 33-36)
HOUSE_CLASSIFICATIONS = {
    'kendra': [1, 4, 7, 10],           # Angular houses - most powerful
    'trikona': [1, 5, 9],               # Trines - very auspicious
    'dusthana': [6, 8, 12],             # Evil houses
    'upachaya': [3, 6, 10, 11],         # Growth houses - malefics do well here
    'panapara': [2, 5, 8, 11],          # Succedent houses
    'apoklima': [3, 6, 9, 12],          # Cadent houses
    'chaturasra': [4, 8],               # Squares from lagna
    'maraka': [2, 7],                    # Death-inflicting houses
}

# Karakas for each house (BPHS Ch. 32, Sloka 31-34)
HOUSE_KARAKAS = {
    1: 'Sun',
    2: 'Jupiter',
    3: 'Mars',
    4: 'Moon',
    5: 'Jupiter',
    6: 'Mars',
    7: 'Venus',
    8: 'Saturn',
    9: 'Jupiter',
    10: 'Mercury',
    11: 'Jupiter',
    12: 'Saturn'
}

# Special considerations for analyzing houses
HOUSE_ANALYSIS_RULES = {
    'lord_placement': 'The lord of a house gives results based on where it is placed',
    'karaka_in_house': 'Karaka in own karaka house can reduce results (Karako Bhava Nashaya)',
    'benefic_aspect': 'Benefic aspects on house and lord strengthen the house',
    'malefic_aspect': 'Malefic aspects weaken the house unless it is an upachaya',
    'reference': 'BPHS Ch. 24-25'
}
