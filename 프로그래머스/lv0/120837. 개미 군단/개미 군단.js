function solution(hp) {
    const general = 5;
    const soldier = 3;
    const worker = 1;
    
    const ants = Math.floor(hp/5) + Math.floor((hp%5)/3) + Math.floor((hp%5)%3)
    return ants;
}