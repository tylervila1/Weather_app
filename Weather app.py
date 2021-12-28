import requests
from pprint import pprint


# help https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/
# https://openweathermap.org/api/one-call-api

API_KEY = '3bc2eb4e47c088902c1e9676a5a5406b'

city = input("enter a city:")

base_url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&units=imperial&appid="+API_KEY

weather_data = requests.get(base_url)

x = weather_data.json()
def current_weather ():
        if x["cod"] != "404":
            y = x["main"]
            t = x["wind"]
            z = x['weather']
            a = x['snow']



            current_temp = y["temp"]
            feels_like = y["feels_like"]
            weather_location = x["name"]
            wind_speed = t["speed"]
            gusts = t["gust"]
            weather_conditions = z[0]['description']
            max_temp = y["temp_max"]
            min_temp = y["temp_min"]
            snow_fall = a["1h"]




        print("The current temperature in "+str(weather_location)+" is "+str(current_temp)+"°F but it feels like " + str(feels_like)+"°F"+
              "\nWeather conditions are " + weather_conditions+ " with " + str(wind_speed)+ " MPH wind speeds and wind gusts of " + str(gusts) + " MPH.")

        print("\nThe high today is " + str(max_temp) + "°F and a low of " + str(min_temp)+ "°F" )
        print("In the last hour there has been a recorded " +str(snow_fall)+ " inches of snowfall")

current_weather()

