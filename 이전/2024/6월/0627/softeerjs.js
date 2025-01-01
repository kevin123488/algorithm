const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let n = 0;
let nanRow = []; // 난로 반지름 저장 리스트
let input = []; // 입력값 저장할 리스트

rl.on('line', (line) => {
    input.push(line)
}).on('close', () => {
    n = parseInt(input[0]);
    nanRow = input[1].split(' ').map(Number);

    // 연탄의 반지름 * n = 난로의 반지름 -> 이 부분을 만족해야 연탄을 사용 가능
    // 난로 반지름 길이는 2 ~ 100까지
    let ansList = [0, 0];
    for (let i = 2; i <= 100; i++) {
    // i의 값은 연탄의 반지름.
    // 난로 반지름 리스트를 순회하며 연탄 반지름과 나누어 떨어지는 수를 카운트
    let cnt = 0;
    for (let j = 0; j < nanRow.length; j++) {
        if (nanRow[j] % i == 0 && nanRow[j] > 0) {
            cnt += 1;
        };
    };
    
    if (cnt >= ansList[1]) {
        ansList = [i, cnt];
    };
}

console.log(ansList[1])
});