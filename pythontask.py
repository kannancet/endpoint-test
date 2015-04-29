import urllib2
import json

response = urllib2.urlopen('http://gdata.youtube.com/feeds/api/standardfeeds/most_popular?v=2&alt=json')
data = json.load(response)

largest = data["feed"]["entry"][0]
for entry in data["feed"]["entry"]:
	if int(entry["yt$statistics"]["viewCount"]) > int(largest["yt$statistics"]["viewCount"]):
    	largest = entry

print largets["link"][0]["href"]




