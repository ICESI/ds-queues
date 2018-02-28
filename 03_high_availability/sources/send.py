#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('ICESI', 'password')
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.33.14',virtual_host='/icesi',credentials=credentials))
channel = connection.channel()


channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
