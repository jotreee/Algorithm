function solution(x, n) {
    var answer = [];
    for (let cnt = 1; cnt <= n; cnt++) {
        answer.push(x * cnt)
    }
    return answer;
}