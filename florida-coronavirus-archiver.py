import requests
from time import sleep
import re

archiveprefix = "https://web.archive.org/save/"
naptime = 1   # Seconds to sleep between requests
maxrequestwait = 20    # How long to wait before calling it quits on a connection?

with open("things-to-archive.txt", "r") as infile:
    thingstoarchive = infile.read().splitlines()

for thingtoarchive in thingstoarchive:
    thingtoarchive = re.sub(r"#.*", "", thingtoarchive).strip()
    if thingtoarchive:
        print(f"Trying to archive {thingtoarchive}")
        try:
            requests.get(archiveprefix + thingtoarchive, allow_redirects=False, timeout=maxrequestwait)
            # This looks like a GET that we discard, and it is, but the point is that it has the
            # side-effect of making The Wayback Machine store any updated copy. Demand drives storage.
        except Exception as exc:
            print(f"Error fetching {thingtoarchive} because {exc}")
        sleep(naptime)
