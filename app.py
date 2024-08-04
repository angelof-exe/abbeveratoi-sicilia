from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def fetch_watering_places():
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = """
    [out:json][timeout:25];
    nwr["amenity"="watering_place"](36.3203615818532,12.008056640625,39.15214258358986,16.644287109375004);
    out geom;
    """
    response = requests.get(overpass_url, params={'data': overpass_query})
    data = response.json()
    
    watering_places = []
    for element in data['elements']:
        lat = element.get('lat')
        lon = element.get('lon')
        
        if not lat or not lon:
            if 'center' in element:
                lat = element['center'].get('lat')
                lon = element['center'].get('lon')

        if lat and lon:  # Ensure we have valid coordinates before adding to list
            place = {
                'id': element['id'],
                'lat': lat,
                'lon': lon,
                'tags': element['tags'],
                'status': element['tags'].get('status', 'unknown')
            }
            watering_places.append(place)
    
    return watering_places

@app.route('/', methods=['GET', 'POST'])
def index():
    watering_places = fetch_watering_places()
    return render_template('index.html', watering_places=watering_places)

if __name__ == '__main__':
    app.run(debug=True)
