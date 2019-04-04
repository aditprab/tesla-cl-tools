#!/usr/bin/env python

import requests
import json
import propertiesReader
import authTokenGenerator

print('''
  ______ ______ _____  __     ___ 
 /_  __// ____// ___/ / /    /   |
  / /  / __/   \__ \ / /    / /| |
 / /  / /___  ___/ // /___ / ___ |
/_/  /_____/ /____//_____//_/  |_|
                                                                
''')

authToken = authTokenGenerator.getAuthToken()
chargeStateUrl = propertiesReader.getChargeStateUrl()

headers = {
    'User-Agent':propertiesReader.getUserAgent(),
    'Content-Type': "application/json",
    'Authorization': "Bearer " + authToken
}

res = requests.request("GET", chargeStateUrl, headers=headers)
resJson = res.json()
response = resJson['response']

print("The Black Panther is: " + response['charging_state'] + ".")
print("The current charge level is: " + str(response['battery_range']) + " miles.")
print("Battery is " + str(response['battery_level']) + "%" " full");