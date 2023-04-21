function solution(numbers) {
    let sum =0;
    let ave;
    let length = numbers.length;
    
    
    for(let i = 0; i < length; i++){
        sum = sum + numbers[i];
    }
    ave = sum/length;
    
    return ave;    
}