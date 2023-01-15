import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a fanout exchange
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# Send 10 messages
for i in range(10):
    message = f"message {i}"
    channel.basic_publish(exchange='logs', routing_key='', body=message)
    print(f" [x] Sent {message}")

connection.close()
