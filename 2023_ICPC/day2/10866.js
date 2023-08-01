const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split("\n");

const len = input.shift();
const dequeue = [];
const result = [];

for (let i = 0; i < len; i++) {
    let check = input[i].split(' ');
    if (check.length == 2) {
        switch (check[0]) {
            case 'push_front':
                dequeue.unshift(check[1]);
                break;
            case 'push_back':
                dequeue.push(check[1]);
                break;
        }
    } else {
        switch (input[i]) {
            case 'pop_front':
                result.push(dequeue.shift() || -1);
                break;
            case 'pop_back':
                result.push(dequeue.pop() || -1);
                break;
            case 'size':
                result.push(dequeue.length);
                break;
            case 'empty':
                result.push((dequeue.length === 0) ? 1 : 0);
                break;
            case 'front':
                result.push(dequeue[0] || -1);
                break;
            case 'back':
                result.push(dequeue[dequeue.length - 1] || -1);
                break;
        }
    }
}


console.log(result.join("\n"));