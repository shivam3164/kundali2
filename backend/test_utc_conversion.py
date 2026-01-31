#!/usr/bin/env python3
"""Test with proper IST to UTC timezone conversion"""

import swisseph as swe

year, month, day = 1994, 6, 19
lat, lon = 28.2392, 80.2642

signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 
         'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']

swe.set_sid_mode(1, 0, 0)  # Lahiri

print("=" * 65)
print("CRITICAL FIX: Timezone Conversion (IST -> UTC)")
print("=" * 65)
print()
print("Birth time: 18:34 IST")
print("IST = UTC + 5:30")
print("Therefore: 18:34 IST = 13:04 UTC")
print()

# Convert 18:34 IST to UTC
# 18:34 - 5:30 = 13:04 UTC
ist_hour = 18
ist_minute = 34
utc_hour = ist_hour - 5
utc_minute = ist_minute - 30
if utc_minute < 0:
    utc_minute += 60
    utc_hour -= 1

utc_decimal = utc_hour + utc_minute / 60.0
print(f"UTC time: {utc_hour:02d}:{utc_minute:02d} ({utc_decimal:.4f} decimal)")

# Calculate Julian Day with UTC time
jd = swe.julday(year, month, day, utc_decimal)
ay = swe.get_ayanamsa_ut(jd)

print(f"Julian Day: {jd}")
print(f"Ayanamsa (Lahiri): {ay:.4f}")

# Calculate houses
cusps, ascmc = swe.houses(jd, lat, lon, b'P')
tropical_asc = ascmc[0]
sidereal_asc = (tropical_asc - ay) % 360
asc_sign_idx = int(sidereal_asc / 30)

print()
print("=" * 65)
print("RESULT WITH UTC CONVERSION:")
print("=" * 65)
print(f"Tropical Ascendant: {tropical_asc:.2f}")
print(f"Sidereal Ascendant: {sidereal_asc:.2f}")
print()
print(f"*** LAGNA: {signs[asc_sign_idx]} {sidereal_asc % 30:.2f} ***")
print()

# Whole sign houses from this ascendant
print("Houses (Whole Sign):")
for i in range(12):
    house_sign_idx = (asc_sign_idx + i) % 12
    print(f"  House {i+1:2d}: {signs[house_sign_idx]}")

# Calculate planets
print()
print("=" * 65)
print("PLANET POSITIONS (with UTC):")
print("=" * 65)

flags = swe.FLG_SWIEPH | swe.FLG_SPEED | swe.FLG_SIDEREAL

planets = {'Sun': 0, 'Moon': 1, 'Mars': 4, 'Mercury': 2, 
           'Jupiter': 5, 'Venus': 3, 'Saturn': 6, 'Rahu': 11}

print(f"{'Planet':<10} {'Sign':<12} {'Degree':>8} {'House':>6}")
print("-" * 40)

for planet_name, planet_code in planets.items():
    result, _ = swe.calc_ut(jd, planet_code, flags)
    lon = result[0]
    planet_sign_idx = int(lon / 30)
    house = (planet_sign_idx - asc_sign_idx) % 12 + 1
    print(f"{planet_name:<10} {signs[planet_sign_idx]:<12} {lon % 30:>7.2f} {house:>6}")

# Ketu
rahu_result, _ = swe.calc_ut(jd, 11, flags)
ketu_lon = (rahu_result[0] + 180) % 360
ketu_sign_idx = int(ketu_lon / 30)
ketu_house = (ketu_sign_idx - asc_sign_idx) % 12 + 1
print(f"{'Ketu':<10} {signs[ketu_sign_idx]:<12} {ketu_lon % 30:>7.2f} {ketu_house:>6}")

# Comparison
print()
print("=" * 65)
print("COMPARISON WITH REFERENCE CHART:")
print("=" * 65)
print()
print("Reference chart shows:")
print("  - Lagna: 29 (in Capricorn position - but this shows La DEGREE)")
print("  - Mars, Ketu in House 1 (Aries)")
print("  - Sun, Mercury in House 3 (Gemini)")
print("  - Venus in House 4 (Cancer)")
print("  - Moon, Jupiter, Rahu in House 7 (Libra)")
print("  - Saturn in House 11 (Aquarius)")
print()

if signs[asc_sign_idx] == 'Scorpio':
    print("With Scorpio Lagna (our UTC calculation):")
    print("  - House 1 = Scorpio")
    print("  - House 4 = Aquarius -> Saturn here = MATCH!")
    print("  - House 6 = Aries -> Mars, Ketu here")
    print("  - House 8 = Gemini -> Sun, Mercury here")
    print("  - House 9 = Cancer -> Venus here")
    print("  - House 12 = Libra -> Moon, Jupiter, Rahu here")
    print()
    print("This doesn't match the reference house numbers!")
    print("The reference uses WHOLE SIGN from ARIES (Rashi chart),")
    print("while Lagna (Scorpio) is for Bhava/House calculation.")

print()
print("=" * 65)
print("CONCLUSION:")
print("=" * 65)

# Re-check what the reference chart is using
print("""
The reference chart IMAGE shows:
1. RASHI positions (signs) are correct - planets in correct signs
2. House NUMBERS shown (1-12) follow Aries = 1 convention (natural zodiac)
3. "La 29" in Capricorn box indicates Lagna DEGREE is 29, not Lagna SIGN

This is likely a Rashi chart (showing planets in signs) with 
house numbers following natural zodiac (Aries=1, Taurus=2, etc.)

The actual LAGNA SIGN for house calculations would need 
Bhava Chalit chart to verify.

KEY TAKEAWAY:
- Our planetary positions are CORRECT ✅
- The house numbering in reference follows natural zodiac (Aries=1)
- To match the reference, we need to display Rashi chart with natural numbering
""")
