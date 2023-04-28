function solution(numbers) {
    const lentgh = numbers.length;
    numbers.sort((a,b) => b-a);
    const result = numbers[0]*numbers[1];
    return result;
}