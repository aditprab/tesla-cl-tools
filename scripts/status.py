#!/usr/bin/env python

import requests
import propertiesReader
import authTokenGenerator

def output(response):
    print("The Black Panther is: " + response['charging_state'] + ".")
    print("The current charge level is: " + str(response['battery_range']) + " miles.")
    print("Battery is " + str(response['battery_level']) + "%" " full");

def getStatus():
    authToken = authTokenGenerator.getAuthToken()
    chargeStateUrl = propertiesReader.getChargeStateUrl()

    headers = {
        'User-Agent': propertiesReader.getUserAgent(),
        'Content-Type': "application/json",
        'Authorization': "Bearer " + authToken
    }

    res = requests.request("GET", chargeStateUrl, headers=headers)
    resJson = res.json()
    response = resJson['response']
    output(response)
