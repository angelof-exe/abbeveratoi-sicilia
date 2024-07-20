from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

GOOGLE_MAPS_API_KEY = os.getenv('API_KEY')  
MAP_ID = os.getenv('MAP_ID')

def get_water_troughs(location='37.5999948,13.7189441', radius=50000, keyword='abbeveratoio'):
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        'location': location,
        'radius': radius,
        'keyword': keyword,
        'key': GOOGLE_MAPS_API_KEY
    }
    response = requests.get(url, params=params)
    results = response.json().get('results', [])
    return results

@app.route('/')
def index():
    water_troughs = get_water_troughs()
    return render_template('index.html', api_key=GOOGLE_MAPS_API_KEY, map_id=MAP_ID, water_troughs=water_troughs)

if __name__ == '__main__':
    app.run(debug=True)
