# BPHS House Interpretations
# From Brihat Parashara Hora Shastra Chapters 11-25

"""
Complete House Interpretation Data from BPHS
Each house contains:
- Basic significations
- Planet effects in house
- House lord effects when placed in various houses
- Remedial measures
"""

# ============================================
# HOUSE SIGNIFICATIONS - BPHS Ch. 11-23
# ============================================

HOUSE_SIGNIFICATIONS = {
    1: {
        "name": "Tanu Bhava",
        "english": "House of Self",
        "karaka": "Sun",
        "body_parts": ["Head", "Brain", "Physical appearance", "General constitution"],
        "significations": {
            "primary": ["Self", "Body", "Health", "Longevity", "Character", "Fame"],
            "secondary": ["Beginning of life", "General fortune", "Dignity", "Honor", "Complexion"],
        },
        "represents": "The native's physical body, personality, general health, fame, and the beginning of life",
        "natural_sign": "Aries",
        "element_association": "Fire - Initiative, self-expression",
        "benefic_occupation": "Good health, fame, longevity, happiness, attractive appearance",
        "malefic_occupation": "Health issues, struggles, obstacles, injury-prone",
        "lord_strong": "Native is healthy, prosperous, confident, well-built, respected",
        "lord_weak": "Health problems, lack of confidence, struggles in early life",
        "source": "BPHS Ch. 11, Sloka 1-7"
    },
    2: {
        "name": "Dhana Bhava",
        "english": "House of Wealth",
        "karaka": "Jupiter",
        "body_parts": ["Face", "Right eye", "Mouth", "Tongue", "Teeth", "Nose"],
        "significations": {
            "primary": ["Wealth", "Family", "Speech", "Food", "Early education"],
            "secondary": ["Accumulated assets", "Bank balance", "Precious stones", "Truthfulness"],
        },
        "represents": "Wealth, family values, speech, food habits, early childhood, and accumulated resources",
        "natural_sign": "Taurus",
        "element_association": "Earth - Material security, resources",
        "benefic_occupation": "Wealthy, sweet speech, happy family, good food, precious gems",
        "malefic_occupation": "Financial troubles, harsh speech, family discord, dental problems",
        "lord_strong": "Wealthy, good family life, sweet speech, accumulates assets easily",
        "lord_weak": "Financial struggles, family problems, speech defects",
        "source": "BPHS Ch. 12"
    },
    3: {
        "name": "Sahaja Bhava",
        "english": "House of Siblings",
        "karaka": "Mars",
        "body_parts": ["Right ear", "Shoulders", "Arms", "Hands", "Collar bone"],
        "significations": {
            "primary": ["Siblings", "Courage", "Short journeys", "Communication", "Skills"],
            "secondary": ["Neighbors", "Valor", "Hobbies", "Writing", "Self-effort"],
        },
        "represents": "Younger siblings, courage, short travels, communication skills, and self-efforts",
        "natural_sign": "Gemini",
        "element_association": "Air - Communication, movement",
        "benefic_occupation": "Brave, good siblings, artistic skills, successful short journeys",
        "malefic_occupation": "Sibling troubles, accidents in travel, lack of courage",
        "lord_strong": "Valorous, helpful siblings, good communication, artistic talent",
        "lord_weak": "Sibling problems, lack of courage, accidents, ear problems",
        "source": "BPHS Ch. 13"
    },
    4: {
        "name": "Bandhu Bhava",
        "english": "House of Mother/Home",
        "karaka": "Moon",
        "body_parts": ["Chest", "Lungs", "Heart", "Breasts"],
        "significations": {
            "primary": ["Mother", "Home", "Property", "Vehicles", "Education", "Happiness"],
            "secondary": ["Land", "Domestic peace", "Ancestral property", "Comfort", "Final years"],
        },
        "represents": "Mother, home, landed property, vehicles, formal education, and inner happiness",
        "natural_sign": "Cancer",
        "element_association": "Water - Emotions, nurturing",
        "benefic_occupation": "Happy home, loving mother, properties, vehicles, good education",
        "malefic_occupation": "Domestic troubles, mother's health issues, property losses",
        "lord_strong": "Owns property, vehicles, happy home, good education, maternal blessings",
        "lord_weak": "Lack of domestic happiness, mother troubles, property disputes",
        "source": "BPHS Ch. 14"
    },
    5: {
        "name": "Putra Bhava",
        "english": "House of Children",
        "karaka": "Jupiter",
        "body_parts": ["Stomach", "Upper abdomen", "Spine"],
        "significations": {
            "primary": ["Children", "Intelligence", "Education", "Creativity", "Romance"],
            "secondary": ["Speculation", "Past life merit", "Mantras", "Devotion", "Stomach"],
        },
        "represents": "Children, creative intelligence, higher education, romance, and past life karma (Purva Punya)",
        "natural_sign": "Leo",
        "element_association": "Fire - Creativity, self-expression",
        "benefic_occupation": "Intelligent, blessed children, creative, speculative gains, romantic",
        "malefic_occupation": "Child troubles, lack of intelligence, failed romance, stomach issues",
        "lord_strong": "Blessed with children, highly intelligent, creative, spiritually inclined",
        "lord_weak": "Child problems, lack of creativity, poor judgment, stomach ailments",
        "source": "BPHS Ch. 15"
    },
    6: {
        "name": "Ari Bhava",
        "english": "House of Enemies",
        "karaka": "Mars/Saturn",
        "body_parts": ["Intestines", "Waist", "Navel region", "Lower abdomen"],
        "significations": {
            "primary": ["Enemies", "Diseases", "Debts", "Service", "Obstacles"],
            "secondary": ["Maternal uncle", "Pets", "Routine work", "Competition", "Litigation"],
        },
        "represents": "Enemies, diseases, debts, service, daily work routine, and obstacles",
        "natural_sign": "Virgo",
        "element_association": "Earth - Service, health",
        "benefic_occupation": "Overcomes enemies, good health, success in service, wins competitions",
        "malefic_occupation": "Chronic diseases, debt troubles, enemy harassment, work problems",
        "lord_strong": "Conquers enemies, recovers from illness, clears debts, wins legal battles",
        "lord_weak": "Health issues, persistent enemies, debt problems, service difficulties",
        "source": "BPHS Ch. 16"
    },
    7: {
        "name": "Yuvati Bhava",
        "english": "House of Marriage",
        "karaka": "Venus",
        "body_parts": ["Lower back", "Kidneys", "Reproductive organs", "Bladder"],
        "significations": {
            "primary": ["Marriage", "Spouse", "Partnerships", "Business", "Foreign travel"],
            "secondary": ["Public dealings", "Contracts", "Legal bonds", "Death (maraka)"],
        },
        "represents": "Marriage, spouse, partnerships, business relationships, and public dealings",
        "natural_sign": "Libra",
        "element_association": "Air - Relationships, balance",
        "benefic_occupation": "Happy marriage, good spouse, successful partnerships, foreign gains",
        "malefic_occupation": "Marital discord, spouse problems, partnership failures, kidney issues",
        "lord_strong": "Happy marriage, devoted spouse, successful business partnerships",
        "lord_weak": "Marriage delays, spouse troubles, partnership losses, relationship problems",
        "source": "BPHS Ch. 17"
    },
    8: {
        "name": "Randhra Bhava",
        "english": "House of Longevity",
        "karaka": "Saturn",
        "body_parts": ["Private parts", "Chronic diseases", "Anus", "Pelvic region"],
        "significations": {
            "primary": ["Longevity", "Death", "Transformation", "Occult", "Inheritance"],
            "secondary": ["Sudden events", "Research", "Insurance", "Spouse's wealth", "Mysteries"],
        },
        "represents": "Longevity, death, transformation, hidden matters, occult sciences, and inheritance",
        "natural_sign": "Scorpio",
        "element_association": "Water - Transformation, hidden depths",
        "benefic_occupation": "Long life, inheritance, occult knowledge, research abilities",
        "malefic_occupation": "Sudden troubles, chronic illness, accidents, scandals",
        "lord_strong": "Long life, gains through inheritance, occult wisdom, transformative experiences",
        "lord_weak": "Health concerns, sudden obstacles, hidden enemies, scandals",
        "source": "BPHS Ch. 18"
    },
    9: {
        "name": "Dharma Bhava",
        "english": "House of Fortune",
        "karaka": "Jupiter",
        "body_parts": ["Thighs", "Hips", "Arterial system"],
        "significations": {
            "primary": ["Fortune", "Father", "Guru", "Religion", "Long journeys"],
            "secondary": ["Higher learning", "Dharma", "Grandchildren", "Temple", "Luck"],
        },
        "represents": "Fortune, father, guru, religion, higher education, long journeys, and dharma",
        "natural_sign": "Sagittarius",
        "element_association": "Fire - Expansion, wisdom",
        "benefic_occupation": "Very fortunate, blessed father, religious, higher education, travels",
        "malefic_occupation": "Father troubles, lack of fortune, irreligious, obstacles in higher learning",
        "lord_strong": "Highly fortunate, blessed by father and guru, spiritual, educated",
        "lord_weak": "Misfortune, father problems, lack of higher education, irreligious",
        "source": "BPHS Ch. 19"
    },
    10: {
        "name": "Karma Bhava",
        "english": "House of Career",
        "karaka": "Sun/Mercury/Jupiter/Saturn",
        "body_parts": ["Knees", "Joints", "Bones"],
        "significations": {
            "primary": ["Career", "Profession", "Status", "Authority", "Government"],
            "secondary": ["Father's longevity", "Fame", "Rank", "Commerce", "Public image"],
        },
        "represents": "Career, profession, reputation, social status, government, and authority",
        "natural_sign": "Capricorn",
        "element_association": "Earth - Achievement, structure",
        "benefic_occupation": "Successful career, high status, government favor, fame",
        "malefic_occupation": "Career obstacles, bad reputation, problems with authority",
        "lord_strong": "Excellent career, high position, respected, government connections",
        "lord_weak": "Career struggles, lack of recognition, problems with authority figures",
        "source": "BPHS Ch. 20"
    },
    11: {
        "name": "Labha Bhava",
        "english": "House of Gains",
        "karaka": "Jupiter",
        "body_parts": ["Left ear", "Ankles", "Calves", "Shins"],
        "significations": {
            "primary": ["Gains", "Income", "Elder siblings", "Friends", "Desires"],
            "secondary": ["Social circle", "Profits", "Hopes", "Aspirations", "Recovery from illness"],
        },
        "represents": "Gains, income, elder siblings, friends, social networks, and fulfillment of desires",
        "natural_sign": "Aquarius",
        "element_association": "Air - Social connections, aspirations",
        "benefic_occupation": "Abundant gains, elder sibling blessings, good friends, desires fulfilled",
        "malefic_occupation": "Limited gains, elder sibling troubles, false friends, unfulfilled desires",
        "lord_strong": "Multiple income sources, supportive friends, elder siblings help, wishes fulfilled",
        "lord_weak": "Financial limitations, friend betrayals, elder sibling problems",
        "source": "BPHS Ch. 21"
    },
    12: {
        "name": "Vyaya Bhava",
        "english": "House of Loss",
        "karaka": "Saturn",
        "body_parts": ["Left eye", "Feet", "Sleep patterns"],
        "significations": {
            "primary": ["Expenses", "Losses", "Foreign lands", "Liberation", "Sleep"],
            "secondary": ["Hospitalization", "Imprisonment", "Hidden enemies", "Charity", "Moksha"],
        },
        "represents": "Expenses, losses, foreign residence, isolation, spirituality, and final liberation (Moksha)",
        "natural_sign": "Pisces",
        "element_association": "Water - Dissolution, transcendence",
        "benefic_occupation": "Spiritual gains, foreign success, good sleep, charitable, moksha",
        "malefic_occupation": "Heavy expenses, hospitalization, hidden enemies, imprisonment",
        "lord_strong": "Spiritual evolution, foreign gains, peaceful sleep, charitable nature",
        "lord_weak": "Excessive losses, sleep problems, hidden enemies, isolation",
        "source": "BPHS Ch. 22-23"
    }
}

# ============================================
# PLANETS IN HOUSES - Effects from BPHS
# ============================================

PLANET_IN_HOUSE_EFFECTS = {
    "Sun": {
        1: {
            "effect": "Strong personality, leadership qualities, good health, government favor",
            "positive": ["Natural leader", "Confident", "Recognized", "Healthy constitution"],
            "negative": ["Ego issues", "Dominating nature"],
            "source": "BPHS"
        },
        2: {
            "effect": "Wealth through government or authority, strong speech, family pride",
            "positive": ["Authoritative speech", "Family wealth", "Respected in family"],
            "negative": ["Harsh speech possible", "Eye problems"],
            "source": "BPHS"
        },
        3: {
            "effect": "Brave, courageous, good relationship with siblings, interest in arts",
            "positive": ["Valorous", "Self-made", "Good siblings"],
            "negative": ["Conflicts with siblings if afflicted"],
            "source": "BPHS"
        },
        4: {
            "effect": "Government land/property, authority in home, strong mother connection",
            "positive": ["Property from government", "Domestic authority", "Political connections"],
            "negative": ["Mother's health if afflicted", "Domestic ego clashes"],
            "source": "BPHS"
        },
        5: {
            "effect": "Creative intelligence, success in speculation, good children",
            "positive": ["Brilliant mind", "Success in investments", "Talented children"],
            "negative": ["Ego in romance", "Issues with first child if afflicted"],
            "source": "BPHS"
        },
        6: {
            "effect": "Victory over enemies, service in government, health awareness",
            "positive": ["Defeats enemies", "Government service", "Strong immunity"],
            "negative": ["Health issues (digestive)", "Father's enemies"],
            "source": "BPHS"
        },
        7: {
            "effect": "Dominant spouse or partner, business with government, public recognition",
            "positive": ["Successful partnerships", "Public fame", "Government contracts"],
            "negative": ["Spouse ego clashes", "Late marriage"],
            "source": "BPHS"
        },
        8: {
            "effect": "Interest in occult, inheritance from father, research abilities",
            "positive": ["Occult knowledge", "Inheritance", "Transformation"],
            "negative": ["Health concerns", "Eye problems", "Father's longevity"],
            "source": "BPHS"
        },
        9: {
            "effect": "Very fortunate, religious, good father, pilgrimage, higher learning",
            "positive": ["Highly fortunate", "Blessed father", "Religious", "Higher education"],
            "negative": ["Father abroad or distant"],
            "source": "BPHS"
        },
        10: {
            "effect": "Excellent career, government position, authority, fame",
            "positive": ["Career success", "High position", "Government favor", "Famous"],
            "negative": ["Workaholic tendencies"],
            "source": "BPHS"
        },
        11: {
            "effect": "Gains through government, influential friends, elder sibling success",
            "positive": ["Abundant gains", "Powerful friends", "Fulfilled desires"],
            "negative": ["Elder sibling rivalry if afflicted"],
            "source": "BPHS"
        },
        12: {
            "effect": "Spiritual inclinations, foreign government work, expenditure on good causes",
            "positive": ["Spiritual growth", "Foreign success", "Charity"],
            "negative": ["Father abroad", "Eye problems", "Loss of position"],
            "source": "BPHS"
        }
    },
    "Moon": {
        1: {
            "effect": "Attractive personality, emotional nature, public appeal, travels",
            "positive": ["Charming", "Popular", "Adaptable", "Nurturing"],
            "negative": ["Emotional fluctuations", "Restless mind"],
            "source": "BPHS"
        },
        2: {
            "effect": "Wealth fluctuations, sweet speech, food lover, family oriented",
            "positive": ["Sweet speech", "Family happiness", "Love for food"],
            "negative": ["Income fluctuations", "Emotional eating"],
            "source": "BPHS"
        },
        3: {
            "effect": "Emotional courage, close to sisters, short journeys, artistic",
            "positive": ["Creative communication", "Good sisters", "Artistic"],
            "negative": ["Emotional decisions", "Restless in one place"],
            "source": "BPHS"
        },
        4: {
            "effect": "Happy home, loving mother, property gains, emotional security",
            "positive": ["Domestic happiness", "Mother's blessings", "Property", "Vehicles"],
            "negative": ["Too attached to home", "Mother's health focus"],
            "source": "BPHS"
        },
        5: {
            "effect": "Emotional intelligence, love for children, creative, romantic",
            "positive": ["Many children", "Creative mind", "Romantic", "Intuitive"],
            "negative": ["Emotional in romance", "Overthinking"],
            "source": "BPHS"
        },
        6: {
            "effect": "Health fluctuations (especially digestion), service to others, emotional enemies",
            "positive": ["Caring in service", "Healing abilities"],
            "negative": ["Digestive issues", "Emotional enemies", "Worry-prone"],
            "source": "BPHS"
        },
        7: {
            "effect": "Emotional marriage, beautiful spouse, public dealings, partnerships",
            "positive": ["Loving spouse", "Happy marriage", "Public popularity"],
            "negative": ["Emotional dependency", "Multiple relationships possible"],
            "source": "BPHS"
        },
        8: {
            "effect": "Emotional upheavals, interest in mysteries, inheritance through mother",
            "positive": ["Intuitive", "Psychic abilities", "Research mind"],
            "negative": ["Emotional turmoil", "Mother's health concerns"],
            "source": "BPHS"
        },
        9: {
            "effect": "Spiritual emotions, fortunate, religious mother, pilgrimages",
            "positive": ["Spiritual", "Fortunate travels", "Religious"],
            "negative": ["Emotional about beliefs"],
            "source": "BPHS"
        },
        10: {
            "effect": "Public career, emotional reputation, career changes, popularity",
            "positive": ["Public fame", "Popular career", "Nurturing profession"],
            "negative": ["Career fluctuations", "Public emotional exposure"],
            "source": "BPHS"
        },
        11: {
            "effect": "Gains through public, many friends, emotional fulfillment",
            "positive": ["Many friends", "Social gains", "Desires fulfilled"],
            "negative": ["Emotional friends", "Fluctuating income"],
            "source": "BPHS"
        },
        12: {
            "effect": "Spiritual, foreign lands, sleep important, emotional isolation",
            "positive": ["Spiritual growth", "Foreign gains", "Intuitive dreams"],
            "negative": ["Sleep issues", "Emotional isolation", "Hidden sorrows"],
            "source": "BPHS"
        }
    },
    "Mars": {
        1: {
            "effect": "Energetic, athletic, competitive, courageous, aggressive",
            "positive": ["Strong body", "Courageous", "Athletic", "Leader"],
            "negative": ["Aggressive", "Injury-prone", "Manglik effects"],
            "source": "BPHS"
        },
        2: {
            "effect": "Harsh speech, family conflicts, wealth through courage, land property",
            "positive": ["Direct speech", "Property gains", "Family protector"],
            "negative": ["Harsh words", "Family disputes", "Eye/face issues"],
            "source": "BPHS"
        },
        3: {
            "effect": "Very brave, self-made, good with hands, younger sibling dynamics",
            "positive": ["Extremely courageous", "Technical skills", "Self-effort"],
            "negative": ["Sibling conflicts", "Rash decisions"],
            "source": "BPHS"
        },
        4: {
            "effect": "Property through effort, domestic conflicts, strong conveyances",
            "positive": ["Land property", "Vehicles", "Strong determination"],
            "negative": ["Domestic unrest", "Mother's health", "Property disputes"],
            "source": "BPHS"
        },
        5: {
            "effect": "Active children, competitive intelligence, sports, speculation risks",
            "positive": ["Sports talent", "Quick mind", "Active children"],
            "negative": ["Speculation losses", "Child health concerns", "Impulsive romance"],
            "source": "BPHS"
        },
        6: {
            "effect": "Defeats enemies, wins competitions, surgical abilities, service success",
            "positive": ["Victory over enemies", "Wins competitions", "Medical field"],
            "negative": ["Accidents", "Inflammatory diseases"],
            "source": "BPHS - Excellent placement"
        },
        7: {
            "effect": "Passionate marriage, business conflicts, Manglik effects",
            "positive": ["Passionate spouse", "Business drive"],
            "negative": ["Marital conflicts", "Partnership disputes", "Manglik dosha"],
            "source": "BPHS"
        },
        8: {
            "effect": "Accidents, surgery, occult interests, inheritance through fights",
            "positive": ["Occult research", "Inheritance", "Transformation through crisis"],
            "negative": ["Accidents", "Surgery", "Sudden events"],
            "source": "BPHS"
        },
        9: {
            "effect": "Active in religion, father conflicts, adventurous travels",
            "positive": ["Religious warrior", "Adventure travel", "Sports in higher education"],
            "negative": ["Father conflicts", "Aggressive beliefs"],
            "source": "BPHS"
        },
        10: {
            "effect": "Successful career in action fields, authority, government/military",
            "positive": ["Career success", "Authority", "Military/police/surgery"],
            "negative": ["Work conflicts", "Aggressive with authority"],
            "source": "BPHS - Good placement"
        },
        11: {
            "effect": "Gains through courage, active elder siblings, competitive friends",
            "positive": ["Gains through effort", "Influential friends", "Goals achieved"],
            "negative": ["Sibling competition", "Friend conflicts"],
            "source": "BPHS - Good placement"
        },
        12: {
            "effect": "Expenses on conflicts, foreign lands, hidden enemies, bed pleasures",
            "positive": ["Foreign success through effort", "Tantric abilities"],
            "negative": ["Hidden enemies", "Hospitalization", "Sleep issues"],
            "source": "BPHS"
        }
    },
    "Mercury": {
        1: {
            "effect": "Intelligent, communicative, youthful appearance, versatile",
            "positive": ["Sharp intellect", "Good communication", "Youthful", "Witty"],
            "negative": ["Nervous energy", "Overthinking", "Indecisive"],
            "source": "BPHS"
        },
        2: {
            "effect": "Wealthy through intelligence, excellent speech, business acumen",
            "positive": ["Business mind", "Eloquent speech", "Financial intelligence"],
            "negative": ["Talks about money", "Calculative"],
            "source": "BPHS"
        },
        3: {
            "effect": "Excellent communication, writing skills, media, younger siblings",
            "positive": ["Writer", "Media skills", "Good siblings", "Short travel"],
            "negative": ["Too many interests", "Restless mind"],
            "source": "BPHS - Excellent placement"
        },
        4: {
            "effect": "Educated, intelligent mother, property through business",
            "positive": ["Higher education", "Intelligent mother", "Home business"],
            "negative": ["Mental restlessness at home"],
            "source": "BPHS"
        },
        5: {
            "effect": "Highly intelligent, creative writing, smart children",
            "positive": ["Brilliant mind", "Creative intelligence", "Smart children"],
            "negative": ["Overthinking in romance", "Nervous children"],
            "source": "BPHS"
        },
        6: {
            "effect": "Analytical in service, health through nerves, intellectual enemies",
            "positive": ["Analytical work", "Service success", "Problem solver"],
            "negative": ["Nervous disorders", "Anxiety", "Skin issues"],
            "source": "BPHS"
        },
        7: {
            "effect": "Business partnerships, intelligent spouse, contracts",
            "positive": ["Business success", "Communicative spouse", "Legal skills"],
            "negative": ["Over-analysis of partner", "Multiple interests"],
            "source": "BPHS"
        },
        8: {
            "effect": "Research mind, occult study, inheritance calculation",
            "positive": ["Research abilities", "Occult study", "Insurance/tax work"],
            "negative": ["Nervous about death", "Anxiety about hidden matters"],
            "source": "BPHS"
        },
        9: {
            "effect": "Higher learning, philosophical mind, religious texts, teaching",
            "positive": ["Higher education", "Teaching", "Publishing", "Philosophy"],
            "negative": ["Dogmatic if afflicted"],
            "source": "BPHS"
        },
        10: {
            "effect": "Career in communication, business success, accounting",
            "positive": ["Business career", "Communication field", "Accounting"],
            "negative": ["Multiple career changes"],
            "source": "BPHS"
        },
        11: {
            "effect": "Gains through intellect, networking, intelligent friends",
            "positive": ["Network gains", "Intelligent friends", "Multiple income sources"],
            "negative": ["Scattered goals"],
            "source": "BPHS - Good placement"
        },
        12: {
            "effect": "Foreign languages, imagination, spiritual study",
            "positive": ["Foreign language skills", "Imaginative", "Spiritual texts"],
            "negative": ["Nervous sleep", "Anxiety", "Isolation"],
            "source": "BPHS"
        }
    },
    "Jupiter": {
        1: {
            "effect": "Wise, optimistic, religious, blessed personality, teacher",
            "positive": ["Wisdom", "Optimism", "Religious", "Respected", "Good health"],
            "negative": ["Weight gain", "Over-confidence"],
            "source": "BPHS - Excellent placement"
        },
        2: {
            "effect": "Wealthy, wise speech, good family, precious possessions",
            "positive": ["Wealth", "Family happiness", "Truthful speech", "Good values"],
            "negative": ["Overindulgence in food"],
            "source": "BPHS"
        },
        3: {
            "effect": "Religious siblings, wise communication, auspicious travels",
            "positive": ["Wise communication", "Religious siblings", "Blessed efforts"],
            "negative": ["Less dynamic energy"],
            "source": "BPHS"
        },
        4: {
            "effect": "Happy home, wise mother, property, vehicles, education",
            "positive": ["Domestic happiness", "Large house", "Good education", "Vehicles"],
            "negative": ["Attachment to comfort"],
            "source": "BPHS - Excellent placement"
        },
        5: {
            "effect": "Blessed children, high intelligence, spiritual, speculation gains",
            "positive": ["Blessed children", "Brilliant", "Spiritual", "Good investments"],
            "negative": ["Over-expectation from children"],
            "source": "BPHS - Excellent placement"
        },
        6: {
            "effect": "Overcomes enemies through wisdom, service in education/law",
            "positive": ["Wins through wisdom", "Legal success", "Teaching service"],
            "negative": ["Liver issues", "Enemies through over-optimism"],
            "source": "BPHS"
        },
        7: {
            "effect": "Wise spouse, happy marriage, successful partnerships, legal",
            "positive": ["Happy marriage", "Wise spouse", "Business success", "Legal"],
            "negative": ["Spouse may dominate through wisdom"],
            "source": "BPHS"
        },
        8: {
            "effect": "Long life, inheritance, occult wisdom, transformation through knowledge",
            "positive": ["Longevity", "Inheritance", "Occult wisdom", "Insurance gains"],
            "negative": ["Debilitated here - challenges in transformation"],
            "source": "BPHS"
        },
        9: {
            "effect": "Extremely fortunate, religious, guru, father blessings",
            "positive": ["Highly fortunate", "Religious leader", "Father blessed", "Travels"],
            "negative": ["Over-religious if afflicted"],
            "source": "BPHS - Own house, excellent"
        },
        10: {
            "effect": "Excellent career, high position, respected, judge/teacher",
            "positive": ["Career success", "High position", "Respected", "Fame"],
            "negative": ["Career in traditional fields only"],
            "source": "BPHS - Excellent placement"
        },
        11: {
            "effect": "Abundant gains, influential friends, elder sibling blessings",
            "positive": ["Multiple gains", "Wealthy friends", "Elder sibling success"],
            "negative": ["Over-optimistic about gains"],
            "source": "BPHS - Excellent placement"
        },
        12: {
            "effect": "Spiritual liberation, foreign residence, charitable, moksha",
            "positive": ["Spiritual growth", "Foreign gains", "Charity", "Moksha yoga"],
            "negative": ["Excessive spending on good causes"],
            "source": "BPHS"
        }
    },
    "Venus": {
        1: {
            "effect": "Attractive, artistic, charming, pleasure-loving, beautiful",
            "positive": ["Beauty", "Charm", "Artistic", "Comfortable life"],
            "negative": ["Vanity", "Self-indulgence"],
            "source": "BPHS"
        },
        2: {
            "effect": "Wealthy, sweet speech, beautiful face, precious items",
            "positive": ["Wealth", "Beautiful speech", "Luxury items", "Family harmony"],
            "negative": ["Overindulgence", "Materialistic"],
            "source": "BPHS - Good placement"
        },
        3: {
            "effect": "Artistic skills, beautiful sisters, pleasant journeys",
            "positive": ["Artistic", "Good sisters", "Pleasant travels", "Media"],
            "negative": ["Sensual siblings issues"],
            "source": "BPHS"
        },
        4: {
            "effect": "Beautiful home, luxury vehicles, comforts, happy mother",
            "positive": ["Luxurious home", "Nice vehicles", "Comfort", "Happy"],
            "negative": ["Attachment to luxury"],
            "source": "BPHS - Excellent placement"
        },
        5: {
            "effect": "Romantic, beautiful children, creative arts, entertainment",
            "positive": ["Romance", "Beautiful children", "Arts", "Entertainment"],
            "negative": ["Multiple romances", "Over-indulgent children"],
            "source": "BPHS"
        },
        6: {
            "effect": "Service in arts/beauty, enemies through pleasures",
            "positive": ["Beauty/fashion career", "Wins through charm"],
            "negative": ["Relationship with servants", "Health through indulgence"],
            "source": "BPHS"
        },
        7: {
            "effect": "Beautiful spouse, happy marriage, successful partnerships",
            "positive": ["Happy marriage", "Beautiful spouse", "Partnership success"],
            "negative": ["Too focused on partner", "Multiple relationships"],
            "source": "BPHS - Own house, excellent"
        },
        8: {
            "effect": "Inheritance of luxuries, secret affairs, spouse's wealth",
            "positive": ["Inheritance", "Spouse's wealth", "Occult arts"],
            "negative": ["Secret relationships", "Reproductive issues"],
            "source": "BPHS"
        },
        9: {
            "effect": "Fortunate in love, artistic religion, beautiful journeys",
            "positive": ["Fortunate", "Religious arts", "Beautiful travels"],
            "negative": ["Affair with religious person possible"],
            "source": "BPHS"
        },
        10: {
            "effect": "Career in arts/beauty/entertainment, public charm",
            "positive": ["Arts career", "Entertainment", "Fashion", "Public popularity"],
            "negative": ["Scandals in career if afflicted"],
            "source": "BPHS"
        },
        11: {
            "effect": "Gains through arts, beautiful friends, elder sister success",
            "positive": ["Gains through beauty", "Artistic friends", "Luxury gains"],
            "negative": ["Friends through pleasure only"],
            "source": "BPHS - Good placement"
        },
        12: {
            "effect": "Bed pleasures, foreign luxury, spiritual arts, expenses on comfort",
            "positive": ["Sexual happiness", "Foreign luxury", "Spiritual arts"],
            "negative": ["Secret affairs", "Excessive spending on pleasure"],
            "source": "BPHS - Good for pleasures"
        }
    },
    "Saturn": {
        1: {
            "effect": "Hardworking, disciplined, serious, delayed success, thin body",
            "positive": ["Disciplined", "Hardworking", "Longevity", "Eventually successful"],
            "negative": ["Early struggles", "Health issues", "Delays"],
            "source": "BPHS"
        },
        2: {
            "effect": "Slow wealth accumulation, harsh speech, family restrictions",
            "positive": ["Eventually wealthy", "Conservative with money"],
            "negative": ["Family troubles", "Speech problems", "Dental issues"],
            "source": "BPHS"
        },
        3: {
            "effect": "Patient courage, younger sibling challenges, methodical efforts",
            "positive": ["Patient efforts", "Eventually successful in skills"],
            "negative": ["Sibling troubles", "Delayed courage"],
            "source": "BPHS - Good placement (Upachaya)"
        },
        4: {
            "effect": "Old property, domestic responsibilities, mother's health",
            "positive": ["Old/ancestral property", "Stable home eventually"],
            "negative": ["Domestic troubles", "Mother's health", "Less comfort"],
            "source": "BPHS"
        },
        5: {
            "effect": "Delayed children, serious intelligence, traditional education",
            "positive": ["Deep thinker", "Traditional education", "Eventually children"],
            "negative": ["Child delays", "Lack of joy", "Speculation losses"],
            "source": "BPHS"
        },
        6: {
            "effect": "Defeats enemies through persistence, chronic health but overcomes",
            "positive": ["Eventually conquers enemies", "Success in service"],
            "negative": ["Chronic diseases", "Long-term obstacles"],
            "source": "BPHS - Good placement (Upachaya)"
        },
        7: {
            "effect": "Delayed/older spouse, business delays, serious partnerships",
            "positive": ["Stable marriage eventually", "Mature spouse"],
            "negative": ["Marriage delays", "Cold relationships", "Partner older"],
            "source": "BPHS"
        },
        8: {
            "effect": "Long life, chronic issues, slow inheritance, research",
            "positive": ["Longevity", "Occult research", "Deep transformation"],
            "negative": ["Chronic illness", "Long struggles", "Delays"],
            "source": "BPHS"
        },
        9: {
            "effect": "Father challenges, traditional religion, late fortune",
            "positive": ["Traditional values", "Late fortune", "Deep philosophy"],
            "negative": ["Father troubles", "Religious restrictions", "Late luck"],
            "source": "BPHS"
        },
        10: {
            "effect": "Career through hard work, authority through discipline",
            "positive": ["Career success through effort", "Authority", "Government"],
            "negative": ["Slow career rise", "Work pressures", "Late success"],
            "source": "BPHS - Good placement"
        },
        11: {
            "effect": "Gains through patience, older friends, long-term goals",
            "positive": ["Steady gains", "Reliable friends", "Goals achieved eventually"],
            "negative": ["Delayed fulfillment", "Elder sibling troubles"],
            "source": "BPHS - Good placement (Upachaya)"
        },
        12: {
            "effect": "Spiritual discipline, foreign lands, isolation, detachment",
            "positive": ["Spiritual growth", "Foreign residence", "Moksha tendency"],
            "negative": ["Hospitalization", "Isolation", "Hidden expenses"],
            "source": "BPHS"
        }
    },
    "Rahu": {
        1: {
            "effect": "Ambitious personality, unconventional, foreign connections",
            "positive": ["Ambitious", "Unique personality", "Foreign success"],
            "negative": ["Identity confusion", "Health mysteries", "Obsessive"],
            "source": "BPHS"
        },
        2: {
            "effect": "Wealth through unconventional means, family mysteries",
            "positive": ["Unusual wealth sources", "Foreign money"],
            "negative": ["Family secrets", "Speech issues", "Dietary problems"],
            "source": "BPHS"
        },
        3: {
            "effect": "Brave in unusual ways, media success, foreign siblings",
            "positive": ["Media/technology skills", "Unconventional courage"],
            "negative": ["Sibling estrangement", "Communication confusion"],
            "source": "BPHS - Good placement (Upachaya)"
        },
        4: {
            "effect": "Foreign property, unusual home, mother mysteries",
            "positive": ["Foreign property", "Unusual vehicles", "Tech at home"],
            "negative": ["Mother troubles", "Domestic unrest", "Heart issues"],
            "source": "BPHS"
        },
        5: {
            "effect": "Unusual children, unconventional creativity, foreign romance",
            "positive": ["Unique creativity", "Foreign romance", "Technical skills"],
            "negative": ["Child issues", "Speculation obsession", "Confusion in love"],
            "source": "BPHS"
        },
        6: {
            "effect": "Defeats enemies powerfully, unusual diseases, foreign service",
            "positive": ["Powerful over enemies", "Success in competition", "Medical field"],
            "negative": ["Mysterious diseases", "Obsessive about health"],
            "source": "BPHS - Good placement (Upachaya)"
        },
        7: {
            "effect": "Foreign/unconventional spouse, unusual partnerships",
            "positive": ["Foreign spouse", "Unusual business success"],
            "negative": ["Marriage confusion", "Partner from different background"],
            "source": "BPHS"
        },
        8: {
            "effect": "Sudden transformations, occult mastery, foreign inheritance",
            "positive": ["Occult powers", "Sudden gains", "Research"],
            "negative": ["Sudden losses", "Mysterious events", "Health scares"],
            "source": "BPHS"
        },
        9: {
            "effect": "Foreign religion, unconventional beliefs, foreign father",
            "positive": ["Foreign education", "Unusual philosophy", "Tech guru"],
            "negative": ["Father issues", "Religious confusion", "Dogmatic"],
            "source": "BPHS"
        },
        10: {
            "effect": "Career in foreign/technology/unconventional fields",
            "positive": ["Tech career", "Foreign career", "Fame through unusual means"],
            "negative": ["Career instability", "Reputation issues"],
            "source": "BPHS - Good placement (Upachaya)"
        },
        11: {
            "effect": "Gains through foreign/technology, unusual friends",
            "positive": ["Large gains", "Foreign friends", "Tech network"],
            "negative": ["Deceptive friends", "Unfulfilled obsessions"],
            "source": "BPHS - Excellent placement (Upachaya)"
        },
        12: {
            "effect": "Foreign residence, spiritual obsession, mysterious expenses",
            "positive": ["Foreign settlement", "Spiritual growth", "Moksha through unusual path"],
            "negative": ["Hidden enemies", "Sleep disorders", "Imprisonment fears"],
            "source": "BPHS"
        }
    },
    "Ketu": {
        1: {
            "effect": "Spiritual personality, detached, past life skills",
            "positive": ["Spiritual", "Intuitive", "Past life talents"],
            "negative": ["Identity issues", "Health mysteries", "Detached"],
            "source": "BPHS"
        },
        2: {
            "effect": "Detachment from family/wealth, speech issues, spiritual values",
            "positive": ["Spiritual values", "Not materialistic"],
            "negative": ["Family separation", "Wealth loss", "Speech problems"],
            "source": "BPHS"
        },
        3: {
            "effect": "Spiritual courage, sibling separation, intuitive skills",
            "positive": ["Intuitive communication", "Spiritual courage"],
            "negative": ["Sibling distance", "Lack of worldly courage"],
            "source": "BPHS"
        },
        4: {
            "effect": "Detachment from home, spiritual mother, past life property karma",
            "positive": ["Spiritual home", "Moksha tendency", "Inner peace"],
            "negative": ["Mother separation", "No property", "Domestic unrest"],
            "source": "BPHS"
        },
        5: {
            "effect": "Spiritual children, past life intelligence, detached romance",
            "positive": ["Spiritual intelligence", "Past life merit", "Intuitive"],
            "negative": ["Child issues", "Romance disappointments", "Speculation loss"],
            "source": "BPHS"
        },
        6: {
            "effect": "Spiritual service, overcomes enemies through detachment",
            "positive": ["Service without ego", "Health through spirituality"],
            "negative": ["Mysterious diseases", "Strange enemies"],
            "source": "BPHS - Good placement"
        },
        7: {
            "effect": "Spiritual spouse, detached partnerships, past life marriage karma",
            "positive": ["Spiritual marriage", "Partner helps moksha"],
            "negative": ["Marriage issues", "Partner detachment", "Separation"],
            "source": "BPHS"
        },
        8: {
            "effect": "Occult mastery, moksha, sudden spiritual transformation",
            "positive": ["Occult powers", "Moksha yoga", "Deep research"],
            "negative": ["Sudden losses", "Mysterious events"],
            "source": "BPHS - Good for spirituality"
        },
        9: {
            "effect": "Spiritual inclination, father karma, past life religious merit",
            "positive": ["Deep spirituality", "Past life blessings"],
            "negative": ["Father issues", "Confused beliefs"],
            "source": "BPHS"
        },
        10: {
            "effect": "Detachment from career, spiritual profession",
            "positive": ["Spiritual career", "Healing professions"],
            "negative": ["Career instability", "Lack of ambition"],
            "source": "BPHS"
        },
        11: {
            "effect": "Spiritual gains, detached from desires, unusual friends",
            "positive": ["Spiritual fulfillment", "Not materialistic"],
            "negative": ["Limited worldly gains", "Friend separation"],
            "source": "BPHS"
        },
        12: {
            "effect": "Moksha, liberation, spiritual enlightenment, foreign ashram",
            "positive": ["Moksha yoga", "Spiritual liberation", "Enlightenment"],
            "negative": ["Isolation", "Expenses", "Past life debts"],
            "source": "BPHS - Excellent for spirituality"
        }
    }
}

# ============================================
# HOUSE LORD PLACEMENT EFFECTS - Full BPHS Ch. 24
# ============================================

HOUSE_LORD_IN_HOUSES = {
    1: {  # Lagna Lord placements
        1: {"effect": "Endowed with physical happiness and prowess, intelligent, two wives", "source": "BPHS Ch.24, Sl.1"},
        2: {"effect": "Gainful, scholarly, happy, good qualities, religious, many wives", "source": "BPHS Ch.24, Sl.2"},
        3: {"effect": "Valorous like lion, all kinds of wealth, honorable, two wives, intelligent", "source": "BPHS Ch.24, Sl.3"},
        4: {"effect": "Paternal and maternal happiness, many brothers, lustful, virtuous, charming", "source": "BPHS Ch.24, Sl.4"},
        5: {"effect": "Mediocre progenic happiness, loses first child, honorable, angry, dear to king", "source": "BPHS Ch.24, Sl.5"},
        6: {"effect": "Devoid of physical happiness, troubled by enemies if no benefic aspect", "source": "BPHS Ch.24, Sl.6"},
        7: {"effect": "Wife may not live long (if malefic), wanders aimlessly, penury (if benefic but weak)", "source": "BPHS Ch.24, Sl.7"},
        8: {"effect": "Accomplished scholar, sickly, thievish, angry, gambler, joins others' wives", "source": "BPHS Ch.24, Sl.8"},
        9: {"effect": "Fortunate, dear to people, devotee of Vishnu, skilled, eloquent, blessed with wife and sons", "source": "BPHS Ch.24, Sl.9"},
        10: {"effect": "Paternal happiness, royal honor, fame, self-earned wealth", "source": "BPHS Ch.24, Sl.10"},
        11: {"effect": "Always endowed with gains, good qualities, fame, many wives", "source": "BPHS Ch.24, Sl.11"},
        12: {"effect": "Bereft of physical happiness, spends unfruitfully, given to anger", "source": "BPHS Ch.24, Sl.12"}
    },
    2: {  # Dhana Lord placements
        1: {"effect": "Endowed with sons and wealth, inimical to family, lustful, hard-hearted", "source": "BPHS Ch.24, Sl.13"},
        2: {"effect": "Wealthy, proud, two or more wives, bereft of progeny", "source": "BPHS Ch.24, Sl.14"},
        3: {"effect": "Valorous, wise, virtuous, lustful, miserly (if benefic)", "source": "BPHS Ch.24, Sl.15"},
        4: {"effect": "Acquires all kinds of wealth, equal to king if with Jupiter exalted", "source": "BPHS Ch.24, Sl.16"},
        5: {"effect": "Wealthy, sons also intent on earning wealth", "source": "BPHS Ch.24, Sl.17"},
        6: {"effect": "Gains wealth through enemies (if benefic), loss through enemies (if malefic)", "source": "BPHS Ch.24, Sl.18"},
        7: {"effect": "Addicted to others' wives, doctor, wife questionable if malefic", "source": "BPHS Ch.24, Sl.19"},
        8: {"effect": "Abundant land and wealth, limited marital felicity", "source": "BPHS Ch.24, Sl.20"},
        9: {"effect": "Wealthy, diligent, skilled, sick in childhood, happy later", "source": "BPHS Ch.24, Sl.21"},
        10: {"effect": "Libidinous, honorable, learned, many wives, much wealth", "source": "BPHS Ch.24, Sl.22"},
        11: {"effect": "All kinds of wealth, ever diligent, honorable, famous", "source": "BPHS Ch.24, Sl.23"},
        12: {"effect": "Adventurous, devoid of wealth, interested in others' wealth", "source": "BPHS Ch.24, Sl.24"}
    },
    3: {  # Sahaj Lord placements
        1: {"effect": "Self-made wealth, disposed to worship, valorous, intelligent", "source": "BPHS Ch.24, Sl.25"},
        2: {"effect": "Corpulent, devoid of valor, not happy, eyes on others' wealth", "source": "BPHS Ch.24, Sl.26"},
        3: {"effect": "Happiness through siblings, wealth and sons, cheerful", "source": "BPHS Ch.24, Sl.27"},
        4: {"effect": "Happy, wealthy, intelligent, acquires wicked spouse", "source": "BPHS Ch.24, Sl.28"},
        5: {"effect": "Has sons, virtuous, formidable wife if malefic aspect", "source": "BPHS Ch.24, Sl.29"},
        6: {"effect": "Inimical to siblings, affluent, dear to maternal aunt", "source": "BPHS Ch.24, Sl.30"},
        7: {"effect": "Interested in serving king, unhappy in boyhood, happy later", "source": "BPHS Ch.24, Sl.31"},
        8: {"effect": "Thief, derives livelihood serving others, dies at royal gate", "source": "BPHS Ch.24, Sl.32"},
        9: {"effect": "Lacks paternal bliss, fortunes through wife", "source": "BPHS Ch.24, Sl.33"},
        10: {"effect": "All kinds of happiness, self-made wealth, nurtures females", "source": "BPHS Ch.24, Sl.34"},
        11: {"effect": "Always gains in trading, intelligent, adventurous", "source": "BPHS Ch.24, Sl.35"},
        12: {"effect": "Spends on evil deeds, wicked father, fortunate through wife", "source": "BPHS Ch.24, Sl.36"}
    },
    4: {  # Bandhu Lord placements
        1: {"effect": "Endowed with learning, virtues, ornaments, lands, vehicles, maternal happiness", "source": "BPHS Ch.24, Sl.37"},
        2: {"effect": "Enjoys pleasures, all kinds of wealth, family life, honor, adventurous", "source": "BPHS Ch.24, Sl.38"},
        3: {"effect": "Valorous, has servants, liberal, virtuous, charitable", "source": "BPHS Ch.24, Sl.39"},
        4: {"effect": "Minister, all kinds of wealth, skillful, virtuous, honorable, happy spouse", "source": "BPHS Ch.24, Sl.40"},
        5: {"effect": "Happy, liked by all, devoted to Vishnu, virtuous, self-earned wealth", "source": "BPHS Ch.24, Sl.41"},
        6: {"effect": "Devoid of maternal happiness, angry, thief, indisposed", "source": "BPHS Ch.24, Sl.42"},
        7: {"effect": "High education, sacrifices patrimony, silent in assembly", "source": "BPHS Ch.24, Sl.43"},
        8: {"effect": "Devoid of domestic comforts, not much parental happiness", "source": "BPHS Ch.24, Sl.44"},
        9: {"effect": "Dear to all, devoted to God, virtuous, honorable, all happiness", "source": "BPHS Ch.24, Sl.45"},
        10: {"effect": "Royal honors, alchemist, extremely pleased, conquers senses", "source": "BPHS Ch.24, Sl.46"},
        11: {"effect": "Fear of secret disease, liberal, virtuous, charitable", "source": "BPHS Ch.24, Sl.47"},
        12: {"effect": "Devoid of domestic comforts, vices, foolish, indolent", "source": "BPHS Ch.24, Sl.48"}
    },
    5: {  # Putra Lord placements
        1: {"effect": "Scholarly, progenic happiness, miser, crooked, steals others' wealth", "source": "BPHS Ch.24, Sl.49"},
        2: {"effect": "Many sons and wealth, pater familias, honorable, famous", "source": "BPHS Ch.24, Sl.50"},
        3: {"effect": "Attached to siblings, tale bearer, miser, interested in own work", "source": "BPHS Ch.24, Sl.51"},
        4: {"effect": "Happy, maternal happiness, wealth, intelligence, king or minister", "source": "BPHS Ch.24, Sl.52"},
        5: {"effect": "Progeny if benefic, no issues if malefic, virtuous, dear to friends", "source": "BPHS Ch.24, Sl.53"},
        6: {"effect": "Sons equal to enemies, or loses them, adopted son possible", "source": "BPHS Ch.24, Sl.54"},
        7: {"effect": "Honorable, very religious, progenic happiness, helpful", "source": "BPHS Ch.24, Sl.55"},
        8: {"effect": "Not much progenic happiness, cough disorders, angry, no happiness", "source": "BPHS Ch.24, Sl.56"},
        9: {"effect": "Prince or equal, authors treatises, famous, shines in race", "source": "BPHS Ch.24, Sl.57"},
        10: {"effect": "Raj Yoga, various pleasures, very famous", "source": "BPHS Ch.24, Sl.58"},
        11: {"effect": "Learned, dear to people, author, skillful, many sons and wealth", "source": "BPHS Ch.24, Sl.59"},
        12: {"effect": "Bereft of happiness from own sons, adopted son", "source": "BPHS Ch.24, Sl.60"}
    },
    6: {  # Ari Lord placements
        1: {"effect": "Sickly, famous, inimical to own men, rich, honorable, adventurous", "source": "BPHS Ch.24, Sl.61"},
        2: {"effect": "Adventurous, famous, lives in alien places, skillful speaker", "source": "BPHS Ch.24, Sl.62"},
        3: {"effect": "Given to anger, bereft of courage, inimical to siblings", "source": "BPHS Ch.24, Sl.63"},
        4: {"effect": "Devoid of maternal happiness, intelligent, tale bearer, jealous, rich", "source": "BPHS Ch.24, Sl.64"},
        5: {"effect": "Fluctuating finances, enmity with sons, happy, selfish, kind", "source": "BPHS Ch.24, Sl.65"},
        6: {"effect": "Enmity with kinsmen, friendly to others, mediocre happiness", "source": "BPHS Ch.24, Sl.66"},
        7: {"effect": "Deprived of marital happiness, famous, virtuous, wealthy", "source": "BPHS Ch.24, Sl.67"},
        8: {"effect": "Sickly, inimical, desires others' wealth and wives", "source": "BPHS Ch.24, Sl.68"},
        9: {"effect": "Trades in wood and stones, fluctuating professional fortunes", "source": "BPHS Ch.24, Sl.69"},
        10: {"effect": "Well known, not respectful to father, happy in foreign countries", "source": "BPHS Ch.24, Sl.70"},
        11: {"effect": "Gains wealth through enemies, virtuous, less progenic happiness", "source": "BPHS Ch.24, Sl.71"},
        12: {"effect": "Always spends on vices, hostile to learned, tortures beings", "source": "BPHS Ch.24, Sl.72"}
    },
    7: {  # Yuvati Lord placements
        1: {"effect": "Goes to others' wives, wicked, skillful, devoid of courage, windy diseases", "source": "BPHS Ch.24, Sl.73"},
        2: {"effect": "Many wives, gains wealth through wife, procrastinating", "source": "BPHS Ch.24, Sl.74"},
        3: {"effect": "Loss of children, living son with difficulty, daughter possible", "source": "BPHS Ch.24, Sl.75"},
        4: {"effect": "Wife not under control, fond of truth, intelligent, religious, dental issues", "source": "BPHS Ch.24, Sl.76"},
        5: {"effect": "Honorable, endowed with virtues, always delighted, wealthy", "source": "BPHS Ch.24, Sl.77"},
        6: {"effect": "Sickly wife, inimical to her, angry, devoid of happiness", "source": "BPHS Ch.24, Sl.78"},
        7: {"effect": "Happiness through wife, courageous, skillful, intelligent, windy diseases", "source": "BPHS Ch.24, Sl.79"},
        8: {"effect": "Deprived of marital happiness, wife troubled by diseases", "source": "BPHS Ch.24, Sl.80"},
        9: {"effect": "Union with many women, well-disposed to wife, many undertakings", "source": "BPHS Ch.24, Sl.81"},
        10: {"effect": "Disobedient wife, religious, endowed with wealth and sons", "source": "BPHS Ch.24, Sl.82"},
        11: {"effect": "Gains wealth through wife, less happiness from sons, daughters", "source": "BPHS Ch.24, Sl.83"},
        12: {"effect": "Penury, miser, livelihood related to clothes, spendthrift wife", "source": "BPHS Ch.24, Sl.84"}
    },
    8: {  # Randhra Lord placements
        1: {"effect": "Devoid of physical felicity, wounds, hostile to gods and brahmins", "source": "BPHS Ch.24, Sl.85"},
        2: {"effect": "Devoid of bodily vigor, little wealth, cannot regain lost wealth", "source": "BPHS Ch.24, Sl.86"},
        3: {"effect": "Devoid of fraternal happiness, indolent, devoid of servants and strength", "source": "BPHS Ch.24, Sl.87"},
        4: {"effect": "Deprived of mother, devoid of house, lands, happiness, betrays friends", "source": "BPHS Ch.24, Sl.88"},
        5: {"effect": "Dull-witted, limited children, long-lived, wealthy", "source": "BPHS Ch.24, Sl.89"},
        6: {"effect": "Wins over enemies, afflicted by diseases, childhood danger from snakes/water", "source": "BPHS Ch.24, Sl.90"},
        7: {"effect": "Two wives, downfall in business if malefic conjunction", "source": "BPHS Ch.24, Sl.91"},
        8: {"effect": "Long-lived, if weak medium life, thief, blameworthy", "source": "BPHS Ch.24, Sl.92"},
        9: {"effect": "Betrays religion, heterodox, wicked wife, steals others' wealth", "source": "BPHS Ch.24, Sl.93"},
        10: {"effect": "Devoid of paternal bliss, tale-bearer, bereft of livelihood", "source": "BPHS Ch.24, Sl.94"},
        11: {"effect": "Devoid of wealth, miserable in boyhood, happy later, long-lived if benefic", "source": "BPHS Ch.24, Sl.95"},
        12: {"effect": "Spends on evil deeds, short life if additional malefic", "source": "BPHS Ch.24, Sl.96"}
    },
    9: {  # Dharma Lord placements
        1: {"effect": "Fortunate, honored by king, virtuous, charming, learned, honored by public", "source": "BPHS Ch.24, Sl.97"},
        2: {"effect": "Scholar, dear to all, wealthy, sensuous, happiness from wife and sons", "source": "BPHS Ch.24, Sl.98"},
        3: {"effect": "Fraternal bliss, wealthy, virtuous, charming", "source": "BPHS Ch.24, Sl.99"},
        4: {"effect": "Houses, vehicles, happiness, all wealth, devoted to mother", "source": "BPHS Ch.24, Sl.100"},
        5: {"effect": "Sons and prosperity, devoted to elders, bold, charitable, learned", "source": "BPHS Ch.24, Sl.101"},
        6: {"effect": "Meager prosperity, no happiness from maternal relatives, troubled by enemies", "source": "BPHS Ch.24, Sl.102"},
        7: {"effect": "Happiness after marriage, virtuous, famous", "source": "BPHS Ch.24, Sl.103"},
        8: {"effect": "Not prosperous, no happiness from elder brother", "source": "BPHS Ch.24, Sl.104"},
        9: {"effect": "Abundant fortunes, virtues, beauty, happiness from siblings", "source": "BPHS Ch.24, Sl.105"},
        10: {"effect": "King or equal, minister or army chief, virtuous, dear to all", "source": "BPHS Ch.24, Sl.106"},
        11: {"effect": "Financial gains day by day, devoted to elders, virtuous", "source": "BPHS Ch.24, Sl.107"},
        12: {"effect": "Loss of fortunes, spends on auspicious acts, poor from entertaining guests", "source": "BPHS Ch.24, Sl.108"}
    },
    10: {  # Karma Lord placements
        1: {"effect": "Scholarly, famous, poet, diseases in boyhood, happy later, wealth increases", "source": "BPHS Ch.24, Sl.109"},
        2: {"effect": "Wealthy, virtuous, honored by king, charitable, happiness from father", "source": "BPHS Ch.24, Sl.110"},
        3: {"effect": "Happiness from brothers and servants, valorous, virtuous, eloquent", "source": "BPHS Ch.24, Sl.111"},
        4: {"effect": "Happy, interested in mother's welfare, vehicles, lands, houses, wealthy", "source": "BPHS Ch.24, Sl.112"},
        5: {"effect": "All kinds of learning, always delighted, wealthy, endowed with sons", "source": "BPHS Ch.24, Sl.113"},
        6: {"effect": "Bereft of paternal bliss, skillful but bereft of wealth, troubled by enemies", "source": "BPHS Ch.24, Sl.114"},
        7: {"effect": "Happiness through wife, intelligent, virtuous, eloquent, truthful, religious", "source": "BPHS Ch.24, Sl.115"},
        8: {"effect": "Devoid of good acts, long-lived, intent on blaming others", "source": "BPHS Ch.24, Sl.116"},
        9: {"effect": "Royal person becomes king, ordinary native equal to king, wealth and children", "source": "BPHS Ch.24, Sl.117"},
        10: {"effect": "Skillful in all jobs, valorous, truthful, devoted to elders", "source": "BPHS Ch.24, Sl.118"},
        11: {"effect": "Wealth, happiness, sons, virtuous, truthful, always delighted", "source": "BPHS Ch.24, Sl.119"},
        12: {"effect": "Spends through royal abodes, fear from enemies, worried though skillful", "source": "BPHS Ch.24, Sl.120"}
    },
    11: {  # Labha Lord placements
        1: {"effect": "Genuine, rich, happy, even-sighted, poet, eloquent, always gains", "source": "BPHS Ch.24, Sl.121"},
        2: {"effect": "All kinds of wealth and accomplishments, charitable, religious, happy", "source": "BPHS Ch.24, Sl.122"},
        3: {"effect": "Skillful in all jobs, wealthy, fraternal bliss, sometimes gout", "source": "BPHS Ch.24, Sl.123"},
        4: {"effect": "Gains from maternal relatives, visits shrines, house and land happiness", "source": "BPHS Ch.24, Sl.124"},
        5: {"effect": "Happy, educated, virtuous, religious", "source": "BPHS Ch.24, Sl.125"},
        6: {"effect": "Afflicted by diseases, cruel, foreign residence, troubled by enemies", "source": "BPHS Ch.24, Sl.126"},
        7: {"effect": "Gains through wife's relatives, liberal, virtuous, obeys spouse", "source": "BPHS Ch.24, Sl.127"},
        8: {"effect": "Reversals in undertakings, long-lived, wife may predecease", "source": "BPHS Ch.24, Sl.128"},
        9: {"effect": "Fortunate, skillful, truthful, honored by king, affluent", "source": "BPHS Ch.24, Sl.129"},
        10: {"effect": "Honored by king, virtuous, religious, intelligent, truthful, subdues senses", "source": "BPHS Ch.24, Sl.130"},
        11: {"effect": "Gains in all undertakings, learning and happiness increase daily", "source": "BPHS Ch.24, Sl.131"},
        12: {"effect": "Depends on good deeds, sensuous, many wives, befriends foreigners", "source": "BPHS Ch.24, Sl.132"}
    },
    12: {  # Vyaya Lord placements
        1: {"effect": "Spendthrift, weak constitution, eye afflictions, unkind", "source": "BPHS Ch.24, Sl.133"},
        2: {"effect": "Always in trouble, devoid of wealth, thievish, harsh speech", "source": "BPHS Ch.24, Sl.134"},
        3: {"effect": "Lazy, forsaken by siblings, loss through relatives", "source": "BPHS Ch.24, Sl.135"},
        4: {"effect": "Devoid of maternal happiness, few comforts, loses ancestral property", "source": "BPHS Ch.24, Sl.136"},
        5: {"effect": "Bereft of son, angry, worried, devoid of happiness", "source": "BPHS Ch.24, Sl.137"},
        6: {"effect": "Interested in other females, troubled by enemies, spends on sinful", "source": "BPHS Ch.24, Sl.138"},
        7: {"effect": "Penury, disrespects women, gives up own wife", "source": "BPHS Ch.24, Sl.139"},
        8: {"effect": "Long life, suffers penury throughout, eye diseases", "source": "BPHS Ch.24, Sl.140"},
        9: {"effect": "Irreligious, enters others' houses, deprived of fortune", "source": "BPHS Ch.24, Sl.141"},
        10: {"effect": "Spends on sinful, no paternal bliss, unkind, foolish", "source": "BPHS Ch.24, Sl.142"},
        11: {"effect": "Suffers many losses, devoid of wealth, truthful, affectionate to friends", "source": "BPHS Ch.24, Sl.143"},
        12: {"effect": "Spends well, spiritual, goes to heaven, observes fasts and pilgrimages", "source": "BPHS Ch.24, Sl.144"}
    }
}


# ============================================
# HOUSE STRENGTH FACTORS
# ============================================

HOUSE_STRENGTH_FACTORS = {
    "lord_dignity": {
        "exalted": 5,
        "own_sign": 4,
        "moolatrikona": 4,
        "friendly": 3,
        "neutral": 2,
        "enemy": 1,
        "debilitated": 0
    },
    "lord_house": {
        "kendra": {"houses": [1, 4, 7, 10], "score": 4, "desc": "Lord in angular house - very strong"},
        "trikona": {"houses": [1, 5, 9], "score": 5, "desc": "Lord in trinal house - excellent"},
        "upachaya": {"houses": [3, 6, 10, 11], "score": 3, "desc": "Lord in growth house - improves over time"},
        "dusthana": {"houses": [6, 8, 12], "score": 1, "desc": "Lord in difficult house - challenges"}
    },
    "occupancy": {
        "benefic": {"planets": ["Jupiter", "Venus", "Mercury", "Moon"], "score": 3},
        "malefic": {"planets": ["Saturn", "Mars", "Rahu", "Ketu", "Sun"], "score": -1}
    }
}


# ============================================
# REMEDIAL MEASURES BY HOUSE
# ============================================

HOUSE_REMEDIES = {
    1: {
        "weak_lord": ["Strengthen ascendant lord through gemstone", "Surya Namaskar for vitality", "Wear copper (for Sun-ruled)"],
        "afflicted": ["Rudrabhishek for protection", "Chant Maha Mrityunjaya mantra", "Donate as per afflicting planet"],
        "general": ["Maintain good health practices", "Regular exercise", "Self-improvement activities"]
    },
    2: {
        "weak_lord": ["Strengthen 2nd lord", "Donate food on Thursdays", "Respect elders"],
        "afflicted": ["Remedies for afflicting planet", "Feed birds daily", "Speak truthfully"],
        "general": ["Save money regularly", "Maintain family harmony", "Speak sweetly"]
    },
    3: {
        "weak_lord": ["Strengthen Mars (natural karaka)", "Help younger siblings", "Develop courage"],
        "afflicted": ["Hanuman Chalisa recitation", "Donate red items on Tuesdays"],
        "general": ["Short pilgrimages", "Communication skills development", "Physical exercise"]
    },
    4: {
        "weak_lord": ["Strengthen Moon", "Serve mother", "Worship Goddess"],
        "afflicted": ["Donate white items on Mondays", "Feed cows", "Plant trees"],
        "general": ["Maintain home peace", "Care for mother", "Acquire property through honest means"]
    },
    5: {
        "weak_lord": ["Strengthen Jupiter", "Worship Lord Ganesha", "Study scriptures"],
        "afflicted": ["Donate to educational institutions", "Help children", "Saraswati puja"],
        "general": ["Creative pursuits", "Teaching", "Mantra recitation"]
    },
    6: {
        "weak_lord": ["Strengthen 6th lord carefully", "Service to the sick", "Help employees"],
        "afflicted": ["Durga puja", "Donate medicines", "Feed dogs"],
        "general": ["Maintain health", "Clear debts", "Avoid litigation"]
    },
    7: {
        "weak_lord": ["Strengthen Venus", "Respect spouse", "Worship Lakshmi"],
        "afflicted": ["Donate to couples", "Fast on Fridays", "Marriage counseling"],
        "general": ["Partnership harmony", "Business ethics", "Respect women"]
    },
    8: {
        "weak_lord": ["Strengthen Saturn", "Seva at old age homes", "Maha Mrityunjaya jaap"],
        "afflicted": ["Shani puja", "Donate black items on Saturdays", "Sesame oil donation"],
        "general": ["Insurance planning", "Spiritual practices", "Yoga and meditation"]
    },
    9: {
        "weak_lord": ["Strengthen Jupiter", "Respect father and guru", "Pilgrimage"],
        "afflicted": ["Guru puja", "Donate yellow items on Thursdays", "Study philosophy"],
        "general": ["Religious practices", "Higher education", "Visit temples"]
    },
    10: {
        "weak_lord": ["Strengthen 10th lord", "Career prayers", "Respect authority"],
        "afflicted": ["Remedies as per afflicting planet", "Karma yoga", "Professional ethics"],
        "general": ["Work honestly", "Respect seniors", "Public service"]
    },
    11: {
        "weak_lord": ["Strengthen 11th lord", "Help elder siblings", "Charity"],
        "afflicted": ["Donate to friends in need", "Social service"],
        "general": ["Networking", "Help others achieve goals", "Gratitude practices"]
    },
    12: {
        "weak_lord": ["Strengthen 12th lord for spiritual gains", "Meditation", "Foreign pilgrimage"],
        "afflicted": ["Donate to ashrams", "Hospital visits", "Help prisoners"],
        "general": ["Spiritual practices", "Charity", "Reduce unnecessary expenses"]
    }
}
