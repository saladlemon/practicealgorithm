function solution(n) {
  let i = 1;
  while (i <= 10) {
    let factorial = 1;
    for (let j = 1; j <= i; j++) {
      factorial *= j;
    }
    if (factorial > n) {
      break;
    }
    i++;
  }
  return i - 1;
}
