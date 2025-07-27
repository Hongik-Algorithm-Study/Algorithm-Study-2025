function solution(progresses, speeds) {
    var answer = [];
    while (progresses.length > 0){
        let count = 0;
        while (progresses[0] >= 100) {
            progresses.shift();
            speeds.shift();
            count += 1;
        }
        if (count > 0) {
            answer.push(count);
        }
        for (let i = 0; i < progresses.length; i++){
            progresses[i] += speeds[i];
        }
    }
    return answer;
}