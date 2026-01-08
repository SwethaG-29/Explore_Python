import pandas as pd
from dotenv import load_dotenv
import os
from pathlib import Path
load_dotenv(Path("API_Key.env")) #To ensure actual API is not exposed.
key = os.getenv("API_KEY")
print(key)

import requests
### STEP: Check for API key is read or not 
if key:
    print("Successfully loaded API key")
else:
    print("Failed to load API key")

address = [
"Tata Consultancy Services, Fort, Mumbai, Maharashtra",
"Infosys, Electronics City, Bengaluru, Karnataka",
"Wipro, Sarjapur Road, Bengaluru, Karnataka",
"HCL Technologies, Sector 126, Noida, Uttar Pradesh",
"Tech Mahindra, Hinjewadi, Pune, Maharashtra"
]

def address_func(addr):
    ### STEP: Use the API key to make a request to the Google Maps Geocoding API


    params = {
        "address": addr,
        "key": key}

    try:
        url = "https://maps.googleapis.com/maps/api/geocode/json?"
        response = requests.get(url,params = params) 
        if response.status_code == 200:
            print("Connection established successfully")

    response = response.json()

    address = response["results"][0]["formatted_address"]
    coordinates = response["results"][0]["geometry"]["location"]
    lat, lng = coordinates.values()
    print("Address is:",address, "and its co-ordinates:","lat:", lat,"lng:",lng)
    print("\n")

    except Exception as e:
    print(e)

    
for addr in address:
    address_func(addr)



### Scenario step by step excution in order:
# 1. 1st check if connection is established successfully for one record 
# 2. Try for 1 address and make it work (Done)
# 3. Give a list of address and then make it work. Once done try importing a csv/excel file
# 4. Remove duplicates
# 5. Address is wrong/ address not matching then return null/empty
# 6. Create a Cache file (no of request gets saved and no need to restry for all records multiple times)
# 7. function/ normal flow ?
# 8. In case if there is any network issue or program craches handle the error.

#Note:
#API are very important, so ensure the security for them is considered.
