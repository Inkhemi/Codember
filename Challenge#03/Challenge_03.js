const fs = require('fs')

const input = fs.readFileSync('Challenge#03/message_03.txt', 'utf8').split('\n')

// Contador de contraseñas invalidas 
let error_count = 0

for (const line of input) {
    // Separación de variables
    const [key, password] = line.split(':')
    const [numbers, letter] = key.split(" ")
    const [minimum, maximum] = numbers.split("-")

    // Contar ocurrencias de la letra en la contraseña
    let letter_count = 0
    for (const char of password) {
        if (char === letter) {
            letter_count++
        }
    }

    // Verificar si la cantidad de ocurrencias está dentro del rango
    if (letter_count < minimum || letter_count > maximum) {
        error_count++
    }

    // Imprimir contraseñas en caso de error_count igual a 42 o 13
    if (error_count === 42 || error_count === 13) {
        console.log(password)
    }
}
