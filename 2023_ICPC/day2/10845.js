const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split("\n");

const len = input.shift();
const queue = [];
const result = [];

for(let i=0; i<len; i++) {
    switch(input[i]) {
        case 'pop':
            result.push(queue.shift() || -1);
            break;
        case 'size':
            result.push(queue.length);
            break;
        case 'empty':
            result.push((queue.length === 0) ? 1 : 0);
            break;
        case 'front':
            result.push(queue[0] || -1);
            break;
        case 'back':
            result.push(queue[queue.length-1] || -1);
            break;
        default:
            queue.push(input[i].split(" ")[1]);
            break;
    }
}

console.log(result.join("\n"));