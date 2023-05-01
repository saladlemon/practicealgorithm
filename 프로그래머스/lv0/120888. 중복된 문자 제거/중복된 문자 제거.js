function solution(my_string) {
    let arr = my_string.split("");
    for(i=0;i<arr.length;i++){
        for(j=i+1;j<arr.length;j++){
            if(arr[i] == arr[j]){
                arr.splice(j,1);
                j--;
            }
        }
    }
    let str = arr.join('');
    return str
}