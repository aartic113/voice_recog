import requests 


api_address = "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + "c38c64b316b14a58a7a3e34d9bf11e59"
json_data = requests.get(api_address).json()


ar = [ ]

def news():
	for i in range(3):
		ar.append("Number " + str(i+1) + ", " + json_data["articles"][i]["title"] + ".")

	return ar


# arr = news()

# print(arr)

