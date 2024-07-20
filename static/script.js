function initMap() {
    const sicilyBounds = {
        north: 38.5,
        south: 36.5,
        west: 12.0,
        east: 15.8
    };
    const sicily = { lat: 37.5999948, lng: 13.7189441 };
    const map = new google.maps.Map(document.getElementById("map"), {
        center: sicily,
        zoom: 8,
        mapId: MAP_ID,
        restriction: {
            latLngBounds: sicilyBounds,
            strictBounds: true
        }
    });

    waterTroughs.forEach(trough => {
        const marker = new google.maps.marker.AdvancedMarkerElement({
            map: map,
            position: { lat: trough.geometry.location.lat, lng: trough.geometry.location.lng },
            title: trough.name,
        });

        const infowindow = new google.maps.InfoWindow({
            content: `
                <div>
                    <h3>${trough.name}</h3>
                    ${trough.photos ? `<img src="https://maps.googleapis.com/maps/api/place/photo?maxwidth=100&photoreference=${trough.photos[0].photo_reference}&key=${API_KEY}" alt="${trough.name}">` : ''}
                </div>
            `
        });

        marker.addListener('click', () => {
            infowindow.open(map, marker);
        });
    });
}
