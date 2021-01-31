import requests
import json

def jprint(obj):

    text = json.dumps(obj, sort_keys=True, indent=4)
    
    return text

def jload(obj):

    loaded_json = json.loads(formatted_json)

    return loaded_json
    

def get_vacs_json():

    response = requests.get("https://data.gov.gr/api/v1/query/mdg_emvolio", headers={'Authorization': 'Token d99450c9e2d9654b8b911ffb8d33f9a6291e95f8'})

    if (response.status_code == 200):

        print ("Successful Request")

        return response.json()

    else :

        print ("Unsuccessful Request with error code :",response.status_code)

        return None

vacs_json = get_vacs_json()

formatted_json = jprint(vacs_json)

loaded_json = jload(vacs_json)
