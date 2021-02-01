# Import libraries
import requests

import json

import datetime

from itertools import groupby

import csv

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

alt_total_distinct_vacs = 0

alt_total_non_distinct_vacs = 0

datesArray = []

total_distinct_vac_Array = []

total_non_distinct_vacs_Array = []

# Request JSON object and turn it into a Python dictionary
vacs_json = get_vacs_json()

formatted_json = jprint(vacs_json)

loaded_json = jload(vacs_json)

# Get previous day string
now = datetime.date.today() - datetime.timedelta(1)

alt_now = now = datetime.date.today() - datetime.timedelta(2)

time_compare_string = now.strftime("%Y-%m-%d") + 'T00:00:00'

alternative_compare_string = alt_now.strftime("%Y-%m-%d") + 'T00:00:00'

loaded_json.sort(key=lambda content: content['referencedate'])

# then use groupby with the same key
groups = groupby(loaded_json, lambda content: content['referencedate'])

# Group data by reference date in order to iterate through areas over a single day
for refDate, group in groups:

    refDate = refDate.replace('T00:00:00', '')
    
    datesArray.append(refDate)
    
    temp_distinct = 0
    temp_non_distinct = 0
    for content in group:
        
        temp_distinct = temp_distinct + int(content['totaldistinctpersons'])
        temp_non_distinct = temp_non_distinct + int(content['totalvaccinations'])

    total_distinct_vac_Array.append(temp_distinct)
    total_non_distinct_vacs_Array.append(temp_non_distinct)

with open('covidVacsGreece.csv', 'w', newline='') as file:

    writer = csv.writer(file)

    writer.writerow(["Date", "Total Vacs", "Total Distinct Vacs"])

    count_item = 0

    for item in datesArray:

        writer.writerow([item, total_non_distinct_vacs_Array[count_item], total_distinct_vac_Array[count_item]])

        count_item += 1

