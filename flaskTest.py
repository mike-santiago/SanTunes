import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    url = "https://us.api.iheart.com/api/v3/live-meta/stream/1201/currentTrackMeta?defaultMetadata=true"

    req = requests.get(url)

    if req.status_code == 200:
        data = req.json()
        title = data["title"]
        artist = data["artist"]
    else:
        title = "Commercial"
        artist = ""

    return render_template(
        "santunes.html",
        title=title,
        artist=artist
    )