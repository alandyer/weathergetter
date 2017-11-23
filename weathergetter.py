#!/usr/bin/env python3

import json, requests, sys, os

def get_weather_for_loc(loc, api_key):
  try:
    result = requests.get("http://dataservice.accuweather.com/currentconditions/v1/" + loc + "?apikey=" + api_key)
  except:
    print("Exception while getting weather")
  else:
    if result.ok:
      return json.loads(result.text)[0]
    else:
      sys.exit("Error retrieving location data from server")

def get_loc(location, api_key):
  try:
    result = requests.get("http://dataservice.accuweather.com/locations/v1/search?apikey=" + api_key + "&q=" + location)
  except:
    print("Exception while getting location")
  else:
    if result.ok:
      return json.loads(result.text)[0]
    else:
      sys.exit("Error retrieving location '" + location + "' from server")


#### Main
if len(sys.argv) != 2:
  exit("Usage: python " + __file__ + " some_location")

arg1 = sys.argv[1]

api_key = os.getenv('ACCUWEATHER_API_KEY', "nokey")

if api_key == "nokey":
  exit("Set environment variable ACCUWEATHER_API_KEY=YOURKEY")

loc = get_loc(arg1, api_key)

weather = get_weather_for_loc(loc['Key'], api_key)

print("The temperature in " + loc['EnglishName'] + " is " + repr(weather['Temperature']['Metric']['Value']) + "C and the condition is " + repr(weather['WeatherText']))
