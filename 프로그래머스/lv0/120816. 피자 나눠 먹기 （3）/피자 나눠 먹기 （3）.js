function solution(slice, n) {
    let pizza;
    if(n<=slice){
        pizza = 1;
    }else{
        if(n%slice == 0){
            pizza = n/slice;
        }else{
            pizza = Math.floor((n/slice) +1);
        }
    }return pizza;
}