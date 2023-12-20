import argparse
import sys
import pika


def send_message(message):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )
    channel = connection.channel()
    channel.exchange_declare(exchange='logs', exchange_type='fanout')
    channel.basic_publish(exchange='logs', routing_key='', body=message)
    print(f'[x] message "{message}" sent')
    connection.close()


if __name__ == '__main__':
    message = ' '.join(sys.argv[1:])
    send_message(message)
