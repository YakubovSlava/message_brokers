from kafka import KafkaProducer
import sys
import json


def send_message(message):
    producer = KafkaProducer(bootstrap_servers='localhost:9092',
                             value_serializer=lambda x: json.dumps(x).encode('utf-8')
                             )
    producer.send('logging', message)

    producer.flush()
    producer.close()


if __name__ == '__main__':
    message = ' '.join(sys.argv[1:])
    # topic, message = message.split(' ')[0], ' '.join(message.split(' ')[1:])
    send_message(message)
