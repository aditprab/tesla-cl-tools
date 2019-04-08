#!/usr/bin/env python

import authTokenGenerator
import json
import prompt
import propertiesReader
import requests

def setup():
    print("Starting set up process. Your login information is only used to connect to Tesla auth once, and is not stored locally.")
    (email,password) = prompt.promptLogin()
    authToken = authTokenGenerator.fetchAuthToken(email, password)
    if authToken is not None:
        print("Auth token was successfully generated, you can now call other commands")