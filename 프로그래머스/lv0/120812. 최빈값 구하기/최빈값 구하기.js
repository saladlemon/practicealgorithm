function solution(array) {
    const length = array.length;
    const arr = array.sort();
    let mode;
    let Subcount = 0;
    let count = 0;
    
    
        for(i=0; i<length; i++){
            if(arr[i] === arr[i+1]){
                count = count + 1;
            }else{
                count = count + 1;
                if(Subcount < count){
                    Subcount = count;
                    mode = arr[i];
                }else if(Subcount === count){
                    mode = -1;
                }
                count = 0;
            }
        }
    var answer = mode;
    return answer;
}