from rabbitmq.listeners import start_listeners
from rabbitmq.tellers import setup_rabbitmq_teller

def main():
    setup_rabbitmq_teller()
    start_listeners()

if __name__ == '__main__':
    main()
