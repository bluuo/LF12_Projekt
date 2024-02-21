import requests

def sendRequest(location):
    query = '[out:json];area["admin_level"="8"]["name"='+location+'];out body;node["highway"="speed_camera"](area);out body;>;out skel qt;'
    return str(query)

def send_request(location):
    overpass_url = "http://overpass-api.de/api/interpreter"
    
    # Your Overpass Query
    query = f'[out:json];area["admin_level"="8"]["name"="{location}"];out body;node["highway"="speed_camera"](area);out body;>;out skel qt;'

    # Set up the request headers and parameters
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    params = {
        'data': query
    }

     # Make the request
    response = requests.post(overpass_url, headers=headers, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the response content (JSON data)
        print(response.json())
    else:
        print(f"Error: {response.status_code}")

def main():
    location = "berlin"
    ##request = sendRequest(location)

    ##print("Request Test")
    ##print("Start of the Query: \n" + request + "\nEnd of query")
    send_request(location)



if __name__ == "__main__":
    main()


