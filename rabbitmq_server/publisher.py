import pika
import json
from datetime import datetime

def run():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq_server'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    message = {
        "text": "Hello from RabbitMQ Publisher",
        "timestamp": str(datetime.now())
    }
    channel.basic_publish(exchange='', routing_key='hello', body=json.dumps(message))
    print("RabbitMQ Publisher sent: " + json.dumps(message))

    connection.close()

if __name__ == '__main__':
    run()
