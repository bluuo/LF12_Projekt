class JsonParser:
    def __init__(self, json_data):
        self.json_data = json_data

    def parse(self):
        parsed_data = []
        for element in self.json_data["elements"]:
            if element["type"] == "area":
                parsed_element = {
                    "id": element["id"],
                    "name": element["tags"]["name"],
                    "type": element["tags"].get("place", ""),
                    "admin_level": element["tags"]["admin_level"],
                    "boundary_type": element["tags"]["boundary"],
                    "wikidata": element["tags"].get("wikidata", ""),
                    "wikipedia": element["tags"].get("wikipedia", ""),
                }
                parsed_data.append(parsed_element)
        return parsed_data

    def extract_elements(self):
        return self.json_data.get("elements", [])

