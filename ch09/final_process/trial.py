import requests

class trial:
  
  def __init__(self):
  
    self.api_url = requests.get("https://coffee.alexflipnote.dev/random.json")
    print(self.api_url)
    
