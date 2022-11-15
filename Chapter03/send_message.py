'''
Send message example
'''
import json
import pika
jsonMessage = json.loads("{\"name\":\"message\", \"message\":\"test\"}")
connection = pika.BlockingConnection(   pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='server1Queue')
channel.basic_publish(exchange='', routing_key='server1Key', body=json.dumps(jsonMessage))
# This requires a string, but I assume we would deal with json format
connection.close()
