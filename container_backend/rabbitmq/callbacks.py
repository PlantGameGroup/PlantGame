import pika
import json
import requests
from validation.user_guess_handler import process_user_guess

def callback_user_guesses(ch, method, properties, body):
    # This is the callback function that will be called when a message is received
    # Decode the JSON string from the RabbitMQ message body
    message_body = json.loads(body)

    # Extract individual headers
    # Add plantID header
    gameID = message_body.get('gameID')
    plantID = message_body.get('plantID')
    imageURI = message_body.get('imageURI')
    guessedSpecies = message_body.get('guessedSpecies')

    process_user_guess(gameID, plantID, imageURI, guessedSpecies)

    # Acknowledge the message to RabbitMQ
    ch.basic_ack(delivery_tag=method.delivery_tag)
