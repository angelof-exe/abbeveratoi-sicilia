![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

# Abbeveratoi in Sicilia

**Abbeveratoi in Sicilia** is a simple web application built with [Flask](https://flask.palletsprojects.com/en/3.0.x/). It displays the various watering places ("abbeveratoi") scattered across Sicily, utilizing data from OpenStreetMap.

The project is aimed at mapping active, inactive, and unknown-status watering places, with the ultimate goal of identifying and highlighting those that are inactive but could be restored. The restoration of these facilities could be crucial in supporting agricultural needs and ensuring water availability during periods of extreme drought. 

This project combines historical preservation with modern water resource management, promoting environmental sustainability and the conservation of cultural heritage during critical times of water scarcity.

## Features

- **Interactive Map**: Visualize Sicilian watering places on a map with different markers representing their statuses (active, inactive, unknown).
- **Filter Functionality**: Easily filter watering places based on their status using buttons in the UI.
- **Detail View**: Clicking on a watering place in the list or on the map provides details, including location and status, with a direct link to OpenStreetMap.

## Future Enhancements

- **Restoration Feature**: Identify potential inactive watering places that could be restored for public use.
- **Data Collection**: Integrate feedback mechanisms to collect updated status and information directly from users or local authorities.

## Setup

Follow these steps to set up the project on your local machine:

### Prerequisites

Make sure you have Python installed. You can download it from the [official Python website](https://www.python.org/downloads/).

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/abbeveratoi-in-sicilia.git
   cd abbeveratoi-in-sicilia
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Visit `http://127.0.0.1:5000/` in your browser to view the web app.

## Project Structure

```
.
├── app.py                        # Main Flask app
├── README.md                     # Project documentation
├── requirements.txt              # Dependencies
├── static
│   ├── css
│   │   └── style.css             # Custom styling
│   └── style.css
├── templates
│   └── index.html                # HTML template
└── watering_place_status.json    # Example data file with watering place statuses
```

## Technologies Used

- **Python**: Main programming language.
- **Flask**: Web framework used for building the app.
- **Bootstrap**: Frontend framework for responsive design.
- **Leaflet.js**: JavaScript library for interactive maps.
- **OpenStreetMap API**: Data source for mapping watering places.

## Relevant Links

Read more about the restoration efforts related to these watering places:

- [Pulizia e valorizzazione degli abbeveratoi - Riberalab al lavoro](https://www.risoluto.it/notizie-ribera/pulizia-e-valorizzazione-degli-abbeveratoi-riberalab-al-lavoro/)
- [Sicily Abbeveratoi Restoration News - Il Fatto Nisseno](https://www.ilfattonisseno.it/2024/07/848488/)

