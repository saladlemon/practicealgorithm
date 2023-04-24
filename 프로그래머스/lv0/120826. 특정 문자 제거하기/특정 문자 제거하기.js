function solution(my_string, letter) {
    const newArray = my_string.split(letter).join('');
    return newArray;
}