function solution(my_string) {
    const changeArray = my_string.split('');
    const reverseArray = changeArray.reverse();
    const reverseString = reverseArray.join('');
    
    return reverseString;    
}