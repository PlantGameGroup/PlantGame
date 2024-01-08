import pika

def callback(ch, method, properties, body):
    # This is the callback function that will be called when a message is received
    message = body.decode('utf-8')
    print(f"Received message: {message}")

    # Add your processing logic here

    # Acknowledge the message to RabbitMQ
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():

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
    channel.basic_consume(queue='user_guesses', on_message_callback=callback)

    print("Waiting for messages. To exit press CTRL+C")

    # Start consuming messages
    channel.start_consuming()

if __name__ == '__main__':
    main()
