import pika

def callback_user_guesses(ch, method, properties, body):
    # This is the callback function that will be called when a message is received
    message = body.decode('utf-8')
    print(f"Received message: {message}")

    # Add your processing logic here



    # Acknowledge the message to RabbitMQ
    ch.basic_ack(delivery_tag=method.delivery_tag)
