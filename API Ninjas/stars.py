import requests
import json

name = 'vega'
api_url = 'https://api.api-ninjas.com/v1/stars?name={}'.format(name)
response = requests.get(api_url, headers={'X-Api-Key': os.environ['NINJA']})

if response.status_code == requests.codes.ok:
    data = json.loads(response.text)

    for item in data:
        print(item['name'])

else:
    print("Error:", response.status_code, response.text)
