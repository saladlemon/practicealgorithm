function solution(numbers, direction) {
    const length = numbers.length;
    
    if(direction == "left"){
        const L = numbers[0];
        for(i = 0; i < length-1; i++){
            numbers[i] = numbers[i+1];
        }
        numbers[length-1] = L;
        return numbers;
    }else if(direction == "right"){
        const R = numbers[length-1];
        for(i = length-1; i > 0; i--){
            numbers[i] = numbers[i-1];
        }
        numbers[0] = R;
        return numbers;
    }
}