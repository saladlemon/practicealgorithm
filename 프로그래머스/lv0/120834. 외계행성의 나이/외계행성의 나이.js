function solution(age) {
    const Age = String(age);
    let str = Age.split('');
    
    for(i=0;i<str.length;i++){
        if(str[i] === "0"){
            str[i] = "a";
        }else if(str[i] === "1"){
            str[i] = "b";
        }else if(str[i] === "2"){
            str[i] = "c";
        }else if(str[i] === "3"){
            str[i] = "d";
        }else if(str[i] === "4"){
            str[i] = "e";
        }else if(str[i] === "5"){
            str[i] = "f";
        }else if(str[i] === "6"){
            str[i] = "g";
        }else if(str[i] === "7"){
            str[i] = "h";
        }else if(str[i] === "8"){
            str[i] = "i";
        }else if(str[i] === "9"){
            str[i] = "j";
        }
    }
    let b = str.join('');
    return b;
}