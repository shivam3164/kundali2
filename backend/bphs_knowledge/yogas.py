# BPHS Yogas (Planetary Combinations)
# From Brihat Parashara Hora Shastra Chapters 34-36

"""
Yoga Karakas and Planetary Combinations from BPHS
This module contains comprehensive yoga definitions for accurate kundali analysis
"""

# ============================================
# RAJ YOGAS (Royal Combinations) - BPHS Ch. 34
# ============================================

RAJ_YOGAS = {
    'kendra_trikona_exchange': {
        'name': 'Kendra-Trikona Parivartana Yoga',
        'description': 'Exchange between lord of Kendra and lord of Trikona',
        'conditions': ['kendra_lord_in_trikona', 'trikona_lord_in_kendra'],
        'effects': 'Native will become a king and be famous',
        'source': 'BPHS Ch. 34, Sloka 11-12'
    },
    'kendra_trikona_conjunction': {
        'name': 'Kendra-Trikona Yoga',
        'description': 'Lord of Kendra conjunct lord of Trikona in Kendra or Trikona',
        'conditions': ['kendra_lord_conjunct_trikona_lord', 'in_kendra_or_trikona'],
        'effects': 'Native becomes a king and famous',
        'source': 'BPHS Ch. 34, Sloka 11-12'
    },
    'same_planet_kendra_trikona': {
        'name': 'Single Planet Raj Yoga',
        'description': 'One planet owns both Kendra and Trikona',
        'conditions': ['single_planet_owns_kendra_and_trikona'],
        'effects': 'Specially a Yoga Karaka',
        'source': 'BPHS Ch. 34, Sloka 13'
    },
}

# ============================================
# NABHASH YOGAS - BPHS Ch. 35
# ============================================

NABHASH_YOGAS = {
    # ASRAYA YOGAS (3 types)
    'rajju': {
        'name': 'Rajju Yoga',
        'type': 'Asraya',
        'condition': 'All planets in movable signs',
        'effects': 'Fond of wandering, charming, earns in foreign countries, cruel and mischievous',
        'source': 'BPHS Ch. 35, Sloka 7, 18'
    },
    'musala': {
        'name': 'Musala Yoga',
        'type': 'Asraya',
        'condition': 'All planets in fixed signs',
        'effects': 'Endowed with honour, wisdom, wealth, dear to king, famous, many sons, firm disposition',
        'source': 'BPHS Ch. 35, Sloka 7, 19'
    },
    'nala': {
        'name': 'Nala Yoga',
        'type': 'Asraya',
        'condition': 'All planets in dual signs',
        'effects': 'Uneven physique, interested in accumulating money, very skilful, helpful to relatives',
        'source': 'BPHS Ch. 35, Sloka 7, 20'
    },
    
    # DALA YOGAS (2 types)
    'maal': {
        'name': 'Maal Yoga',
        'type': 'Dala',
        'condition': 'All 3 Kendras occupied by benefics',
        'effects': 'Ever happy, endowed with conveyances, robes, food, pleasures, splendorous, many females',
        'source': 'BPHS Ch. 35, Sloka 8, 21'
    },
    'sarpa': {
        'name': 'Sarpa/Bhujang Yoga',
        'type': 'Dala',
        'condition': 'All 3 Kendras occupied by malefics',
        'effects': 'Crooked, cruel, poor, miserable, depends on others for food and drinks',
        'source': 'BPHS Ch. 35, Sloka 8, 22'
    },
    
    # AKRITI YOGAS (20 types)
    'gada': {
        'name': 'Gada Yoga',
        'type': 'Akriti',
        'condition': 'All planets in two successive Kendras',
        'effects': 'Makes efforts to earn wealth, performs sacrificial rites, skilful in Shastras and songs',
        'source': 'BPHS Ch. 35, Sloka 9, 23'
    },
    'sakat': {
        'name': 'Sakat Yoga',
        'type': 'Akriti',
        'condition': 'All planets in Lagna and 7th house only',
        'effects': 'Afflicted by diseases, diseased nails, foolish, poor, devoid of friends and relatives',
        'source': 'BPHS Ch. 35, Sloka 9, 24'
    },
    'vihag': {
        'name': 'Vihag Yoga',
        'type': 'Akriti',
        'condition': 'All planets in 4th and 10th house only',
        'effects': 'Fond of roaming, messenger, lives by sexual dealings, shameless, interested in quarrels',
        'source': 'BPHS Ch. 35, Sloka 9, 25'
    },
    'shringatak': {
        'name': 'Shringatak Yoga',
        'type': 'Akriti',
        'condition': 'All planets in Lagna, 5th and 9th house',
        'effects': 'Fond of quarrels and battles, happy, dear to king, auspicious wife, rich',
        'source': 'BPHS Ch. 35, Sloka 9, 26'
    },
    'hala': {
        'name': 'Hala Yoga',
        'type': 'Akriti',
        'condition': 'All planets in 2nd, 6th and 10th OR 3rd, 7th and 11th OR 4th, 8th and 12th',
        'effects': 'Eats a lot, very poor, miserable, agitated, given up by friends and relatives, servant',
        'source': 'BPHS Ch. 35, Sloka 9-11, 27'
    },
    'vajra': {
        'name': 'Vajra Yoga',
        'type': 'Akriti',
        'condition': 'All benefics in 1st and 7th OR all malefics in 4th and 10th',
        'effects': 'Happy in beginning and end of life, valorous, charming, devoid of desires',
        'source': 'BPHS Ch. 35, Sloka 11, 28'
    },
    'yava': {
        'name': 'Yava Yoga',
        'type': 'Akriti',
        'condition': 'All benefics in 4th and 10th OR all malefics in 1st and 7th',
        'effects': 'Observes fasts and religious rules, does auspicious acts, wealth and sons in mid-life',
        'source': 'BPHS Ch. 35, Sloka 11, 29'
    },
    'kamala': {
        'name': 'Kamala Yoga',
        'type': 'Akriti',
        'condition': 'All planets in all 4 Kendras',
        'effects': 'Rich and virtuous, long lived, very famous, pure, performs auspicious acts, will be a king',
        'source': 'BPHS Ch. 35, Sloka 12, 30'
    },
    'vapi': {
        'name': 'Vapi Yoga',
        'type': 'Akriti',
        'condition': 'All planets in all Apoklimas OR all Panapharas',
        'effects': 'Capable of accumulating wealth, lasting wealth and happiness and sons, will be a king',
        'source': 'BPHS Ch. 35, Sloka 12, 31'
    },
    'yupa': {
        'name': 'Yupa Yoga',
        'type': 'Akriti',
        'condition': 'All 7 planets in 4 houses from Lagna',
        'effects': 'Spiritual knowledge, interested in sacrificial rites, strong, interested in fasts',
        'source': 'BPHS Ch. 35, Sloka 13, 32'
    },
    'shara': {
        'name': 'Shara Yoga',
        'type': 'Akriti',
        'condition': 'All 7 planets in 4 houses from 4th house',
        'effects': 'Makes arrows, head of prison, earns through animals, eats meat, indulges in torture',
        'source': 'BPHS Ch. 35, Sloka 13, 33'
    },
    'shakti': {
        'name': 'Shakti Yoga',
        'type': 'Akriti',
        'condition': 'All 7 planets in 4 houses from 7th house',
        'effects': 'Bereft of wealth, unsuccessful, miserable, lazy, long lived, skilful in war',
        'source': 'BPHS Ch. 35, Sloka 13, 34'
    },
    'danda': {
        'name': 'Danda Yoga',
        'type': 'Akriti',
        'condition': 'All 7 planets in 4 houses from 10th house',
        'effects': 'Loses sons and wife, indigent, unkind, away from his men, serves mean people',
        'source': 'BPHS Ch. 35, Sloka 13, 35'
    },
    'nauka': {
        'name': 'Nauka Yoga',
        'type': 'Akriti',
        'condition': 'All planets occupy 7 houses from Lagna',
        'effects': 'Derives livelihood through water, wealthy, famous, wicked, dirty, miserly',
        'source': 'BPHS Ch. 35, Sloka 14, 36'
    },
    'kuta': {
        'name': 'Kuta Yoga',
        'type': 'Akriti',
        'condition': 'All planets occupy 7 houses from 4th house',
        'effects': 'Liar, heads a jail, poor, crafty, cruel, lives in hills and fortresses',
        'source': 'BPHS Ch. 35, Sloka 14, 37'
    },
    'chatra': {
        'name': 'Chatra Yoga',
        'type': 'Akriti',
        'condition': 'All planets occupy 7 houses from 7th house',
        'effects': 'Helps his own men, kind, dear to kings, intelligent, happy at beginning and end',
        'source': 'BPHS Ch. 35, Sloka 14, 38'
    },
    'chapa': {
        'name': 'Chapa/Dhanushi Yoga',
        'type': 'Akriti',
        'condition': 'All planets occupy 7 houses from 10th house',
        'effects': 'Liar, protects secrets, thief, fond of wandering forests, happy in middle of life',
        'source': 'BPHS Ch. 35, Sloka 14, 39'
    },
    'ardha_chandra': {
        'name': 'Ardha Chandra Yoga',
        'type': 'Akriti',
        'condition': 'All planets in 7 continuous houses from non-angular house',
        'effects': 'Leads an army, splendorous body, dear to king, strong, endowed with gems and gold',
        'source': 'BPHS Ch. 35, Sloka 40'
    },
    'chakra': {
        'name': 'Chakra Yoga',
        'type': 'Akriti',
        'condition': 'All planets in 6 alternate signs from Lagna',
        'effects': 'Will be an emperor at whose feet kings prostrate',
        'source': 'BPHS Ch. 35, Sloka 15, 41'
    },
    'samudra': {
        'name': 'Samudra Yoga',
        'type': 'Akriti',
        'condition': 'All planets in 6 alternate signs from 2nd house',
        'effects': 'Many precious stones, abundant wealth, pleasures, dear to people, firm wealth',
        'source': 'BPHS Ch. 35, Sloka 15, 42'
    },
    
    # SANKHYA YOGAS (7 types)
    'veena': {
        'name': 'Veena/Vallaki Yoga',
        'type': 'Sankhya',
        'condition': 'All planets in 7 signs',
        'effects': 'Fond of songs, dance and musical instruments, skilful, happy, wealthy, leader of men',
        'source': 'BPHS Ch. 35, Sloka 16-17, 43'
    },
    'daamini': {
        'name': 'Daamini/Daam Yoga',
        'type': 'Sankhya',
        'condition': 'All planets in 6 signs',
        'effects': 'Helpful to others, righteously earned wealth, affluent, famous, many sons, courageous',
        'source': 'BPHS Ch. 35, Sloka 16-17, 44'
    },
    'paasha': {
        'name': 'Paasha Yoga',
        'type': 'Sankhya',
        'condition': 'All planets in 5 signs',
        'effects': 'Liable to imprisonment, skilful in work, deceiving, talks much, bereft of good qualities',
        'source': 'BPHS Ch. 35, Sloka 16-17, 45'
    },
    'kedara': {
        'name': 'Kedara Yoga',
        'type': 'Sankhya',
        'condition': 'All planets in 4 signs',
        'effects': 'Useful to many, agriculturist, truthful, happy, fickle minded, wealthy',
        'source': 'BPHS Ch. 35, Sloka 16-17, 46'
    },
    'shoola': {
        'name': 'Shoola Yoga',
        'type': 'Sankhya',
        'condition': 'All planets in 3 signs',
        'effects': 'Sharp, indolent, bereft of wealth, tortuous, valiant, famous through war',
        'source': 'BPHS Ch. 35, Sloka 16-17, 47'
    },
    'yuga': {
        'name': 'Yuga Yoga',
        'type': 'Sankhya',
        'condition': 'All planets in 2 signs',
        'effects': 'Heretic, devoid of wealth, discarded by others, devoid of sons, mother and virtues',
        'source': 'BPHS Ch. 35, Sloka 16-17, 48'
    },
    'gola': {
        'name': 'Gola Yoga',
        'type': 'Sankhya',
        'condition': 'All planets in 1 sign',
        'effects': 'Strong, devoid of wealth, learning and intelligence, dirty, sorrowful, miserable',
        'source': 'BPHS Ch. 35, Sloka 16-17, 49'
    },
}

# ============================================
# PANCHA MAHAPURUSHA YOGAS
# ============================================

PANCHA_MAHAPURUSHA_YOGAS = {
    'ruchaka': {
        'name': 'Ruchaka Yoga',
        'planet': 'Mars',
        'condition': 'Mars in own sign or exalted in a Kendra',
        'effects': 'Long face, acquired wealth through many means, conqueror of foes, valorous, victorious, arrogant',
        'houses': [1, 4, 7, 10],
        'signs': ['Aries', 'Scorpio', 'Capricorn'],  # Own and exalted
        'source': 'BPHS Ch. 36'
    },
    'bhadra': {
        'name': 'Bhadra Yoga',
        'planet': 'Mercury',
        'condition': 'Mercury in own sign or exalted in a Kendra',
        'effects': 'Lion-like face, well-developed chest, walks like an elephant, long arms, learned, wealthy',
        'houses': [1, 4, 7, 10],
        'signs': ['Gemini', 'Virgo'],  # Own and exalted
        'source': 'BPHS Ch. 36'
    },
    'hamsa': {
        'name': 'Hamsa Yoga',
        'planet': 'Jupiter',
        'condition': 'Jupiter in own sign or exalted in a Kendra',
        'effects': 'Honey-colored eyes, elevated nose, fair complexion, loved by women, righteous, king',
        'houses': [1, 4, 7, 10],
        'signs': ['Sagittarius', 'Pisces', 'Cancer'],  # Own and exalted
        'source': 'BPHS Ch. 36'
    },
    'malavya': {
        'name': 'Malavya Yoga',
        'planet': 'Venus',
        'condition': 'Venus in own sign or exalted in a Kendra',
        'effects': 'Beautiful limbs, thin waist, rich, loved by spouse, possesses vehicles, famous',
        'houses': [1, 4, 7, 10],
        'signs': ['Taurus', 'Libra', 'Pisces'],  # Own and exalted
        'source': 'BPHS Ch. 36'
    },
    'shasha': {
        'name': 'Shasha Yoga',
        'planet': 'Saturn',
        'condition': 'Saturn in own sign or exalted in a Kendra',
        'effects': 'Good teeth, swift, intrepid, leader of army, knows the weak points of enemies',
        'houses': [1, 4, 7, 10],
        'signs': ['Capricorn', 'Aquarius', 'Libra'],  # Own and exalted
        'source': 'BPHS Ch. 36'
    },
}

# ============================================
# CHANDRA (MOON) YOGAS
# ============================================

CHANDRA_YOGAS = {
    'sunafa': {
        'name': 'Sunafa Yoga',
        'condition': 'Planet other than Sun in 2nd from Moon',
        'effects': 'Self-made person, intelligent, wealthy, good reputation',
        'source': 'BPHS Ch. 36'
    },
    'anafa': {
        'name': 'Anafa Yoga',
        'condition': 'Planet other than Sun in 12th from Moon',
        'effects': 'Powerful, healthy, renowned, charitable, prosperous',
        'source': 'BPHS Ch. 36'
    },
    'durudhura': {
        'name': 'Durudhura Yoga',
        'condition': 'Planets other than Sun in both 2nd and 12th from Moon',
        'effects': 'Enjoys all comforts, charitable, wealthy, vehicles',
        'source': 'BPHS Ch. 36'
    },
    'kemadruma': {
        'name': 'Kemadruma Yoga',
        'condition': 'No planets in 2nd or 12th from Moon, and no planets in Kendras from Moon',
        'effects': 'Poor, sorrowful, doing unrighteous deeds, dirty, dependent',
        'source': 'BPHS Ch. 36'
    },
    'gajakesari': {
        'name': 'Gajakesari Yoga',
        'condition': 'Jupiter in Kendra from Moon',
        'effects': 'Many relations, intelligent, virtuous, pleases king, famous, long-lived',
        'source': 'BPHS Ch. 36'
    },
    'chandra_mangala': {
        'name': 'Chandra-Mangala Yoga',
        'condition': 'Moon conjunct Mars',
        'effects': 'Earns money through questionable means, wins over enemies, deals in various things',
        'source': 'BPHS Ch. 36'
    },
    'adhi': {
        'name': 'Adhi Yoga',
        'condition': 'Benefics in 6th, 7th and 8th from Moon',
        'effects': 'Commander, minister, or king depending on number of benefics',
        'source': 'BPHS Ch. 36'
    },
}

# ============================================
# SURYA (SUN) YOGAS
# ============================================

SURYA_YOGAS = {
    'vesi': {
        'name': 'Vesi Yoga',
        'condition': 'Planet other than Moon in 2nd from Sun',
        'effects': 'Truthful, eloquent, lazy, good memory, charitable',
        'source': 'BPHS Ch. 36'
    },
    'vosi': {
        'name': 'Vosi Yoga',
        'condition': 'Planet other than Moon in 12th from Sun',
        'effects': 'Intelligent, fickle, charitable, strong memory, skilled',
        'source': 'BPHS Ch. 36'
    },
    'ubhayachari': {
        'name': 'Ubhayachari Yoga',
        'condition': 'Planets other than Moon in both 2nd and 12th from Sun',
        'effects': 'Equal to king, eloquent, handsome, pleasant',
        'source': 'BPHS Ch. 36'
    },
}

# ============================================
# DHANA YOGAS (Wealth Combinations)
# ============================================

DHANA_YOGAS = {
    'dhana_yoga_1': {
        'name': 'Dhana Yoga (Basic)',
        'condition': '2nd lord in angle or trine',
        'effects': 'Wealthy',
        'source': 'BPHS Ch. 13'
    },
    'dhana_yoga_2': {
        'name': 'Dhana Yoga (Exchange)',
        'condition': '2nd lord in 11th, 11th lord in 2nd',
        'effects': 'Wealth acquired by the native',
        'source': 'BPHS Ch. 13, Sloka 4'
    },
    'dhana_yoga_3': {
        'name': 'Dhana Yoga (Jupiter)',
        'condition': 'Jupiter in 2nd as 2nd lord OR Jupiter with Mars in 2nd',
        'effects': 'Wealthy',
        'source': 'BPHS Ch. 13, Sloka 3'
    },
    'lakshmi_yoga': {
        'name': 'Lakshmi Yoga',
        'condition': '9th lord in own/exalted sign in Kendra or Trikona, Lagna lord strong',
        'effects': 'Very wealthy, virtuous, famous, blessed by Goddess Lakshmi',
        'source': 'BPHS Ch. 36'
    },
}

# ============================================
# DARIDRA YOGAS (Poverty Combinations)
# ============================================

DARIDRA_YOGAS = {
    'daridra_yoga_1': {
        'name': 'Daridra Yoga (Basic)',
        'condition': '2nd and 11th lords in 6th, 8th, or 12th',
        'effects': 'Penniless, poor',
        'source': 'BPHS Ch. 13, Sloka 6-7'
    },
    'daridra_yoga_2': {
        'name': 'Daridra Yoga (Combust)',
        'condition': '2nd and 11th lords combust or with malefics',
        'effects': 'Penury from birth, begs for food',
        'source': 'BPHS Ch. 13, Sloka 7'
    },
}

# ============================================
# VIPARITA RAJ YOGAS (Reversal of Fortune)
# ============================================

VIPARITA_RAJ_YOGAS = {
    'harsha': {
        'name': 'Harsha Yoga',
        'condition': '6th lord in 6th, 8th, or 12th',
        'effects': 'Happy, has good fortune, enjoys good health, famous, victorious',
        'source': 'BPHS Ch. 36'
    },
    'sarala': {
        'name': 'Sarala Yoga',
        'condition': '8th lord in 6th, 8th, or 12th',
        'effects': 'Long-lived, fearless, learned, prosperous, pure',
        'source': 'BPHS Ch. 36'
    },
    'vimala': {
        'name': 'Vimala Yoga',
        'condition': '12th lord in 6th, 8th, or 12th',
        'effects': 'Frugal, happy, independent, honored',
        'source': 'BPHS Ch. 36'
    },
}

# ============================================
# YOGA KARAKA PLANETS BY LAGNA - BPHS Ch. 34
# ============================================

YOGA_KARAKAS_BY_LAGNA = {
    'Aries': {
        'yogakarakas': ['Jupiter', 'Sun'],
        'malefics': ['Saturn', 'Mercury', 'Venus'],
        'neutral': ['Mars'],  # 8th lord but helpful
        'killers': ['Venus'],  # Primary killer
        'source': 'BPHS Ch. 34, Sloka 19-22'
    },
    'Taurus': {
        'yogakarakas': ['Saturn'],  # Causes Raj Yoga
        'malefics': ['Jupiter', 'Venus', 'Moon'],
        'neutral': ['Mercury'],
        'killers': ['Jupiter', 'Moon', 'Venus', 'Mars'],
        'source': 'BPHS Ch. 34, Sloka 23-24'
    },
    'Gemini': {
        'yogakarakas': ['Venus'],  # Only auspicious
        'malefics': ['Mars', 'Jupiter', 'Sun'],
        'neutral': [],
        'killers': ['Moon'],  # Prime killer
        'source': 'BPHS Ch. 34, Sloka 25-26'
    },
    'Cancer': {
        'yogakarakas': ['Mars'],  # Full-fledged Yoga Karaka
        'malefics': ['Venus', 'Mercury'],
        'neutral': ['Saturn', 'Sun'],  # Killers based on association
        'killers': [],
        'source': 'BPHS Ch. 34, Sloka 27-28'
    },
    'Leo': {
        'yogakarakas': ['Mars', 'Jupiter', 'Sun'],
        'malefics': ['Mercury', 'Venus', 'Saturn'],
        'neutral': [],
        'killers': ['Saturn', 'Moon'],  # Based on association
        'source': 'BPHS Ch. 34, Sloka 29-30'
    },
    'Virgo': {
        'yogakarakas': ['Mercury', 'Venus'],  # Venus conjunction produces Yoga
        'malefics': ['Mars', 'Jupiter', 'Moon'],
        'neutral': ['Sun'],
        'killers': ['Venus'],  # Also a killer
        'source': 'BPHS Ch. 34, Sloka 31-32'
    },
    'Libra': {
        'yogakarakas': ['Saturn', 'Mercury'],  # Moon-Mercury produce Raj Yoga
        'malefics': ['Jupiter', 'Sun', 'Mars'],
        'neutral': ['Venus'],
        'killers': ['Mars', 'Jupiter'],
        'source': 'BPHS Ch. 34, Sloka 33-34'
    },
    'Scorpio': {
        'yogakarakas': ['Jupiter', 'Moon', 'Sun'],  # Sun-Moon are Yoga Karakas
        'malefics': ['Venus', 'Mercury', 'Saturn'],
        'neutral': ['Mars'],
        'killers': ['Venus', 'Mercury', 'Saturn'],
        'source': 'BPHS Ch. 34, Sloka 35-36'
    },
    'Sagittarius': {
        'yogakarakas': ['Mars', 'Sun'],  # Sun-Mercury produce Yoga
        'malefics': ['Venus'],  # Only Venus is inauspicious
        'neutral': ['Jupiter'],
        'killers': ['Saturn', 'Venus'],
        'source': 'BPHS Ch. 34, Sloka 37-38'
    },
    'Capricorn': {
        'yogakarakas': ['Venus'],  # Only Venus causes superior Yoga
        'malefics': ['Mars', 'Jupiter', 'Moon'],
        'neutral': ['Sun'],
        'killers': ['Mars', 'Jupiter', 'Moon'],
        'source': 'BPHS Ch. 34, Sloka 39-40'
    },
    'Aquarius': {
        'yogakarakas': ['Venus'],  # Only planet causing Raj Yoga
        'malefics': ['Jupiter', 'Moon', 'Mars'],
        'neutral': ['Mercury'],  # Meddling effects
        'killers': ['Jupiter', 'Sun', 'Mars'],
        'source': 'BPHS Ch. 34, Sloka 41-42'
    },
    'Pisces': {
        'yogakarakas': ['Mars', 'Moon'],  # Mars-Jupiter cause Yoga
        'malefics': ['Saturn', 'Venus', 'Sun', 'Mercury'],
        'neutral': [],
        'killers': ['Saturn', 'Mercury'],  # Mars won't kill independently
        'source': 'BPHS Ch. 34, Sloka 43-44'
    },
}

# ============================================
# CHAPTER 36 YOGAS - BPHS Many Other Yogas
# ============================================

CHAPTER_36_YOGAS = {
    # Slokas 1-2: Subh and Asubh Yogas
    'subh_yoga_lagna': {
        'name': 'Subh Yoga (Lagna)',
        'condition': 'Benefic in Lagna',
        'effects': 'Eloquent, charming, virtuous',
        'source': 'BPHS Ch. 36, Sloka 1-2'
    },
    'asubh_yoga_lagna': {
        'name': 'Asubh Yoga (Lagna)',
        'condition': 'Malefic in Lagna',
        'effects': 'Sensuous, sinful acts, enjoys others wealth',
        'source': 'BPHS Ch. 36, Sloka 1-2'
    },
    'subh_yoga_dhan_vyaya': {
        'name': 'Subh Yoga (2nd & 12th)',
        'condition': 'Benefics in both 2nd and 12th houses',
        'effects': 'Eloquent, charming, virtuous',
        'source': 'BPHS Ch. 36, Sloka 1-2'
    },
    'asubh_yoga_dhan_vyaya': {
        'name': 'Asubh Yoga (2nd & 12th)',
        'condition': 'Malefics in both 2nd and 12th houses',
        'effects': 'Sensuous, sinful acts, enjoys others wealth',
        'source': 'BPHS Ch. 36, Sloka 1-2'
    },
    
    # Sloka 3-4: Gajakesari Yoga
    'gajakesari': {
        'name': 'Gajakesari Yoga',
        'condition': 'Jupiter in Kendra from Lagna OR Moon, conjunct/aspected by benefic, NOT in debilitation, combustion, or inimical sign',
        'effects': 'Splendorous, wealthy, intelligent, many laudable virtues, pleases king',
        'source': 'BPHS Ch. 36, Sloka 3-4'
    },
    
    # Sloka 5-6: Amal Yoga
    'amala': {
        'name': 'Amala Yoga',
        'condition': 'EXCLUSIVELY a benefic in 10th from Lagna or Moon',
        'effects': 'Fame lasting till Moon and stars exist, honored by king, abundant pleasures, charitable, fond of relatives, helpful, pious, virtuous',
        'source': 'BPHS Ch. 36, Sloka 5-6'
    },
    
    # Sloka 7-8: Parvata Yoga
    'parvata': {
        'name': 'Parvata Yoga',
        'condition': 'Benefics in Kendras while 7th and 8th are vacant OR occupied by only benefics',
        'effects': 'Wealthy, eloquent, charitable, learned in Shastras, fond of mirth, famous, splendorous, leader of city',
        'source': 'BPHS Ch. 36, Sloka 7-8'
    },
    
    # Sloka 9-10: Kahal Yoga
    'kahala': {
        'name': 'Kahala Yoga',
        'condition': '4th lord and Jupiter in mutual Kendras + Lagna lord strong, OR 4th lord in own/exaltation conjunct 10th lord',
        'effects': 'Energetic, adventurous, charming, endowed with complete army (chariots, elephants, horses, infantry), lord over villages',
        'source': 'BPHS Ch. 36, Sloka 9-10'
    },
    
    # Sloka 11-12: Chamar Yoga
    'chamara': {
        'name': 'Chamara Yoga',
        'condition': 'Lagna lord exalted in Kendra aspected by Jupiter, OR two benefics in 1st/7th/9th/10th',
        'effects': 'King or honored by king, long-lived, scholarly, eloquent, versed in all arts',
        'source': 'BPHS Ch. 36, Sloka 11-12'
    },
    
    # Sloka 13-14: Shankha Yoga
    'shankha': {
        'name': 'Shankha Yoga',
        'condition': 'Lagna lord strong + 5th and 6th lords in mutual Kendras, OR Lagna lord with 10th lord in movable sign + 9th lord strong',
        'effects': 'Endowed with wealth, spouse and sons, kindly disposed, propitious, intelligent, meritorious, long-lived',
        'source': 'BPHS Ch. 36, Sloka 13-14'
    },
    
    # Sloka 15-16: Bheri Yoga
    'bheri': {
        'name': 'Bheri Yoga',
        'condition': '12th, 1st, 2nd, and 7th houses occupied + 9th lord strong, OR Venus, Jupiter and Lagna lord in Kendra + 9th lord strong',
        'effects': 'Endowed with wealth, wife and sons, king, famous, virtuous, good behavior, happiness and pleasures',
        'source': 'BPHS Ch. 36, Sloka 15-16'
    },
    
    # Sloka 17: Mridanga Yoga
    'mridanga': {
        'name': 'Mridanga Yoga',
        'condition': 'Lagna lord strong + other planets in Kendras, Konas, own houses or exaltation signs',
        'effects': 'King or equal to king, happy',
        'source': 'BPHS Ch. 36, Sloka 17'
    },
    
    # Sloka 18: Shrinatha Yoga
    'shrinatha': {
        'name': 'Shrinatha Yoga',
        'condition': '7th lord in 10th + 10th lord exalted + conjunct 9th lord',
        'effects': 'Equal to Lord Devendra (god of gods)',
        'source': 'BPHS Ch. 36, Sloka 18'
    },
    
    # Sloka 19-20: Sharada Yoga
    'sharada': {
        'name': 'Sharada Yoga',
        'condition': '10th lord in 5th + Mercury in Kendra + Sun with strength in Leo, OR Jupiter/Mercury in trine to Moon + Mars in 11th',
        'effects': 'Wealth, spouse and sons, happy, scholarly, dear to king, pious, virtuous',
        'source': 'BPHS Ch. 36, Sloka 19-20'
    },
    
    # Sloka 21-22: Matsya Yoga
    'matsya': {
        'name': 'Matsya Yoga',
        'condition': 'Benefics in 1st and 9th + mixed planets in 5th + malefics in 4th and 8th',
        'effects': 'Jyotishi (astrologer), synonym of kindness, virtuous, strong, beautiful, famous, learned, pious',
        'source': 'BPHS Ch. 36, Sloka 21-22'
    },
    
    # Sloka 23-24: Kurma Yoga
    'kurma': {
        'name': 'Kurma Yoga',
        'condition': 'Benefics in 5th, 6th, 7th in own/exalted/friendly signs + malefics in 3rd, 11th, 1st in own/exalted',
        'effects': 'King, courageous, virtuous, famous, helpful, happy, leader of men',
        'source': 'BPHS Ch. 36, Sloka 23-24'
    },
    
    # Sloka 25-26: Khadga Yoga
    'khadga': {
        'name': 'Khadga Yoga',
        'condition': 'Exchange between 2nd and 9th lords + Lagna lord in Kendra or Trikona',
        'effects': 'Endowed with wealth, fortune and happiness, learned in Shastras, intelligent, mighty, grateful, skilful',
        'source': 'BPHS Ch. 36, Sloka 25-26'
    },
    
    # Sloka 27-28: Lakshmi Yoga
    'lakshmi': {
        'name': 'Lakshmi Yoga',
        'condition': '9th lord in Kendra in Moolatrikona, own sign, or exaltation + Lagna lord with strength',
        'effects': 'Charming, virtuous, kingly status, many sons, abundant wealth, famous, high moral merits',
        'source': 'BPHS Ch. 36, Sloka 27-28'
    },
    
    # Sloka 29-30: Kusuma Yoga
    'kusuma': {
        'name': 'Kusuma Yoga',
        'condition': 'Venus in Kendra + Moon in Trikona with benefic + Saturn in 10th + Fixed sign rising',
        'effects': 'King or equal, charitable, enjoys pleasures, happy, prime among race, virtuous, red-lettered',
        'source': 'BPHS Ch. 36, Sloka 29-30'
    },
    
    # Sloka 31-32: Kalanidhi Yoga
    'kalanidhi': {
        'name': 'Kalanidhi Yoga',
        'condition': 'Jupiter in 2nd or 5th + aspected by Mercury and Venus',
        'effects': 'Virtuous, honored by kings, bereft of diseases, happy, wealthy, learned',
        'source': 'BPHS Ch. 36, Sloka 31-32'
    },
    
    # Sloka 33-34: Kalpadruma Yoga
    'kalpadruma': {
        'name': 'Kalpadruma Yoga',
        'condition': 'Chain of 4 lords (Lagna lord → its dispositor → its dispositor → Navamsha dispositor) all in Kendras/Konas or exalted',
        'effects': 'All kinds of wealth, king, pious, strong, fond of war, merciful',
        'source': 'BPHS Ch. 36, Sloka 33-34'
    },
    
    # Sloka 35-36: Trimurthi Yogas
    'hari_yoga': {
        'name': 'Hari Yoga',
        'condition': 'Benefics in 2nd, 12th, and 8th from 2nd lord',
        'effects': 'Happy, learned, endowed with wealth and sons',
        'source': 'BPHS Ch. 36, Sloka 35-36'
    },
    'hara_yoga': {
        'name': 'Hara Yoga',
        'condition': 'Benefics in 4th, 9th, and 8th from 7th lord',
        'effects': 'Happy, learned, endowed with wealth and sons',
        'source': 'BPHS Ch. 36, Sloka 35-36'
    },
    'brahma_yoga': {
        'name': 'Brahma Yoga',
        'condition': 'Benefics in 4th, 10th, and 11th from Lagna lord',
        'effects': 'Happy, learned, endowed with wealth and sons',
        'source': 'BPHS Ch. 36, Sloka 35-36'
    },
    
    # Sloka 37: Lagna Adhi Yoga
    'lagna_adhi': {
        'name': 'Lagna Adhi Yoga',
        'condition': 'Benefics in 7th and 8th from Lagna, without conjunction/aspect from malefics',
        'effects': 'Great person, learned in Shastras, happy',
        'source': 'BPHS Ch. 36, Sloka 37'
    },
}

# ============================================
# CHAPTER 37 - CHANDRA (MOON) YOGAS
# ============================================

CHANDRA_YOGAS = {
    # Sloka 1: Moon-Sun Position Rule
    'chandra_kendra_from_surya': {
        'name': 'Moon in Kendra from Sun',
        'condition': 'Moon in Kendra (1, 4, 7, 10) from Sun',
        'effects': 'Wealth, intelligence, and skill will be LITTLE',
        'source': 'BPHS Ch. 37, Sloka 1'
    },
    'chandra_panapara_from_surya': {
        'name': 'Moon in Panapara from Sun',
        'condition': 'Moon in Panapara (2, 5, 8, 11) from Sun',
        'effects': 'Wealth, intelligence, and skill will be MIDDLING',
        'source': 'BPHS Ch. 37, Sloka 1'
    },
    'chandra_apoklima_from_surya': {
        'name': 'Moon in Apoklima from Sun',
        'condition': 'Moon in Apoklima (3, 6, 9, 12) from Sun',
        'effects': 'Wealth, intelligence, and skill will be EXCELLENT',
        'source': 'BPHS Ch. 37, Sloka 1'
    },
    
    # Sloka 2-4: Day/Night Birth Moon Rules
    'chandra_day_birth': {
        'name': 'Moon Day Birth Yoga',
        'condition': 'Day birth + Moon in own/friendly Navamsha + aspected by Jupiter',
        'effects': 'Endowed with wealth and happiness',
        'source': 'BPHS Ch. 37, Sloka 2-4'
    },
    'chandra_night_birth': {
        'name': 'Moon Night Birth Yoga',
        'condition': 'Night birth + Moon in own/friendly Navamsha + aspected by Venus',
        'effects': 'Endowed with wealth and happiness',
        'source': 'BPHS Ch. 37, Sloka 2-4'
    },
    
    # Standard Moon Yogas
    'sunafa': {
        'name': 'Sunafa Yoga',
        'condition': 'Planet other than Sun in 2nd from Moon',
        'effects': 'Self-made person, intelligent, wealthy, good reputation',
        'source': 'BPHS'
    },
    'anafa': {
        'name': 'Anafa Yoga',
        'condition': 'Planet other than Sun in 12th from Moon',
        'effects': 'Powerful, healthy, renowned, charitable, prosperous',
        'source': 'BPHS'
    },
    'durudhura': {
        'name': 'Durudhura Yoga',
        'condition': 'Planets other than Sun in both 2nd and 12th from Moon',
        'effects': 'Enjoys all comforts, charitable, wealthy, vehicles',
        'source': 'BPHS'
    },
    'kemadruma': {
        'name': 'Kemadruma Yoga',
        'condition': 'No planets in 2nd or 12th from Moon, and no planets in Kendras from Moon',
        'effects': 'Poor, sorrowful, doing unrighteous deeds, dirty, dependent',
        'source': 'BPHS'
    },
    'gajakesari': {
        'name': 'Gajakesari Yoga (from Moon)',
        'condition': 'Jupiter in Kendra from Moon',
        'effects': 'Many relations, intelligent, virtuous, pleases king, famous, long-lived',
        'source': 'BPHS Ch. 36'
    },
    'chandra_mangala': {
        'name': 'Chandra-Mangala Yoga',
        'condition': 'Moon conjunct Mars',
        'effects': 'Earns money through questionable means, wins over enemies, deals in various things',
        'source': 'BPHS'
    },
    'adhi': {
        'name': 'Adhi Yoga',
        'condition': 'Benefics in 6th, 7th and 8th from Moon',
        'effects': 'Commander, minister, or king depending on number of benefics',
        'source': 'BPHS'
    },
}

# ============================================
# SURYA (SUN) YOGAS
# ============================================

SURYA_YOGAS = {
    'vesi': {
        'name': 'Vesi Yoga',
        'condition': 'Planet other than Moon in 2nd from Sun',
        'effects': 'Truthful, eloquent, lazy, good memory, charitable',
        'source': 'BPHS'
    },
    'vosi': {
        'name': 'Vosi Yoga',
        'condition': 'Planet other than Moon in 12th from Sun',
        'effects': 'Intelligent, fickle, charitable, strong memory, skilled',
        'source': 'BPHS'
    },
    'ubhayachari': {
        'name': 'Ubhayachari Yoga',
        'condition': 'Planets other than Moon in both 2nd and 12th from Sun',
        'effects': 'Equal to king, eloquent, handsome, pleasant',
        'source': 'BPHS'
    },
}

# ============================================
# SPECIAL YOGAS (Legacy - Kept for Compatibility)
# ============================================

SPECIAL_YOGAS = {
    'buddha_aditya': {
        'name': 'Budha-Aditya Yoga',
        'condition': 'Mercury conjunct Sun (not combust)',
        'effects': 'Intelligent, skilful, learned, good reputation',
        'source': 'BPHS Ch. 36'
    },
    'amala': {
        'name': 'Amala Yoga',
        'condition': 'Only benefic in 10th from Lagna or Moon',
        'effects': 'Spotless character, lasting fame, charitable, prosperous',
        'source': 'BPHS Ch. 36, Sloka 5-6'
    },
    'kahala': {
        'name': 'Kahala Yoga',
        'condition': '4th and 9th lords in mutual Kendras, Lagna lord strong',
        'effects': 'Courageous, commanding, stubborn',
        'source': 'BPHS Ch. 36, Sloka 9-10'
    },
    'parvata': {
        'name': 'Parvata Yoga',
        'condition': 'Benefics in Kendras, 6th and 8th empty or only benefics',
        'effects': 'Wealthy, famous, charitable, leader, long-lived',
        'source': 'BPHS Ch. 36, Sloka 7-8'
    },
    'pushkala': {
        'name': 'Pushkala Yoga',
        'condition': 'Lagna lord with Moon in Kendra, aspected by benefic, strong Lagna',
        'effects': 'Famous, wealthy, honored by king, eloquent, pleasing',
        'source': 'BPHS Ch. 36'
    },
}

# ============================================
# HELPER FUNCTIONS FOR YOGA DETECTION
# ============================================

def get_sign_type(sign):
    """Return whether sign is movable, fixed, or dual"""
    movable = ['Aries', 'Cancer', 'Libra', 'Capricorn']
    fixed = ['Taurus', 'Leo', 'Scorpio', 'Aquarius']
    dual = ['Gemini', 'Virgo', 'Sagittarius', 'Pisces']
    
    if sign in movable:
        return 'movable'
    elif sign in fixed:
        return 'fixed'
    elif sign in dual:
        return 'dual'
    return None

def is_benefic(planet):
    """Check if planet is natural benefic"""
    return planet in ['Jupiter', 'Venus', 'Mercury', 'Moon']  # Moon when waxing

def is_malefic(planet):
    """Check if planet is natural malefic"""
    return planet in ['Sun', 'Mars', 'Saturn', 'Rahu', 'Ketu']

def get_house_type(house):
    """Get the type of house - Kendra, Trikona, Dusthana, etc."""
    kendras = [1, 4, 7, 10]
    trikonas = [1, 5, 9]  # 1 is both
    dusthanas = [6, 8, 12]
    upachayas = [3, 6, 10, 11]
    
    types = []
    if house in kendras:
        types.append('kendra')
    if house in trikonas:
        types.append('trikona')
    if house in dusthanas:
        types.append('dusthana')
    if house in upachayas:
        types.append('upachaya')
    return types if types else ['neutral']
