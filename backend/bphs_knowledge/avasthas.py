# BPHS Planetary Avasthas (States)
# From Brihat Parashara Hora Shastra Chapter 45

"""
Avasthas (States) of Planets - BPHS Ch. 45
The state of a planet determines the percentage of its results it can deliver
"""

# ============================================
# BAAL ADI AVASTHAS (Age-Based States)
# ============================================

BAAL_ADI_AVASTHAS = {
    'baal': {
        'name': 'Baal (Infant)',
        'degree_range_odd': (0, 6),
        'degree_range_even': (24, 30),
        'result_percentage': 25,
        'description': 'Planet in infant state gives one-fourth results'
    },
    'kumar': {
        'name': 'Kumar (Youthful)',
        'degree_range_odd': (6, 12),
        'degree_range_even': (18, 24),
        'result_percentage': 50,
        'description': 'Planet in youthful state gives half results'
    },
    'yuva': {
        'name': 'Yuva (Adolescent)',
        'degree_range_odd': (12, 18),
        'degree_range_even': (12, 18),
        'result_percentage': 100,
        'description': 'Planet in adolescent state gives full results'
    },
    'vriddha': {
        'name': 'Vriddha (Old)',
        'degree_range_odd': (18, 24),
        'degree_range_even': (6, 12),
        'result_percentage': 5,
        'description': 'Planet in old state gives negligible results'
    },
    'mrita': {
        'name': 'Mrita (Dead)',
        'degree_range_odd': (24, 30),
        'degree_range_even': (0, 6),
        'result_percentage': 0,
        'description': 'Planet in dead state gives nil results'
    }
}

# ============================================
# JAGRAT ADI AVASTHAS (Consciousness States)
# ============================================

JAGRAT_ADI_AVASTHAS = {
    'jagrat': {
        'name': 'Jagrat (Awakening)',
        'condition': 'Planet in own sign or exaltation',
        'result_percentage': 100,
        'description': 'Full results in awakened state'
    },
    'swapna': {
        'name': 'Swapna (Dreaming)',
        'condition': 'Planet in friend\'s or neutral sign',
        'result_percentage': 50,
        'description': 'Medium results in dreaming state'
    },
    'sushupti': {
        'name': 'Sushupti (Sleeping)',
        'condition': 'Planet in enemy\'s sign or debilitation',
        'result_percentage': 0,
        'description': 'Nil results in sleeping state'
    }
}

# ============================================
# DEEPTADI AVASTHAS (9 States Based on Dignity)
# ============================================

DEEPTADI_AVASTHAS = {
    'deepta': {
        'name': 'Deepta (Brilliant)',
        'condition': 'Planet in exaltation',
        'effect': 'Excellent results, high visibility'
    },
    'swastha': {
        'name': 'Swastha (Healthy)',
        'condition': 'Planet in own sign',
        'effect': 'Good health-related results'
    },
    'pramudita': {
        'name': 'Pramudita (Delighted)',
        'condition': 'Planet in great friend\'s sign',
        'effect': 'Joyful, happy results'
    },
    'shanta': {
        'name': 'Shanta (Peaceful)',
        'condition': 'Planet in friend\'s sign',
        'effect': 'Peaceful, harmonious results'
    },
    'dina': {
        'name': 'Dina (Weak)',
        'condition': 'Planet in neutral sign',
        'effect': 'Weak, limited results'
    },
    'vikala': {
        'name': 'Vikala (Distressed)',
        'condition': 'Planet conjunct malefic',
        'effect': 'Distressed, troubled results'
    },
    'dukhita': {
        'name': 'Dukhita (Sorrowful)',
        'condition': 'Planet in enemy\'s sign',
        'effect': 'Sorrowful results'
    },
    'khala': {
        'name': 'Khala (Wicked)',
        'condition': 'Planet in great enemy\'s sign',
        'effect': 'Negative, harmful results'
    },
    'kopa': {
        'name': 'Kopa (Angry)',
        'condition': 'Planet combusted by Sun',
        'effect': 'Angry, frustrated results'
    }
}

# ============================================
# LAJJITADI AVASTHAS (6 Special States)
# ============================================

LAJJITADI_AVASTHAS = {
    'lajjita': {
        'name': 'Lajjita (Ashamed)',
        'condition': 'Planet in 5th house conjunct Rahu/Ketu/Sun/Saturn/Mars',
        'effects': [
            'Aversion to God',
            'Loss of intelligence',
            'Loss of children',
            'Interest in evil speeches',
            'Listlessness in good things'
        ]
    },
    'garvita': {
        'name': 'Garvita (Proud)',
        'condition': 'Planet in exaltation or Moolatrikona',
        'effects': [
            'Happiness through new houses and gardens',
            'Regal status',
            'Skill in arts',
            'Financial gains at all times',
            'Improvement in business'
        ]
    },
    'kshudhita': {
        'name': 'Kshudhita (Hungry)',
        'condition': 'Planet in enemy sign, conjunct enemy, aspected by enemy, or conjunct Saturn',
        'effects': [
            'Downfall due to grief and passion',
            'Grief on account of relatives',
            'Physical decline',
            'Troubles from enemies',
            'Financial distress',
            'Loss of physical strength',
            'Eclipsed mind due to miseries'
        ]
    },
    'trushita': {
        'name': 'Trushita (Thirsty)',
        'condition': 'Planet in watery sign, aspected by malefic, not aspected by benefic',
        'effects': [
            'Diseases through association with females',
            'Leading over wicked deeds',
            'Loss of wealth due to own people',
            'Physical weakness',
            'Miseries caused by evil people',
            'Decline of honor'
        ]
    },
    'mudita': {
        'name': 'Mudita (Happy)',
        'condition': 'Planet in friendly sign, conjunct/aspected by benefic, or conjunct Jupiter',
        'effects': [
            'Residences, clothes, ornaments',
            'Happiness from lands and wife',
            'Happiness from relatives',
            'Living in royal places',
            'Destruction of enemies',
            'Acquisition of wisdom and learning'
        ]
    },
    'kshobhita': {
        'name': 'Kshobhita (Agitated)',
        'condition': 'Planet conjunct Sun, aspected by/conjunct malefic, aspected by enemy',
        'effects': [
            'Acute penury',
            'Evil disposition',
            'Miseries',
            'Financial debacles',
            'Distress to feet',
            'Obstruction to income due to royal wrath'
        ]
    }
}

# ============================================
# SHAYANADI AVASTHAS (12 Activity States)
# ============================================

SHAYANADI_AVASTHAS = {
    1: {
        'name': 'Shayan (Lying Down)',
        'effects': {
            'Sun': 'Digestive deficiency, many diseases, stoutness of legs, bilious vitiation, heart strokes',
            'Moon': 'Honorable, sluggish, given to lust, financial destruction',
            'Mars': 'Troubled by wounds, itch, ulcer',
            'Mercury': 'Lame, reddish eyes if in Lagna; licentious pleasures if elsewhere',
            'Jupiter': 'Strong but speaks in whispers, tawny complexion, fear from enemies',
            'Venus': 'Strong but dental disease, short-tempered, seeks courtezans',
            'Saturn': 'Troubled by hunger and thirst, diseases in boyhood, wealthy later'
        }
    },
    2: {
        'name': 'Upaveshan (Sitting)',
        'effects': {
            'Sun': 'Poverty, carries loads, litigations, hard-hearted, wicked',
            'Moon': 'Troubled by diseases, dull-witted, negligible wealth, hard-hearted',
            'Mars': 'Strong, sinful, untruthful, eminent, wealthy, bereft of virtues',
            'Mercury': 'Possesses virtues if in Lagna; results vary with aspects',
            'Jupiter': 'Garrulous, proud, troubled by king and enemies, ulcers',
            'Venus': 'Endowed with gems, golden ornaments, ever happy, destroys enemies',
            'Saturn': 'Troubled by enemies, dangers, ulcers, self-respected, punished by king'
        }
    },
    3: {
        'name': 'Netrapani (Hands on Eyes)',
        'effects': {
            'Sun': 'Happy, wise, helpful, wealthy, royal favors (in 5,7,9,10); eye diseases elsewhere',
            'Moon': 'Troubled by diseases, garrulous, wicked, bad deeds',
            'Mars': 'Penury if in Lagna; rulership of city elsewhere',
            'Mercury': 'Devoid of learning, wisdom, satisfaction; but honorable',
            'Jupiter': 'Afflicted by diseases, devoid of wealth, fond of music, attached to other castes',
            'Venus': 'Loss of wealth due to eye diseases in 1,7,10; large houses elsewhere',
            'Saturn': 'Endowed with charming female, wealth, royal favor, many arts, eloquent'
        }
    },
    4: {
        'name': 'Prakash (Shining)',
        'effects': {
            'Sun': 'Liberal, wealthy, significant speaker, meritorious, strong, charming',
            'Moon': 'Famous in world, virtues exposed through royal patronage, visits shrines',
            'Mars': 'Shines with virtues, honored by king; loss of children/wife in 5th house',
            'Mercury': 'Charitable, merciful, meritorious, great discrimination, destroys evil',
            'Jupiter': 'Virtues, happy, splendorous, visits holy places; great if exalted',
            'Venus': 'Sports like lofty elephant, equal to king, skilled in poetry/music if dignified',
            'Saturn': 'Very virtuous, wealthy, intelligent, sportive, merciful, devoted to Shiva'
        }
    },
    5: {
        'name': 'Gaman (Going)',
        'effects': {
            'Sun': 'Lives in foreign places, miserable, indolent, bereft of intelligence and wealth',
            'Moon': 'Sinful, cruel, afflictions of sight if waning; fear if waxing',
            'Mars': 'Always roaming, fear of ulcers, misunderstandings with females, financial decline',
            'Mercury': 'Visits courts of kings, Goddess Lakshmi dwells in abode',
            'Jupiter': 'Adventurous, happy on account of friends, scholarly, Vedic learning',
            'Venus': 'Short-lived mother, lamenting separation from own people, fear from enemies',
            'Saturn': 'Very rich, endowed with sons, grabs enemy lands, scholar at royal court'
        }
    },
    6: {
        'name': 'Agaman (Coming)',
        'effects': {
            'Sun': 'Interested in others\' wives, devoid of own people, dirty, ill-disposed, tale bearer',
            'Moon': 'Honorable, diseases of feet, secretly sinful, poor, devoid of intelligence',
            'Mars': 'Virtuous, precious gems, walks majestically, destroys enemies',
            'Mercury': 'Same as Gaman - visits courts of kings, wealthy',
            'Jupiter': 'Serving force, excellent women, wealth never leave abode',
            'Venus': 'Abundant wealth, visits superior shrines, enthusiastic, hand/foot diseases',
            'Saturn': 'Akin to donkey, bereft of wife and children happiness, roams pitiably'
        }
    },
    7: {
        'name': 'Sabha (Assembly)',
        'effects': {
            'Sun': 'Helps others, endowed with wealth and gems, virtuous, lands, new houses',
            'Moon': 'Eminent among men, honored by kings, beautiful, subdues women\'s passion',
            'Mars': 'If exalted: skilled in wars, flag of righteousness, wealthy',
            'Mercury': 'If exalted: affluent, meritorious, equal to Kuber, devoted to Vishnu/Shiva',
            'Jupiter': 'Comparable to Guru in speech, superior corals/rubies, rich, supremely learned',
            'Venus': 'Eminence in king\'s court, virtuous, destroys enemies, equal to Kuber',
            'Saturn': 'Great possessions of precious stones and gold, great judicial knowledge'
        }
    },
    8: {
        'name': 'Agam (Coming Back)',
        'effects': {
            'Sun': 'Distressed due to enemies, fickle-minded, evil-minded, emaciated, proud',
            'Moon': 'Garrulous, virtuous; if dark fortnight: two wives, sick, wicked, violent',
            'Mars': 'Devoid of virtues, distressed by diseases, ear diseases, gout, timid',
            'Mercury': 'Serves base men, gains wealth thereby, two sons, one fame-bringing daughter',
            'Jupiter': 'Endowed with conveyances, honors, children, wife, friends, learning',
            'Venus': 'No advent of wealth, troubles from enemies, separation, diseases',
            'Saturn': 'Incurs diseases, not skilled in earning royal patronage'
        }
    },
    9: {
        'name': 'Bhojan (Eating)',
        'effects': {
            'Sun': 'Pains in joints, loses money due to females, untruthful, headaches',
            'Moon': 'If full: honor, conveyances, attendants, wife, daughters; if dark: none',
            'Mars': 'If strong: eats sweet food; if weak: base acts, dishonorable',
            'Mercury': 'Financial losses through litigations, physical loss from king, fickle-minded',
            'Jupiter': 'Always gets excellent food, horses, elephants, chariots; Lakshmi never leaves',
            'Venus': 'Distressed by hunger, diseases, fear from enemies; if in Virgo: very rich',
            'Saturn': 'Enjoys tastes of food, weak-sighted, fickle-minded due to mental delusion'
        }
    },
    10: {
        'name': 'Nritya Lipsa (Desire to Dance)',
        'effects': {
            'Sun': 'Honored by learned, scholar, knowledge of poetry, adored by kings',
            'Moon': 'If strong: strong, knowledge of songs, critic of beauty; if weak: sinful',
            'Mars': 'Earns wealth through king, house full of gold, diamonds, corals',
            'Mercury': 'Honor, conveyances, corals, sons, friends, prowess, scholarship',
            'Jupiter': 'Royal honors, wealthy, knowledge of Dharma and Tantra, great grammarian',
            'Venus': 'Skilled in literature, intelligent, plays musical instruments, meritorious',
            'Saturn': 'Righteous, extremely opulent, honored by king, brave, heroic in war'
        }
    },
    11: {
        'name': 'Kautuk (Curiosity)',
        'effects': {
            'Sun': 'Always happy, Vedic knowledge, performs Yagyas, moves amidst kings',
            'Moon': 'Attains kingship, lordship over wealth, skill in sexual acts',
            'Mars': 'Curious disposition, endowed with friends and sons; if exalted: honored',
            'Mercury': 'If in Lagna: skilled in music; if in 7,8: addicted to courtezans',
            'Jupiter': 'Curious, very rich, shines like Sun, exceedingly kind, happy',
            'Venus': 'Equal to Lord Indra, great in assembly, learned, Lakshmi always present',
            'Saturn': 'Endowed with lands and wealth, happy, pleasures through charming females'
        }
    },
    12: {
        'name': 'Nidra (Sleep)',
        'effects': {
            'Sun': 'Tendency to be drowsy, lives in foreign places, harm to wife, financial destruction',
            'Moon': 'If with Jupiter waxing: quite eminent; otherwise: loses wealth due to females',
            'Mars': 'Short-tempered, devoid of intelligence and wealth, wicked, troubled by diseases',
            'Mercury': 'Uncomfortable sleep, neck diseases, devoid of co-born, miseries, litigations',
            'Jupiter': 'Foolish in undertakings, irredeemable penury, devoid of righteous acts',
            'Venus': 'Interested in serving others, blames others, heroic, garrulous, wandering',
            'Saturn': 'Rich, endowed with charming virtues, valorous, destroys fierce enemies'
        }
    }
}

# ============================================
# AVASTHA CALCULATION FORMULA
# ============================================

SHAYANADI_CALCULATION = """
Formula for Shayan Adi Avastha:
(s × p × n) + (a + g + r)
------------------------- mod 12 = Avastha
Where:
s = Serial number of star occupied by planet (from Ashwini)
p = Planet number (Sun=1, Moon=2, Mars=3, Mercury=4, Jupiter=5, Venus=6, Saturn=7)
n = Navamsha position (1-9)
a = Janma Nakshatra (birth star)
g = Birth Ghati (time in ghatis)
r = Lagna order from Aries (Aries=1, Taurus=2, etc.)

Sub-state calculation:
Stage 1: (A × A + f) / 12 = R
Stage 2: (R + pa) / 3 = sub-state
Where f = first syllable value of name, pa = planet additive

Sub-states:
1 = Drishti (medium results)
2 = Cheshta (full results)
0 = Vicheshta (negligible results)
"""

# Planet additives for sub-state calculation
PLANET_ADDITIVES = {
    'Sun': 5,
    'Moon': 2,
    'Mars': 2,
    'Mercury': 3,
    'Jupiter': 5,
    'Venus': 3,
    'Saturn': 3,
    'Rahu': 4,
    'Ketu': 4
}

# First syllable values (Anka)
SYLLABLE_VALUES = {
    'a': 1, 'ka': 1, 'cha': 1, 'da': 1, 'va': 1,
    'i': 2, 'kha': 2, 'ja': 2, 'sha': 2,
    'u': 3, 'ga': 3, 'jha': 3, 'ta': 3, 'pa': 3, 'ya': 3,
    'e': 4, 'gha': 4, 'tha': 4, 'pha': 4, 'ra': 4, 'ma': 4,
    'o': 5, 'ha': 5
}

# Source reference
AVASTHA_SOURCE = 'BPHS Ch. 45, Slokas 1-155'
