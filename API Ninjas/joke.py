import requests
import json

api_url = 'https://api.api-ninjas.com/v1/jokes?limit=1'
response = requests.get(api_url, headers={'X-Api-Key': os.environ['NINJA']})
if response.status_code == requests.codes.ok:
    data = json.loads(response.text)

    for item in data:
        print(item['joke'])
    
else:
    print("Error:", response.status_code, response.text)
