const fs = require('fs')
const inputData = fs.readFileSync('/dev/stdin').toString().split(' ').map(value => +value)

const[A, B] = inputData
console.log(A * B)