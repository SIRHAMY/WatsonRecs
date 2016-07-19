import requests
import environment_vars as env

print("watsonrecs running...")

textForKeyword = 'I like dogs and cats'
requestUrl = 'https://watson-api-explorer.mybluemix.net/alchemy-api/calls/text/TextGetRankedKeywords'

payload = {
    'apikey': env.API_KEY, 
    'text': textForKeyword,
    'outputMode': 'json'
}
r = requests.get(requestUrl, params=payload)

# Get request content out
r.json()

print("After r.json")
print(r.json())