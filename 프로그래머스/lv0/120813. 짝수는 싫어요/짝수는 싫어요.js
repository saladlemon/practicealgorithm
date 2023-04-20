function solution(n) {
    let arr = [];
    let num = 0;
    
    for(let i = 1; i<=n; i++){
        if(i%2 === 1){
            arr[num] = i;
            num++;
        }
    }
    var answer = arr;
    return answer;
}