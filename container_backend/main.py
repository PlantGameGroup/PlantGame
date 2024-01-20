from rabbitmq.listeners import start_listeners
from validation.user_guess_handler import process_user_guess

def main():
    process_user_guess(1,1,"https://www.plantura.garden/wp-content/uploads/2018/05/Orchidee-Bl%C3%BCte.jpg", "test")

    # start_listeners()

    # TODO:
    # - RabbitMQ reading all queues
    # - extracting message content
    # - plantnet request preparation
    # - extracting necessary information out of plantnet response
    # - calling gameboard API

if __name__ == '__main__':
    main()
