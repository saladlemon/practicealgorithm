function solution(n) {
    let pizza;
    
    for(let i=1;i<=100;i++){
        let piece = n/7;
        
        if(n/7 <= i){
            pizza = i;
            break;
        }
    }
    var answer = pizza;
    return answer;
}