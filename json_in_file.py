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

def read_json():

    file = open('configs.json','r')
    deserialized_json = json.loads(file.read())
    user_configs = Configs(deserialized_json['gameFolder'],deserialized_json['googleDriveFolder'])
    return user_configs