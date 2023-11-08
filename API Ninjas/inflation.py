import requests
import json

country = input("Enter Country Name : ")
api_url = 'https://api.api-ninjas.com/v1/inflation?country={}'.format(country)
response = requests.get(api_url, headers={'X-Api-Key': 'Yhl7iIvZsSp+Z1wgz7IClw==elM4rnguiSPIrIRI'})

if response.status_code == requests.codes.ok:
    data = json.loads(response.text)

    for item in data:
        print("Country:", item["country"])
        print("Type:", item["type"])
        print("Period:", item["period"])
        print("Monthly Rate (%):", item["monthly_rate_pct"])
        print("Yearly Rate (%):", item["yearly_rate_pct"])
        print()
else:
    print("Error:", response.status_code, response.text)