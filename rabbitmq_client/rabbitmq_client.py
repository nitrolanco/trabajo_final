import pika
import json
from datetime import datetime

def callback(ch, method, properties, body):
    message = json.loads(body)
    print(f"Received: {message['text']} at {message['timestamp']}")

def run():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq_server'))
    channel = connection.channel() 
    channel.queue_declare(queue='hello')

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
    print('RabbitMQ Client is waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    run()
