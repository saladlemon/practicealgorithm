function solution(n) {
    let arr = [];
    let a = 0;
    for(i=2;i<=n;i++){
        while(n%i === 0){
            arr[a] = i;
            a++;
            n = n/i;
        }
    }
    let num = arr.filter((el) => el !== null);
    num.sort((a,b) => a-b);
    const result = [...new Set(num)];
    return result;
}