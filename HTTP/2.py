import requests

r = requests.get("https://randomuser.me/api/")
data = r.json()

name = data["results"][0]["name"]["first"]
country = data["results"][0]["location"]["country"]
phone = data["results"][0]["phone"]

print(f"Hi, I'm {name}, I'm from {country}, my phone number is {phone}")