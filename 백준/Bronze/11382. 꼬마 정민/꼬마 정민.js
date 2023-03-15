const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().split(' ').map(value => +value)

const [A, B, C] = input
console.log(A + B + C)