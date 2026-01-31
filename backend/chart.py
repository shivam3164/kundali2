from ephemeris import get_planet_positions
import swisseph as swe

def generate_chart(year, month, day, hour, minute, lat, lon, ayanamsa=0):
    jd = swe.julday(year, month, day, hour + minute/60.0)
    positions = get_planet_positions(jd, ayanamsa)
    # TODO: Compute ascendant, houses, nakshatra, panchanga, etc.
    chart = {
        'planet_positions': positions,
        'ascendant': None,
        'houses': None,
        'nakshatra': None,
        'panchanga': None
    }
    return chart
