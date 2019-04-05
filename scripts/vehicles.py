#!/usr/bin/env python

import authTokenGenerator
import propertiesReader
import requests

authToken = authTokenGenerator.getAuthToken()
vehiclesUrl = propertiesReader.getVehiclesUrl()

headers = {
    'User-Agent':propertiesReader.getUserAgent(),
    'Content-Type': "application/json",
    'Authorization': "Bearer " + authToken
}

def getVehicles():
	res = requests.request("GET", vehiclesUrl, headers=headers)
	resJson = res.json()
	response = resJson['response']
	print(response)