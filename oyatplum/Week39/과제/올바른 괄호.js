function solution(s){
    let temp = [];

    for (let i = 0; i < s.length; i++) {
        if (temp.length === 0) {
            temp.push(s[i]);
        }
        else {
            let poped = temp.shift();
            if (s[i] === ")" && poped === "(") {
                continue
            }
            else {
                temp.push(poped);
                temp.push(s[i]);
            }
        }
    }

    if (temp.length > 0) {
        return false;
    }
    else {
        return true;
    }
}