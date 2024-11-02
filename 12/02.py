import requests
from secret_weather_api_key import weatherkey
# which is just the key as a string ^^^

print(f'''
	-------------------
	|COOL WEATHER APP!|
	-------------------
  (just provide your own api key)
''')

location = input("What location's weather data do you want? ")
request = f"http://api.openweathermap.org/data/2.5/weather?appid={weatherkey}&units=metric&q={location}"
response = requests.get(request).json()
'''
example response:
response = {'coord': {'lon': 24.9355, 'lat': 60.1695}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 8.08, 'feels_like': 3.41, 'temp_min': 6.91, 'temp_max': 8.94, 'pressure': 1002, 'humidity': 79, 'sea_level': 1002, 'grnd_level': 1000}, 'visibility': 10000, 'wind': {'speed': 11.18, 'deg': 284, 'gust': 14.31}, 'clouds': {'all': 0}, 'dt': 1730272358, 'sys': {'type': 2, 'id': 2011913, 'country': 'FI', 'sunrise': 1730266710, 'sunset': 1730298548}, 'timezone': 7200, 'id': 658225, 'name': 'Helsinki', 'cod': 200}
'''
if response["cod"] == 200:
	location = response["name"]
	weather = response["weather"][0]
	conditions = response["main"]
	print(f'''
Location: {location}

Weather: {weather["description"]}

Temperature: {conditions["temp"]}°C
which feels like {conditions["feels_like"]}°C

The maximum temperature today will be {conditions["temp_max"]}°C
while the minimum temperature will be {conditions["temp_min"]}°C

Humidity: {conditions["humidity"]}%
	''')
else:
	print("invalid input")