function solution(num_list) {
    let even = 0;
    let odd = 0;
    
    for(i=0;i<num_list.length;i++){
        if(num_list[i]%2==0){
            even++;           
        }else{
            odd++;
        }
    }
    var answer = [even, odd];
    return answer;
}