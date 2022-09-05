import requests
from pprint import pprint

url = "https://www.reddit.com/r/gifs/top.json"

response = requests.get(url, headers={"User-agent": "netology"}, params={"t": "hour"})
pprint(response.json())
