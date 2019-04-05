#!/usr/bin/env python

import ConfigParser
import os

config = ConfigParser.RawConfigParser()
try:
	config.read('/tmp/Configurations.properties')
except Exception as e :
	print(str(e))


def getAuthTokenUrl():
	return config.get('urls', 'baseUrl') + config.get('urls', 'tokenEndpoint')

def getChargeStateUrl():
    chargeStateUrl = config.get('urls', 'baseUrl') + config.get('urls', 'chargeStatusEndpoint')
    return chargeStateUrl % getVehicleId()

def getVehiclesUrl():
	return config.get('urls', 'baseUrl') + config.get('urls', 'vehiclesEndpoint')

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

