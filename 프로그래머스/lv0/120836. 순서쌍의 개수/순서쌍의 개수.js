function solution(n) {
    let result = 0;
    
    for(a=1;a<=n;a++){
        if(n%a === 0){
            result++;
        }
    }
    return result;
}