function solution(emergency) {
    const A = [...emergency];
    const B = A.sort((a,b) => b-a);
    let C = [];
    for(i=0;i<emergency.length;i++){
        for(j=0;j<B.length;j++){
            if(emergency[i]===B[j]){
               C[i] = j+1; 
            }
        }
    }
    return C;
}