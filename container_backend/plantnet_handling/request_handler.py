import requests
import json

def plantnet_api_call(imageURI):

    # Make the API call to Plantnet
    plantnet_api_url = 'https://my-api.plantnet.org/v2/identify/all'
    plantnet_api_params = {
        'images': imageURI,
        'include-related-images': 'false',
        'no-reject': 'false',
        'lang': 'en',
        'api-key': '2b10XVwzvES8lf368OlEP2vG'
    }

    response = requests.get(plantnet_api_url, params=plantnet_api_params)

    # Handle the API response as needed
    if response.status_code == 200:
        plantnet_data = response.json()
        # Process plantnet_data as needed
        print(f"Plantnet Response: {plantnet_data}")
        return plantnet_data
    else:
        print(f"Error in Plantnet API call. Status Code: {response.status_code}, Response Text: {response.text}")
        return 0
