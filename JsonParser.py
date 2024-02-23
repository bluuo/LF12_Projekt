class JsonParser:
    def __init__(self, json_data):
        self.json_data = json_data

    def parse(self):
        parsed_data = []
        for element in self.json_data["elements"]:
            if element["type"] == "node":
                parsed_element = {
                    "lat": element,
                    "lon": element,
                    "maxspeed": element["tags"]
                }
                parsed_data.append(parsed_element)
        return parsed_data

    def extract_elements(self):
        return self.json_data.get("elements", [])

