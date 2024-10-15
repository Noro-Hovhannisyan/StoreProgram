import json


class JsonManager:
    def load(self, file_name):
        with open(file_name) as json_file:
            data = json.load(json_file)
            return data

    def dump(self, data, file_name):
        with open(file_name, 'w') as json_file:
            json.dump(data, json_file)
