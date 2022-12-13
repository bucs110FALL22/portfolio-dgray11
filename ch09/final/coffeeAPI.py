import requests

class coffeeAPI:

    def __init__(self):
        self.url = 'https://coffee.alexflipnote.dev/random.json'

    def get(self):
        pic = requests.get(self.url)
        response = pic.json()
        print(response)
        if response.get('file'):
            return response['file']
        else:
            return None

        # print()
        # if response.get('name'):
        #     return response['name']
        # else:
        #     return None