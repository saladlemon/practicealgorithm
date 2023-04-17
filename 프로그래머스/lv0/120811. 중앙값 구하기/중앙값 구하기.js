function solution(array) {
    const length = array.length;
    
    for (i = 0; i < length; i++){
        for (j = i + 1; j < length; j++){
            if (array[i] > array[j]){
                const temp = array[j];
                array[j] = array[i];
                array[i] = temp;
            }
        }
    }    
    const Mid = array[((length + 1) / 2) - 1];
    
    let answer = Mid;
    return answer;
}