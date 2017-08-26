import requests

def get_weather_forecast():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Gurgaon&units=metric&appid=5541fee053ab030b29d83cd944afe230'
    weather_response = requests.get(url).json()
    weather_desc = weather_response['weather'][0]['description']
    max_temp = weather_response['main']['temp_max']
    min_temp = weather_response['main']['temp_min']
    avg_temp = weather_response['main']['temp']
    forecast = 'The weather forcast for today is ' + weather_desc + ', with an average of around ' + str(avg_temp)
    forecast += ', with ' + str(max_temp) + ' being the highest and ' + str(min_temp) + ' being the lowest'
    return forecast