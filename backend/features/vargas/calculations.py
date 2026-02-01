def get_sign_and_degree(longitude):
    """
    Converts absolute longitude (0-360) to (sign_index 1-12, degree_in_sign 0-30).
    """
    sign_index = int(longitude / 30)
    degree_in_sign = longitude % 30
    return (sign_index + 1), degree_in_sign

def normalize_sign(sign):
    """
    Keeps sign within 1-12 range.
    """
    return ((sign - 1) % 12) + 1

def is_odd_sign(sign):
    return sign in [1, 3, 5, 7, 9, 11]

def get_sign_type(sign):
    """
    Returns 'movable', 'fixed', or 'dual'.
    """
    if sign in [1, 4, 7, 10]:
        return 'movable'
    elif sign in [2, 5, 8, 11]:
        return 'fixed'
    else:
        return 'dual'

# --- D1: Rashi (Born Chart) ---
def calculate_d1_rashi(longitude):
    sign, _ = get_sign_and_degree(longitude)
    return sign

# --- D2: Hora (Wealth) ---
def calculate_d2_hora(longitude):
    sign, deg = get_sign_and_degree(longitude)
    is_odd = is_odd_sign(sign)
    is_first_half = deg < 15

    # Odd Signs: 1st half -> Sun (Leo-5), 2nd half -> Moon (Cancer-4)
    if is_odd:
        return 5 if is_first_half else 4
    # Even Signs: 1st half -> Moon (Cancer-4), 2nd half -> Sun (Leo-5)
    else:
        return 4 if is_first_half else 5

# --- D3: Dreshkana (Siblings/Co-born) ---
def calculate_d3_dreshkana(longitude):
    sign, deg = get_sign_and_degree(longitude)
    part = int(deg / 10) # 0, 1, or 2

    # 1st part: Same sign. 2nd part: 5th from sign. 3rd part: 9th from sign.
    offset = part * 4
    return normalize_sign(sign + offset)

# --- D4: Chaturthamsha (Fortune/Property) ---
def calculate_d4_chaturthamsha(longitude):
    sign, deg = get_sign_and_degree(longitude)
    part = int(deg / 7.5)
    offset = part * 3
    return normalize_sign(sign + offset)

# --- D7: Saptamsha (Children) ---
def calculate_d7_saptamsha(longitude):
    sign, deg = get_sign_and_degree(longitude)
    part = int(deg / (30/7))
    start_sign = sign if is_odd_sign(sign) else normalize_sign(sign + 6)
    return normalize_sign(start_sign + part)

# --- D9: Navamsha (Spouse/Dharma) ---
def calculate_d9_navamsha(longitude):
    sign, deg = get_sign_and_degree(longitude)
    part = int(deg / (30/9))
    st = get_sign_type(sign)
    
    if st == 'movable':
        start_sign = sign
    elif st == 'fixed':
        start_sign = normalize_sign(sign + 8)
    else: # dual
        start_sign = normalize_sign(sign + 4)
        
    return normalize_sign(start_sign + part)

# --- D10: Dashamsha (Career/Power) ---
def calculate_d10_dashamsha(longitude):
    sign, deg = get_sign_and_degree(longitude)
    part = int(deg / 3)
    start_sign = sign if is_odd_sign(sign) else normalize_sign(sign + 8)
    return normalize_sign(start_sign + part)

# --- D12: Dwadashamsha (Parents) ---
def calculate_d12_dwadashamsha(longitude):
    sign, deg = get_sign_and_degree(longitude)
    part = int(deg / 2.5)
    return normalize_sign(sign + part)

# --- D16: Shodashamsha (Conveyances) ---
def calculate_d16_shodashamsha(longitude):
    sign, deg = get_sign_and_degree(longitude)
    part = int(deg / (30/16))
    st = get_sign_type(sign)
    
    # Movable: Aries(1), Fixed: Leo(5), Dual: Sagittarius(9)
    if st == 'movable':
        start_sign = 1
    elif st == 'fixed':
        start_sign = 5
    else: # dual
        start_sign = 9
        
    return normalize_sign(start_sign + part)

# --- D20: Vimshamsha (Worship/Spiritual) ---
def calculate_d20_vimshamsha(longitude):
    sign, deg = get_sign_and_degree(longitude)
    part = int(deg / 1.5)
    st = get_sign_type(sign)
    
    # Movable: Aries(1), Fixed: Sagittarius(9), Dual: Leo(5)
    if st == 'movable':
        start_sign = 1
    elif st == 'fixed':
        start_sign = 9
    else: # dual
        start_sign = 5
        
    return normalize_sign(start_sign + part)

# --- D24: Chaturvimshamsha (Learning/Knowledge) ---
def calculate_d24_chaturvimshamsha(longitude):
    sign, deg = get_sign_and_degree(longitude)
    part = int(deg / 1.25)
    
    # Odd: Leo(5), Even: Cancer(4)
    start_sign = 5 if is_odd_sign(sign) else 4
    return normalize_sign(start_sign + part)

# --- D27: Saptavimshamsha (Strength) ---
def calculate_d27_saptavimshamsha(longitude):
    sign, deg = get_sign_and_degree(longitude)
    part = int(deg / (30/27))
    st = get_sign_type(sign)
    
    # Movable: Aries(1), Fixed: Cancer(4), Dual: Libra(7)
    if st == 'movable':
        start_sign = 1
    elif st == 'fixed':
        start_sign = 4
    else: # dual
        start_sign = 7
        
    return normalize_sign(start_sign + part)

# --- D30: Trimshamsha (Misfortunes/Evil) ---
def calculate_d30_trimshamsha(longitude):
    sign, deg = get_sign_and_degree(longitude)
    is_odd = is_odd_sign(sign)
    
    if is_odd:
        if deg < 5:
            return 1   # Mars
        elif deg < 10:
            return 11 # Saturn
        elif deg < 18:
            return 9  # Jupiter
        elif deg < 25:
            return 3  # Mercury
        else:
            return 7         # Venus
    else:
        if deg < 5:
            return 2   # Venus
        elif deg < 12:
            return 6 # Mercury
        elif deg < 20: 
            return 12 # Jupiter
        elif deg < 25:
            return 10 # Saturn
        else:
            return 8         # Mars

# --- D40: Khavedamsha (Auspicious/Inauspicious) ---
def calculate_d40_khavedamsha(longitude):
    sign, deg = get_sign_and_degree(longitude)
    part = int(deg / (30/40))
    start_sign = 1 if is_odd_sign(sign) else 7
    return normalize_sign(start_sign + part)

# --- D45: Akshavedamsha (All Indications) ---
def calculate_d45_akshavedamsha(longitude):
    sign, deg = get_sign_and_degree(longitude)
    part = int(deg / (30/45))
    st = get_sign_type(sign)
    
    # Movable: Aries(1), Fixed: Leo(5), Dual: Sagittarius(9)
    if st == 'movable':
        start_sign = 1
    elif st == 'fixed':
        start_sign = 5
    else: # dual
        start_sign = 9
        
    return normalize_sign(start_sign + part)

# --- D60: Shashtiamsha (All Indications - Primary) ---
def calculate_d60_shashtiamsha(longitude):
    sign, deg = get_sign_and_degree(longitude)
    part = int(deg / 0.5)
    return normalize_sign(sign + part)

def get_all_vargas(longitude):
    return {
        "D1": calculate_d1_rashi(longitude),
        "D2": calculate_d2_hora(longitude),
        "D3": calculate_d3_dreshkana(longitude),
        "D4": calculate_d4_chaturthamsha(longitude),
        "D7": calculate_d7_saptamsha(longitude),
        "D9": calculate_d9_navamsha(longitude),
        "D10": calculate_d10_dashamsha(longitude),
        "D12": calculate_d12_dwadashamsha(longitude),
        "D16": calculate_d16_shodashamsha(longitude),
        "D20": calculate_d20_vimshamsha(longitude),
        "D24": calculate_d24_chaturvimshamsha(longitude),
        "D27": calculate_d27_saptavimshamsha(longitude),
        "D30": calculate_d30_trimshamsha(longitude),
        "D40": calculate_d40_khavedamsha(longitude),
        "D45": calculate_d45_akshavedamsha(longitude),
        "D60": calculate_d60_shashtiamsha(longitude)
    }
