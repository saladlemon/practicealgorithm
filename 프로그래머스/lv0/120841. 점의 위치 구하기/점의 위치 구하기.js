function solution(dot) {
    const x = dot[0];
    const y = dot[1];
    let area;
    if(x > 0 && y > 0){
        area = 1;
    }else if(x < 0 && y > 0){
        area = 2;
    }else if(x < 0 && y < 0){
        area = 3;
    }else if(x > 0 && y < 0){
        area = 4;
    }
    return area;
}