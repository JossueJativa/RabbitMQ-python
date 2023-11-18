from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pika, smtplib
from . import config

emailsOptions = []
options = []

def sendEmail(mail, body):
    email = config.email
    password = config.password
    smtp_server = config.smtp_server
    smtp_port = 587

    # Crear el mensaje de correo electrónico
    mensaje = MIMEMultipart()
    mensaje['From'] = email
    mensaje['To'] = mail
    mensaje['Subject'] = 'RabbitMQ'

    cuerpo_mensaje = body
    mensaje.attach(MIMEText(cuerpo_mensaje, 'plain'))

    # Establecer conexión con el servidor SMTP
    with smtplib.SMTP(smtp_server, smtp_port) as servidor:
        # Iniciar sesión en el servidor
        servidor.starttls()
        servidor.login(email, password)

        # Enviar el mensaje
        servidor.send_message(mensaje)

def on_message_recived(ch, method, propieties, body):
    print(f"Mensaje enviado: {body}")
    for i in range(len(options)):
        if options[i] == 1:
            print(options[i])
            email = getEmails()[i]
            sendEmail(mail=email, body="Bienvenido a los juegos")
        elif options[i] == 2:
            print(options[i])
            email = getEmails()[i]
            sendEmail(mail=email, body="Bienvenido a tu trabajo")

def consumeTopic(name):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    chanel = connection.channel()

    chanel.queue_declare(queue=name)

    chanel.basic_consume(queue=name, auto_ack=True, 
                        on_message_callback=on_message_recived)

    print("Waiting for messages...")
    chanel.start_consuming()

def saveEmails(mail):
    emailsOptions.append(mail)
    for emails in emailsOptions:
        print(emails)

def saveOptions(option):
    options.append(option)
    for option in options:
        print(option)

def getOptions():
    return options

def getEmails():
    return emailsOptions