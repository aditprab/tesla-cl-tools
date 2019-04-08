#!/usr/bin/env python
import sys
import status
import setup

# Entry point for CL tool. Usage: python tesla.py <option>

print('''
  ______ ______ _____  __     ___ 
 /_  __// ____// ___/ / /    /   |
  / /  / __/   \__ \ / /    / /| |
 / /  / /___  ___/ // /___ / ___ |
/_/  /_____/ /____//_____//_/  |_|
                                                                
''')

def badInput(input):
    if input is None:
        print("No option provided. Provide a valid option: ")
    else:
        print("Invalid option provided. Provide a valid option: ")

    print('''
           Options: 
           $ tesla setup  --- To set up authentication for the first time.
           $ tesla status  --- Get basic vehicle status.
        ''')
    sys.exit()


def setupOption():
    setup.setup()
def statusOption():
    status.getStatus()

def route(option):
    switcher = {
        "setup": setupOption,
        "status": statusOption
    }
    func = switcher.get(option, lambda: badInput(option))
    func()

def main():
    if (len(sys.argv) != 2):
        badInput(None)
    else:
        route(sys.argv[1])

if __name__ == "__main__":
    main()

