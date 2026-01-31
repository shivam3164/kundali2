# BPHS Planetary Strengths (Shadbala)
# From Brihat Parashara Hora Shastra Chapter 27

"""
Shadbala (Six-fold Strength) of Planets - BPHS Ch. 27
This determines the actual strength of planets to deliver results
"""

# ============================================
# SHADBALA COMPONENTS - BPHS Ch. 27
# ============================================

SHADBALA_COMPONENTS = {
    'sthana_bala': {
        'name': 'Sthana Bala (Positional Strength)',
        'weight': 'Primary',
        'components': {
            'uccha_bala': {
                'name': 'Exaltation Strength',
                'max_value': 60,
                'unit': 'Virupas',
                'calculation': 'Based on distance from exaltation point',
                'description': 'Maximum at exaltation, zero at debilitation'
            },
            'saptavargaja_bala': {
                'name': 'Divisional Strength',
                'max_value': 45,
                'unit': 'Virupas',
                'calculation': 'Based on placement in 7 vargas',
                'description': 'Strength from D1, D2, D3, D7, D9, D12, D30'
            },
            'ojhayugma_bala': {
                'name': 'Odd-Even Strength',
                'max_value': 15,
                'unit': 'Virupas',
                'calculation': 'Based on odd/even sign and navamsha placement',
                'rules': {
                    'Moon_Venus': 'Gain strength in even signs',
                    'others': 'Gain strength in odd signs'
                }
            },
            'kendradi_bala': {
                'name': 'Angular Strength',
                'max_value': 60,
                'unit': 'Virupas',
                'calculation': 'Based on house position',
                'values': {
                    'kendra': 60,     # Houses 1, 4, 7, 10
                    'panapara': 30,   # Houses 2, 5, 8, 11
                    'apoklima': 15    # Houses 3, 6, 9, 12
                }
            },
            'drekkana_bala': {
                'name': 'Decanate Strength',
                'max_value': 15,
                'unit': 'Virupas',
                'calculation': 'Based on decanate placement',
                'rules': {
                    'male_planets': 'Strong in 1st decanate',
                    'neutral_planets': 'Strong in 2nd decanate',
                    'female_planets': 'Strong in 3rd decanate'
                }
            }
        },
        'source': 'BPHS Ch. 27, Slokas 3-14'
    },
    'dig_bala': {
        'name': 'Dig Bala (Directional Strength)',
        'weight': 'Primary',
        'max_value': 60,
        'unit': 'Virupas',
        'calculation': 'Based on house position relative to directional strength',
        'directional_strengths': {
            'Sun': {'direction': 'South', 'strong_house': 10, 'weak_house': 4},
            'Moon': {'direction': 'North', 'strong_house': 4, 'weak_house': 10},
            'Mars': {'direction': 'South', 'strong_house': 10, 'weak_house': 4},
            'Mercury': {'direction': 'East', 'strong_house': 1, 'weak_house': 7},
            'Jupiter': {'direction': 'East', 'strong_house': 1, 'weak_house': 7},
            'Venus': {'direction': 'North', 'strong_house': 4, 'weak_house': 10},
            'Saturn': {'direction': 'West', 'strong_house': 7, 'weak_house': 1}
        },
        'source': 'BPHS Ch. 27, Slokas 15-17'
    },
    'kala_bala': {
        'name': 'Kala Bala (Temporal Strength)',
        'weight': 'Primary',
        'components': {
            'nathonnatha_bala': {
                'name': 'Day/Night Strength',
                'max_value': 60,
                'unit': 'Virupas',
                'rules': {
                    'day_strong': ['Sun', 'Jupiter', 'Venus'],
                    'night_strong': ['Moon', 'Mars', 'Saturn'],
                    'always_strong': ['Mercury']
                }
            },
            'paksha_bala': {
                'name': 'Fortnight Strength',
                'max_value': 60,
                'unit': 'Virupas',
                'rules': {
                    'shukla_paksha': 'Benefics gain strength',
                    'krishna_paksha': 'Malefics gain strength'
                }
            },
            'tribhaga_bala': {
                'name': 'Three-Part Day/Night Strength',
                'max_value': 60,
                'unit': 'Virupas',
                'rules': {
                    'first_third_day': 'Mercury strong',
                    'middle_third_day': 'Sun strong',
                    'last_third_day': 'Saturn strong',
                    'first_third_night': 'Moon strong',
                    'middle_third_night': 'Venus strong',
                    'last_third_night': 'Mars strong',
                    'always': 'Jupiter always strong'
                }
            },
            'abda_bala': {
                'name': 'Year Lord Strength',
                'max_value': 15,
                'unit': 'Virupas',
                'description': 'Strength for being lord of the year'
            },
            'masa_bala': {
                'name': 'Month Lord Strength',
                'max_value': 30,
                'unit': 'Virupas',
                'description': 'Strength for being lord of the month'
            },
            'vara_bala': {
                'name': 'Weekday Lord Strength',
                'max_value': 45,
                'unit': 'Virupas',
                'description': 'Strength for being lord of the weekday'
            },
            'hora_bala': {
                'name': 'Hour Lord Strength',
                'max_value': 60,
                'unit': 'Virupas',
                'description': 'Strength for being lord of the hora'
            },
            'ayana_bala': {
                'name': 'Solstice Strength',
                'max_value': 60,
                'unit': 'Virupas',
                'rules': {
                    'uttarayana_strong': ['Sun', 'Mars', 'Jupiter'],
                    'dakshinayana_strong': ['Moon', 'Saturn'],
                    'neutral': ['Mercury', 'Venus']
                }
            },
            'yuddha_bala': {
                'name': 'War Strength',
                'max_value': 60,
                'unit': 'Virupas',
                'description': 'Strength gained/lost in planetary war'
            }
        },
        'source': 'BPHS Ch. 27, Slokas 18-31'
    },
    'cheshta_bala': {
        'name': 'Cheshta Bala (Motional Strength)',
        'weight': 'Primary',
        'max_value': 60,
        'unit': 'Virupas',
        'states': {
            'vakra': {'name': 'Retrograde', 'strength': 60},
            'anuvakra': {'name': 'Entering retrograde', 'strength': 30},
            'vikala': {'name': 'Stationary', 'strength': 15},
            'manda': {'name': 'Slow motion', 'strength': 15},
            'mandatara': {'name': 'Very slow', 'strength': 7.5},
            'sama': {'name': 'Normal speed', 'strength': 30},
            'chara': {'name': 'Fast motion', 'strength': 45},
            'atichara': {'name': 'Very fast', 'strength': 30}
        },
        'note': 'Sun and Moon only have Ayana Bala as Cheshta Bala',
        'source': 'BPHS Ch. 27, Slokas 32-35'
    },
    'naisargika_bala': {
        'name': 'Naisargika Bala (Natural Strength)',
        'weight': 'Constant',
        'max_value': 60,
        'unit': 'Virupas',
        'values': {
            'Sun': 60,
            'Moon': 51.43,
            'Venus': 42.85,
            'Jupiter': 34.28,
            'Mercury': 25.71,
            'Mars': 17.14,
            'Saturn': 8.57
        },
        'source': 'BPHS Ch. 27, Sloka 36'
    },
    'drik_bala': {
        'name': 'Drik Bala (Aspectual Strength)',
        'weight': 'Variable',
        'max_value': 60,
        'unit': 'Virupas',
        'calculation': 'Based on benefic/malefic aspects received',
        'rules': {
            'benefic_aspect': 'Adds to strength',
            'malefic_aspect': 'Subtracts from strength'
        },
        'source': 'BPHS Ch. 27, Slokas 37-40'
    }
}

# ============================================
# MINIMUM REQUIRED STRENGTH - BPHS
# ============================================

MINIMUM_SHADBALA = {
    'Sun': {'rupas': 5.0, 'virupas': 300, 'description': 'Minimum for Sun to give good results'},
    'Moon': {'rupas': 6.0, 'virupas': 360, 'description': 'Minimum for Moon to give good results'},
    'Mars': {'rupas': 5.0, 'virupas': 300, 'description': 'Minimum for Mars to give good results'},
    'Mercury': {'rupas': 7.0, 'virupas': 420, 'description': 'Minimum for Mercury to give good results'},
    'Jupiter': {'rupas': 6.5, 'virupas': 390, 'description': 'Minimum for Jupiter to give good results'},
    'Venus': {'rupas': 5.5, 'virupas': 330, 'description': 'Minimum for Venus to give good results'},
    'Saturn': {'rupas': 5.0, 'virupas': 300, 'description': 'Minimum for Saturn to give good results'}
}

# ============================================
# BHAVA BALA (HOUSE STRENGTH)
# ============================================

BHAVA_BALA_COMPONENTS = {
    'bhavadhipati_bala': {
        'name': 'House Lord Strength',
        'description': 'Strength derived from house lord\'s Shadbala'
    },
    'bhava_digbala': {
        'name': 'House Directional Strength',
        'description': 'Strength based on house cusp position'
    },
    'bhava_drishti_bala': {
        'name': 'House Aspectual Strength',
        'description': 'Strength from aspects on house'
    }
}

# ============================================
# ISHTA AND KASHTA PHALA - BPHS Ch. 27
# ============================================

ISHTA_KASHTA = {
    'ishta_phala': {
        'name': 'Auspicious Result',
        'calculation': 'From Uccha Bala and Cheshta Bala',
        'formula': '(Uccha Bala + Cheshta Bala) × 0.5',
        'description': 'Indicates capacity to do good'
    },
    'kashta_phala': {
        'name': 'Inauspicious Result',
        'calculation': '60 - Ishta Phala',
        'description': 'Indicates capacity to cause harm'
    }
}

# ============================================
# PLANETARY DIGNITY AND STRENGTH
# ============================================

DIGNITY_STRENGTHS = {
    'exalted': {
        'sthana_bala_contribution': 60,
        'overall_effect': 'Maximum positive results',
        'percentage': 100
    },
    'moolatrikona': {
        'sthana_bala_contribution': 45,
        'overall_effect': 'Very strong positive results',
        'percentage': 90
    },
    'own_sign': {
        'sthana_bala_contribution': 30,
        'overall_effect': 'Strong positive results',
        'percentage': 80
    },
    'great_friend': {
        'sthana_bala_contribution': 22.5,
        'overall_effect': 'Good positive results',
        'percentage': 70
    },
    'friend': {
        'sthana_bala_contribution': 15,
        'overall_effect': 'Moderately positive results',
        'percentage': 60
    },
    'neutral': {
        'sthana_bala_contribution': 7.5,
        'overall_effect': 'Average results',
        'percentage': 50
    },
    'enemy': {
        'sthana_bala_contribution': 3.75,
        'overall_effect': 'Weak results',
        'percentage': 30
    },
    'great_enemy': {
        'sthana_bala_contribution': 1.875,
        'overall_effect': 'Very weak results',
        'percentage': 20
    },
    'debilitated': {
        'sthana_bala_contribution': 0,
        'overall_effect': 'Negative results (unless cancelled)',
        'percentage': 0
    }
}

# ============================================
# NEECHABHANGA (DEBILITATION CANCELLATION)
# ============================================

NEECHABHANGA_RULES = {
    'rule_1': {
        'condition': 'Lord of the sign occupied by debilitated planet is in Kendra from Moon or Lagna',
        'effect': 'Debilitation cancelled, forms Raja Yoga'
    },
    'rule_2': {
        'condition': 'Lord of the exaltation sign of debilitated planet is in Kendra from Moon or Lagna',
        'effect': 'Debilitation cancelled, forms Raja Yoga'
    },
    'rule_3': {
        'condition': 'Planet who exalts in the sign of debilitation aspects the debilitated planet',
        'effect': 'Debilitation cancelled'
    },
    'rule_4': {
        'condition': 'Planet who is lord of debilitation sign aspects the debilitated planet',
        'effect': 'Debilitation cancelled'
    },
    'rule_5': {
        'condition': 'Debilitated planet is in Kendra from Moon or Lagna',
        'effect': 'Partial cancellation'
    },
    'rule_6': {
        'condition': 'Debilitated planet is exalted in Navamsha',
        'effect': 'Debilitation greatly reduced'
    },
    'neechabhanga_raja_yoga': {
        'condition': 'When debilitation is cancelled strongly',
        'effect': 'Person rises from humble beginnings to great heights',
        'examples': 'Many kings and leaders have this yoga'
    }
}

# ============================================
# VIMSOPAKA BALA (20-Point Strength)
# ============================================

VIMSOPAKA_DIGNITY_POINTS = {
    'own_sign': 20,
    'great_friend': 18,
    'friend': 15,
    'neutral': 10,
    'enemy': 7,
    'great_enemy': 5
}

VIMSOPAKA_DESIGNATIONS = {
    (16, 20): 'Sri Vallabha - Extremely strong',
    (14, 16): 'Goloka - Very strong',
    (12, 14): 'Chakra Simhasana - Strong',
    (10, 12): 'Dhanvantari - Good',
    (8, 10): 'Poornachandra - Average',
    (6, 8): 'Chandana Vana - Weak',
    (4, 6): 'Kalpa Vriksha - Very weak',
    (2, 4): 'Kerala - Extremely weak',
    (0, 2): 'Bhedaka - Almost nil'
}

# ============================================
# COMBUSTION AND STRENGTH LOSS
# ============================================

COMBUSTION_EFFECTS = {
    'Moon': {
        'combustion_orb': 12,  # degrees
        'strength_loss': 'Loses 50% of its strength',
        'exception': 'New Moon considered natural'
    },
    'Mars': {
        'combustion_orb': 17,
        'strength_loss': 'Loses Cheshta Bala',
        'effect': 'Anger issues, accidents'
    },
    'Mercury': {
        'combustion_orb': 14,
        'strength_loss': 'Loses intellectual clarity',
        'exception': 'If retrograde, only 12 degrees'
    },
    'Jupiter': {
        'combustion_orb': 11,
        'strength_loss': 'Loses wisdom and guidance',
        'effect': 'Poor judgment'
    },
    'Venus': {
        'combustion_orb': 10,
        'strength_loss': 'Loses relationship harmony',
        'exception': 'If retrograde, only 8 degrees'
    },
    'Saturn': {
        'combustion_orb': 15,
        'strength_loss': 'Loses patience and persistence',
        'effect': 'Hasty decisions'
    }
}

# Source reference
SHADBALA_SOURCE = 'BPHS Ch. 27, Slokas 1-45'
