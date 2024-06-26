const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on('line', function (line) {
  input = line.split(' ');
}).on('close', function () {
  let height = Number(input[0]);
  for (let i = 0; i < height; i++) {
    let output = '*'.repeat(i + 1);
    console.log(output);
  }
});
