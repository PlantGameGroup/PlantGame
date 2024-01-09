from flask import Flask, request, jsonify
import pika

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
        data = request.json

        rabbitmq_connection = get_rabbitmq_connection()
        rabbitmq_channel_new_games = rabbitmq_connection.channel()
        # Publish the content to RabbitMQ
        rabbitmq_channel_new_games.basic_publish(
            exchange='',
            routing_key='new_games',
            body="test"
        )

        return jsonify({"status": "The list of 5 species inside a plant will be posted to the gameboard."}), 200

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
