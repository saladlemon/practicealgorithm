function solution(money) {
    let americano = Math.floor(money/5500);
    let balance = money%5500;
    return [americano, balance];
}