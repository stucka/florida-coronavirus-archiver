import requests
from time import sleep

archiveprefix = "https://web.archive.org/save/"
naptime = 1   # Seconds to sleep between requests

with open("things-to-archive.txt", "r") as infile:
    thingstoarchive = infile.read().splitlines()

for thingtoarchive in thingstoarchive:
    thingtoarchive = thingtoarchive.strip()
    if len(thingtoarchive) > 0:   # If not a blank line:
        print(f"Trying to archive {thingtoarchive}")
        r = requests.get(archiveprefix + thingtoarchive)
        sleep(naptime)
