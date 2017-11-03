import pika


class MessageConsumer:
    def __init__(self):
        # TODO: Factor out 'localhost' to a new config.py file.
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
