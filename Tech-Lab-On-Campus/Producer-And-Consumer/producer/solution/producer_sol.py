import pika
import os
from producer_interface import mqProducerInterface

class mqProducer(mqProducerInterface):
    def __init__(self, routing_key, exchange_name):
        self.routing_key = routing_key
        self.exchange = exchange_name
        
        self.setupRMQConnection()

    def setupRMQConnection(self):
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.connection = pika.BlockingConnection(parameters=con_params)

        self.channel = self.connection.channel()

        self.exchange = self.channel.exchange_declare(exchange="Exchange Name")

    def publishOrder(self, message):
        self.channel.basic_publish(
            exchange="Exchange Name",
            routing_key="Routing Key",
            body="Message",
        )

        self.channel.close()
        self.connection.close()