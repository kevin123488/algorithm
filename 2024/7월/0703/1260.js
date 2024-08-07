// 문제
// 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
// 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
// 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

// 입력
// 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000),
// 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
// 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

// 출력
// 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

const fs = require('fs')
const fileStream = fs.createReadStream('input_1260.txt')

const readline = require('readline')
const rl = readline.createInterface({
    input: fileStream,
    output: process.stdout,
    terminal: false,
})

let input = []
let checkLink = []
let dfsAnsList = []
let bfsAnsList = []

function dfs(visited, now, n) {
    dfsAnsList.push(now)
    visited[now] = 1
    for (let i = 1; i <= n; i++) {
        if (checkLink[now][i] === 1 && visited[i] === 0) {
            dfs(visited, i, n)
        }
    }
}

function bfs(visited, now, n) {
    visited[now] = 1
    let q = []
    q.push(now)
    while (q.length > 0) {
        let nowNode = q.shift()
        bfsAnsList.push(nowNode)
        for (let i = 1; i <= n; i++) {
            if (checkLink[nowNode][i] === 1 && visited[i] === 0) {
                q.push(i)
                visited[i] = 1
            }
        }
    }
}

rl.on('line', (line) => {
    input.push(line)
}).on('close', () => {
    [n, m, v] = input[0].split(' ').map(Number)
    for (let i = 0; i <= n; i++) {
        let tempList = []
        for (let j = 0; j <= n; j++) {
            tempList.push(0)
        }
        checkLink.push(tempList)
    }
    for (let i = 0; i < m; i++) {
        let first = input[i + 1].split(' ').map(Number)[0]
        let second = input[i + 1].split(' ').map(Number)[1]
        // console.log(first, second)
        checkLink[first][second] = 1
        checkLink[second][first] = 1
    }

    // console.log(checkLink)
    // DFS 결과
    let dfsVisited = []
    for (let i = 0; i <= n; i++) {
        dfsVisited.push(0)
    }
    dfs(dfsVisited, v, n)
    console.log(dfsAnsList.join(" "))

    // BFS 결과
    let bfsVisited = []
    for (let i = 0; i <= n; i++) {
        bfsVisited.push(0)
    }
    bfs(bfsVisited, v, n)
    console.log(bfsAnsList.join(" "))
})