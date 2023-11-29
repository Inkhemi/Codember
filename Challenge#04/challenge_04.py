def find_checksum():
    with open("Challenge#04/files_quarantine.txt", "r") as f:
        codes = f.readlines()

    count = 0  # Obtener el checksum número 33
    for code in codes:
        correct = True  # Se asume que esta correcto al principio

        password, checksum = code.strip().split("-")
        for letter in password:
            if letter in checksum:
                if password.count(letter) != 1:
                    correct = False  # Si la letra se encuentra en el checksum y existe más de una vez se cambia a False

        if correct == True:
            count += 1

        if count == 33:
            return checksum


checksum = find_checksum()
if checksum:
    print(checksum)
