import json


keys = None

def get_keys():
    global keys
    if keys:
        return keys

    with open("key.json", "r") as f:
        keys = json.load(f)
    return keys

def parse_character_name(name):
    if "-" in name:
        splitted = name.split("-")
        if len(splitted) > 1:
            return splitted[0], splitted[1]
    return name, None
