import random 
import delete #Proxy Class

def main():
    
    api = delete.delete()
    results = api.get()
  
    for i in results:
      picture = ['img']
      print(f"{i['img']} this is the url")

main()
