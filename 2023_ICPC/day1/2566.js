const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split("\n").map(el=>el.split(" ").map(Number));

let maxValue = 0;
let maxI = 0;
let maxJ = 0;
for(i=0; i<9; i++) {
    for(j=0; j<9; j++) {
        if(maxValue < input[i][j]) {
            maxValue = input[i][j];
            maxI = i;
            maxJ = j;
        }
    }
}
console.log(maxValue);
console.log(maxI+1, maxJ+1);