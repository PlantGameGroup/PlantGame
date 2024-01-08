from flask import Flask, request, jsonify
import pika

app = Flask(__name__)

# Set up RabbitMQ connection parameters
rabbitmq_connection_params = pika.ConnectionParameters('plantgame-rabbitmq-service',
    port=5672,
    credentials=pika.PlainCredentials('guest', 'guest'),
    heartbeat=10)
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
rabbitmq_connection = get_rabbitmq_connection()
rabbitmq_channel = rabbitmq_connection.channel()

# Declare the RabbitMQ queue
rabbitmq_channel.queue_declare(queue='guesses')
@app.route('/guess', methods=['POST'])
def guess_endpoint():
    try:
        data = request.json

        rabbitmq_connection = get_rabbitmq_connection()
        rabbitmq_channel = rabbitmq_connection.channel()
        # Publish the content to RabbitMQ
        rabbitmq_channel.basic_publish(
            exchange='',
            routing_key='guesses',
            body="test"
        )

        return jsonify({"status": "success"}), 200

    except Exception as e:
        app.logger.error(f"Error processing request: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
