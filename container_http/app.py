from flask import Flask, request, jsonify
import pika

rabbitmq_channel_user_guesses = None
rabbitmq_channel_new_parks = None

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

def setup_rabbitmq():
    global rabbitmq_channel_user_guesses
    global rabbitmq_channel_new_parks
    #rabbitmq setup
    rabbitmq_connection = get_rabbitmq_connection()
    rabbitmq_channel_user_guesses = rabbitmq_connection.channel()
    rabbitmq_channel_user_guesses.queue_declare(queue='user_guesses')
    rabbitmq_channel_new_parks = rabbitmq_connection.channel()
    rabbitmq_channel_new_parks.queue_declare(queue='new_parks')

@app.route('/guess', methods=['POST'])
def post_guess_endpoint():
    try:
        header_value_gameID = request.headers.get('gameID')
        header_value_imageURI = request.headers.get('imageURI')
        header_value_guessedSpecies = request.headers.get('guessedSpecies')

        if header_value_gameID is None:
            raise ValueError("The 'gameID' header is missing in the request.")
        if header_value_imageURI is None:
            raise ValueError("The 'imageURI' header is missing in the request.")
        if header_value_guessedSpecies is None:
            raise ValueError("The 'guessedSpecies' header is missing in the request.")

        # Combine headers into a dictionary
        message_body = {
            'gameID': header_value_gameID,
            'imageURI': header_value_imageURI,
            'guessedSpecies': header_value_guessedSpecies
        }
        try:
            # Publish the content to RabbitMQ
            rabbitmq_channel_user_guesses.basic_publish(
                exchange='',
                routing_key='user_guesses',
                body=jsonify(message_body).get_data(as_text=True)
            )
        except Exception as ex:
            print("RabbitMQ connection lost. Reconnecting...")
            setup_rabbitmq()
            rabbitmq_channel_user_guesses.basic_publish(
                exchange='',
                routing_key='user_guesses',
                body=jsonify(message_body).get_data(as_text=True)
            )
        return jsonify({"status": "The guess is going to be processed."}), 200

    except Exception as e:
        app.logger.error(f"Error processing request: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/park', methods=['GET'])
def get_parks_endpoint():
    try:
        park_param_value = request.args.get('park')

        if park_param_value is None:
            raise ValueError("The 'park' header is missing in the request.")

        # mock_species_list = ["Alocasia_macrorrhiza", "Philodendron_selloum", "Anthurium_andraeanum", "Calathea_orbifolia", "Monstera_deliciosa"]
        # json_data = jsonify(mock_species_list)
        # Update the response to match the desired structure
        species_data = [
            {
                "commonName": "Aloe Vera",
                "latinName": "Aloe_Vera",
                "imageURL": "https://www.aloeverahq.com/wp-content/uploads/2012/01/shutterstock_112140473.jpg"
            },
            {
                "commonName": "Evergreen Oak",
                "latinName": "Quercus_ilex",
                "imageURL": "https://de.academic.ru/pictures/dewiki/79/Oak_tree_in_Corsica.jpg"
            },
            {
                "commonName": "Rosemary",
                "latinName": "Rosmarinus_officinalis",
                "imageURL": "https://www.attainable-sustainable.net/wp-content/uploads/2021/11/rosemary.jpg"
            },
            {
                "commonName": "Thyme",
                "latinName": "thymus",
                "imageURL": "https://www.thespruceeats.com/thmb/PGJbPvXkvXQdYP7lyiVwqQjllf8=/5616x3744/filters:no_upscale():max_bytes(150000):strip_icc()/lemon-thyme-185225229-b0e5bf60a5464b3fa2a627187984a313.jpg""
            },
            {
                "commonName": "Cotton Lavender",
                "latinName": "santolina_cumbens",
                "imageURL": "https://de.academic.ru/pictures/dewiki/72/Heiligenkraut_(Santolina_chamaecyparissus_L_).jpg"
            }
        ]

        json_data = jsonify(species_data)
        return json_data, 200

    except Exception as e:
        app.logger.error(f"Error processing request: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route('/park', methods=['POST'])
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
    setup_rabbitmq()
    app.run(host='0.0.0.0', port=5000)
