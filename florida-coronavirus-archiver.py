import requests
from time import sleep

archiveprefix = "https://web.archive.org/save/"
naptime = 1   # Seconds to sleep between requests

with open("things-to-archive.txt", "r") as infile:
    thingstoarchive = infile.read().splitlines()

for thingtoarchive in thingstoarchive:
    try:
        thingtoarchive = thingtoarchive.strip().split("#")[0].split()[0].strip()    # Lose all comments
        if len(thingtoarchive) > 0:   # If not a blank line:
            print(f"Trying to archive {thingtoarchive}")
            r = requests.get(archiveprefix + thingtoarchive, allow_redirects=False, timeout=10)
            sleep(naptime)
    except:
        print(f"Error fetching {thingtoarchive}")
        sleep(naptime)