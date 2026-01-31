#!/usr/bin/env python3
"""Find the correct parameters for Scorpio ascendant"""

import swisseph as swe

# User's expected chart:
# - Ascendant: Scorpio
# - Saturn: 4th house, Aquarius 18°
# If Lagna is Scorpio, then 4th house is Aquarius (Scorpio -> Sag -> Cap -> Aquarius)

# User's birth data
year, month, day = 1994, 6, 19
lat, lon = 28.6139, 77.2090  # Delhi

swe.set_sid_mode(1, 0, 0)  # Lahiri

print("=" * 60)
print("FINDING SCORPIO LAGNA TIME")
print("=" * 60)
print(f"Date: {year}-{month:02d}-{day:02d}")
print(f"Location: Delhi ({lat}, {lon})")
print("\nSearching for times that give Scorpio ascendant (210-240°)...")
print("-" * 60)

signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 
         'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']

# Try different hours throughout the day
print("\nHour-by-hour ascendant check:")
for hour in range(0, 24):
    jd = swe.julday(year, month, day, hour)
    ayanamsa = swe.get_ayanamsa_ut(jd)
    cusps, ascmc = swe.houses(jd, lat, lon, b'P')
    sidereal_asc = (ascmc[0] - ayanamsa) % 360
    sign_idx = int(sidereal_asc / 30)
    if signs[sign_idx] == 'Scorpio':
        print(f"{hour:02d}:00 IST -> {signs[sign_idx]} {sidereal_asc % 30:.2f}° **SCORPIO**")
    else:
        print(f"{hour:02d}:00 IST -> {signs[sign_idx]} {sidereal_asc % 30:.2f}°")

print("\n" + "=" * 60)
print("DETAILED SEARCH: Finding exact time for Scorpio ascendant")
print("=" * 60)

# Find the exact minute range when Scorpio rises
scorpio_start = None
scorpio_end = None

for minute_of_day in range(0, 24*60):
    hour = minute_of_day // 60
    minute = minute_of_day % 60
    decimal_time = hour + minute / 60.0
    
    jd = swe.julday(year, month, day, decimal_time)
    ayanamsa = swe.get_ayanamsa_ut(jd)
    cusps, ascmc = swe.houses(jd, lat, lon, b'P')
    sidereal_asc = (ascmc[0] - ayanamsa) % 360
    
    sign_idx = int(sidereal_asc / 30)
    
    if signs[sign_idx] == 'Scorpio':
        if scorpio_start is None:
            scorpio_start = (hour, minute)
        scorpio_end = (hour, minute)

if scorpio_start:
    print(f"\nScorpio rises from {scorpio_start[0]:02d}:{scorpio_start[1]:02d} to {scorpio_end[0]:02d}:{scorpio_end[1]:02d} IST")
else:
    print("Scorpio ascendant not found for this date!")

# Now check what happens at 18:30 with UTC conversion
print("\n" + "=" * 60)
print("IMPORTANT: CHECKING SIDEREAL HOUSE SYSTEM")
print("=" * 60)
print("What if we need to use Whole Sign House system?")

# With Whole Sign houses, if Scorpio is ascendant:
# House 1 = Scorpio (210-240°)
# House 2 = Sagittarius (240-270°)
# House 3 = Capricorn (270-300°)
# House 4 = Aquarius (300-330°)

# Saturn at 318.61° Aquarius IS in sign Aquarius, which would be 4th house in Whole Sign

print("\nIf we use WHOLE SIGN HOUSE system with Scorpio ascendant:")
print("  1st House = Scorpio")
print("  2nd House = Sagittarius")
print("  3rd House = Capricorn")  
print("  4th House = Aquarius <- Saturn here at 18°!")
print("  5th House = Pisces")
print("  ...")

# Let's verify: if user enters 18:30 IST and system interprets it as UTC
print("\n" + "=" * 60)
print("KEY DISCOVERY!")
print("=" * 60)

# Try around 22:00-23:00 IST which might give Scorpio
for hour in [22, 23]:
    for minute in [0, 15, 30, 45]:
        decimal_time = hour + minute / 60.0
        jd = swe.julday(year, month, day, decimal_time)
        ayanamsa = swe.get_ayanamsa_ut(jd)
        cusps, ascmc = swe.houses(jd, lat, lon, b'P')
        sidereal_asc = (ascmc[0] - ayanamsa) % 360
        sign_idx = int(sidereal_asc / 30)
        
        print(f"{hour:02d}:{minute:02d} IST -> Ascendant: {signs[sign_idx]} {sidereal_asc % 30:.2f}°")
        
        if signs[sign_idx] == 'Scorpio':
            # Calculate Saturn house with Whole Sign
            flags = swe.FLG_SWIEPH | swe.FLG_SPEED | swe.FLG_SIDEREAL
            saturn_result, _ = swe.calc_ut(jd, 6, flags)
            saturn_lon = saturn_result[0]
            saturn_sign_idx = int(saturn_lon / 30)
            
            # In Whole Sign: house number = (planet_sign - ascendant_sign) % 12 + 1
            asc_sign = sign_idx
            saturn_house_whole = (saturn_sign_idx - asc_sign) % 12 + 1
            
            print(f"   -> Saturn at {signs[saturn_sign_idx]} {saturn_lon % 30:.2f}°")
            print(f"   -> Saturn in House {saturn_house_whole} (Whole Sign)")
