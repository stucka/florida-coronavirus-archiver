import requests
from time import sleep

archiveprefix = "https://web.archive.org/save/"
naptime = 1   # Seconds to sleep between requests
maxrequestwait = 20    # How long to wait before calling it quits on a connection?

with open("things-to-archive.txt", "r") as infile:
    thingstoarchive = infile.read().splitlines()

for thingtoarchive in thingstoarchive:
    try:
        if len(thingtoarchive) > 0 and thingtoarchive[0] != "#":
            thingtoarchive = thingtoarchive.strip().split("#")[0].split()[0].strip()    # Lose all comments
            if len(thingtoarchive) > 0:   # If not a blank line:
                print(f"Trying to archive {thingtoarchive}")
                r = requests.get(archiveprefix + thingtoarchive, allow_redirects=False, timeout=maxrequestwait)
                sleep(naptime)
    except:
        print(f"Error fetching {thingtoarchive}")
        sleep(naptime)