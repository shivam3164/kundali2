import swisseph as swe

# Example function to get planetary positions

def get_planet_positions(jd, lat, lon, ayanamsa=0):
    swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)  # Default to Lahiri ayanamsa
    planets = ['Sun', 'Moon', 'Mars', 'Mercury', 'Jupiter', 'Venus', 'Saturn', 'Rahu', 'Ketu']
    planet_codes = [swe.SUN, swe.MOON, swe.MARS, swe.MERCURY, swe.JUPITER, swe.VENUS, swe.SATURN, swe.TRUE_NODE, swe.MEAN_NODE]
    positions = {}
    for name, code in zip(planets, planet_codes):
        res = swe.calc_ut(jd, code)
        lon, lat, dist = res[0:3]
        retrograde = res[3] < 0
        # Nakshatra and pada calculation
        nakshatra = int(lon // (360/27)) + 1
        pada = int((lon % (360/27)) // ((360/27)/4)) + 1
        positions[name] = {
            'longitude': lon,
            'latitude': lat,
            'retrograde': retrograde,
            'nakshatra': nakshatra,
            'pada': pada
        }
    # Ascendant calculation
    asc = swe.houses(jd, lat, lon, b'A')[0][0]
    # House cusps
    houses = swe.houses(jd, lat, lon, b'P')[0]
    return {
        'planets': positions,
        'ascendant': asc,
        'houses': houses
    }

# Example usage:
# jd = swe.julday(year, month, day, hour)
# positions = get_planet_positions(jd)
