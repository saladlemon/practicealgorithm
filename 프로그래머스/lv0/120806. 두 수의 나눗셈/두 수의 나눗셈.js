function solution(num1, num2) {
    divideAndMulThousand = (num1/num2)*1000;
    var answer = parseInt(divideAndMulThousand);
    return answer;
}