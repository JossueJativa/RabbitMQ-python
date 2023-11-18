from consumer import consumeTopic, getEmails, getOptions, saveEmails, saveOptions
from producer import createTopic


if __name__ == '__main__':
    start = True
    while start:
        print("Ingresa el topic a tu preferencia")
        print("1. Juegos")
        print("2. Trabajo")
        print("3. Salir")
        option = int(input("Seleccione una opción: "))
        if option != 3:
            email = input("Ingrese su correo: ")
            saveEmails(email)
            saveOptions(option)
        elif option == 3:
            print("Salir de adjuntar topics")
            start = False
        else:
            print("Opción no válida")

    for i in range(len(getOptions())):
        if getOptions()[i] == 1:
            createTopic("Juegos", "Bienvenido a los juegos")
        elif getOptions()[i] == 2:
            createTopic("Trabajo", "Bienvenido a tu trabajo")

    for i in range(len(getEmails())):
        if getOptions()[i] == 1:
            consumeTopic("Juegos")
        elif getOptions()[i] == 2:
            consumeTopic("Trabajo")