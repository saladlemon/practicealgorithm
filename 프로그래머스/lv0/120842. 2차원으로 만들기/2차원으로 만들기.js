function solution(num_list, n) {
    const row = num_list.length/n;
    const col = n;
    const arr = [];
    for(i=0;i<row;i++){
        arr[i] = [];
        for(j=0;j<col;j++){
            arr[i][j] = num_list[i*col+j];
        }
    }
    
    return arr;
}