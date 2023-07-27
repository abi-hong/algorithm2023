// 입력
const input = require('fs')
	.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
	.toString()
    .trim()
    .split("\n")
    .map(el => el.split(" ").map(Number));

//console.log(input);
const [N, M] = input.shift(); // shift() : 배열의 맨 앞에 값을 제거하는 함수

// JS에서 2차원 배열 [[], [] ... , []] 만들기
let arr = new Array(N) // 크기가 N인 배열을 생성
                .fill() // undefined으로 배열 안 값 결정
                .map(() => new Array(M).fill(0)); // map을 통해 각각의 원소들의 값 안에 다시 크기가 M인 배열을 생성하고 그 배열을 0으로 채우기 위함

for(let i=0; i<N; i++) {
    for(let j=0; j<M; j++) {
        arr[i][j] = input[i][j] + input[i+N][j];
    }
}

// 출력 형태가 같지 않아 출력에 해당하는 형태로 바꿔야 한다.
let answer = ""; // 문자열로 입력하기 위해
for(let i=0; i<arr.length; i++) {
    for(let j=0; j<arr[0].length; j++) {
        answer += arr[i][j] + " "; // 각각의 값과 공백을 차례대로 넣어줌
    }
    answer += "\n"; // 한줄을 다 넣으면 다음줄로 넘어가도록
}
console.log(answer.trim()); // 공백제거