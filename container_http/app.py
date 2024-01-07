from flask import Flask, request, jsonify
import pika
import time

app = Flask(__name__)

# Set up RabbitMQ connection parameters
time.sleep(10)
rabbitmq_connection_params = pika.ConnectionParameters('plantgame-rabbitmq-service',
    port=5672,
    credentials=pika.PlainCredentials('guest', 'guest')
)
rabbitmq_connection = pika.BlockingConnection(rabbitmq_connection_params)
rabbitmq_channel = rabbitmq_connection.channel()

# Declare the RabbitMQ queue
rabbitmq_channel.queue_declare(queue='guesses')
@app.route('/guess', methods=['POST'])
def guess_endpoint():
    try:
        data = request.json

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
