import requests


api_address = 'https://api.openweathermap.org/data/2.5/weather?q=London&appid=dfedd0d2146b68099b5107a72b15e46d'
json_data = requests.get(api_address).json()

def temp():
	temperature = round(json_data["main"]["temp"]-273,1)
	return temperature


def des():
	description = json_data["weather"][0]["description"]
	return description

# print(temp())
# print(des())
