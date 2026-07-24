import requests
from bs4 import BeautifulSoup

url = "https://us.api.iheart.com/api/v3/live-meta/stream/1201/currentTrackMeta?defaultMetadata=true"
req = requests.get(url)

if req.status_code == 200:
    reqJSON = req.json()
    print(reqJSON["title"], "-", reqJSON["artist"])

elif req.status_code == 204:
    print("Commercial in progress")