function solution(letter) {
    const morse = {
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    };
    const trans = letter.split(' ');
    let decode = [];
    for(let i=0; i<trans.length; i++){
        for(let key in morse){
            if(trans[i] === key){
                decode[i] = morse[key];
            }
        }
    }
    const result = decode.join('');    
    return result;
}