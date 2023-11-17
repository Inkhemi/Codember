const fs = require('fs');
const { workerData } = require('worker_threads');

const input = fs.readFileSync('Challenge#01/message_01.txt', 'utf8').split('\n');
const words_split = input[0].split(' ');

let words = [];

for (let elements of words_split) {
    if (!words.includes(elements)) {
        words.push(elements);
        words.push(words_split.filter(x => x === elements).length)
    }
}

words = words.join('');
console.log(words)
