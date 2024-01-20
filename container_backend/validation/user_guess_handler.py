from plantnet_handling.request_handler import plantnet_api_call

threshold_score = 0.4

def process_user_guess(gameID, plantID, imageURI, guessedSpecies):
    best_match, best_match_score = plantnet_api_call(imageURI)

    if best_match_score > threshold_score:
        print(f"The {best_match} has made the threshold.")
