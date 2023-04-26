function solution(rsp) {
    const RSP = rsp.split('');
    for(i=0;i<RSP.length;i++){
        if(RSP[i] === "2"){
            RSP[i] = "0";
        }else if(RSP[i] === "0"){
            RSP[i] = "5";
        }else if(RSP[i] === "5"){
            RSP[i] = "2";
        }
    }
    const result = RSP.join('');
    return result;
}