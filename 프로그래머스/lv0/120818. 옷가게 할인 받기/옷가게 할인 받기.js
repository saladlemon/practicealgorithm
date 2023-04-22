function solution(price) {
    if(100000 <= price && price < 300000){
        price = price*0.95;
    }else if(300000 <= price && price < 500000){
        price = price*0.9;        
    }else if(500000 <= price){
        price = price*0.8;
    }
    return Math.floor(price);
}