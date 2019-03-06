import json


def get_keys():
    with open("key.json", "r") as f:
        keys = json.load(f)
    return keys
