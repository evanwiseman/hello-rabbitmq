import pika

# Establish connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# Declare the hello queue to send on
channel.queue_declare(queue="hello")

# Send a hello world message
channel.basic_publish(
    exchange="",
    routing_key="hello",
    body="Hello World!",
)
print(" [x] Sent 'Hello World!'")

# Close the connection
connection.close()
