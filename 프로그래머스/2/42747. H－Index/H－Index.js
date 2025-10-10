function solution(citations) {
  let answer = 0;
  const len = citations.length;

  citations.sort((a, b) => a - b);

  for (let i = 0; i < len; i++) {
    const h = len - i; 
    if (citations[i] >= h) {
      answer = h;
      break;
    }
  }

  return answer;
}