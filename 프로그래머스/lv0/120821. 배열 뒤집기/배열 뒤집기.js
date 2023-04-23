function solution(num_list) {
    let length = num_list.length;
    let arr = [];
    let j = length-1;
    
    for(let i = 0; i < length; i++){
        arr[i] = num_list[j]
        j--;
    }
    return arr;
}