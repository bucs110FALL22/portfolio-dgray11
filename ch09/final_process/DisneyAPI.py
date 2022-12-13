import requests

class DisneyAPI:
    def __init__(self):
        self.url = 'https://api.disneyapi.dev/character/7'
      #'https://icanhazdadjoke.com/slack'
      #'https://coffee.alexflipnote.dev/random.json'
      #print(self.url)

    def get(self):
        r = requests.get(self.url)
        response = r.json()
        if response.get('imageUrl'):
            return response['imageUrl']
        else:
            return None
          
#     def change_category(self, category):
#         pass
# ############## delete after
#    def __init__(self, category=18, amount=1):
#         self.url = f'https://opentdb.com/api.php?amount={amount}&category={category}'

#     def get(self):
#         r = requests.get(self.url)
#         #response is just a json dictonary of values after .json() call
#         response = r.json()
#         #check to make sure I got a question, i.e. results
#         if response.get('results'):
#             return response['results']
#         else:
#             return None
