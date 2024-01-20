import requests
import json

plantnet_api_identification_url = 'https://my-api.plantnet.org/v2/identify/all'

def plantnet_api_call(imageURI):

    # Make the API call to Plantnet
    plantnet_api_params = {
        'images': imageURI,
        'include-related-images': 'false',
        'no-reject': 'false',
        'lang': 'en',
        'api-key': '2b10XVwzvES8lf368OlEP2vG'
    }

    response = requests.get(plantnet_api_identification_url, params=plantnet_api_params)

    # Handle the API response as needed
    if response.status_code == 200:
        plantnet_data = response.json()
        best_match = extract_information(plantnet_data, "scientificNameWithoutAuthor")
        best_match_score = extract_score(plantnet_data)

        return best_match, best_match_score
    else:
        print(f"Error in Plantnet API call. Status Code: {response.status_code}, Response Text: {response.text}")
        return "no_match", "no_score"

def extract_score(plantnet_data):
    # Extract info from the best match
    best_match_score = plantnet_data['results'][0]["score"]
    return best_match_score

def extract_information(plantnet_data, name):
    # Extract info from the best match
    best_match_info = plantnet_data['results'][0]["species"][name]
    return best_match_info
