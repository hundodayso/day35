from KEY import api_key
import requests
from twilio.rest import Client
# lat = 45.077713
# long = 6.702118
lat = 45.326908
long = 14.441000

api_key = api_key

payload = {'lat': lat,
           'lon':long,
           'appid':api_key,
           'units': 'metric',
           'cnt': 4
           }


response = requests.get('https://api.openweathermap.org/data/2.5/forecast?', params=payload)
response.raise_for_status()

#print(response.json())
weather_data = response.json()
will_rain = False

for time in weather_data['list']:
    for item in time['weather']:
        if int(item['id']) < 700:
            will_rain = True
            print(item["id"])
if will_rain:
    print("Bring an umbrella")






