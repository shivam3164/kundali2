# Placeholder for Vimshottari Dasha calculation

import datetime

# Nakshatra lords and dasha years
VIMSHOTTARI_SEQUENCE = [
    ('Ketu', 7), ('Venus', 20), ('Sun', 6), ('Moon', 10), ('Mars', 7),
    ('Rahu', 18), ('Jupiter', 16), ('Saturn', 19), ('Mercury', 17)
]

def calculate_vimshottari_dasha(moon_longitude, birth_date):
    # Find nakshatra index
    nakshatra_index = int(moon_longitude // (360/27))
    lord, years = VIMSHOTTARI_SEQUENCE[nakshatra_index % 9]
    # Calculate balance of first dasha
    nakshatra_start = nakshatra_index * (360/27)
    elapsed = moon_longitude - nakshatra_start
    balance = (1 - (elapsed / (360/27))) * years
    # Build dasha timeline
    dashas = []
    start_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d")
    # First dasha
    dashas.append({
        'lord': lord,
        'start': start_date.strftime('%Y-%m-%d'),
        'end': (start_date + datetime.timedelta(days=balance*365.25)).strftime('%Y-%m-%d'),
        'years': balance
    })
    # Remaining dashas
    idx = (nakshatra_index + 1) % 9
    date = start_date + datetime.timedelta(days=balance*365.25)
    for i in range(9):
        lord, years = VIMSHOTTARI_SEQUENCE[idx]
        dashas.append({
            'lord': lord,
            'start': date.strftime('%Y-%m-%d'),
            'end': (date + datetime.timedelta(days=years*365.25)).strftime('%Y-%m-%d'),
            'years': years
        })
        date += datetime.timedelta(days=years*365.25)
        idx = (idx + 1) % 9
    return dashas
