#!/usr/bin/env python

import authTokenGenerator
import json
import prompt
import propertiesReader
import requests

email, password = prompt.promptLogin()
authTokenGenerator.fetchAuthToken(email, password)
