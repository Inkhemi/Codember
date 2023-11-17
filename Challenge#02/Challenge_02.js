let code = "&###@&*&###@@##@##&######@@#####@#@#@#@##@@@@@@@@@@@@@@@*&&@@@@@@@@@####@@@@@@@@@#########&#&##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@&"

function spy_code(code) {
    let number = 0;
    let out = "";

    for (operation of code) {
        if (operation == "#") {
            number += 1;
        } else if (operation == "@") {
            number -= 1;
        } else if (operation == "*") {
            number *= number
        } else if (operation == "&") {
            out += number.toString();
        }
    }
    
    return out;
}

console.log(spy_code(code));
