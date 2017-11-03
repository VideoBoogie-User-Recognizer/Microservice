import unittest

from app.message_consumer import MessageConsumer


class MessageConsumerTestCase(unittest.TestCase):
    def test_that_pika_connection_has_been_created(self):
        receiver = MessageConsumer()
        self.assertIsNotNone(receiver.connection)

    def test_that_pika_channel_has_been_created(self):
        receiver = MessageConsumer()
        self.assertIsNotNone(receiver.channel)