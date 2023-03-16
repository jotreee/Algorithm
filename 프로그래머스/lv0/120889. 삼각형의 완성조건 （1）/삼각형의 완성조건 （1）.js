function solution(sides) {
    var answer = 1;
    sum = sides.reduce((a, b) => (a + b))
    if(Math.max(...sides) * 2 >= sum){
        answer = 2
    }
    return answer;
}