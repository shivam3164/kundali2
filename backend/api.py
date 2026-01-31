from fastapi import FastAPI, Request
from chart import generate_chart
from dasha import calculate_vimshottari_dasha
from yoga import detect_yogas
from interpretation import generate_interpretations

app = FastAPI()

@app.post('/chart')
async def create_chart(request: Request):
    data = await request.json()
    year = data['year']
    month = data['month']
    day = data['day']
    hour = data['hour']
    minute = data['minute']
    lat = data['lat']
    lon = data['lon']
    ayanamsa = data.get('ayanamsa', 0)
    chart = generate_chart(year, month, day, hour, minute, lat, lon, ayanamsa)
    dashas = calculate_vimshottari_dasha(chart['planet_positions']['Moon']['longitude'], f"{year}-{month}-{day}")
    yogas = detect_yogas(chart)
    interpretations = generate_interpretations(chart, dashas, yogas)
    return {
        'chart': chart,
        'dashas': dashas,
        'yogas': yogas,
        'interpretations': interpretations
    }
