const input = require('fs')
    .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
    .toString()
    .trim()
    .split("\n")
    .map(Number);
input.shift();

input.sort((a, b) => a-b);

console.log(input.join("\n"));