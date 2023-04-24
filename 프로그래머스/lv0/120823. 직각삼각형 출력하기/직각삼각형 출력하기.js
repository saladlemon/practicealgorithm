const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
    const n = Number(input);
    let result = "*";
    for(i=1;i<n+1;i++){
        console.log(result);
        result = result + "*";
    }
});