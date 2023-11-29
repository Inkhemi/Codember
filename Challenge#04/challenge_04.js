const fs = require('fs')
const input = fs.readFileSync('Challenge#04/files_quarantine.txt', 'utf8').split('\n')

let count = 0 // Obtener el checksum cuando sea 33

for (let elements of input) {
    let correct = true 

    const [password, checksum] = elements.split("-")

    // Si la letra esta dentro del checksum y está más de una vez en la contraseña se asigna como false
    for (const letter of password) {
        if (checksum.includes(letter)) {
            if (password.split(letter).length - 1 !== 1) {
                correct = false
            }
        }
    }

    if (correct) {
        count++;
    }
    if (count === 33) {
        console.log(checksum);
    }
}
