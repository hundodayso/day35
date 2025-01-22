from KEY import api_key
import requests
lat = '45.077713'
long = '6.702118'

api_key = api_key

payload = {'lat': lat, 'lon':long, 'appid':api_key, 'units': 'metric' }


r1 = requests.get('https://api.openweathermap.org/data/2.5/forecast?', params=payload)
print(r1.json())






