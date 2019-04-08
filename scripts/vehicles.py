#!/usr/bin/env python

import authTokenGenerator
import propertiesReader
import requests


def getVehicles():
    authToken = authTokenGenerator.getAuthToken()

    headers = {
        'User-Agent':propertiesReader.getUserAgent(),
        'Content-Type': "application/json",
        'Authorization': "Bearer " + authToken
    }

    vehiclesUrl = propertiesReader.getVehiclesUrl()
    response = requests.request("GET", vehiclesUrl, headers=headers)
    json = response.json()
    resJson =  json['response'][0]
    return (resJson['display_name'],resJson['id'])
