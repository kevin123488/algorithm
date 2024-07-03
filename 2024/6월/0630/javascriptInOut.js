const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input = []

rl.on('line', (line) => {
    input.push(line)
    // rl.close()
}).on('close', () => {
    // console.log(input)
    let n = '*'
    console.log(n)
    console.log(typeof(n))
    console.log(n * 5)
    console.log(typeof(n * 5))
    console.log(5 === '5')
    console.log(5 + '5')
})