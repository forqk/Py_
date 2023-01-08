import sys
import pprint
import requests
from dateutil.parser import parse


class YahooWeatherForecast:

    #def __init__(self):
    #    self._city_cache = {}

    def get(self, city):
        #if city in self._cached_data:
        #     return self._cached_data[city]
        lat = 55.75
        lon = 37.62
        api_key = '' #personal key.
        url = f"https://api.openweathermap.org/data/2.5/weather?q=London&APPID={api_key}"
        data = requests.get(url).json()
        forecast = []
        print(data)
        forecast_data = data["main"]
        for day_data in forecast_data:
            forecast.append({
              # "date": parse(day_data["time"]),
                "high_temp": int(day_data["temp_max"])
            })
        #self._cached_data[city] = forecast
        return forecast


class CityInfo:
    def __init__(self, city, forecast_provider=None):
        self.city = city.lower()
        self._forecast_provider = forecast_provider or YahooWeatherForecast()

    def weather_forecast(self):
        return self._forecast_provider.get(self.city)


def _main():
    city = CityInfo(sys.argv[1]) # latitude longitude .
    forecast = city.weather_forecast()
    pprint.pprint(forecast)


if __name__ == "__main__":
    _main()