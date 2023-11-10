def spy_language(operations: str) -> str:
    '''
    Calcula un número a base de operaciones utilizando caracteres especiales
    # = suma 1, @ = resta 1, * = cuadrado, & = fin
    '''
    number = 0
    out = ""

    for operation in operations:
        if operation == "#":
            number += 1
        elif operation == "@":
            number -= 1
        elif operation == "*":
            number *= number
        elif operation == "&":
            out += str(number)
    return out


print(spy_language("&###@&*&###@@##@##&######@@#####@#@#@#@##@@@@@@@@@@@@@@@*&&@@@@@@@@@####@@@@@@@@@#########&#&##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@&"))
