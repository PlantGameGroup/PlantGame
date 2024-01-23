from plantnet_handling.request_handler import plantnet_api_call
from rabbitmq.tellers import send_guess_result

threshold_score = 0.4

def process_user_guess(gameID, plantID, requestID, imageURI, guessedSpecies):
    best_match_name , best_match_score = plantnet_api_call(imageURI)

    if best_match_score > threshold_score:
        print(f"The {best_match_name} has made the threshold.")
        success = True
    else :
        success = False
    send_guess_result(gameID, plantID, requestID, best_match_name, best_match_score)
