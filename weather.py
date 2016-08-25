# -*- coding: utf-8 -*-
import sys
from json import load
from urllib2 import urlopen
from netaddr import valid_ipv4


def main():

    print "Please supply an IP address to display the current weather or press [enter] to check using your public IP"
    ip_adddress = raw_input()

    if not(ip_adddress):
        print "Getting your public IP"
        ip_adddress = get_public_addrress()

    if valid_ipv4(ip_adddress):
        print "IP address valid: " + str(ip_adddress)

        lat, long = get_location(ip_adddress)

        print "Location: Lat: " + str(lat) + " Long: " + str(long)

        weather = get_weather(str(lat), str(long))

        print "---------------------------------------------"
        print "Current temperature: "  + str(weather['temp'])
        print "Humidity: " + str(weather['humidity'])
        print "Pressure: " + str(weather['pressure'])
        print "Max temperature: " + str(weather['temp_max'])
        print "Min temperature: " + str(weather['temp_min'])
        print "---------------------------------------------"

    else:
        sys.exit("Invalid IP address")


def get_public_addrress():
    """
    Retrieves public UP using ipify
    """

    GET_IP_URL = 'https://api.ipify.org/?format=json'

    try:
        my_ip = load(urlopen(GET_IP_URL))['ip']
    except:
        raise

    return my_ip

def get_location(ip_address):
    """
    Retrieves location coordinates using freegeoip
    """

    GET_LOCATION_URL = "http://freegeoip.net/json/" + ip_address


    try:
        location = load(urlopen(GET_LOCATION_URL))
        latitude = location['latitude']
        longitude = location['longitude']
    except:
        raise
    return latitude, longitude

def get_weather(lat, long):
    """
    Retrieves current weather using openweathermap API
    """


    API_KEY = '1e9445ea75b934fee438f0c688407dc5'

    GET_WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?units=metric&lat=" + lat + "&lon=" + long + "&APPID=" + API_KEY

    try:
        weather = load(urlopen(GET_WEATHER_URL))
        weather = weather['main']
    except:
        raise

    return weather


if __name__ == "__main__":

    main()
    sys.exit()

