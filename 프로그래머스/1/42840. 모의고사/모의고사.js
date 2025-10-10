function solution(answers) {
    const len = answers.length;
    var answer = [];
    const patternA = [1, 2, 3, 4, 5];
    const patternB = [2, 1, 2, 3, 2, 4, 2, 5];
    const patternC = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    
    let correctA = 0;
    let correctB = 0;
    let correctC = 0;
    
    for( let i = 0; i < len; i++ ){
        if( patternA[i%patternA.length] === answers[i] ){
            correctA++;
        }
        if( patternB[i%patternB.length] === answers[i] ){
            correctB++;
        }
        if( patternC[i%patternC.length] === answers[i] ){
            correctC++;
        }
    }
    
    const resultArr = [correctA, correctB, correctC];
    
    const maxVal = Math.max(...resultArr);
    
    if( correctA === maxVal ){
        answer.push(1);
    }
    if( correctB === maxVal ){
        answer.push(2);
    }
    if( correctC === maxVal ){
        answer.push(3);
    }
    
    return answer;
}