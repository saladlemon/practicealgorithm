function solution(numer1, denom1, numer2, denom2) {
    0 < numer1 , denom1, numer2, denom2 < 1000;
    const numer = numer1*denom2+ numer2*denom1;
    const denom = denom1*denom2;
    
    let a = numer;
    let b = denom;
    while(b !== 0){
        const temp = b;
        b = a % b;
        a = temp;
    }
    const gcd = a;
    N = numer/gcd;
    D = denom/gcd;
     
    const answer = [N,D];
    return answer;
}