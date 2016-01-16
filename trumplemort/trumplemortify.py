import json


class Trumplemortifier:


    def __init__(self):
        with open("trumplemapping.json") as jsonfile:
           self.terms_file = json.load(jsonfile)

    def trumplemortify(self, status):
        return status

