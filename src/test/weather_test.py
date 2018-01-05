import requests
import unittest
from unittest.mock import MagicMock

from weather import get_weather_forecast


class WeatherTest(unittest.TestCase):
    expected_output = {'base': 'stations',
                       'clouds': {'all': 0},
                       'cod': 200,
                       'coord': {'lat': 28.47, 'lon': 77.03},
                       'dt': 1515150000,
                       'id': 1270642,
                       'main': {'humidity': 55,
                                'pressure': 1013,
                                'temp': 17,
                                'temp_max': 17,
                                'temp_min': 17},
                       'name': 'Gurgaon',
                       'sys': {'country': 'IN',
                               'id': 7809,
                               'message': 0.0079,
                               'sunrise': 1515116712,
                               'sunset': 1515154182,
                               'type': 1},
                       'visibility': 1200,
                       'weather': [{'description': 'smoke',
                                    'icon': '50d',
                                    'id': 711,
                                    'main': 'Smoke'}],
                       'wind': {'deg': 90, 'speed': 3.1}}

    def test_weather(self):
        mock = MagicMock()
        requests.get = mock
        mock().json = MagicMock(return_value=self.expected_output)

        actual_response = get_weather_forecast()

        requests.get.assert_called_with("http://api.openweathermap.org/data/2.5/weather"
                                        "?q=Gurgaon&units=metric&appid=5541fee053ab030b29d83cd944afe230")

        expected_response = 'The weather forcast for today is smoke, with an average of around 17, with 17 being the highest and 17 being the lowest'

        self.assertEqual(actual_response, expected_response)


if __name__ == '__main__':
    unittest.main()
