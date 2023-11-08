import requests
import json

limit = 1
api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(limit)
response = requests.get(api_url, headers={'X-Api-Key': os.environ['NINJA']})

if response.status_code == requests.codes.ok:
    data = json.loads(response.text)

    for item in data:
        print(item['fact'])

else:
    print("Error:", response.status_code, response.text)
