import requests

def request(query):
    overpass_url = "http://overpass-api.de/api/interpreter"
    params = {
        "data": query,
    }

    response = requests.get(overpass_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def main():
    location = "Berlin"
    overpass_query_template = f"""
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

    result = request(overpass_query_template)

    if result:
        # Process the result as needed
        for element in result.get("elements", []):
            print(element)

if __name__ == "__main__":
    main()
