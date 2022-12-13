import requests
  
class digimonAPI:
  
      def __init__(self):
          self.url('https://digimon-api.vercel.app/api/digimon')
  
      def get(self):
          r = requests.get(self.url)
          response = r.json()
          if response.get('img'):
              return response['img']
          else:
              return None



# response = requests.get("https://api.open-notify.org/astros.json")
# print(response.status_code)

# print(response.json())