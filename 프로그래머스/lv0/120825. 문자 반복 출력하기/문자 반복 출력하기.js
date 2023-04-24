function solution(my_string, n) {
    const myArray = my_string.split('');
    const newArray = [];
    
    for(i=0;i<myArray.length;i++){
        newArray[i] = myArray[i].repeat(n);
    }
    const newString = newArray.join('');
    var answer = newString;
    return answer;
}