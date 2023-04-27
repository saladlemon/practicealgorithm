function solution(numbers, k) {
    const length = numbers.length;
    let man = 1;
    
    for(i=1;i<k;i++){
        man = man + 2;
        if(man > length){
            man = man - length;
        }
    }return man;
}