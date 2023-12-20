import pika


def callback(ch, method, properties, body):
    print(f'[x] message "{body}" received')


def build_consumer():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )
    channel = connection.channel()
    channel.exchange_declare(exchange='logs', exchange_type='fanout')
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange="logs", queue=queue_name)

    print('[x] waiting for logs. to exit press ctrl+c')

    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True
    )
    channel.start_consuming()


if __name__ == '__main__':
    build_consumer()

