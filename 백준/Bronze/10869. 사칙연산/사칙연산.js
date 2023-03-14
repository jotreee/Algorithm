const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().split(' ').map(value =>+value)

const[A, B] = input
console.log(A + B)
console.log(A - B)
console.log(A * B)
console.log(Math.floor(A / B))
console.log(A % B)