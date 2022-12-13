import requests

class digimonAPI:

    def __init__(self):
        self.api_url = 'https://digimon-api.vercel.app/api/digimon'

    def get(self):
        pic = requests.get(self.api_url)
        response = pic.json()
        print(response)

        # print()
        # if response.get('name'):
        #     return response['name']
        # else:
        #     return None
