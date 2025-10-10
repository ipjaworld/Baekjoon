function solution(sizes) {
  let maxW = 0; 
  let maxH = 0;

  for (let i = 0; i < sizes.length; i++) {
    const [w, h] = sizes[i][0] > sizes[i][1] ? sizes[i] : [sizes[i][1], sizes[i][0]];
    
    if (w > maxW) maxW = w;
    if (h > maxH) maxH = h;
  }

  return maxW * maxH;
}