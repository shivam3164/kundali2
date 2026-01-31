#!/usr/bin/env python3
"""Test chart calculation with corrected coordinates"""

import swisseph as swe

# Corrected birth data
year, month, day = 1994, 6, 19
hour, minute = 18, 34
lat, lon = 28.2392, 80.2642  # Corrected coordinates

print("=" * 60)
print("CHART CALCULATION - CORRECTED DATA")
print("=" * 60)
print(f"Birth: {year}-{month:02d}-{day:02d} at {hour:02d}:{minute:02d}")
print(f"Location: Lat {lat}°N, Lon {lon}°E")
print("=" * 60)

# Convert to decimal hour
decimal_hour = hour + minute/60.0

# Calculate Julian Day
jd = swe.julday(year, month, day, decimal_hour)
print(f"\nJulian Day: {jd}")

# Get Lahiri ayanamsa
swe.set_sid_mode(1, 0, 0)  # Lahiri = 1
ayanamsa = swe.get_ayanamsa_ut(jd)
print(f"Ayanamsa (Lahiri): {ayanamsa:.4f}°")

# Calculate houses with Placidus
cusps, ascmc = swe.houses(jd, lat, lon, b'P')
tropical_asc = ascmc[0]
sidereal_asc = (tropical_asc - ayanamsa) % 360

signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 
         'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']

sign_index = int(sidereal_asc / 30)
print(f"\nTropical Ascendant: {tropical_asc:.2f}°")
print(f"Sidereal Ascendant: {sidereal_asc:.2f}°")
print(f"\n*** ASCENDANT: {signs[sign_index]} {sidereal_asc % 30:.2f}° ***")

# Calculate all sidereal cusps
sidereal_cusps = [(c - ayanamsa) % 360 for c in cusps[0:12]]

print("\n" + "=" * 60)
print("HOUSE CUSPS (Sidereal - Placidus)")
print("=" * 60)
for i, cusp in enumerate(sidereal_cusps):
    cusp_sign_idx = int(cusp / 30)
    print(f"House {i+1:2d}: {signs[cusp_sign_idx]:12s} {cusp % 30:5.2f}°")

# Calculate all planets
print("\n" + "=" * 60)
print("PLANET POSITIONS (Sidereal - Lahiri)")
print("=" * 60)

planets = {
    'Sun': 0, 'Moon': 1, 'Mars': 4, 'Mercury': 2, 
    'Jupiter': 5, 'Venus': 3, 'Saturn': 6, 'Rahu': 11
}

flags = swe.FLG_SWIEPH | swe.FLG_SPEED | swe.FLG_SIDEREAL

def get_house(planet_lon, cusps):
    """Determine house using Placidus cusps"""
    for i in range(12):
        cusp_start = cusps[i]
        cusp_end = cusps[(i + 1) % 12]
        if cusp_start > cusp_end:  # Wraps around 360
            if planet_lon >= cusp_start or planet_lon < cusp_end:
                return i + 1
        else:
            if cusp_start <= planet_lon < cusp_end:
                return i + 1
    return 1

def get_house_whole_sign(planet_lon, asc_sign_idx):
    """Determine house using Whole Sign system"""
    planet_sign = int(planet_lon / 30)
    return (planet_sign - asc_sign_idx) % 12 + 1

print(f"\n{'Planet':<10} {'Longitude':>10} {'Sign':<12} {'Deg':>6} {'Placidus':>9} {'WholeSgn':>9}")
print("-" * 60)

ketu_lon = None
for planet_name, planet_code in planets.items():
    result, _ = swe.calc_ut(jd, planet_code, flags)
    lon = result[0]
    
    if planet_name == 'Rahu':
        ketu_lon = (lon + 180) % 360
    
    sign_idx = int(lon / 30)
    house_placidus = get_house(lon, sidereal_cusps)
    house_whole = get_house_whole_sign(lon, sign_index)
    
    print(f"{planet_name:<10} {lon:>10.2f}° {signs[sign_idx]:<12} {lon % 30:>5.2f}° {house_placidus:>9} {house_whole:>9}")

# Ketu
ketu_sign_idx = int(ketu_lon / 30)
ketu_house_placidus = get_house(ketu_lon, sidereal_cusps)
ketu_house_whole = get_house_whole_sign(ketu_lon, sign_index)
print(f"{'Ketu':<10} {ketu_lon:>10.2f}° {signs[ketu_sign_idx]:<12} {ketu_lon % 30:>5.2f}° {ketu_house_placidus:>9} {ketu_house_whole:>9}")

print("\n" + "=" * 60)
print("VERIFICATION")
print("=" * 60)
print(f"Expected Ascendant: Scorpio")
print(f"Calculated Ascendant: {signs[sign_index]}")

# Saturn check
saturn_result, _ = swe.calc_ut(jd, 6, flags)
saturn_lon = saturn_result[0]
saturn_sign_idx = int(saturn_lon / 30)
saturn_house_whole = get_house_whole_sign(saturn_lon, sign_index)

print(f"\nExpected Saturn: 4th house, Aquarius 18°")
print(f"Calculated Saturn: {signs[saturn_sign_idx]} {saturn_lon % 30:.2f}° - House {saturn_house_whole} (Whole Sign)")

if signs[sign_index] == 'Scorpio':
    print("\n✅ ASCENDANT MATCHES!")
else:
    print(f"\n❌ Ascendant mismatch: Expected Scorpio, got {signs[sign_index]}")

if saturn_house_whole == 4:
    print("✅ SATURN HOUSE MATCHES (Whole Sign)!")
else:
    print(f"❌ Saturn house mismatch: Expected 4, got {saturn_house_whole}")
