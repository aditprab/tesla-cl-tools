#!/usr/bin/env python

import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('Configurations.properties')

def getAuthTokenUrl():
	return config.get('urls', 'baseUrl') + config.get('urls', 'tokenEndpoint')

def getChargeStateUrl():
    chargeStateUrl = config.get('urls', 'baseUrl') + config.get('urls', 'chargeStatusEndpoint')
    return chargeStateUrl % getVehicleId()

def getUsername():
	return config.get('auth', 'username')

def getPassword():
	return config.get('auth', 'password')

def getUserAgent():
	return config.get('auth', 'user-agent')

def getClientId():
	return config.get('auth', 'client-id')

def getClientSecret():
	return config.get('auth', 'client-secret')

def getVehicleId():
	return config.get('auth', 'vehicle-id')
