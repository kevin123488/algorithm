// dfs 활용
function dfs(numbers, target, nowSum, nowIdx) {
    if (nowIdx < numbers.length) {
        dfs(numbers, target, nowSum + numbers[nowIdx], nowIdx + 1)
        dfs(numbers, target, nowSum - numbers[nowIdx], nowIdx + 1)
    } else if (nowIdx === numbers.length) {
        if (nowSum === target) {
            answer ++;
        }
    }
}
var answer = 0
function solution(numbers, target) {
    // var answer = 0;
    // console.log(visited)
    dfs(numbers, target, 0, 0);
    return answer;
}

console.log(solution([4, 1, 2, 1], 4))