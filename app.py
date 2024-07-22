from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap
import requests
import json
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'
Bootstrap(app)

OVERPASS_URL = "http://overpass-api.de/api/interpreter"
OVERPASS_QUERY = """
[out:json][timeout:25];
nwr["amenity"="watering_place"](36.3203615818532,12.008056640625,39.15214258358986,16.644287109375004);
out geom;
"""

STATUS_FILE = 'watering_place_status.json'

# Carica lo stato degli abbeveratoi dal file
if os.path.exists(STATUS_FILE):
    with open(STATUS_FILE, 'r') as f:
        watering_place_status = json.load(f)
else:
    watering_place_status = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/watering_places')
def watering_places():
    response = requests.get(OVERPASS_URL, params={'data': OVERPASS_QUERY})
    data = response.json()

    # Aggiungi lo stato degli abbeveratoi
    for element in data['elements']:
        if element['type'] == 'node':
            key = f"{element['lat']},{element['lon']}"
            element['status'] = watering_place_status.get(key, 'unknown')

    return jsonify(data)

@app.route('/report_status', methods=['POST'])
def report_status():
    lat = float(request.form['lat'])
    lon = float(request.form['lon'])
    status = request.form.get('status')

    if status not in ['active', 'inactive']:
        flash('Per favore seleziona lo stato dell\'abbeveratoio.')
        return redirect(url_for('index'))

    key = f"{lat},{lon}"
    watering_place_status[key] = status

    # Salva lo stato degli abbeveratoi nel file
    with open(STATUS_FILE, 'w') as f:
        json.dump(watering_place_status, f)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
