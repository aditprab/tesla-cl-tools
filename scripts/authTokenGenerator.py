#!/usr/bin/env python

import requests
import json
import propertiesReader


def getAuthToken():
	url = propertiesReader.getAuthTokenUrl()
	querystring = {"grant_type":"password"}
	requestDict = {
	    'grant_type':'password',
	    'client_id':propertiesReader.getClientId(),
	    'client_secret':propertiesReader.getClientSecret(),
	    'email':propertiesReader.getUsername(),
	    'password':propertiesReader.getPassword()
	}

	payload = json.dumps(requestDict)

	headers = {
	    'Content-Type': "application/json",
	    'User-Agent': propertiesReader.getUserAgent()
	}

	response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
	resJson = response.json()
	authToken = resJson['access_token']
	return authToken

