#!/usr/bin/env python

import getpass

def promptLogin():
	email = raw_input('Enter your Tesla account email address:\t')
	password = getpass.getpass()
	return (email, password)