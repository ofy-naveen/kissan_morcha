document.addEventListener('DOMContentLoaded', (event) => {
    const soilProperties = {
        'Acrisols': [10, 5, 20, 5.5],
        'Albeluvisols': [12, 6, 22, 6.0],
        'Alisols': [8, 4, 18, 5.0],
        'Andosols': [15, 7, 25, 6.5],
        'Arenosols': [5, 3, 10, 4.5],
        'Calcisols': [20, 10, 30, 7.0],
        'Cambisols': [14, 6, 23, 6.2],
        'Chernozems': [18, 8, 27, 6.8],
        'Cryosols': [7, 3, 15, 4.8],
        'Durisols': [11, 5, 21, 5.6],
        'Ferralsols': [13, 7, 26, 6.3],
        'Fluvisols': [16, 8, 28, 6.7],
        'Gleysols': [9, 4, 19, 5.4],
        'Gypsisols': [6, 3, 12, 4.9],
        'Histosols': [20, 9, 29, 6.9],
        'Kastanozems': [17, 8, 24, 6.6],
        'Leptosols': [8, 4, 17, 5.2],
        'Lixisols': [14, 6, 22, 6.1],
        'Luvisols': [12, 5, 20, 5.8],
        'Nitisols': [15, 7, 23, 6.4],
        'Phaeozems': [18, 9, 26, 6.9],
        'Planosols': [10, 4, 18, 5.5],
        'Plinthosols': [11, 5, 19, 5.7],
        'Podzols': [7, 3, 14, 4.6],
        'Regosols': [13, 6, 22, 6.0],
        'Solonchaks': [9, 4, 16, 5.3],
        'Solonetz': [11, 5, 20, 5.9],
        'Stagnosols': [12, 6, 23, 6.2],
        'Umbrisols': [14, 7, 25, 6.8],
        'Vertisols': [16, 8, 27, 6.5]
    };

    const apiKey = '010630c56f4a42ddadf61525241705';
    const soilTypeCache = new Map(); // Cache to store soil types based on location

    function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition, showError);
        } else {
            alert("Geolocation is not supported by this browser.");
        }
    }

    function showPosition(position) {
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;

        document.getElementById('latitude').value = lat;
        document.getElementById('longitude').value = lon;

        const locationKey = `${lat},${lon}`;
        
        if (soilTypeCache.has(locationKey)) {
            // Use cached soil type
            const soilType = soilTypeCache.get(locationKey);
            fillFormFields(soilType, lat, lon);
        } else {
            determineSoilType(lat, lon)
                .then(soilType => {
                    soilTypeCache.set(locationKey, soilType); // Cache the soil type
                    fillFormFields(soilType, lat, lon);
                })
                .catch(error => {
                    alert('Unable to determine soil type.');
                    console.error(error);
                });
        }
    }

    function fillFormFields(soilType, lat, lon) {
        const properties = soilProperties[soilType] || [0, 0, 0, 0]; // Fallback to default values

        document.getElementById('potassium').value = properties[0];
        document.getElementById('nitrogen').value = properties[1];
        document.getElementById('phosphorous').value = properties[2];
        document.getElementById('phlevel').value = properties[3];

        fetchWeatherData(lat, lon).then(weatherData => {
            document.getElementById('temperature').value = weatherData.temperature;
            document.getElementById('humidity').value = weatherData.humidity;
            document.getElementById('rainfall').value = weatherData.rainfall;

        }).catch(error => {
            alert('Unable to retrieve weather data.');
            console.error(error);
        });
    }

    function determineSoilType(lat, lon) {
        // Replace this with actual logic to determine soil type based on coordinates.
        return new Promise((resolve, reject) => {
            // Example: return a random soil type from the list
            const soilTypes = Object.keys(soilProperties);
            const randomSoilType = soilTypes[Math.floor(Math.random() * soilTypes.length)];
            resolve(randomSoilType);
        });
    }

    function fetchWeatherData(lat, lon) {
        const url = `https://api.weatherapi.com/v1/current.json?key=${apiKey}&q=${lat},${lon}`;

        return fetch(url)
            .then(response => response.json())
            .then(data => {
                return {
                    temperature: data.current.temp_c,
                    humidity: data.current.humidity,
                    rainfall: data.current.precip_mm
                };
            });
    }

    function showError(error) {
        switch(error.code) {
            case error.PERMISSION_DENIED:
                alert("User denied the request for Geolocation.");
                break;
            case error.POSITION_UNAVAILABLE:
                alert("Location information is unavailable.");
                break;
            case error.TIMEOUT:
                alert("The request to get user location timed out.");
                break;
            case error.UNKNOWN_ERROR:
                alert("An unknown error occurred.");
                break;
        }
    }

    // Attach the getLocation function to the button click
    document.querySelector('.loc-button').addEventListener('click', getLocation);
});
