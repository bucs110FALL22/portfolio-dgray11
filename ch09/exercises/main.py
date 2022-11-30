import requests

#facts = requests.get("https://dog-api.kinduff.com/api/facts").json()
#print(facts.get("facts"))

pic = requests.get("http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=false").json()
print(pic)

