import json
from configs import *


def save_configurations(configs):
    baseJson = {
        "gameFolder": configs.gameFolder,
        "googleDriveFolder": configs.googleDriveFolder,
    }
    json_object = json.dumps(baseJson, indent = 4)
    with open("configs.json", "w") as outfile:
        outfile.write(json_object)

def read_json(json):
    print()