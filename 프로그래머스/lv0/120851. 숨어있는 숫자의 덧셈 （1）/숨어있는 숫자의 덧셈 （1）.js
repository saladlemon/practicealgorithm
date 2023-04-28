function solution(my_string) {
    const arr = my_string.replace(/[abcdefghijklmnopqrstuvwxyz]/ig,"");
    const split = arr.split("");
    let num = [];
    let sum = 0;
    for(i=0;i<split.length;i++){
        num[i] = parseInt(split[i]);
    }
    for(j=0;j<num.length;j++){
        sum = sum + num[j];
    }
    return sum;
}