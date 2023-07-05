function solution(array, n) {
  let closenum = array[0];
  let mindiff = Math.abs(array[0] - n);

  for (let i = 1; i < array.length; i++) {
    const diff = Math.abs(array[i] - n);
    if (diff < mindiff) {
      mindiff = diff;
      closenum = array[i];
    } else if (diff === mindiff && array[i] < closenum) {
      closenum = array[i];
    }
  }

  return closenum;
}
