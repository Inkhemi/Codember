# ** Tu desafío: **
# Determina cuántas claves de cifrado son válidas según sus políticas.

file = open("Challenge#03\message_03.txt")
file = list(file)
cont_failures = 0

for line in file:

    letter_cont = 0
    cipher, password = line.split(":")
    password = (password.split("\n"))[0]
    password = password.strip()
    numbers, letters = cipher.split(" ")
    minimum, maximum = numbers.split("-")
    minimum = int(minimum)
    maximum = int(maximum)

    for letter in password:
        if letter == letters:
            letter_cont += 1

    if letter_cont < minimum or letter_cont > maximum:
        cont_failures += 1
        if cont_failures == 42:
            print(password)
            
        # Pista para secreto
        if cont_failures == 13:
            print(password)
