#!/usr/bin/env bash
#Makes entry script executable, renames it, copies Configs to /tmp, and copies all py scripts to
#/usr/local/bin (which should already be on user PATH).


chmod 777 tesla.py
cp Configurations.properties /tmp/
cp *.py /usr/local/bin
cd /usr/local/bin
mv tesla.py tesla