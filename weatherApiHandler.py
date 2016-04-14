#!/usr/bin/python
#

import requests
import json


class ApiHandler:

    def temperature(self, address):
        """
        This is basically the address to find the temperature for
        :param address:
        :return:true if it found the address False otherwise
        """

        api_endpoint_location = "https://maps.googleapis.com/maps/api/geocode/json?address="

        api_endpoint_forecast = "https://api.forecast.io/forecast/c931a56775202db9dee5bf09e73d5511/"

        location_response = requests.get(api_endpoint_location + address)

        json_data_location = json.loads(location_response.text)

        try:
            lat_lon_convert = json_data_location['results'][0]['geometry']['location']

            location_weather = requests.get(api_endpoint_forecast + str(lat_lon_convert['lat'])
                                            + "," + str(lat_lon_convert['lng']))

            json_data_weather = json.loads(location_weather.text)

            weather_convert = json_data_weather['currently']

            print "Current Temperature: " + str(weather_convert['temperature'])
        except IndexError as e:
            print "There was an error getting the data."
            print e.message

    def humidity(self, address):
        """
        This will find the humidity for the address
        :param address:
        :return: true if it found the address False otherwise
        """

        api_endpoint_location = "https://maps.googleapis.com/maps/api/geocode/json?address=?"

        api_endpoint_forecast = "https://api.forecast.io/forecast/c931a56775202db9dee5bf09e73d5511/"

        location_response = requests.get(api_endpoint_location + address)

        json_data_location = json.loads(location_response.text)

        try:
            lat_lon_convert = json_data_location['results'][0]['geometry']['location']

            location_weather = requests.get(api_endpoint_forecast + str(lat_lon_convert['lat'])
                                            + "," + str(lat_lon_convert['lng']))

            json_data_weather = json.loads(location_weather.text)

            weather_convert = json_data_weather['currently']

            print "Current Humidity: " + str(weather_convert['humidity'])
        except IndexError as e:
            print "There was an error getting the data."
            print e.message
