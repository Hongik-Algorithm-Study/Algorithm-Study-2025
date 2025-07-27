function solution(arr)
{
    const temp = [];

    for (let i = 0; i < arr.length; i++) {
        if (temp.length == 0) {
            temp.push(arr[i]);
        }
        else {
            const poped = temp.pop();
            if (poped === arr[i]) {
                temp.push(poped);
            }
            else {
                temp.push(poped);
                temp.push(arr[i]);
            }
        }
    }

    return temp;
}