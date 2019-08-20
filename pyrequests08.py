#!/usr/bin/python3

import requests
from pprint import pprint

def main():
    r = requests.get('https://www.anapioficeandfire.com/api') # send HTTP GET to this URL
    pprint(r.json()) # strip off the JSON and display on screen

main()
