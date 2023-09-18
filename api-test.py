import requests, json

#
# response = requests.get(url, param or payload, headers)
# Using REST API
"""response = requests.get("https://randomuser.me/api/") # enter a base url
print(response.text)  # print out the object
"""

# can use endpoint part of url to specify what resource to return. Can be found in API reference docs

"""
CRUD or create, read, update, delete
HTTP Method	    Description	                    Requests method
POST            Create a new resource.	        requests.post()
GET	            Read an existing resource.	    requests.get()
PUT	            Update an existing resource.    requests.put()
DELETE          Delete an existing resource.    requests.delete()
"""

url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"

payload = { "q": "English is hard, but detectably so" }
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "81ccb34677msh069d4401a28d838p1989b2jsn64b242c88d32",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

#response = requests.post(url, data=payload, headers=headers) # returns an object
#print(response.json())
# or
# response = requests.post(url, data=payload, headers=headers).json()
response = {'data': {'detections': [[{'isReliable': False, 'language': 'en', 'confidence': 1}]]}}
langtype = response["data"]["detections"][0][0]["language"]
print(langtype)

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

payload = {
	"q": "Hello, world!",
	"target": "es",
	"source": "en"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "81ccb34677msh069d4401a28d838p1989b2jsn64b242c88d32",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

#response = requests.post(url, data=payload, headers=headers)
response = {'data': {'translations': [{'translatedText': 'Hola Mundo!'}]}}
translation = response["data"]["translations"][0]["translatedText"]
print(translation)