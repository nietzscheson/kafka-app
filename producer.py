import os
from confluent_kafka import Producer
from faker import Faker
from time import sleep

p = Producer({'bootstrap.servers': os.environ['KAFKA_BROKER']})

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

fake = Faker()

for e in range(10):
    name = fake.name()

    future = p.produce('my-topic', name.encode("utf-8"), callback=delivery_report)

p.flush()

