import pika

def createTopic(name, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    chanel = connection.channel()
    chanel.queue_declare(queue=name)

    chanel.basic_publish(exchange='', routing_key=name, body=message)
    print(f"Enviando {message}")
    connection.close()