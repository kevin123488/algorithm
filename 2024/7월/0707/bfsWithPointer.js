const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input = []
let nodeLink = []

function bfs(n, m, v, nodeLinkList) {
    let q = []
    q.push(v)
    let pointer = 0
    let visited = Array(n + 1).fill(0)
    visited[v] = 1
    while (pointer < q.length) {
        let nowNode = q[pointer]
        console.log(nowNode)
        
        pointer ++
        for (let i = 0; i <= n; i++) {
            if (nodeLinkList[nowNode][i] === 1 && visited[i] === 0) {
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
    // console.log(n, m, v)
    for (let i = 0; i < m; i++) {
        nodeLink.push(input[i + 1].split(' ').map(Number))
    }
    // console.log(nodeLink)
    let nodeLinkList = []
    for (let i = 0; i <= n; i++) {
        nodeLinkList.push(Array(n + 1).fill(0))
    }
    // console.log(nodeLinkList)
    for (let i = 0; i < m; i++) {
        nodeLinkList[nodeLink[i][0]][nodeLink[i][1]] = 1
        nodeLinkList[nodeLink[i][1]][nodeLink[i][0]] = 1
    }
    // console.log(nodeLinkList)
    bfs(n, m, v, nodeLinkList)
})