function solution(s) {
    let num = 0;
    const arr = s.split(' ');
    for(i=0;i<arr.length;i++){
        if(arr[i] === "Z"){
            num = num - parseInt(arr[i-1]);
        }else{
            num = num + parseInt(arr[i]);
        }
    }
    return num
}