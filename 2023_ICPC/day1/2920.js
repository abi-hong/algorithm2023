let input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split(" ");
input = input.join(" ");

let arrAscend = [1, 2, 3, 4, 5, 6, 7, 8];
arrAscend = arrAscend.join(" ");

let arrDescend = [8, 7, 6, 5, 4, 3, 2, 1];
arrDescend = arrDescend.join(" ");

if (input === arrAscend) {
    console.log('ascending');
    return;
} else if (input === arrDescend) {
    console.log('descending');
    return;
} else {
    console.log('mixed');
}