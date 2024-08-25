
function getLocation() {
    if(navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    }
    else {
     console.log("error in getting location")
    }
}

async function showPosition(position) {

    const userCoordinates = {
        lat: position.coords.latitude,
        lon: position.coords.longitude,
    }

    console.log(userCoordinates)
    const response = await fetch(
        "https://api-test.openepi.io/soil/type?" +
            new URLSearchParams({
                lon: userCoordinates.lon,
                lat: userCoordinates.lat,
            })
    )
    const json = await response.json()
    
    
    const mostProbableSoilType = json.properties.most_probable_soil_type
    
    console.log(`Most probable soil type: ${mostProbableSoilType}`)

}


         
      
  


     

