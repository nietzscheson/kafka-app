import os
<<<<<<< HEAD
from time import sleep
from json import dumps
from kafka import KafkaProducer
from kafka.errors import KafkaError
from faker import Faker
from time import sleep

producer = KafkaProducer(bootstrap_servers=[os.environ['KAFKA_BROKER']], value_serializer=lambda x: dumps(x).encode('utf-8'), api_version=(0, 10, 1))
=======
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
>>>>>>> feature/confluent

fake = Faker()

for e in range(10):
<<<<<<< HEAD
    data = {'number' : e, 'name': fake.name()}
    future = producer.send('my-topic', data)
    # Block for 'synchronous' sends
    try:
        record_metadata = future.get(timeout=10)
    except KafkaError:
        # Decide what to do if produce request failed...
        log.exception()
        pass

    print ("Topic: " + str(record_metadata.topic) + " Partition: " + str(record_metadata.partition) + " Offset: " + str(record_metadata.offset))
=======
    name = fake.name()

    future = p.produce('my-topic', name.encode("utf-8"), callback=delivery_report)

p.flush()

>>>>>>> feature/confluent
