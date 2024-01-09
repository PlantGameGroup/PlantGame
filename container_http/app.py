from flask import Flask, request, jsonify
import pika

app = Flask(__name__)

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

#rabbitmq setup
rabbitmq_connection = get_rabbitmq_connection()
rabbitmq_channel_user_guesses = rabbitmq_connection.channel()
rabbitmq_channel_user_guesses.queue_declare(queue='user_guesses')
rabbitmq_channel_new_parks = rabbitmq_connection.channel()
rabbitmq_channel_new_parks.queue_declare(queue='new_parks')

@app.route('/guess', methods=['POST'])
def post_guess_endpoint():
    try:
        data = request.json

        rabbitmq_connection = get_rabbitmq_connection()
        rabbitmq_channel_user_guesses = rabbitmq_connection.channel()
        # Publish the content to RabbitMQ
        rabbitmq_channel_user_guesses.basic_publish(
            exchange='',
            routing_key='user_guesses',
            body="test"
        )

        return jsonify({"status": "The guess is going to be processed."}), 200

    except Exception as e:
        app.logger.error(f"Error processing request: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/parks', methods=['GET'])
def get_parks_endpoint():
    try:
        park_header_value = request.headers.get('park')

        if park_header_value is None:
            raise ValueError("The 'park' header is missing in the request.")

        mock_species_list = ["Alocasia_macrorrhiza", "Philodendron_selloum", "Anthurium_andraeanum", "Calathea_orbifolia", "Monstera_deliciosa"]
        json_data = jsonify(mock_species_list)

        return json_data, 200

    except Exception as e:
        app.logger.error(f"Error processing request: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route('/parks', methods=['POST'])
def post_parks_endpoint():
    try:
        data = request.json

        rabbitmq_connection = get_rabbitmq_connection()
        rabbitmq_channel_new_parks = rabbitmq_connection.channel()
        # Publish the content to RabbitMQ
        rabbitmq_channel_new_parks.basic_publish(
            exchange='',
            routing_key='new_parks',
            body="test"
        )

        return jsonify({"status": "The park and its species is added to the database"}), 200

    except Exception as e:
        app.logger.error(f"Error processing request: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
