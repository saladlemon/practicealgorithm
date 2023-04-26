function solution(balls, share) {
    const m = balls - share + 1;
    let Afact = 1, Bfact = 1;
    for (let i = m; i <= balls; i++) {
        Afact *= i;
    }
    for (let j = 1; j <= share; j++) {
        Bfact *= j;
    }
    const result = Math.floor(Afact / Bfact);
    return result;
}
