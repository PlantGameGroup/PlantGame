from rabbitmq.listeners import start_listeners

def main():
    start_listeners()

    # TODO:
    # - RabbitMQ reading all queues
    # - extracting message content
    # - plantnet request preparation
    # - extracting necessary information out of plantnet response
    # - calling gameboard API

if __name__ == '__main__':
    main()
