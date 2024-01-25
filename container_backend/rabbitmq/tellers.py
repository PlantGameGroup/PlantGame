import pika
import json

channel = None

def setup_rabbitmq_teller():
    global channel

    connection = get_rabbitmq_connection()
    # Create a channel
    channel = connection.channel()
    # Declare the queue if not exists
    channel.queue_declare(queue='guess_results')
    print("RabbitMQ setup successful!")

def get_rabbitmq_connection():
    # Check if the connection already exists
    if 'rabbitmq_connection' in globals() and rabbitmq_connection.is_open:
        return rabbitmq_connection
    # Connection parameters
    rabbitmq_connection_params = pika.ConnectionParameters(
        host='plantgame-rabbitmq-service',
        port=5672,
        credentials=pika.PlainCredentials('guest', 'guest'),
        heartbeat=10
    )
    # Create a new connection
    new_connection = pika.BlockingConnection(rabbitmq_connection_params)
    return new_connection

def send_guess_result(game_id, plant_id, request_id, result_latin_name, confidence):
    # Create the JSON payload
    payload = {
        "gameID": game_id,
        "plantID": plant_id,
        "requestID": request_id,
        "resultLatinName": result_latin_name,
        "confidence": confidence
    }
    # Convert the payload to JSON
    json_payload = json.dumps(payload)
    try:
        # Publish the JSON payload to the queue
        channel.basic_publish(
            exchange='',
            routing_key='guess_results',
            body=json_payload
        )
    except Exception as e:
        print("RabbitMQ connection lost. Reconnecting...")
        setup_rabbitmq_teller()
        channel.basic_publish(
            exchange='',
            routing_key='guess_results',
            body=json_payload
        )

    print(f" [x] Sent {json_payload}")
