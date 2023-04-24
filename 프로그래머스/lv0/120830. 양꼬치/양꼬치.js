function solution(n, k) {
    let money;
    if(n>=10){
        let service = Math.floor(n/10);
        money = 12000*n + 2000*k - 2000*service;
    }else{
        money = 12000*n + 2000*k;
    }return money;
}