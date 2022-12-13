import requests
import json

class trial_digimonAPI:

    def __init__(self):
        self.url = requests.get('https://digimon-api.vercel.app/api/digimon')

    def get(self):
        #r = requests.get(self.url)
        
        data = self.url.text
        parse_json = json.loads(data)
        active_case = parse_json['img']
        print("This is the URL for a digimon image:", active_case)



      
        # #response is just a json dictonary of values after .json() call
        # response = r.json()
        # #check to make sure I got a question, i.e. results
        # if response.get('img'):
        #     return response['img']
        # else:
        #     return None
