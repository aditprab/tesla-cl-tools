#!/usr/bin/env python

import authTokenGenerator
import json
import prompt
import propertiesReader
import requests

def setup():
    print("Starting set up process. Your login information is only used to connect to Tesla auth once, and is not stored locally.")
    (email,password) = prompt.promptLogin()
    authTokenGenerator.fetchAuthToken(email, password)
