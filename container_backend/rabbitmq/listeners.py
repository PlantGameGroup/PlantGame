from rabbitmq.callbacks import callback_user_guesses
import pika

# TODO: make a function with argument out of it
def start_user_guesses_listener():
    rabbitmq_connection_params = pika.ConnectionParameters(
        host='plantgame-rabbitmq-service',
        port=5672,
        credentials=pika.PlainCredentials('guest', 'guest'),
        heartbeat=10
    )
    connection = pika.BlockingConnection(rabbitmq_connection_params)
    channel = connection.channel()

    # Declare a queue named 'your_queue_name'
    channel.queue_declare(queue='user_guesses')

    # Set up the callback function to handle incoming messages
    channel.basic_consume(queue='user_guesses', on_message_callback=callback_user_guesses)

    print("Waiting for messages. To exit press CTRL+C")

    # Start consuming messages
    channel.start_consuming()


def start_listeners():
    start_user_guesses_listener()
