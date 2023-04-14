function solution(numbers) {
    const length = numbers.length;
    
    for (let i = 0; i < length; i++){
        numbers[i] = numbers[i] * 2;
    }
    return numbers;
}