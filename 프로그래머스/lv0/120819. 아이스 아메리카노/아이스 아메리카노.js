function solution(money) {
    let americano = Math.floor(money/5500);
    let balance = money%5500;
    let arr = [];
    arr[0] = americano;
    arr[1] = balance;
    return arr;
}