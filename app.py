import json
from flask import Flask, escape, request, jsonify
from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import KafkaError
from faker import Faker
from time import sleep

app = Flask(__name__)

consumer = KafkaConsumer(bootstrap_servers=['kafka:9092'], auto_offset_reset='earliest')

consumer.subscribe(['my-topic'])

@app.route('/')
def index():
    for msg in consumer:
        print(msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
