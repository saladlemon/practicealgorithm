function solution(my_string) {
    const arr = my_string.replace(/[abcdefghijklmnopqrstuvwxyz]/ig, "");
    const num = arr.split('');
    let A = [];
    for(i=0;i<num.length;i++){
        A[i] = parseInt(num[i]);
    }
    return A.sort((a, b) => a - b);
}