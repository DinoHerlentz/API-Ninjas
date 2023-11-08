import requests
import json

ip_addr = input("Enter IP : ")
api_url = 'https://api.api-ninjas.com/v1/iplookup?address={}'.format(ip_addr)
response = requests.get(api_url, headers = {'X-Api-Key': os.environ['NINJA']})

if response.status_code == requests.codes.ok:
    data = json.loads(response.text)

    if data["is_valid"]:
        print("IP Address   : ", data["address"])
        print("Country      : ", data["country"])
        print("Country Code : ", data["country_code"])
        print("Region       : ", data["region"])
        print("Region Code  : ", data["region_code"])
        print("City         : ", data["city"])
        print("Zip          : ", data["zip"])
        print("Latitude     : ", data["lat"])
        print("Longitude    : ", data["lon"])
        print("Timezone     : ", data["timezone"])
        print("ISP          : ", data["isp"])
    else:
        print("Invalid IP address.")
else:
    print("Error:", response.status_code, response.text)
