const input = require('fs')
.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
.toString()
.trim()
.split('\n')
.map(e => Number(e));

input.shift();

function swap(arr, indexA, indexB) {
    let temp = arr[indexA];
    arr[indexA] = arr[indexB];
    arr[indexB] = temp;
  }

for(i=0; i<input.length; i++) {
    for(j=0; j<input.length-i; j++){
        if(input[j] > input[j+1]) {
            swap(input, j, j+1);
        }
    }
}
for (i=0; i < input.length; i++) {
    console.log(input[i]);
}