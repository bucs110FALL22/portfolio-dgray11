import requests

class DAPI:
    def __init__(self):
        self.url = f'https://api.disneyapi.dev/character/7'



# def get(self):
#         r = requests.get(self.url)
#         #response is just a json dictonary of values after .json() call
#         response = r.json()
#         #check to make sure I got a question, i.e. results
        
#         return response['imageUrl']
        