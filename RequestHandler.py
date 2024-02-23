import requests

def requestSpeedCameras(location):
    overpass_url = "http://overpass-api.de/api/interpreter"
    query = f"""
    [out:json];
    area
        ["admin_level"="8"]
        ["name"="{location}"];
    out body;

    node["highway"="speed_camera"](area);
    out body;
    >;
    out skel qt;
    """
    params = {
        "data": query,
    }
    response = requests.get(overpass_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
    
def requestAllCities(location):
    overpass_url = "http://overpass-api.de/api/interpreter"
    query = f"""
    [out:json];
    area["ISO3166-1"="DE"][admin_level=2]->.searchArea;
    (
    node["place"="city"](area.searchArea);
    );
    out center;
    """
    params = {
        "data": query,
    }
    response = requests.get(overpass_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def requestPrintAllElements(location):
    requestAnswer = requestSpeedCameras(location)
    
    if requestAnswer:
        # Process the result as needed
        for element in requestAnswer.get("elements", []):
           print(element)
    
