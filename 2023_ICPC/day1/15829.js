const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split("\n");

const strL = Number(input.shift());
const str = input.shift();

// 문제에서 주어진 해시함수와 입력으로 주어진 문자열을 사용해 계산한 해시 값을 정수로 출력한다.
const M = 1234567891;
let r = 1;
let hash = 0;

for(let i=0; i<str.length; i++) {
    hash += (str.charCodeAt(i) - 'a'.charCodeAt() + 1) * r;
    r *= 31;
    //r이 M보다 커지는 것을 막기 위해 r을 곱해준다음 나눈 나머지로 r을 바꿔준다
    r %= M;
    hash %= M;
}

console.log(hash);