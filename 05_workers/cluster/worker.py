#!/usr/bin/env python
import pika
import time

credentials = pika.PlainCredentials('icesi', 'distribuidos')
connection = pika.BlockingConnection(pika.ConnectionParameters(
host='192.168.33.14',virtual_host='/icesi',credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_queue')

channel.start_consuming()
