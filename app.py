from flask import Flask, render_template
import requests
import json
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

# Load OpenStreetMap data with status
def load_watering_places():
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = """
    [out:json][timeout:25];
    nwr["amenity"="watering_place"](36.3203615818532,12.008056640625,39.15214258358986,16.644287109375004);
    out geom;
    """
    response = requests.get(overpass_url, params={'data': overpass_query})
    data = response.json()
    return data['elements']

watering_places = load_watering_places()

@app.route('/')
def index():
    return render_template('index.html', watering_places=watering_places)

if __name__ == '__main__':
    app.run(debug=True)
