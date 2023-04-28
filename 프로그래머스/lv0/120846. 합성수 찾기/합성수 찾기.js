function solution(n) {
    let count = 0;
    let num = 0;
    let result = 0;
    for(i=1;i<=n;i++){
        for(j=1;j<=i;j++){
            if(i%j === 0){
                count++;
                if(count>2){
                    result++;
                    break;
                }
            }
        }count = 0;
    }return result;
}