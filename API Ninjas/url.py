import requests
import json

url = 'example.com'
api_url = 'https://api.api-ninjas.com/v1/urllookup?url={}'.format(url)
response = requests.get(api_url, headers = {'X-Api-Key': 'Yhl7iIvZsSp+Z1wgz7IClw==elM4rnguiSPIrIRI'})

if response.status_code == requests.codes.ok:
    data = json.loads(response.text)

    print(data['is_valid'])

else:
    print("Error:", response.status_code, response.text)