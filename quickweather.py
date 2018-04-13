#! python3
# quickweather.py - Prints the weather for a location from the command line

import json
import requests
import sys
import time

if len(sys.argv) < 2:
    print('Usage: quickWeather.py key location')
    sys.exit()

# Download the JSON data from OpenWeatherMap.org's API using key
# from command line arguments.
key = sys.argv[1]

# Compute location from command line arguments.
location = ' '.join(sys.argv[2:])

# Only available for paid accounts.
url1 = 'https://api.openweathermap.org/data/2.5/forecast/daily?' + \
        'q=%s&cnt=3&units=imperial&APPID=%s' % (location, key)

# Available for free accounts.
url2 = 'https://api.openweathermap.org/data/2.5/weather?' + \
        'q=%s&units=imperial&APPID=%s' % (location, key)
url3 = 'https://api.openweathermap.org/data/2.5/forecast?' + \
        'q=%s&units=imperial&APPID=%s' % (location, key)

response = requests.get(url2)
response.raise_for_status()

# Load JSON data into a Python variable.
weather_data = json.loads(response.text)

# Print weather descriptions.
m = weather_data['main']
w = weather_data['wind']
dt_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(weather_data['dt']))
print('Current weather in %s at %s: ' % (location, dt_str))
print('  Wind     - ', round(w['speed']), 'm/h' )
print('  Temp     - ', round(m['temp']), '\b\u00b0F')  # unicode is  u'\u2109'
print('  Pressure - ', round(m['pressure']), 'hpa')
print('  Humidity - ', round(m['humidity']), '\b%')
print()

response = requests.get(url3)
response.raise_for_status()

# Load JSON data into a Python variable.
weather_data = json.loads(response.text)

# Print weather descriptions.
w = weather_data['list']
dt_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(w[0]['dt']))
print('Weather in %s: ' % (location))
print('  Today at %s' % (dt_str))
print(' ', w[0]['weather'][0]['main'], '-', \
      w[0]['weather'][0]['description'], '-', \
      round(w[0]['main']['temp']),'\b\u00b0F')
print()
dt_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(w[11]['dt']))
print('  Tomorrow at %s' % dt_str)
print(' ', w[11]['weather'][0]['main'], '-', \
      w[11]['weather'][0]['description'], '-',\
      round(w[11]['main']['temp']),'\b\u00b0F')
print()
dt_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(w[19]['dt']))
print('  Day after tomorrow at %s' % dt_str)
print(' ', w[19]['weather'][0]['main'], '-',\
      w[19]['weather'][0]['description'], '-',\
      round(w[19]['main']['temp']),'\b\u00b0F')
