const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split("\n");

const len = input.shift();
const stack = [];
const result = [];

for(let i=0; i<len; i++) {
    switch(input[i]) {
        case 'pop':
            result.push(stack.pop() || -1);
            break;
        case 'size':
            result.push(stack.length);
            break;
        case 'empty':
            result.push((stack.length === 0) ? 1 : 0);
            break;
        case 'top':
            result.push(stack[stack.length-1] || -1);
            break;
        default:
            stack.push(input[i].split(" ")[1]);
            break;
    }
}

console.log(result.join('\n'));