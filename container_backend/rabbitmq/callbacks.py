import pika
import json
import requests

def callback_user_guesses(ch, method, properties, body):
    # This is the callback function that will be called when a message is received
    # Decode the JSON string from the RabbitMQ message body
    message_body = json.loads(body)

    # Extract individual headers
    gameID = message_body.get('gameID')
    imageURI = message_body.get('imageURI')
    guessedSpecies = message_body.get('guessedSpecies')

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
        print(f"GameID: {gameID}, Guessed Species: {guessedSpecies}, Plantnet Response: {plantnet_data}")
    else:
        print(f"Error in Plantnet API call. Status Code: {response.status_code}, Response Text: {response.text}")




    # Acknowledge the message to RabbitMQ
    ch.basic_ack(delivery_tag=method.delivery_tag)
