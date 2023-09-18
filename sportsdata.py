import requests, json, csv

""" From sportsdata.io
All of our API endpoints can be accessed via an HTTP GET request using your API key. The API key can be passed either as a query parameter or using the following HTTP request header.

"""
url = "https://api.sportsdata.io/v3/nfl/scores/json/PlayersBasic/"
headers = {
    "Ocp-Apim-Subscription-Key" : "cf8f0d8d3a1f4f89aafe82dba6442885"
}

# Players = "https://api.sportsdata.io/v3/nfl/scores/json/Players/"  # scrambled
# Roster = "https://api.sportsdata.io/v3/nfl/scores/json/PlayersBasic/"

url = url + "dal"
roster = requests.get(url, headers=headers).json()
#print(type(roster))
keys = roster[0].keys()

with open('dal.csv', 'w', newline='') as f:
    dict_writer = csv.DictWriter(f, keys)
    dict_writer.writeheader()
    dict_writer.writerows(roster)
