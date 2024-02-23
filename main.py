from Frontend import Frontend
from RequestHandler import requestSpeedCameras
from JsonParser import JsonParser
import json

def main():
    print("program start")
    Frontend.loadUi()
    location_value, plz_value = Frontend.getEntryValues()

    
    response = requestSpeedCameras(location_value)
    parser = JsonParser(response)
    elements = parser.extract_elements()
    
    elementCount =  len(elements)
    
    print(elementCount)

if __name__ == "__main__":
    main()