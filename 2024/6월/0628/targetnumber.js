// bfs 활용
function bfs(numbers, target) {
    let q = [[0, 0]]
    let nowIdx;
    let nowSum;
    let cntAns = 0;
    
    while (q.length !== 0) {
        [nowIdx, nowSum] = q.shift()
        if (nowIdx === numbers.length - 1) {
            if (nowSum + numbers[nowIdx] === target) {
                cntAns += 1
            } else if (nowSum - numbers[nowIdx] === target) {
                cntAns += 1
            }
        }
        
        if (nowIdx === numbers.length) {
            return cntAns
        }
        
        
        
        q.push([nowIdx + 1, nowSum + numbers[nowIdx]])
        q.push([nowIdx + 1, nowSum - numbers[nowIdx]])
    }
}

function solution(numbers, target) {
    var answer = 0;
    // console.log(visited)
    answer = bfs(numbers, target);
    return answer;
}

console.log(solution([1, 1, 1, 1, 1], 3))