#!/usr/bin/env python3
"""Test chart calculation to debug ascendant issue"""

import swisseph as swe

# User's birth data - June 19, 1994, 18:30, Delhi
year, month, day = 1994, 6, 19
hour, minute = 18, 30
lat, lon = 28.6139, 77.2090  # Delhi coordinates

print("=" * 60)
print("CHART CALCULATION DEBUG")
print("=" * 60)
print(f"Birth: {year}-{month:02d}-{day:02d} at {hour:02d}:{minute:02d}")
print(f"Location: Lat {lat}, Lon {lon} (Delhi)")
print("=" * 60)

# Convert to decimal hour
decimal_hour = hour + minute/60.0
print(f"\nDecimal Hour: {decimal_hour}")

# Calculate Julian Day
jd = swe.julday(year, month, day, decimal_hour)
print(f"Julian Day: {jd}")

# Get Lahiri ayanamsa
swe.set_sid_mode(1, 0, 0)  # Lahiri = 1
ayanamsa = swe.get_ayanamsa_ut(jd)
print(f"Ayanamsa (Lahiri): {ayanamsa}")

# Calculate houses with Placidus
cusps, ascmc = swe.houses(jd, lat, lon, b'P')
tropical_asc = ascmc[0]
print(f"\nTropical Ascendant: {tropical_asc}")

# Convert to sidereal
sidereal_asc = (tropical_asc - ayanamsa) % 360
print(f"Sidereal Ascendant: {sidereal_asc}")

# Determine sign
sign_index = int(sidereal_asc / 30)
signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 
         'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
print(f"\n*** ASCENDANT SIGN: {signs[sign_index]} ***")
print(f"Degree in Sign: {sidereal_asc % 30:.2f}")

# Calculate all sidereal cusps
sidereal_cusps = [(c - ayanamsa) % 360 for c in cusps[0:12]]
print("\n" + "=" * 60)
print("HOUSE CUSPS (Sidereal - Placidus)")
print("=" * 60)
for i, cusp in enumerate(sidereal_cusps):
    cusp_sign_idx = int(cusp / 30)
    print(f"House {i+1:2d}: {cusp:7.2f}° - {signs[cusp_sign_idx]:12s} {cusp % 30:.2f}°")

# Calculate all planets
print("\n" + "=" * 60)
print("PLANET POSITIONS (Sidereal - Lahiri)")
print("=" * 60)

planets = {
    'Sun': 0, 'Moon': 1, 'Mars': 4, 'Mercury': 2, 
    'Jupiter': 5, 'Venus': 3, 'Saturn': 6, 'Rahu': 11
}

swe.set_sid_mode(1, 0, 0)  # Lahiri
flags = swe.FLG_SWIEPH | swe.FLG_SPEED | swe.FLG_SIDEREAL

for planet_name, planet_code in planets.items():
    result, _ = swe.calc_ut(jd, planet_code, flags)
    lon = result[0]
    if planet_name == 'Rahu':
        ketu_lon = (lon + 180) % 360
    sign_idx = int(lon / 30)
    
    # Determine house
    house = 1
    for i in range(12):
        cusp_start = sidereal_cusps[i]
        cusp_end = sidereal_cusps[(i + 1) % 12]
        if cusp_start > cusp_end:
            if lon >= cusp_start or lon < cusp_end:
                house = i + 1
                break
        else:
            if cusp_start <= lon < cusp_end:
                house = i + 1
                break
    
    print(f"{planet_name:8s}: {lon:7.2f}° - {signs[sign_idx]:12s} {lon % 30:5.2f}° - House {house}")

# Print Ketu
ketu_sign_idx = int(ketu_lon / 30)
ketu_house = 1
for i in range(12):
    cusp_start = sidereal_cusps[i]
    cusp_end = sidereal_cusps[(i + 1) % 12]
    if cusp_start > cusp_end:
        if ketu_lon >= cusp_start or ketu_lon < cusp_end:
            ketu_house = i + 1
            break
    else:
        if cusp_start <= ketu_lon < cusp_end:
            ketu_house = i + 1
            break
print(f"{'Ketu':8s}: {ketu_lon:7.2f}° - {signs[ketu_sign_idx]:12s} {ketu_lon % 30:5.2f}° - House {ketu_house}")

print("\n" + "=" * 60)
print("KEY FINDING:")
print("=" * 60)
print(f"Expected Ascendant: Scorpio")
print(f"Calculated Ascendant: {signs[sign_index]}")
print(f"\nExpected Saturn: 4th house, Aquarius 18°")
saturn_result, _ = swe.calc_ut(jd, 6, flags)
saturn_lon = saturn_result[0]
saturn_sign_idx = int(saturn_lon / 30)
print(f"Calculated Saturn: {signs[saturn_sign_idx]} {saturn_lon % 30:.2f}°")

# Find Saturn's house
saturn_house = 1
for i in range(12):
    cusp_start = sidereal_cusps[i]
    cusp_end = sidereal_cusps[(i + 1) % 12]
    if cusp_start > cusp_end:
        if saturn_lon >= cusp_start or saturn_lon < cusp_end:
            saturn_house = i + 1
            break
    else:
        if cusp_start <= saturn_lon < cusp_end:
            saturn_house = i + 1
            break
print(f"Calculated Saturn House: {saturn_house}")

# Additional check: What if time zone is wrong?
print("\n" + "=" * 60)
print("TIME ZONE CHECK")
print("=" * 60)
print("India is UTC+5:30. The birth time 18:30 should be local time.")
print("If we're using UTC instead of IST, the chart would be ~5.5 hours off!")

# Let's try with IST conversion (subtract 5.5 hours for UTC)
utc_hour = hour - 5 - 30/60  # Convert IST to UTC
print(f"\nIf 18:30 IST -> {utc_hour:.2f} UTC")
jd_utc = swe.julday(year, month, day, utc_hour)
cusps_utc, ascmc_utc = swe.houses(jd_utc, lat, lon, b'P')
tropical_asc_utc = ascmc_utc[0]
sidereal_asc_utc = (tropical_asc_utc - ayanamsa) % 360
sign_index_utc = int(sidereal_asc_utc / 30)
print(f"Using UTC: Ascendant = {signs[sign_index_utc]} at {sidereal_asc_utc % 30:.2f}°")
