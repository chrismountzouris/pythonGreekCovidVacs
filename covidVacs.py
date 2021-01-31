# Import libraries
import requests

import json

import datetime

# Initialize variables
def jprint(obj):

    text = json.dumps(obj, sort_keys=True, indent=4)
    
    return text

def jload(obj):

    loaded_json = json.loads(formatted_json)

    return loaded_json
    
# A function that returns the JSON request respond
def get_vacs_json():

    response = requests.get("https://data.gov.gr/api/v1/query/mdg_emvolio", headers={'Authorization': 'Token d99450c9e2d9654b8b911ffb8d33f9a6291e95f8'})

    if (response.status_code == 200):

        return response.json()

    else :

        print ("Unsuccessful Request with error code :",response.status_code)

        return None

# Initialize variables
total_distinct_vacs = 0

total_non_distinct_vacs = 0

# Request JSON object and turn it into a Python dictionary
vacs_json = get_vacs_json()

formatted_json = jprint(vacs_json)

loaded_json = jload(vacs_json)

# Get previous day string
now = datetime.date.today() - datetime.timedelta(1)

time_compare_string = now.strftime("%Y-%m-%d") + 'T00:00:00'

# Iterate through dictionary and perform actions on the last day's data
for key in loaded_json:
    
    if (key['referencedate'] == time_compare_string):
        
        total_distinct_vacs = total_distinct_vacs + int(key['totaldistinctpersons'])

        total_non_distinct_vacs = total_non_distinct_vacs + int(key['totalvaccinations'])

print ("Total distinct vaccinations are :",total_distinct_vacs)

print ("Total vaccinations are :",total_non_distinct_vacs)
