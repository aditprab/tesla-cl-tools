#!/usr/bin/env python

import requests
import propertiesReader
import authTokenGenerator
import vehicles

def output(vehicleName, response):
    print(vehicleName +  " is: " + response['charging_state'] + ".")
    print("The current charge level is: " + str(response['battery_range']) + " miles.")
    print("Battery is " + str(response['battery_level']) + "%" " full")

def getStatus():
    (vehicleName,vehicleId) = vehicles.getVehicles()
    authToken = authTokenGenerator.getAuthToken()
    url = propertiesReader.getChargeStateUrl()
    chargeStateUrl = url % vehicleId
    headers = {
        'User-Agent': propertiesReader.getUserAgent(),
        'Content-Type': "application/json",
        'Authorization': "Bearer " + authToken
    }


    res = requests.request("GET", chargeStateUrl, headers=headers)
    resJson = res.json()
    response = resJson['response']
    output(vehicleName, response)
