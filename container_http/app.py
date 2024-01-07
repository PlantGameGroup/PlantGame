from flask import Flask, request, jsonify
import pika

app = Flask(__name__)

# # Set up RabbitMQ connection parameters
# rabbitmq_connection_params = pika.ConnectionParameters('localhost')
# rabbitmq_connection = pika.BlockingConnection(rabbitmq_connection_params)
# rabbitmq_channel = rabbitmq_connection.channel()

# Declare the RabbitMQ queue
# rabbitmq_channel.queue_declare(queue='guesses')
app.logger.info("flask appp running from new image")
@app.route('/guess', methods=['POST'])
def guess_endpoint():
    print("guess_endpoint was called")
    try:
        data = request.json
        # Log the request details
        app.logger.info(f"Received {request.method} request to {request.path}")

        # # Publish the content to RabbitMQ
        # rabbitmq_channel.basic_publish(
        #     exchange='',
        #     routing_key='guesses',
        #     body=data
        # )

        return jsonify({"status": "success"}), 200

    except Exception as e:
        app.logger.error(f"Error processing request: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
