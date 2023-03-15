function solution(numbers) {
    sum = function(arr) {
        return arr.reduce((a, b) => a + b, 0)
    }
    var answer = sum(numbers) / numbers.length
    return answer;
}