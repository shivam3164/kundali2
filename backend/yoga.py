# Placeholder for Yoga detection logic

from bphs_rules import YOGAS

def detect_yogas(chart):
    yogas = []
    planets = chart['planets']
    # Helper: get house for a planet
    def get_house(longitude):
        return int(longitude // 30) + 1

    for yoga_rule in YOGAS:
        cond = yoga_rule['conditions']
        # Gaja Kesari Yoga
        if yoga_rule['name'] == 'Gaja Kesari Yoga':
            moon_house = get_house(planets['Moon']['longitude'])
            jupiter_house = get_house(planets['Jupiter']['longitude'])
            if moon_house in cond['houses'] and jupiter_house in cond['houses']:
                yogas.append({
                    'name': yoga_rule['name'],
                    'strength': 80,
                    'notes': yoga_rule['description'],
                    'reference': yoga_rule['reference']
                })
        # Chandra-Mangal Yoga
        elif yoga_rule['name'] == 'Chandra-Mangal Yoga':
            if abs(planets['Moon']['longitude'] - planets['Mars']['longitude']) < 10:
                yogas.append({
                    'name': yoga_rule['name'],
                    'strength': 70,
                    'notes': yoga_rule['description'],
                    'reference': yoga_rule['reference']
                })
        # Budha-Aditya Yoga
        elif yoga_rule['name'] == 'Budha-Aditya Yoga':
            sun_house = get_house(planets['Sun']['longitude'])
            mercury_house = get_house(planets['Mercury']['longitude'])
            if sun_house == mercury_house:
                yogas.append({
                    'name': yoga_rule['name'],
                    'strength': 75,
                    'notes': yoga_rule['description'],
                    'reference': yoga_rule['reference']
                })
        # Neechabhanga Raj Yoga
        elif yoga_rule['name'] == 'Neechabhanga Raj Yoga':
            # Sun in Libra, Venus in kendra
            if 180 <= planets['Sun']['longitude'] < 210:
                venus_house = get_house(planets['Venus']['longitude'])
                if venus_house in [1, 4, 7, 10]:
                    yogas.append({
                        'name': yoga_rule['name'],
                        'strength': 85,
                        'notes': yoga_rule['description'],
                        'reference': yoga_rule['reference']
                    })
        # Vipreet Raj Yoga
        elif yoga_rule['name'] == 'Vipreet Raj Yoga':
            mars_house = get_house(planets['Mars']['longitude'])
            if mars_house in [6, 8, 12]:
                yogas.append({
                    'name': yoga_rule['name'],
                    'strength': 65,
                    'notes': yoga_rule['description'],
                    'reference': yoga_rule['reference']
                })
        # Add more yogas as you expand YOGAS
    return yogas
