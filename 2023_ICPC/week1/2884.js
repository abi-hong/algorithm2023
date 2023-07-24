const input = require('fs')
    .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
    .toString()
    .trim()
    .split(" ")
    .map(Number);
let [H, M] = input;

M = M - 45; // 분

if(M < 0) {
    M = 60 + M;
    H = H - 1;

    if(H === -1) {
        H = 23;
    }
}

console.log(H + ' ' + M);