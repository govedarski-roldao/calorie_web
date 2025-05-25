import requests

url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    bitcoin = data["bitcoin"]["eur"]
    print(bitcoin)
else:
    print("Error accessing bitcoin")


