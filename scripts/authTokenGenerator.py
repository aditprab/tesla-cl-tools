#!/usr/bin/env python

import csv
import json
import propertiesReader
import requests


def fetchAuthToken(email, password):
	url = propertiesReader.getAuthTokenUrl()
	querystring = {"grant_type":"password"}
	requestDict = {
	    'grant_type':'password',
	    'client_id':propertiesReader.getClientId(),
	    'client_secret':propertiesReader.getClientSecret(),
	    'email':email,
	    'password':password
	}

	payload = json.dumps(requestDict)

	headers = {
	    'Content-Type': "application/json",
	    'User-Agent': propertiesReader.getUserAgent()
	}

	# send request
	response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
	resJson = response.json()

	# collect necessary response fields
	authToken = resJson['access_token']
	expiresIn = resJson['expires_in']
	refreshToken = resJson['refresh_token']

	# persist auth info
	with open('./assets/auth', 'w') as auth_file:
		auth_writer = csv.writer(auth_file, delimiter=',')
		auth_writer.writerow([authToken, expiresIn, refreshToken])

	return authToken

# TODO needs work
def getAuthToken():
	with open('./assets/auth', 'r') as auth_file:
		auth_reader = csv.reader(auth_file, delimeter=',')
		for row in auth_reader:
			authToken = row[0]
			expiresIn = row[1]
			refreshToken = row[2]
			return authToken