import re


def check_database():
    with open("Challenge#05/database_attacked.txt", "r") as f:
        users = f.readlines()

    result = ""

    for user in users:
        id_user, username, email, age, location = user.split(",")

        # El id debe ser alfanumérico
        if re.search("^[a-zA-Z0-9]*$", id_user) == None:
            result += username[0]
        # EL usuario debe ser alfanumérico
        elif re.search("^[a-zA-Z0-9]*$", username) == None:
            result += username[0]
        # El mail sigue el formato correcto
        elif re.search("^[a-zA-Z0-9]*@[a-zA-Z0-9]*\.com$", email) == None:
            result += username[0]
        # La edad debe ser un número o estar vacía
        elif re.search("^[0-9]*$", age) == None:
            result += username[0]
        # La ciudad debe ser una cadena de texto
        elif re.search("^[a-zA-Z\s]*$", location) == None:
            result += username[0]

    print(result)


check_database()
