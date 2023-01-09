import sys
import pprint
import requests
from dateutil.parser import parse


class OpenWeatherMap:

    #def __init__(self):
    #    self._city_cache = {}

    def get(self, city):
        #if city in self._cached_data:
        #     return self._cached_data[city]
        api_key = '' #personal key.
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}"
        data = requests.get(url).json()
        forecast = []
      #  print(data)

        forecast.append({"City": data['name']})
        forecast.append({"high_temp": data['main']['temp_min']})
        forecast.append({"high_temp": data['main']['temp_max']})
        
          
        #self._cached_data[city] = forecast
        return forecast


class CityInfo:
    def __init__(self, city, forecast_provider=None):
        self.city = city.lower()
        self._forecast_provider = forecast_provider or OpenWeatherMap()

    def weather_forecast(self):
        return self._forecast_provider.get(self.city)


def _main():
    city = CityInfo(sys.argv[1]) # input Moscow, London etc...
    forecast = city.weather_forecast()
    pprint.pprint(forecast)


if __name__ == "__main__":
    _main()