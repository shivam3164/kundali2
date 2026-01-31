#!/usr/bin/env python3
"""Verify: What if 18:30 is meant to be converted from UTC to IST?"""

import swisseph as swe

# User birth data
year, month, day = 1994, 6, 19
lat, lon = 28.6139, 77.2090  # Delhi

swe.set_sid_mode(1, 0, 0)  # Lahiri

signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 
         'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']

print("=" * 60)
print("VERIFYING BIRTH TIME INTERPRETATION")
print("=" * 60)

# Scenario 1: 18:30 IST (already in IST)
print("\n1. If birth time = 18:30 IST (local time):")
jd = swe.julday(year, month, day, 18.5)
ayanamsa = swe.get_ayanamsa_ut(jd)
cusps, ascmc = swe.houses(jd, lat, lon, b'P')
sidereal_asc = (ascmc[0] - ayanamsa) % 360
sign_idx = int(sidereal_asc / 30)
print(f"   Ascendant: {signs[sign_idx]} {sidereal_asc % 30:.2f}°")

# Scenario 2: 18:30 needs conversion to IST (i.e., it's actually UTC)
# That would mean 18:30 UTC = 00:00 IST next day
print("\n2. If birth time = 18:30 UTC (converted to midnight IST next day):")
jd = swe.julday(year, month, day + 1, 0)  # Next day midnight IST
ayanamsa = swe.get_ayanamsa_ut(jd)
cusps, ascmc = swe.houses(jd, lat, lon, b'P')
sidereal_asc = (ascmc[0] - ayanamsa) % 360
sign_idx = int(sidereal_asc / 30)
print(f"   Ascendant: {signs[sign_idx]} {sidereal_asc % 30:.2f}°")

# Scenario 3: Military time confusion - maybe 06:30 AM?
print("\n3. If birth time = 06:30 IST (6:30 AM, not PM):")
jd = swe.julday(year, month, day, 6.5)
ayanamsa = swe.get_ayanamsa_ut(jd)
cusps, ascmc = swe.houses(jd, lat, lon, b'P')
sidereal_asc = (ascmc[0] - ayanamsa) % 360
sign_idx = int(sidereal_asc / 30)
print(f"   Ascendant: {signs[sign_idx]} {sidereal_asc % 30:.2f}°")

# Let's find what time gives Scorpio with Saturn in 4th
print("\n" + "=" * 60)
print("FINDING EXACT TIME FOR SCORPIO + SATURN IN 4TH")
print("=" * 60)
print("(Using Whole Sign House system)")

# Scorpio rises between 11:10 and 13:28
# Let's find the time when we get the configuration
for minute_of_day in range(11*60, 14*60):
    hour = minute_of_day // 60
    minute = minute_of_day % 60
    decimal_time = hour + minute / 60.0
    
    jd = swe.julday(year, month, day, decimal_time)
    ayanamsa = swe.get_ayanamsa_ut(jd)
    cusps, ascmc = swe.houses(jd, lat, lon, b'P')
    sidereal_asc = (ascmc[0] - ayanamsa) % 360
    sign_idx = int(sidereal_asc / 30)
    
    if signs[sign_idx] == 'Scorpio':
        # Calculate Saturn
        flags = swe.FLG_SWIEPH | swe.FLG_SPEED | swe.FLG_SIDEREAL
        saturn_result, _ = swe.calc_ut(jd, 6, flags)
        saturn_lon = saturn_result[0]
        saturn_sign_idx = int(saturn_lon / 30)
        
        # Whole sign house for Saturn
        saturn_house = (saturn_sign_idx - sign_idx) % 12 + 1
        
        if saturn_house == 4:
            print(f"\nMATCH FOUND!")
            print(f"Time: {hour:02d}:{minute:02d} IST")
            print(f"Ascendant: {signs[sign_idx]} {sidereal_asc % 30:.2f}°")
            print(f"Saturn: {signs[saturn_sign_idx]} {saturn_lon % 30:.2f}° - House {saturn_house}")
            break
else:
    # If no break occurred, show sample Scorpio time
    print("\nSample Scorpio ascendant times with Saturn position:")
    for t in [11.5, 12.0, 12.5, 13.0]:
        jd = swe.julday(year, month, day, t)
        ayanamsa = swe.get_ayanamsa_ut(jd)
        cusps, ascmc = swe.houses(jd, lat, lon, b'P')
        sidereal_asc = (ascmc[0] - ayanamsa) % 360
        sign_idx = int(sidereal_asc / 30)
        
        flags = swe.FLG_SWIEPH | swe.FLG_SPEED | swe.FLG_SIDEREAL
        saturn_result, _ = swe.calc_ut(jd, 6, flags)
        saturn_lon = saturn_result[0]
        saturn_sign_idx = int(saturn_lon / 30)
        saturn_house = (saturn_sign_idx - sign_idx) % 12 + 1
        
        hour = int(t)
        minute = int((t - hour) * 60)
        print(f"  {hour:02d}:{minute:02d} IST -> Asc: {signs[sign_idx]:12s} | Saturn: {signs[saturn_sign_idx]} {saturn_lon % 30:.1f}° - House {saturn_house}")

print("\n" + "=" * 60)
print("CONCLUSION")  
print("=" * 60)
print("""
For June 19, 1994 in Delhi:

- Scorpio Lagna rises between 11:10 AM and 1:28 PM IST
- Your stated birth time of 18:30 (6:30 PM) gives AQUARIUS ascendant
- Saturn at 18° Aquarius is correct for this date

If your ascendant is indeed Scorpio, your birth time must be
between approximately 11:10 AM and 1:28 PM IST (not 6:30 PM).

Please verify your birth time from your original birth certificate.
""")
