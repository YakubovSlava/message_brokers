from kafka import KafkaConsumer
import sys


def create_consumer(group):
    consumer = KafkaConsumer('logging', bootstrap_servers='localhost:9092',
                             group_id=group)

    print('[x] waiting for logs. to exit press ctrl+c')
    while True:
        for message in consumer:
            if message:
                print(message.value.decode())


if __name__ == '__main__':
    group = ' '.join(sys.argv[1:])
    create_consumer(group)