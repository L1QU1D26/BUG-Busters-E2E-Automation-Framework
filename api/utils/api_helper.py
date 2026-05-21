import json

def get_json_value(response, key):

    response_json = response.json()

    return response_json.get(key)